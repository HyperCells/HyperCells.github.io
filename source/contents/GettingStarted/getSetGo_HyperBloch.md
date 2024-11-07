---
title: Getting Started with HyperCells and HyperBloch
layout: code_guide
summary: A getting-started guide for using the software packages <a href="https://github.com/patrick-lenggenhager/HyperCells">HyperCells</a> 
and <a href="https://github.com/patrick-lenggenhager/HyperBloch">HyperBloch</a> for modeling tight-binding models on hyperbolic lattices. 
It includes a brief overview over the purposes of the packages, complete instructions for installing them and simple examples including code scripts to download.
thumbnail: ../../media/thumbnails/project_HyperbolicLattices.jpg
---

# HyperBloch

```{dropdown} Learning goals
:color: success
:icon: light-bulb

Import of:

* cell grah,
* model graph
* and supercell model graphs files.

Visualization of:

* graph representation on a primive cell,
* graph representation on a supercell and

construction of:

* corresponding **Abelian Bloch Hamiltonians**.
```

```{dropdown}  Featured functions
:color: info
:icon: gear

**HyperCells**:

<code class="code-gap">
ProperTriangleGroup, TGQuotient, TGCellGraph, Export, TessellationModelGraph, TGCellSymmetric, TGSuperCellModelGraph
</code>
<br></br>

**HyperBloch**:

<code class="code-gap">
ImportCellGraphString, ImportModelGraphString, VisualizeModelGraph, ShowCellGraphFlattened, ShowCellBoundary, AbelianBlochHamiltonian, ImportCellGraphString, ImportSupercellModelGraphString
</code>
```

In this tutorial we will see how the cell, model and supercell model graphs, constructed through **HyperCells**, can be imported and visualized in the Poincaré disk. Moreover, we go through the intended workflow for the construction of corresponding **Abelian Bloch Hamiltonians** in order to demonstrate the <a target="_blank" href="https://doi.org/10.1103/PhysRevLett.131.226401">supercell</a> method through density of states calculations. Aspects of the content below originate from the  <a target="_blank" href="https:/doi.org/10.5281/zenodo.10142167">Supplementary Data and Code</a>, where the necessary steps to find the **density of states** of an elementary nearest-neighbor hopping model on the {math}`\{8,8\}`-lattice are discussed 
in more depth.


## Prerequisits **in GAP**

In order to get started with the HyperBloch package we construct nearest-neighbor graphs of the {8,8}-tessellation of the hyperbolic plane through the **HyperCells** package in GAP. We first construct the primitive cell and the model graph (based on the tessellation graph), and finally the 2-supercell, as we have established previously in getting started with [HyperCells](./getSetGo_HyperCells) package:

```gap
# load the HyperCells package
LoadPackage( "HyperCells" );

# set up (proper) triangle group
tg := ProperTriangleGroup( [ 2, 8, 8 ] );

# Primitive cell:
# ---------------

# specify the quotient defining the primitive cell
qpc := TGQuotient( [ 2, 6 ] );

# construct symmetric primitive cell
cgpc := TGCellGraph( tg, qpc, 3 : simplify := 5 );
Export( cgpc, "(2,8,8)_T2.6_3.hcc" ); # export

# elementary nearest-neighbor model
model := TessellationModelGraph( cgpc, true : simplify := 0 );
Export( model, "{8,8}-tess_T2.6_3.hcm" ); # export

# Supercell:
# ----------

# specify the quotient defining the supercell cell
qsc := TGQuotient( [ 3, 11 ] );

# construct symmetric supercell
cgsc := TGCellGraph( tg, qsc, 3 : simplify := 3 );
Export(cgsc, "(2,8,8)_T3.11_3.hcc");

# construct symmetric supercell
sc := TGCellSymmetric( tg, qsc, 3 );

# extend the model defined on the primitive cell to the supercell
scmodel := TGSuperCellModelGraph( model, sc : simplify := 0);
Export( scmodel, "{8,8}-tess_T2.6_3_sc-T3.11.hcs" ); # export
```

<div class="flex ">
  <a href="../../misc/code_snippets/GettingStarted/getting_started_HyperCells_pc_sc_files.zip" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download generated files</a>
  <a href="../../misc/code_snippets/GettingStarted/getting_started_HyperCells.g" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download GAP Code</a>
</div>


## Hands-on **in Mathematica**

Next, in Mathematica, we load the **HyperBloch** package

```Mathematica
<< PatrickMLenggenhager`HyperBloch`
```

### Primitive cell

#### Import the cell graph

The cell graph defines a maximally symmetric triangular tessellation of the corresponding connected and compactified translation unit cell.
We import it with the function <code class="code-Mathematica">ImportCellGraphString</code>:

```Mathematica
pcell = ImportCellGraphString[Import["(2,8,8)_T2.6_3.hcc"]];
```

Note the use of the <code class="code-Mathematica">Import</code> function inside the <code class="code-Mathematica">ImportCellGraphString</code> 
function. This is necessary, because the exported file is a text file, which contains the string representation of the cell graph. The 
<code class="code-Mathematica">Import</code> function is used to read the file, while the <code class="code-Mathematica">ImportCellGraphString</code> 
function is used to parse the string and construct the cell graph. Alternatively, we could have used the function 
<code class="code-gap">ExportString</code> in GAP to export the cell graph as a string, copied the string into a Mathematica notebook, 
and then used the <code class="code-Mathematica">ImportCellGraphString</code> function (or one of the analogous functions) directly to parse the
 string and construct the cell graph.

#### Import the model graph

The model graph is derived from cell graph. In our case it defines a nearest-neighbor graph of the {math}`\{8,8\}`-tessellation of the hyperbolic plane restricted to the primitive cell. It can be imported analogously, but requires the use of the function <code class="code-Mathematica">ImportModelGraphString</code> in order to parse the string and construct the model graph instead: 

```Mathematica
pcmodel = ImportModelGraphString[Import["{8,8}-tess_T2.6_3.hcm"]];
```

#### Visualize the the model graph

The HyperBloch package provides convenient functions for the visualization of graph representations of models on unit cells. We can visualize the model graph with the function <code class="code-Mathematica">VisualizeModelGraph</code>:

```Mathematica
VisualizeModelGraph[pcmodel,
	CellGraph -> pcell,
	Elements -> <|
		ShowCellBoundary -> {ShowEdgeIdentification -> True},
		ShowCellGraphFlattened -> {}
	|>,
  ImageSize -> 300,
  NumberOfGenerations -> 2]
```

producing a figure of an elementary nearest-neighbor model on the {math}`\{8,8\}`-lattice:

<figure class="text-center">
  <picture>
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/ENNM_88.png">
    <img src="../../media/figs/getSetGoHyperBloch/ENNM_88.png" class="figure-img img-fluid rounded" alt="elementary nearest-neighbor model on the {8,8} lattice" width="400"/>
  </picture>
</figure>

We have passed the cell graph to the option *CellGraph* which enables us to indicate the unit cell boundary through the function <code class="code-Mathematica">ShowCellBoundary</code>. Moreover, the boundary segments are indicated together with the associated (composite) translation and colored according to the boundary identification. The function <code class="code-Mathematica">ShowCellGraphFlattened</code> is used to shown all edges connecting pairs of vertices as hyperbolic geodesics in the Poincaré disk.

#### Construct the Hamiltonian

In order to construct the **Abelian Bloch Hamiltonian**, parameters need to be assigned to the vertices and the edges in the model graph. This takes a very compact form for an elementary nearest-neighbour tight-binding model. In order to illustrate the procedure, we will start with the most general assignment strategy and demonstrate the compact form afterwards.

```{admonition} Skip to subsection [Compact strategy](#compact-strategy)
:class: seealso-icon

On a first read one may want to skip the subsubsection "General strategy" and resume at the subsubsection "Compact strategy".
```

##### General strategy

Every model graph can be equipped with **multiple orbitals** per site, and even with a varying number of orbitals at each site. We will construct more involved models with multiple orbitals per site in the [Higher-order topology](../Tutorials/HigherOrder_topology.md) tutorial, for now, however, we will set the number of orbitals to one:

```Mathematica
norbits = 1;
```

Next, we need to assign parameters which describe the tight-binding model. This is achieved through the vertices and edges with the model graph and the use of <code class="code-Mathematica">Associtation</code>s.

**On-site** terms in the Hamiltonian are associated with vertices in the model graph. As such, it is instructive to explicitly print these vertices by using the function <code class="code-Mathematica">VertexList</code>, which takes as argument the graph representation:

```Mathematica
VertexList@pcmodel["Graph"]
```

There is only one site residing in the primitive cell, as such the vertex list contains only one entry ``{{3, 1}}``.
 
We choose to set the on-site term to zero by associating the list of vertices with a list of zeros using an <code class="code-Mathematica">Associtation</code>:

```Mathematica
mVec = ConstantArray[0, 1]; 
onsitePC = AssociationThread[VertexList@pcmodel["Graph"] -> mVec];
```

The **hopping terms** are associated with edges in the model graph. Similarly to the on-site terms, it is useful to explicitly print the edges using the function <code class="code-Mathematica">EdgeList</code>, which takes as argument the graph representation:

```Mathematica
EdgeList@pcmodel["Graph"]
```

which returns four edges:

<figure class="text-center">
  <picture>
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/EdgeListPC88.png">
    <img src="../../media/figs/getSetGoHyperBloch/EdgeListPC88.png" class="figure-img img-fluid rounded" alt="Edge list primitive cell {8,8}-lattice" width="600"/>
  </picture>
</figure>

Each element in the list is a <code class="code-Mathematica">DirectedEdge</code>, connecting a pair of vertices. We choose to set the hopping terms to a constant real value {math}`-1` for all edges by associating the edge list with a list of constant values:

```Mathematica
nnHoppingVec = ConstantArray[-1, 4];
hoppingPC = AssociationThread[EdgeList@pcmodel["Graph"] -> nnHoppingVec];
```

If we would consider a more involved model it might be helpful to look at the translation operators associated with the edges:

```Mathematica
pcmodel["EdgeTranslations"]
```

which contains four translation operators ``{g1, g4, g2, g3}``. In our particular case, all edges are associated with a non-trivial translation, i.e., the parameters we have assigned are inter-cell hopping amplitudes. 

The HyperBloch package is equipped with elaborate visualization tools of cell, model and supercell model graphs which can further guide the construction of models in more advanced settings. We will exploit these in subsequent tutorials.

The Abelian Bloch Hamiltonian can now be set up by passing the model graph and the corresponding coupling constants specified above to as arguments to the function <code class="code-Mathematica">AbelianBlochHamiltonian</code> or alternatively <code class="code-Mathematica">AbelianBlochHamiltonianExpression</code>, the former returns the Hamiltonian as a function of momenta. We choose to use the latter for now, in order to print a symbolic expression of the Hamiltonian:

```Mathematica
Hpc = AbelianBlochHamiltonianExpression[pcmodel, norbits, onsitePC, hoppingPC]
```

which results in a function of four momenta:

```Mathematica
{ { -2 (Cos[k[1]] + Cos[k[2]] + Cos[k[3]] + Cos[k[4]]) } }
```

##### Compact strategy

The simplicity of the specified model reduces the construction of the Hamiltonian to just one line of code. Once again we set the number of orbitals per site in the second argument to {math}`1`, the on-site term to {math}`0` and the nearest-neighbor coupling to {math}`-1`, where we use the function <code class="code-Mathematica">AbelianBlochHamiltonian</code>, which returns the Hamiltonian as a function of momenta:

```Mathematica
Hpc = AbelianBlochHamiltonian[pcmodel, 1, 0 &, -1 &];
```

For more efficient evaluation, we precompile the Bloch Hamiltonian
 by specifying the option <code class="code-Mathematica">CompileFunction->True</code>:

```Mathematica
Hpccf = AbelianBlochHamiltonian[pcmodel, 1, 0 &, -1 &, CompileFunction -> True];
```

#### Density of states


To compute the **density of states**, we can now take advantage of the independence of different momentum sectors and therefore parallelize the computation of the eigenvalues. We take a set of <code class="code-Mathematica">Npts</code> random samples in momentum space and partition this set into <code class="code-Mathematica">Nruns</code> subsets. The dimension of **Brillouin zone** is defined by the genus of the compactified primitive cell and is {math}`2 \cdot genus`, which we specify by passing the <code class="code-Mathematica">genus</code> as an argument. As such, we compute the eigenvalues with the following function:

```Mathematica
ComputeEigenvalues[cfH_, Npts_, Nruns_, genus_] := 
  Flatten @ ParallelTable[
    Flatten @ Table[
      Eigenvalues[cfH @@ RandomReal[{-Pi, Pi}, 2 genus]], 
    {i, 1, Round[Npts/Nruns]}], {j, 1, Nruns}, 
  Method -> "FinestGrained"]
```

We compute the Eigenvalues with a set of  {math}`10^6` random samples in momentum space and  {math}`32` subsets:

```Mathematica
evspc = ComputeEigenvalues[Hpc, 10^6, 32];
```

We choose to visualize the density of states via a kernel density estimation with an energy binwidth of {math}`0.005` for the elementary nearest-neighbor model on the primitive cell of the {math}`\{8,8\}`-lattice:

```Mathematica
SmoothHistogram[evals, 0.005, "PDF",
  Frame -> True, FrameLabel -> {"Energy E", "Density of states"} FrameStyle -> Black, 
  ImageSize -> 500, ImagePadding -> {{Automatic, 10}, {Automatic, 10}}, LabelStyle -> 20,
  PlotLabel -> "Primitive cell (T2.6); k sampling: 10^6", PlotRange -> All]
```

<figure class="text-center">
  <picture>
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/dos_88_T2.6.png">
    <img src="../../media/figs/getSetGoHyperBloch/dos_88_T2.6.png" class="figure-img img-fluid rounded" alt="density of Abelian Bloch states of the elementary nearest-neighbor model on the primitive cell T2.6 of the {8,8} lattice" width="500"/>
  </picture>
</figure>


### First supercell

#### Import the cell and supercell model graph

The cell graph for the compactified translation supercell can be imported like the one for the primitive cell through the function <code class="code-Mathematica">ImportCellGraphString</code>:

```Mathematica
scell = ImportCellGraphString[Import["(2,8,8)_T3.11_3.hcc"]];
```

The supercell model graph is derived from cell graph can be imported analogously, but requires the use of the function <code class="code-Mathematica">ImportSupercellModelGraphString</code> instead:

```Mathematica
scmodel = ImportSupercellModelGraphString[Import["{8,8}-tess_T2.6_3_sc-T3.11.hcs"]];
```

#### Visualize the supercell model graph

Let us visualize the supercell model representation of the nearest-neighbor model:

```Mathematica
VisualizeModelGraph[scmodel,
  CellGraph -> scell,
  Elements -> <|
    ShowCellBoundary -> {ShowEdgeIdentification -> True}
    ShowCellGraphFlattened -> {},
  |>,
  ImageMargins -> 0, ImagePadding -> 10, 
  ImageSize -> 300, NumberOfGenerations -> 3]
```

<figure class="text-center">
  <picture>
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/ENNMSC_88.png">
    <img src="../../media/figs/getSetGoHyperBloch/ENNMSC_88.png" class="figure-img img-fluid rounded" alt="elementary nearest-neighbor model on the {8,8} lattice" width="400"/>
  </picture>
</figure>

#### Hamiltonian and density of states

The construction of the model on the primitive cell already specifies all the model specification for the supercell. In order to construct the elementary nearest-neighbor tight-binding model on the supercell, we just need to replace the model graph with the supercell model graph in the first argument in the function <code class="code-Mathematica">AbelianBlochHamiltonian</code>. In addition, we also need to specify the associated model graph with the option *PCModel*. This captures some of the higher-dimensional irreducible representations on the original primitive cell:

```Mathematica
Hsccf = AbelianBlochHamiltonian[scmodel, 1, 0 &, -1 &, PCModel -> pcmodel, CompileFunction -> True];
```

We compute the Eigenvalues with a set of  {math}`10^5` random samples in momentum space and {math}`32` subsets:

```Mathematica
evssc = ComputeEigenvalues[Hsc, 2*10^5, 32];
```

Once again, we choose to visualize the density of states via a kernel density estimation with an energy binwidth of {math}`0.005` for first consecutive supercell of the primitive cell:

```Mathematica
SmoothHistogram[evssc, 0.005, "PDF",
  Frame -> True, FrameLabel -> {"Energy E", "Density of states"} FrameStyle -> Black, 
  ImageSize -> 500, ImagePadding -> {{Automatic, 10}, {Automatic, 10}}, LabelStyle -> 20,
  PlotLabel -> "Primitive cell (T2.6); k sampling: 2*10^5", PlotRange -> All]
```

<figure class="text-center">
  <picture>
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/dos_88_scT3.11.png">
    <img src="../../media/figs/getSetGoHyperBloch/dos_88_scT3.11.png" class="figure-img img-fluid rounded" alt="density of states of the elementary nearest-neighbor model on the {8,8} lattice as computed using the supercell method with sequence T2.6, T3.11, T5.13, T9.20, T17.29, T33.44, T65.78" width="500"/>
  </picture>
</figure>

<div style="text-align: right;">
  <a href="../../misc/code_snippets/GettingStarted/getting_started_HyperBloch.nb" class="btn btn-primary"><i class="fa-solid fa-download"></i> Download Mathematica Notebook</a>
</div>
<br>