..
   :html_theme.sidebar_secondary.remove: true

.. 
   raw:: html

    <style type="text/css">
         @media (min-width: 959.98px) {
            .bd-main .bd-content {
               max-width: 80%!important; 
               text-align:left!important;
               }
            }
    </style>

.. _tutorials:

Tutorials
=========

.. _Supercells: ./Supercells.html
.. _Coherent sequences: ./Coherent_SC_sequences.html
.. _Flat-bands: ./Flat-bands.html
.. _Haldane model: ./Haldane_model.html
.. _Hatano-Nelson model: ./HatanoNelson_model.html
.. _Higher-order topology: ./HigherOrder_topology.html
.. _Advanced visualization: ./AdvancedVisualization.html

.. admonition:: Under construction
   :class: danger

   The HyperCells & HyperBloch website is currently under construction! Some tutorials refer to currently non-available 
   features, which will soon be accessible in the new releases of the HyperCells and HyperBloch packages.


The HyperCells and HyperBloch packages offer a framework for efficient modeling 
of tight-binding models on a broad list of hyperbolic lattices. We provide tutorials 
which are aimed to facilitate a smooth workflow and showcase prominent examples 
of interest.

.. card:: Supercells
   :link: ./Supercells.html 
   :link-alt: Supercells.html
   :text-align: justify
   :margin: 3 3 2 2

   The HyperCells package grants easy access to supercells of hyperbolic lattices through 
   computational group theory. The tight-binding models on these supercells enable systematic
   access to higher-dimensional irreducible representations on the primitive cell through 
   the use of the HyperBloch package by applying **Abelian hyperbolic band theory**. 
   In this tutorial we will construct multiple supercell sequences and demonstrate the 
   convergence to the thermodynamic limit of the density of states through the application 
   of the **supercell method**.

.. card:: Coherent sequences
   :link: ./Coherent_SC_sequences.html
   :link-alt: Coherent_SC_sequences.html
   :text-align: justify
   :margin: 3 3 2 2

   The application of the supercell method relies on the identification of appropriate supercell 
   sequences. Each supercell is associated with a triangle group quotient specified by a corresponding 
   translation group. The sequences of these translation groups form so-called **coherent sequences** defined 
   by a normal subgroup relation between consecutive translation groups. In this tutorial, we showcase how such sequences can be identified.
   Two approaches are presented, which entail the construction of a user defined functions and **normal subgroup 
   tree graphs** which describes the normal subgroup relations between any pairwise distinct translation 
   group of a :math:`\{p,q\}`-tesselation of the hyperbolic plane.

.. card:: Flat-bands
   :link: ./Flat-bands.html 
   :link-alt: Flat-bands.html
   :text-align: justify
   :margin: 3 3 2 2

   The HyperCells package is equipped with built-in functions to model hyperbolic lattices with emergent
   strongly correlated systems. Among prominent examples which develop pronounced flat-bands are 
   hyperbolic lattice variants of the Euclidean **Lieb** and **kagome lattices**. In this tutorial, we will 
   see how hyperbolic Lieb and kagome lattices are constructed through model graphs on a primitive cell 
   and consecutive supercell in tandem with the application of the supercell method.

.. card:: Haldane model
   :link: ./Haldane_model.html 
   :link-alt: Haldane_model.html
   :text-align: justify
   :margin: 3 3 2 2

   Haldane models on hyperbolic lattices can be constructed by using the HyperCells and HyperBloch packages
   in tandem. The HyperCells package provides the necessary framework to decorate nearest-neighbor models
   with **oriented next-nearest-neighbor** terms through a minimal modification of the usual workflow. These models can be 
   endowed with oriented coupling constants in the HyperBloch package. In this tutorial, we will construct next-nearest-neighbor
   tight-binding models and Haldane models. Additionally, we will construct **point-group matrices** in order
   to showcase how **hyperbolic lattice symmetries** can be analyzed.

.. card:: Hatano-Nelson model
   :link: ./HatanoNelson_model.html 
   :link-alt: HatanoNelson_model.html
   :text-align: justify
   :margin: 3 3 2 2
  
   The HyperBloch package provides a framework for the construction of Hermitian as well as **non-Hermitian** Abelian Bloch Hamiltonians
   for tight-binding models on hyperbolic lattices. In this tutorial, we will construct two non-Hermitian tight-binding models. Specifically, 
   we will see how Hermiticity-breaking **gains and losses** can be assigned through **staggered complex on-site potentials** as well as how to construct 
   a variant of the **Hatano-Nelson model** describing a **non-reciprocal** tight-binding model on a hyperbolic lattice.

.. card:: Higher-order topology
   :link: ./HigherOrder_topology.html 
   :link-alt: HigherOrder_topology.html
   :text-align: justify
   :margin: 3 3 2 2
  
   In this tutorial, we will see how to construct an elementary nearest-neighbor hopping model with **multiple orbitals** per site for (supercell) model 
   graphs. This will enable us to set up a variant of the Benalcazar-Bernevig-Hughes model, also known as the **BBH model**. Moreover, we will demonstrate the 
   **bulk-boundary correspondence** by analyzing spectra computed for a BBH model on finite flakes with open boundary conditions. 
   In particular, we will see how **disclination defects** can be introduced in finite size systems, through the **Volterra process** by specifying a negative
   **Frank angle**, which demonstrates an emergent **filling anomaly** through corresponding spectra.

.. 
   card:: Advanced visualization
   :link: ./AdvancedVisualization.html 
   :link-alt: AdvancedVisualization.html
   :text-align: justify
   :margin: 3 3 2 2
  
   Lorem ipsum ....


Featured function index
^^^^^^^^^^^^^^^^^^^^^^^

The getting started and the tutorial page feature the following **HyperCells** and **HyperBloch** functions:

.. include:: interlinkTutorials.rst
   :start-line: 2


.. toctree::
   :maxdepth: 10
   :hidden:

   Supercells.md
   Coherent_SC_sequences.md
   Flat-bands.md
   Haldane_model.md
   HatanoNelson_model.md
   HigherOrder_topology.md
..
   AdvancedVisualization.md
