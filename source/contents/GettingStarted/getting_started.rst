
:html_theme.sidebar_secondary.remove: true


.. raw:: html

   <style type="text/css">
         @media (min-width: 959.98px) {
            .bd-main .bd-content {
               max-width: 80%!important; 
               text-align:left!important;
               }
            }
   </style>

.. _getsetgo:

Getting started
===============


.. |GAP| raw:: html

   <a href="https://www.gap-system.org" target="_blank">GAP</a>

.. |HyperCells| raw:: html

   <a href="https://github.com/patrick-lenggenhager/HyperCells" target="_blank">HyperCells</a>

.. |HyperBloch| raw:: html

   <a href="https://github.com/patrick-lenggenhager/HyperBloch" target="_blank">HyperBloch</a>


.. |documentation| raw:: html

   <a href="https://patrick-lenggenhager.github.io/HyperCells/doc/chap7_mj.html#X8091CEE880E799B4" target="_blank">documentation</a>




The task of modeling tight-binding models on hyperbolic lattices is split into two steps:

.. card:: 1. HyperCells package
   :link: ./getSetGo_HyperCells.html 
   :link-alt: getSetGo_HyperCells.html
   :text-align: justify
   :margin: 3 3 2 2

   **Construction of lattice/model graphs** for finite systems, this includes the construction 
   of appropriate periodic boundary conditions, while for infinite systems, the corresponding 
   primitive cell and successive supercells are constructed in order to apply the supercell 
   method for hyperbolic band theory. This part is implemented in the |GAP| package **HyperCells**. 
   Additionally, the package determines maximally-symmetric Wyckoff positions and simplifies dealing 
   with translation and point group symmetries on the hyperbolic lattice. The package also allows the 
   definition of the graph underlying a specific model, i.e., selecting specific Wyckoff positions, 
   nearest or next-nearest neighbors etc.


.. card:: 2. HyperBloch package
   :link: ./getSetGo_HyperBloch.html 
   :link-alt: getSetGo_HyperBloch.html
   :text-align: justify
   :margin: 3 3 2 2

   **Defining tight-binding models and using hyperbolic band theory** implemented in the second package,
   a Mathematica package called **HyperBloch**. It provides functions for importing and easily visualizing 
   the clusters, supercells, and model graphs. Additionally, it allows the user to easily define 
   tight-binding models on top of the model graph, by placing orbitals at vertices and defining 
   hopping matrices on the edges. Finally, the Abelian Bloch Hamiltonian for the defined model is 
   constructed and thus allows to study eigenstates and eigenvalues.
	
Note that the output of the HyperCells package, i.e., the cell, model and supercell model graphs can be 
read by any programming language, such that using the HyperBloch package is not strictly necessary. 
The file format definition can be found in the |documentation|.


.. toctree::
   :maxdepth: 10
   :hidden:

   getSetGo_HyperCells.md
   getSetGo_HyperBloch.md