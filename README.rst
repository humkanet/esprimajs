**esprimajs** is a es6-compatible javascript minifier written by python.
**esprimajs** uses `esprima-python <https://github.com/Kronuz/esprima-python>`__
as javascript parser library

Features
~~~~~~~~

-  ES6 support
-  Mangling function and variable names
-  Ident output
-  Obfuscate strings

Installation
~~~~~~~~~~~~

.. code:: shell

    pip install esprimajs

Examples
~~~~~~~~

Example javascript file

.. code:: javascript

    const Aconst = Math.PI, Bconst = "Bconst";
    const Cconst = "Cconst";

    function add(a, b){
            function foo(){
                    return a+b;
            }
            return foo();
    }

    const Dconst="Dconst";

    function mul(a, b){
            return a*b;
    }


    const Econst="Econst";
    let Alet="Alet";
    const Fconst="Fconst", Gconst="Gconst";


Rearrange and mangle variables:

.. code:: shell

    python -m esprimajs -r -mv 2 test.js

.. code:: javascript

    const Aconst=Math.PI,Bconst="Bconst",Cconst="Cconst";
    function add($a,$b){
      function foo(){
        return $a+$b;
      }
      return foo();
    }
    const Dconst="Dconst";
    function mul($a,$b){
      return $a*$b;
    }
    const Econst="Econst",Fconst="Fconst",Gconst="Gconst";
    let Alet="Alet";


Rearrange variables and mangle variables (include top-level) and function names (except top-level):

.. code:: shell

    python -m esprimajs -r -mv 1 --mf 2 test.js


.. code:: javascript

    const $a=Math.PI,$b="Bconst",$c="Cconst";
    function add($d,$e){
      function $f(){
        return $d+$e;
      }
      return $f();
    }
    const $d="Dconst";
    function mul($e,$f){
      return $e*$f;
    }
    const $e="Econst",$f="Fconst",$g="Gconst";
    let $h="Alet";

Rearrange variables and mangle variables and function names (include top level) without identing:

.. code:: shell

    python -m esprimajs -i 0 -r -mf 1 -mf 1 test.js

.. code:: javascript

    const $a=Math.PI,$b="Bconst",$c="Cconst";function $d($e,$f){function $g(){return $e+$f;}return $g();}const $e="Dconst";function $f($g,$h){return $g*$h;}const $g="Econst",$h="Fconst",$i="Gconst";let $j="Alet";


API
~~~

Minify javascript string:

.. code:: python

    >>> from esprimajs import Minifier
    >>> c = Minifier(rearrange=True, mangle_variables=1)
    >>> js = """
    ... const A=1;
    ... const B=2;
    ... let C=3;
    ...
    ... class TestClass extends Object{
    ...   constructor(a, b){
    ...     this._a=a;
    ...     this.b=b;
    ...   }
    ...   static get a(){
    ...     return this._a;
    ...   }
    ...   set b(b){
    ...     this.b=b;
    ...   }
    ...
    ...   static async sum(){
    ...     return this.a+this.b
    ...   }
    ... }
    ... """
    >>> buf = c.minify(js)
    >>> print(buf.read())
    const $a=1,$b=2;
    let $c=3;
    class TestClass extends Object{
      constructor($d,$e){
        this._a=$d;
        this.b=$e;
      }
      static get a(){
        return this._a;
      }
      set b($d){
        this.b=$d;
      }
      static async sum(){
        return this.a+this.b;
      }
    }
    >>>

