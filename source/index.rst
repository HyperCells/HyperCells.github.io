:html_theme.sidebar_secondary.remove: true

.. 
   HyperCells website documentation master file, created by
   sphinx-quickstart on Mon Jun 24 10:13:57 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. raw:: html

    <style type="text/css">
         @media (min-width: 959.98px) {
            .bd-main .bd-content .bd-article-container {
               max-width: 80%!important; 
               }
            }
    </style>


.. raw:: html

   <style type="text/css">
      .bd-content .sd-card {
         border: 1px solid var(--pst-color-border);
         text-align: center;
         place-items: center;
         border-radius: 20px;
      }
    </style>


.. raw:: html

   <script type="text/javascript">
      var observer = new MutationObserver(function(mutations) {
         const dark = document.documentElement.dataset.theme == 'dark';
         var windowWidth = window.innerWidth;
         if(windowWidth > 500) {
            document.getElementsByClassName('no-scaled-link')[0].src = dark ? '_static/images/darkMode/TitleFigure2.2_dark.png' : "_static/images/lightMode/TitleFigure2.2_light.png";
         }
         else {
            document.getElementsByClassName('no-scaled-link')[0].src = dark ? '_static/images/darkMode/TitleFigure_mobile_dark.png' : "_static/images/lightMode/TitleFigure_mobile_light.png";
         }
    })
    observer.observe(document.documentElement, {attributes: true, attributeFilter: ['data-theme']});
  
  </script>
  <link rel="preload" href="_static/images/darkMode/TitleFigure2.2_dark.png" as="image">


.. image:: _static/images/lightMode/TitleFigure2.2_light.png
   :width: 100%
   :class: no-scaled-link, dark-light
   :align: center


.. card:: Documentation
   :link: docs
   :link-type: ref
   :link-alt: clickable cards
   :text-align: center
   :margin: 4 2 0 0

.. grid:: 3
   :gutter: 2
   :padding: 0

   .. grid-item-card:: Installation
      :link: ./contents/Installation/installation.html
      :link-alt: installation.html

   .. grid-item-card:: Getting started
      :link: getsetgo
      :link-type: ref
      :link-alt: clickable cards

   .. grid-item-card:: Tutorials
      :link: tutorials
      :link-type: ref
      :link-alt: clickable cards

.. |GAP| raw:: html

   <a href="https://www.gap-system.org/" target="_blank">GAP</a>


.. |Mathematica| raw:: html

   <a href="https://www.wolfram.com/mathematica" target="_blank">Mathematica</a>

.. highlights::
   **HyperCells** is a |GAP| package which enables the construction of graphs underlying tight-binding models 
   on infinite and compactified hyperbolic lattices on primitive cells and supercells based on triangle groups 
   and quotients with normal subgroups.

.. highlights::
   **HyperBloch** is a |Mathematica| package for the construction of the corresponding Bloch Hamiltonian, its
   eigenstates, and spectrum based on Abelian hyperbolic band theory. It enables advanced visualizations of
   hyperbolic lattices and graphs of underlying tight-binding models on the Poincaré disk model.

======

Efficient Modeling of Tight-Binding Models on Hyperbolic Lattices
-----------------------------------------------------------------

Hyperbolic lattices were recently theoretically described by a non-Abelian generalization 
of the Bloch theorem, but practical approaches for efficient computations have remained missing. 
The **supercell method** overcomes the challenges posed by noncommuting translations, and 
enables significant progress towards an analytical description of hyperbolic lattice models in 
momentum space. To encourage further investigations in this emerging field, we have implemented 
the supercell method in a pair of complementary open-source software packages; the GAP package
**HyperCells** and the Mathematica package **HyperBloch**.

Supercell Method
^^^^^^^^^^^^^^^^

.. |Phys. Rev. B 104, 115136 (2021)| raw:: html

   <a href="https://patrick-lenggenhager.github.io/publications/2023/12/01/Supercells.html" target="_blank">Phys. Rev. B 104, 115136 (2021)</a>

.. |PhD thesis| raw:: html

   <a href="https://patrick-lenggenhager.github.io/publications/2023/09/29/PhDThesis.html" target="_blank">PhD thesis</a>

.. |space| unicode:: U+2064 .. space

.. raw:: html

  <script type="text/javascript">
    var observer = new MutationObserver(function(mutations) {
      const dark = document.documentElement.dataset.theme == 'dark';
      document.getElementsByClassName('no-scaled-link')[1].src = dark ? '_static/images/darkMode/SuperCells2_dark.png' : "_static/images/lightMode/SuperCells2_light.png";
    })
    observer.observe(document.documentElement, {attributes: true, attributeFilter: ['data-theme']});
  </script>
  <link rel="preload" href="_static/images/darkMode/SuperCells2_dark.png" as="image">

.. image:: _static/images/lightMode/SuperCells2_light.png
   :scale: 15%
   :class: no-scaled-link, dark-light
   :align: left

More specifically, we use computational group theory to create a sequence of progressively larger unit
cells, each formed as a symmetric aggregate of smaller unit cells. Subsequently, we apply the previously 
established Abelian hyperbolic band theory — which ignores the noncommutativity of translations — to those 
growing supercells and obtain a converging description of the infinite lattice. The method was introduced in
|Phys. Rev. B 104, 115136 (2021)|. Practically, we need to perform the following steps:

| |space| |space| |space| 1. |space| |space| construct the lattice and model graph on the primitive (unit) cell,
| |space| |space| |space| 2. |space| |space| construct the supercell graph relating the model on the primitive cell
| |space| |space| |space| |space| |space| |space| |space| |space| |space| to the model on the supercell,
| |space| |space| |space| 3. |space| |space| set up the tight-binding model in real space on the primitive cell, and
| |space| |space| |space| 4. |space| |space| construct the (Abelian) Bloch Hamiltonian.


|
| For an accessible introduction to the topic in general and these steps specifically, see Dr. Patrick M. Lenggenhager's |PhD thesis|.



.. toctree::
   :maxdepth: 10
   :caption: Contents:
   :hidden:

   contents/About/Intro.md

   contents/Installation/installation.md

   contents/GettingStarted/getting_started.rst
      
   contents/Tutorials/tutorials.rst

   contents/Documentation/documentation.rst

   contents/Gallery/gallery.rst

   contents/Publications/publications.md

   contents/Contribute/contribute.md

   contents/Releases/releases.md

   contents/Contact/contact.md


..
   Indices and tables
   ------------------

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
