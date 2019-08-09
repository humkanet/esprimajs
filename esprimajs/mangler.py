# -*- coding: utf-8 -*-

import string
import json


PREFIXES  = string.ascii_letters
nPREFIXES = len(PREFIXES)

SKIP      = {"do", "if", "in"}


class EAlreadyExists(Exception):
	def __init__(self, id, node=None):
		self.id = id
		self.__node = None
	def __str__(self):
		return f"Identifier '{self.id}' already exists in current scope"


class Mangler:

	@property
	def level(self):
		return self.__level

	@property
	def scope(self):
		return self.__scope


	def __init__(self, prefix=""):
		self.__prefix = prefix
		self.reset()


	def reset(self):
		self.__level =0
		self.__scope = {
			"parent": None,
			"cnt"   : 0,
			"name"  : dict(),
			"mangle": set()
		}


	def enter(self):
		self.__level += 1
		self.__scope = dict(parent=self.__scope, cnt=0, name=dict(), mangle=set())


	def leave(self):
		parent = self.__scope.get("parent")
		if isinstance(parent, dict):
			self.__level -= 1
			self.__scope = parent


	def has(self, name):
		return name==self.demangle(name, False)


	def __setitem__(self, key, value):
		scope = self.__scope
		scope["name"][key] = value
		scope["mangle"].add(value)


	def __getitem__(self, name):
		scope  = self.__scope
		mangle = None
		# Search mangled variable
		while scope and not mangle:
			mangle = scope["name"].get(name)
			if not mangle: scope = scope.get("parent")
		# Return variable
		return mangle


	def __contains__(self, mangle):
		name = self[mangle]
		return name is not None


	def exists(self, mangle):
		exists = False
		scope  = self.__scope
		while scope and not exists:
			exists = mangle in scope["mangle"]
			if not exists: scope = scope["parent"]
		return exists


	def append(self, name):
		if name in self.__scope["name"]: raise EAlreadyExists(name)
		self[name] = name
		return name


	def mangle(self, name):
		scope = self.__scope
		while True:
			cnt = scope["cnt"]
			mangle = ""
			while cnt>=nPREFIXES:
				mangle = f"{PREFIXES[cnt%nPREFIXES]}{mangle}"
				cnt = int(cnt/nPREFIXES)
			if len(mangle)>0: cnt -= 1
			mangle = f"{self.__prefix}{PREFIXES[cnt]}{mangle}"
			scope["cnt"] += 1
			if mangle in SKIP: continue
			if not self.exists(mangle): break
		self[name] = mangle
		return mangle


	def demangle(self, name, return_default=True):
		mangle = self[name]
		return mangle if mangle else name if return_default==True else None
