<style type="text/css">
   @media (min-width: 959.98px) {
      .bd-main .bd-content  {
         max-width: 84.1%;
         align-self: end;
         }
      .bd-main .bd-content .bd-sidebar-secondary .bd-toc {
         align-items:right;
         }
</style>

# Documentation

## HyperCells

The HyperCells documentation can be found here <a target="_blank" href="https://hypercells.github.io/HyperCells/doc/chap0_mj.html">HyperCells documentation</a>. 

Alternatively, provided the HyperCells package was installed properly, the documentation can be generated via the [AutoDoc](https://docs.gap-system.org/pkg/autodoc/doc/chap1_mj.html) package in GAP. Open GAP and execute the following code snippet:

```gap
LoadPackage( "AutoDoc" );
AutoDoc( rec( autodoc := true ) );
QUIT;
```

Then you can generate the HyperCells package manual from the command line with the following command, executed from within in the HyperCells package directory:

```
gap makedoc.g
```

Note that, once the above code snippets are executed you will also be able to use the help functionality for the HyperCells package within GAP. For example:

```gap
?TGCellGraph
```

which opens the corresponding section in the documentation.


## HyperBloch

The reference pages of the HyperBloch documentation can be accessed directly within a Mathematica environment.
Provided the HyperBloch paclet was installed properly, the function <code class="code-Mathematica">Documentation`HelpLookup</code> can be executed in Mathematica:

```Mathematica
Documentation`HelpLookup["PatrickMLenggenhager/HyperBloch/guide/HyperBlochPackage"];
```

alternatively, select a function and press **F1**.
