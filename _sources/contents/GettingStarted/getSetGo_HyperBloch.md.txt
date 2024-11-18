
# HyperBloch

```{dropdown} Learning goals
:color: success
:icon: light-bulb

Import of:

* a cell graph,
* a model graph,
* and a supercell model graph file.

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
Export, ProperTriangleGroup, TessellationModelGraph, TGCellGraph, TGCellSymmetric, TGQuotient, TGSuperCellModelGraph
</code>
<br></br>

**HyperBloch**:

<code class="code-Mathematica">
AbelianBlochHamiltonian, AbelianBlochHamiltonianExpression, ImportCellGraphString, ImportModelGraphString, ImportSupercellModelGraphString, ShowCellBoundary, ShowCellGraphFlattened, ShowCellSchwarzTriangles, VisualizeModelGraph
</code>
```

In this tutorial we will see how the cell, model and supercell model graphs, constructed through **HyperCells**, can be imported and visualized in the Poincaré disk through the **HyperBloch** package. Moreover, we go through the intended workflow for the construction of corresponding **Abelian Bloch Hamiltonians** in order to demonstrate the <a target="_blank" href="https://doi.org/10.1103/PhysRevLett.131.226401">supercell method</a> through density of states calculations. 


## Prerequisits **in GAP**

In order to get started with the HyperBloch package we construct nearest-neighbor graphs of the {8,8}-tessellation of the hyperbolic plane through the **HyperCells** package in GAP. We first construct the primitive cell and the model graph (based on the tessellation graph), and finally the supercell, as we have established previously in getting started with [HyperCells](./getSetGo_HyperCells) package:

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

Next, in Mathematica, we load the **HyperBloch** package and set the current directory to the working directory, assuming it contains the **HyperCells** files created above:

```Mathematica
<< PatrickMLenggenhager`HyperBloch`
SetDirectory[NotebookDirectory[]];
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

The model graph is derived from cell graph. In our case it defines a nearest-neighbor graph of the {math}`\{8,8\}`-tesselation of the hyperbolic plane restricted to the primitive cell. It can be imported analogously, but requires the use of the function <code class="code-Mathematica">ImportModelGraphString</code> in order to parse the string and construct the model graph instead: 

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
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/ENNMPC_88.png">
    <img src="../../media/figs/getSetGoHyperBloch/ENNMPC_88.png" class="figure-img img-fluid rounded" alt="elementary nearest-neighbor model on the {8,8} lattice" width="350"/>
  </picture>
</figure>

The function <code class="code-Mathematica">ShowCellGraphFlattened</code> is used to shown all edges connecting pairs of vertices as hyperbolic geodesics in the Poincaré disk. We have passed the cell graph to the option <code class="code-Mathematica">CellGraph</code> which enables us to indicate the unit cell boundary through the function <code class="code-Mathematica">ShowCellBoundary</code>. Moreover, the boundary segments are indicated together with the associated (composite) translations in the translation group {math}`\Gamma_{pc}` and colored according to the boundary identification.

We can further emphasize the **Schwarz triangles** inside the indicated primitive cell through the function <code class="code-Mathematica">ShowCellSchwarzTriangles</code>:

```Mathematica
VisualizeModelGraph[pcmodel,
  CellGraph -> pcell,
  Elements -> <|
   	ShowCellBoundary -> {ShowEdgeIdentification -> True},
   	ShowCellSchwarzTriangles -> {TriangleStyle -> FaceForm[GrayLevel[0.5]]}
  |>,
  ImageSize -> 300,
  NumberOfGenerations -> 2]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/ENNMPC_UnitCell_88.png">
    <img src="../../media/figs/getSetGoHyperbloch/ENNMPC_UnitCell_88.png" class="figure-img img-fluid rounded" alt="{8,8} pc" width="350"/>
  </picture>
</figure>

There are 8 Schwarz triangles in the primitive cell associated with the chosen representatives in the **right transversal** {math}`T_{\Delta^{+}}(\Gamma_{pc})`.

#### Construct the Hamiltonian

In order to construct the **Abelian Bloch Hamiltonian**, parameters need to be assigned to the vertices and the edges in the model graph. This takes a very compact form for an elementary nearest-neighbour tight-binding model. In order to illustrate the procedure, we will start with the most general assignment strategy and demonstrate the compact form afterwards.

```{admonition} Skip to subsection [Compact strategy](#cs)
:class: seealso-icon

On a first reading, you may want to skip the section "General strategy" and continue with the section "Compact strategy".
```

##### General strategy

###### Number of orbitals

Every model graph can be equipped with **multiple orbitals** per site, and even with a varying number of orbitals at each site. We will construct more involved models with multiple orbitals per site in the [Higher-order topology](../Tutorials/HigherOrder_topology.md) tutorial, for now, however, we will set the number of orbitals to one:

```Mathematica
norbits = 1;
```

Next, we need to assign the parameters which describe the tight-binding model. This is achieved through the vertices and edges specified in the model graph. Each, should be associated with a coupling constant such that they can be called through a function or an <code class="code-Mathematica">Association</code>.

###### On-site terms

**On-site** terms in the Hamiltonian are associated with vertices in the model graph. As such, it is instructive to explicitly print these vertices by using the function <code class="code-Mathematica">VertexList</code>, which takes as argument the graph representation:

```Mathematica
VertexList@pcmodel["Graph"]
```

There is only one site residing in this particular primitive cell of the {math}`\{8,8\}`-lattice, as such the vertex list contains only one entry ``{{3, 1}}``. Each vertex is given in the form <code class="code-Mathematica">{w, gi}</code>, where <code class="code-Mathematica">w</code> is an integer between <code class="code-Mathematica">1</code> and <code class="code-Mathematica">3</code> indicating the type of vertex of the Schwarz triangle <code class="code-Mathematica">(x, y, z)</code>, i.e., a **Wyckoff position**, and <code class="code-Mathematica">gi</code>  is the position in the transversal {math}`T_{G^+}(G_{w}^{+})` labeling the Schwarz triangle the vertex is a part of, as specified in any <code class="code-Mathematica">HCModelGraph</code>. 
 
We choose to set the on-site term to zero by associating the list of vertices with a list of zeros using an <code class="code-Mathematica">Association</code>:

```Mathematica
mVec = ConstantArray[0, 1]; 
onsitePC = AssociationThread[VertexList@pcmodel["Graph"] -> mVec];
```

###### Hopping terms

The **hopping terms** are associated with edges in the model graph. In analogy with the on-site terms, it is useful to explicitly print the edges using the function <code class="code-Mathematica">EdgeList</code>, which takes as argument the graph representation:

```Mathematica
EdgeList@pcmodel["Graph"]
```

<figure class="text-center">
  <picture>
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/EdgeListPC88.png">
    <img src="../../media/figs/getSetGoHyperBloch/EdgeListPC88.png" class="figure-img img-fluid rounded" alt="Edge list primitive cell {8,8}-lattice" width="600"/>
  </picture>
</figure>

Each element in the list is a <code class="code-Mathematica">DirectedEdge</code>, connecting a pair of vertices. The <code class="code-Mathematica">EdgeTags</code> (nested list above the arrows) for the nearest-neighbour edges take the form <code class="code-Mathematica">{1, {ve, s1, s2}}</code>, where the first entry, <code class="code-Mathematica">1</code>, indicates a nearest-neighbor edge, <code class="code-Mathematica">ve={w, g}</code> specifies the cell-graph edge vertex with <code class="code-Mathematica">w</code> the type of vertex and <code class="code-Mathematica">g</code> the position of the element in {math}`T_{G^{+}}(G_{w}^{+})`, and <code class="code-Mathematica">s1</code>, <code class="code-Mathematica">s2</code> are the positions of the Schwarz triangles associated with the cell-graph edges in {math}`T_{\Delta^{+}}(\Gamma)`. However, this labeling convention comes with some exceptions, which we will explore in more the more involved <a href="./../Tutorials/tutorials.html">HyperBloch package tutorials</a>.

We choose to set the hopping terms to a constant real value {math}`-1` for all edges by associating the edge list with a list of constant values:

```Mathematica
nnHoppingVec = ConstantArray[-1, 4];
hoppingPC = AssociationThread[EdgeList@pcmodel["Graph"] -> nnHoppingVec];
```

If we would consider a more involved model it might be helpful to look at the translation operators associated with the edges:

```Mathematica
pcmodel["EdgeTranslations"]
```

which contains the translation operators ``{g1, g4, ... }``. In our particular case, all edges are associated with a non-trivial translation, i.e., the parameters we have assigned are inter-cell hopping amplitudes. 

The HyperBloch package is equipped with elaborate visualization tools of cell, model and supercell model graphs which can further guide the construction of models in more advanced settings. We will exploit these in subsequent tutorials.

###### Hamiltonian

The Abelian Bloch Hamiltonian can now be set up by passing the model graph and the corresponding coupling constants specified above as arguments to the function <code class="code-Mathematica">AbelianBlochHamiltonian</code> or alternatively <code class="code-Mathematica">AbelianBlochHamiltonianExpression</code>, the former returns the Hamiltonian as a function of momenta. We choose to use the latter for now, in order to print a symbolic expression of the Hamiltonian:

```Mathematica
Hpc = AbelianBlochHamiltonianExpression[pcmodel, norbits, onsitePC, hoppingPC]
```

which in this particular example constructs a {math}`1\times1` matrix as a function of four momenta:

```Mathematica
{ { -2 (Cos[k[1]] + Cos[k[2]] + Cos[k[3]] + Cos[k[4]]) } }
```

(cs)=
##### Compact strategy

The simplicity of the specified model reduces the construction of the Hamiltonian to just one line of code. Once again we set the number of orbitals per site in the second argument to {math}`1`, the on-site term to {math}`0` and the nearest-neighbor coupling to {math}`-1`, with the function <code class="code-Mathematica">AbelianBlochHamiltonian</code>, which returns the Hamiltonian as a function of momenta. A very economic way to do this is through the use of constant <code class="code-Mathematica">Function</code>s instead of <code class="code-Mathematica">Association</code>s:

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

We compute the eigenvalues with a set of  {math}`10^6` random samples in momentum space and  {math}`32` subsets:

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
    ShowCellBoundary -> {ShowEdgeIdentification -> True},
    ShowCellGraphFlattened -> {}
  |>,
  ImageMargins -> 0, ImagePadding -> 15, 
  ImageSize -> 300, NumberOfGenerations -> 3]
```

<figure class="text-center">
  <picture>
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/ENNMSC_88.png">
    <img src="../../media/figs/getSetGoHyperBloch/ENNMSC_88.png" class="figure-img img-fluid rounded" alt="elementary nearest-neighbor model on the {8,8} lattice" width="400"/>
  </picture>
</figure>

Let us further emphasize the Schwarz triangles inside the indicated supercell:

```Mathematica
VisualizeModelGraph[scmodel,
  CellGraph -> scell,
  Elements -> <|
    ShowCellBoundary -> {ShowEdgeIdentification -> True},
    ShowCellSchwarzTriangles -> {
      TriangleStyle -> Directive[ Opacity[0.6], FaceForm[GrayLevel[0.5]]]
      }
  |>,
  ImageSize -> 300, ImageMargins -> 0,
  ImagePadding -> 15, NumberOfGenerations -> 3]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/ENNMSC_UnitCell_88.png">
    <img src="../../media/figs/getSetGoHyperbloch/ENNMSC_UnitCell_88.png" class="figure-img img-fluid rounded" alt="{8,8} pc" width="400"/>
  </picture>
</figure>

There are 16 Schwarz triangles in the supercell associated with the chosen representatives in the right transversal {math}`T_{\Delta^{+}}(\Gamma_{sc})`, as such this particular supercell consists of a symmetric aggregation of two primitive cells.

Since the model on the primitive cell already defines all the necessary model specification for the supercell, we do in general not need to explicitly print the vertices and edges of supercell model graphs. However, it is instructive to do so in order to understand the underlying mechanism:

```{admonition} Skip to subsubsection [Hamiltonian and density of states](#scH)
:class: seealso-icon

On a first read one may want to skip the next two subsubsection "Vertices" and "Edges" and continue at the subsection "Hamiltonian and density of states".
```

##### Vertices
 
Analogous to the model graph, the vertices can be extracted by using the function <code class="code-Mathematica">VertexList</code>, which takes as argument the graph representation:

```Mathematica
VertexList@scmodel["Graph"]
```

There are two site residing in this particular supercell ``{{3, 1, 1}, {3, 1, 2}}``. Vertices in the supercell model graphs are given in the form <code class="code-Mathematica">{w, gi, etaj}</code>, where <code class="code-Mathematica">w</code> is an integer between <code class="code-Mathematica">1</code> and <code class="code-Mathematica">3</code> indicating the type of vertex of the Schwarz triangle <code class="code-Mathematica">(x, y, z)</code>, <code class="code-Mathematica">gi</code> is the position in the transversal {math}`T_{G^{+}}(G_{w}^{+})` labeling the Schwarz triangle the vertex is a part of, and <code class="code-Mathematica">etaj</code> the position of the element in the transversal {math}`T_{\Gamma_{pc}}(\Gamma_{sc})` labeling the copy of the primitive cell containing the vertex inside the supercell, as specified in any <code class="code-Mathematica">HCSupercellModelGraph</code>.

##### Edges

Similarly, the edges can be extracted by using the function <code class="code-Mathematica">EdgeList</code>, which takes as argument the graph representation:

```Mathematica
EdgeList@scmodel["Graph"]
```

<figure class="text-center">
  <picture>
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperBloch/EdgeListSC88.png">
    <img src="../../media/figs/getSetGoHyperBloch/EdgeListSC88.png" class="figure-img img-fluid rounded" alt="Edge list supercell {8,8}-lattice" width="1000"/>
  </picture>
</figure>

The edge tags are of the form <code class="code-Mathematica">{v1pc, v2pc, tagpc}</code> with <code class="code-Mathematica">v1pc, v2pc</code> the positions of the vertices in the primitive cell, and <code class="code-Mathematica">tagpc</code> the tag of the edge in the primitive cell. However, also this labeling convention comes with some exceptions, which we will explore in more the more involved <a href="./../Tutorials/tutorials.html">HyperBloch package tutorials</a>.

(scH)=
#### Hamiltonian and density of states

The construction of the model on the primitive cell already defines all the necessary model specification for the supercell. In order to construct the elementary nearest-neighbor tight-binding model on the supercell, we just need to replace the model graph with the supercell model graph in the first argument in the function <code class="code-Mathematica">AbelianBlochHamiltonian</code>. In addition, we also need to specify the associated model graph with the option *PCModel*. This already captures some of the higher-dimensional irreducible representations on the original primitive cell:

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

Aspects of the content above originate from the  <a target="_blank" href="https:/doi.org/10.5281/zenodo.10142167">Supplementary Data and Code</a>, where more examples are provided and the necessary steps to find the **density of states** of an elementary nearest-neighbor hopping model on the {math}`\{8,8\}`-lattice are discussed in detail.