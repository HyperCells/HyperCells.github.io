# Flat-bands

```{dropdown} Learning goals
:color: success
:icon: light-bulb

Construction of:

* hyperbolic Lieb lattices,
* hyperbolic kagome lattice.
```

```{dropdown}  Featured functions
:color: info
:icon: gear

**HyperCells:**

<code class="code-gap">
Export, KagomeModelGraph, LiebModelGraph, LongestSequence, ProperTriangleGroup, TGCellGraph, TGCellModelGraph, TGCellSymmetric, TGQuotient, TGQuotientSequencesStructure, TGSuperCellModelGraph
</code>
<br></br>

**HyperBloch:**

<code class="code-Mathematica">
AbelianBlochHamiltonian, GetSchwarzTriangle, GetWyckoffPosition, ImportCellGraphString, ImportModelGraphString, ImportSupercellModelGraphString, ShowCellBoundary, ShowCellGraphFlattened,  VisualizeModelGraph
</code>
```

```{dropdown}  Needed functions
:color: warning
:icon: tools

**Mathematica:**

In previous tutorials, [Getting started with the HyperBloch](../GettingStarted/getSetGo_HyperBloch.md) package and HyperBloch [Supercells](./Supercells.md) tutorial, we have calculated the density of states of various nearest-neighbor tight-binding models via exact diagonalization and random samples. We predefine a function in order to calculate the eigenvalues for the Abelian Bloch Hamiltonians that we will construct. We  take advantage of the independence of different momentum sectors and parallelize the computation, where we partition the set of <code class="code-Mathematica">Npts</code> into <code class="code-Mathematica">Nruns</code> subsets:

```Mathematica
ComputeEigenvalues[cfH_, Npts_, Nruns_, genus_] :=
 Flatten@ParallelTable[
   Flatten@Table[
     Eigenvalues[cfH @@ RandomReal[{-Pi, Pi}, 2 genus]], 
    {i, 1, Round[Npts/Nruns]}], {j, 1, Nruns}, 
  Method -> "FinestGrained"]
```

The HyperCells package contains built-in functions for several tight-binding models such as:

* <code class="code-gap">TessellationModelGraph</code> which constructs a tessellation graph from a cell graph of a triangle group, i.e. the nearest-neighbor graphs of the {math}`\{p,q\}`-tesselation of the hyperbolic plane.

* <code class="code-gap">LiebModelGraph</code> which constructs a Lieb graph from a cell graph of a triangle group.

* <code class="code-gap">KagomeModelGraph</code> which constructs a kagome graph from a cell graph of a triangle group.

* <code class="code-gap">TGCellModelGraph</code> which constructs a model graph from a cell graph and a specification of which cell-graph vertices are to be used as vertices of the model graph, which define edges, and
which define faces of the model graph.

as well as :

* <code class="code-gap">AddOrientedNNNEdgesToTessellationModelGraph</code> which modifies the {math}`\{p,q\}`-tesselation model graph model by adding oriented next-nearest neighbor edges to all faces with at least five edges.

Previously, in the tutorials [Getting started with the HyperBloch](../GettingStarted/getSetGo_HyperBloch.md) and [Supercells](./Supercells.md), we have constructed tessellation graphs. In this tutorial we will construct hyperbolic Lieb lattices and hyperbolic kagome lattices on primitive cells and supercells. Both constructions rely on the <code class="code-gap">TGCellModelGraph</code> function which we will discuss afterwards.

```{admonition} Skip to page [Haldane model](./Haldane_model.md)
:class: seealso-icon

The construction of next-nearest-neighbor model graphs through the function <code class="code-gap">AddOrientedNNNEdgesToTessellationModelGraph</code> will be discussed in the next tutorial on hyperbolic Haldane models.
```

## {math}`\{6,4\}`-Lieb lattice

Hyperbolic Lieb lattices are specified by placing vertices at **Wyckoff positions** <code class="code-gap">1</code> and <code class="code-gap">2</code> for {math}`\{p,q\}`-tesselations of the hyperbolic plane (here we choose <code class="code-gap">1</code> and <code class="code-gap">2</code> corresponding to the <code class="code-gap">x</code> and <code class="code-gap">y</code> vertices of the fundamental Schwarz triangle). It is instructive to jump a bit ahead to look at the two Wyckoff positions and the fundamental Schwarz in the Poincaré disk, which we will properly discuss shortly after:

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/FlatBands/LiebLattice{6,4}_Wyckoff.png">
    <img src="../../media/figs/Tutorials/FlatBands/LiebLattice{6,4}_Wyckoff.png" class="figure-img img-fluid rounded" alt="{6,4}-Lieb lattice w" width="450"/>
  </picture>
</figure>

Next, let us start by constructing a cell graph on the primitive cell for the {math}`\{6,4\}`-lattice in **GAP**:

```gap
# Primitive cell:
# ---------------
tg := ProperTriangleGroup( [ 2, 4, 6 ] );
qpc := TGQuotient( 1, [ 2, 4, 6 ] );
cgpc := TGCellGraph( tg, qpc, 3 : simplify := 5 );
Export( cgpc, "(2,4,6)_T2.2_3.hcc" ); # export
```

Analogous to the <code class="code-gap">TessellationModelGraph</code> function, all built-in model graph functions only need to be specified on the **primitive cell**. The model specifications are inherited by subsequent supercell model graphs. The Lieb lattice can be constructed as follows:

```gap
# Lieb lattice:
# -------------
# elementary nearest-neighbor model
model_Lieb := LiebModelGraph( cgpc );
Export( model_Lieb, "{6,4}-Lieb_T2.2_3.hcm" ); # export
```

We choose a supercell sequence by following the central concepts discussed in the tutorial [Supercells](./Supercells.md) and [Coherent sequences](./Coherent_SC_sequences.md):

```gap
# Supercells:
# -----------
tgQS := TGQuotientSequencesStructure(tg : boundByGenus := 10);;
sequence := LongestSequence(tgQS : quotient := 1);
sc_lst := sequence{[2..Length(sequence)]};

for sc_i_index in sc_lst do

  qsc_i := TGQuotient( sc_i_index );
  sc_i := TGCellSymmetric(tg, qsc_i, 3);
  scmodel_i := TGSuperCellModelGraph(model_Lieb, sc_i);
  
  sc_i_label := StringFormatted("_T2.2_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
  scmodel_i_name := JoinStringsWithSeparator(["{6,4}-Lieb", sc_i_label], "");
  Export(scmodel_i,  scmodel_i_name); # export
od;
```

<div class="flex ">
  <a href="../../misc/code_snippets/Tutorials/FlatBands/tutorial_FlatBands_{6,4}-Lieb_HyperCells_pc_sc_files.zip" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download generated files</a>
  <a href="../../misc/code_snippets/Tutorials/FlatBands/tutorial_FlatBands_{6,4}-Lieb_HyperCells.g" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download GAP Code</a>
</div>
<br></br>

Next, in **Mathematica** we load the HyperBloch package, set the working directory of the files we have created through the HyperCells package and in addition define a list of available unit cells together with the corresponding genera of the compactified unit cells:

```Mathematica
(* Preliminaries *)
<< PatrickMLenggenhager`HyperBloch`
SetDirectory[NotebookDirectory[]];

cellsLieb = {"T2.2", "T5.4", "T9.3"}; 
genusLstLieb = {2, 5, 9};
```

The cell, model and supercell model graph can now be imported by parsing the imported strings with the functions <code class="code-Mathematica">ImportCellGraphString</code>, <code class="code-Mathematica">ImportModelGraphString</code> and <code class="code-Mathematica">ImportSupercellModelGraphString</code>, respectively:

```Mathematica
(* Primitive cell *)
pcellLieb = ImportCellGraphString[Import["(2,4,6)_T2.2_3.hcc"]];
pcmodelLieb = ImportModelGraphString[Import["{6,4}-Lieb_T2.2_3.hcm"]];

(* Import supercells *)
scmodelsLieb = Association[# -> 
  ImportSupercellModelGraphString[ 
    Import["{6,4}-Lieb_T2.2_3_sc-" <> # <> ".hcs"]] 
  &/@ cellsLieb[[2 ;;]]];
```

It is instructive to visualize the graph representation of the model in the primitive cell after the model graph has been imported. Moreover, we choose to highlight the two Wyckoff positions and the fundamental Schwarz in the Poincaré disk. 

We can visualize Wyckoff positions of the fundamental Schwarz triangle through the function <code class="code-Mathematica">GetWyckoffPosition</code>, which enables us to extract the corresponding coordinates in the Poincaré disk, where we will use the label <code class="code-Mathematica">"1"</code> that identifies the symmetry operation relating the vertices of the fundamental Schwarz triangle to the Wyckoff positions:


```Mathematica
x = GetWyckoffPosition[{2, 4, 6}, {1, "1"}];
y = GetWyckoffPosition[{2, 4, 6}, {2, "1"}];
```

We can highlighted individual Schwarz triangles in the Poincaré disk through the function <code class="code-Mathematica">GetSchwarzTriangle</code>. Let us extract the <code class="code-Mathematica">Polygon</code> representing the fundamental Schwarz triangle associated with the identity element in the proper triangle group {math}`\Delta^{+}(2,4,6)`:

```Mathematica
sf = GetSchwarzTriangle[{2, 4, 6}, "1"];
```

We can highlight the two Wyckoff positions and the fundamental Schwarz triangle in the graph representation of the nearest-neighbor tight-binding model model as follows:

```Mathematica
Show[
 VisualizeModelGraph[pcmodelLieb,
  CellGraph -> pcellLieb,
  NumberOfGenerations -> 3,
  Elements -> <|
    	ShowCellGraphFlattened -> {},
    	ShowCellBoundary -> {ShowEdgeIdentification -> True}
    |>],
 
 Graphics[{Darker[Gray, 0.01], Opacity[0.4], sf}],
 Graphics[{Text[Style["s_f", 17, Thick, White], {0.3, 0.09}]}],
 
 Graphics[{Darker[Green, 0.3], PointSize[0.03], Point@x}],
 Graphics[{Darker[Blue, 0.3], PointSize[0.03], Point@y}],
 
 Graphics[{Darker[Green, 0.5], Text[Style["1", 17, Thick], {0.30, 0.17}]}],
 Graphics[{Darker[Blue, 0.5], Text[Style["2", 17, Thick], {0.43, 0.00}]}],
 
 ImageSize -> 400
 ]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/FlatBands/LiebLattice{6,4}_T2.2.png">
    <img src="../../media/figs/Tutorials/FlatBands/LiebLattice{6,4}_T2.2.png" class="figure-img img-fluid rounded" alt="{6,4}-Lieb lattice pc" width="450"/>
  </picture>
</figure>

Unlike the edge tags of tesselation and kagome model graphs, see [Getting started with the HyperBloch package](../GettingStarted/getSetGo_HyperBloch.md), the edge tags of Lieb models graphs are of a reduced form. Let us take a look at the edges in the model graph:

```Mathematica
EdgeList@pcmodelLieb["Graph"]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/FlatBands/ENNMPC_Lieb_64.png">
    <img src="../../media/figs/Tutorials/FlatBands/ENNMPC_Lieb_64.png" class="figure-img img-fluid rounded" alt="{6,4}-Lieb lattice pc edges" width="400"/>
  </picture>
</figure>

Each element in the list is a <code class="code-Mathematica">DirectedEdge</code>, connecting a pair of vertices. The <code class="code-Mathematica">EdgeTags</code> (the list above the arrows) for the nearest-neighbour edges take the form <code class="code-Mathematica">{1, s}</code>, where the first entry, <code class="code-Mathematica">1</code>, indicates a nearest-neighbor edge, and <code class="code-Mathematica">s</code> is the positions of the Schwarz triangles associated with the cell-graph edges in {math}`T_{\Delta^{+}}(\Gamma)`.

Once the (supercell) model graphs are imported the corresponding Abelian Bloch Hamiltonians for the elementary nearest-neighbor hopping model can be constructed. We set the number of orbital per site to one, the on-site terms {math}`0` and the nearest-neighbor hopping amplitudes to {math}`-1`: 

```Mathematica
(* primitive cell *)
HpcLieb = AbelianBlochHamiltonian[pcmodelLieb, 1, 0 &, -1 &, CompileFunction -> True];

(* supercells *)
HscLieblst = Association[# -> 
  AbelianBlochHamiltonian[scmodelsLieb[#], 1, 0 &, -1 &, PCModel -> pcmodelLieb, CompileFunction -> True] 
  &/@ cellsLieb[[2 ;;]] ];

(* all *)
HcLieblst = Join[Association[cellsLieb[[1]] -> HpcLieb], HscLieblst];
```

The supercell method can be applied as usual, where we use the function <code class="code-gap">ComputeEigenvalues</code>, which can be found in the dropdown menu **Needed function** above:

```Mathematica
(* color maps *)
cLst = (ColorData["SunsetColors", "ColorFunction"] /@ (1 - Range[1, 3]/3.));

(* Compute the Eigenvalues *)
evalsLieb = Association[# ->  ComputeEigenvalues[HcLieblst[#], 10^4, 32, genusLstLieb[#]]&/@cellsLieb];

(* Visualize *)
SmoothHistogram[evalsLieb, 0.01, "PDF",
  Frame -> True, FrameLabel -> {"Energy E", "Density of states"} FrameStyle -> Black, 
  ImageSize -> 500, ImagePadding -> {{Automatic, 10}, {Automatic, 10}}, LabelStyle -> 20,
  PlotLabel -> "k sampling: 10^4", PlotRange -> All, PlotStyle -> cLst]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/FlatBands/dos_Lieb_64_scm.png">
    <img src="../../media/figs/Tutorials/FlatBands/dos_Lieb_64_scm.png" class="figure-img img-fluid rounded" alt="{6,4}-Lieb lattice pc" width="600"/>
  </picture>
</figure>

Pronounced flat-bands emerge in density of states, centered around zero energy 
with gaps developing between the flat-band and the dispersive part of the spectrum.

<div style="text-align: right;">
  <a href="../../misc/code_snippets/Tutorials/FlatBands/tutorial_FlatBands_{6,4}-Lieb_HyperBloch.nb" class="btn btn-primary"><i class="fa-solid fa-download"></i> Download Mathematica Notebook</a>
</div>


## {math}`\{8,3\}`-kagome lattice

Hyperbolic kagome lattices can be constructed just as easily as hyperbolic Lieb lattices. These lattices are specified by placing vertices at Wyckoff positions <code class="code-gap">1</code>. These lattices are **restricted to {math}`\{p,3\}`-tesselation** of the hyperbolic plane. Once again, we start by constructing the cell graph and model graph for the primitive cell in **GAP**:

```gap
# Primitive cell:
# ---------------
tg := ProperTriangleGroup( [ 2, 3, 8 ] );
qpc := TGQuotient( 1, [ 2, 3, 8 ] );
cgpc := TGCellGraph( tg, qpc, 3 : simplify := 5 );
Export( cgpc, "(2,3,8)_T2.1_3.hcc" ); # export
```

The kagome lattice can be constructed as follows:

```gap
# Kagome lattice:
# ---------------
model_kagome := KagomeModelGraph( cgpc );
Export( model_kagome, "{8,3}-kagome_T2.1_3.hcm" ); # export
```

with supercells:

```gap
# Supercells:
# -----------
tgQS := TGQuotientSequencesStructure(tg : boundByGenus := 20);;
sequence := LongestSequence(tgQS : quotient := 1);
sc_lst := sequence{[2..Length(sequence)]};

for sc_i_index in sc_lst do

  qsc_i := TGQuotient( sc_i_index );
  sc_i := TGCellSymmetric(tg, qsc_i, 3);
  scmodel_i := TGSuperCellModelGraph(model_kagome, sc_i);

  sc_i_label := StringFormatted("_T2.1_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
  scmodel_i_name := JoinStringsWithSeparator(["{8,3}-kagome", sc_i_label], "");
  Export(scmodel_i,  scmodel_i_name); # export
od;
```

<div class="flex ">
  <a href="../../misc/code_snippets/Tutorials/FlatBands/tutorial_FlatBands_{8,3}-kagome_HyperCells_pc_sc_files.zip" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download generated files</a>
  <a href="../../misc/code_snippets/Tutorials/FlatBands/tutorial_FlatBands_{8,3}-kagome_HyperCells.g" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download GAP Code</a>
</div>
<br></br>

We can proceed anologously to the hyperbolic Lieb lattice in **Mathematica**, we omitt the detailed specificities which can be found in the downloadable files. As such, let us visualize the {math}`\{8,3\}`-kagome lattice: 

```Mathematica
VisualizeModelGraph[pcmodelKagome,
  CellGraph -> pcellKagome,
  Elements -> <|
        ShowCellGraphFlattened -> {},
   	ShowCellBoundary -> {ShowEdgeIdentification -> True}
  |>,
  ImageSize -> 400,
  NumberOfGenerations -> 3]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/FlatBands/KagomeLattice{8,3}_T2.1.png">
    <img src="../../media/figs/Tutorials/FlatBands/KagomeLattice{8,3}_T2.1.png" class="figure-img img-fluid rounded" alt="{6,4}-Lieb lattice pc" width="450"/>
  </picture>
</figure>

The application of the supercell method shows a fast convergence to the thermodynamic limit in the density of states:

```Mathematica
dos = SmoothHistogram[evalsKagome, 0.01, "PDF",
  Frame -> True, FrameLabel -> {"Energy E", "Density of states"} FrameStyle -> Black, 
  ImageSize -> 500, ImagePadding -> {{Automatic, 10}, {Automatic, 10}}, LabelStyle -> 20,
  PlotLabel -> "k sampling: 2*10^4", PlotRange -> All, PlotStyle -> cLst]

```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/FlatBands/dos_kagome_83_scm.png">
    <img src="../../media/figs/Tutorials/FlatBands/dos_kagome_83_scm.png" class="figure-img img-fluid rounded" alt="{6,4}-Lieb lattice pc" width="600"/>
  </picture>
</figure>

The density of states for the {math}`\{8,3\}`-lattice exhibits pronounced flat-band centered at {math}`E=2` with gaps developing between the flat-band and the dispersive part of the spectrum. The accumulation of higher-dimensional irreducible representations on the primitive cell through the supercell method comes with a characteristic density of states suppression near the edges. As such, let us take a closer look at the band edge in the vicinity of the flat-band:

```Mathematica
Show[dos,
 Epilog -> {
   Inset[Show[First@dos,
     FrameLabel -> None, Frame -> True, ImageSize -> 200,
     LabelStyle -> 15, PlotRange -> {{1.85, 2.05}, {0, 0.4}},
     PlotLabel -> None], {-2, 0.65}]
   }]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/FlatBands/dos_kagome_inset_83_scm.png">
    <img src="../../media/figs/Tutorials/FlatBands/dos_kagome_inset_83_scm.png" class="figure-img img-fluid rounded" alt="{6,4}-Lieb lattice pc" width="600"/>
  </picture>
</figure>

The density of states between the flat-band and the dispersive bands is suppressed with increasing supercell size, such that in the thermodynamic limit the flat-band is detached. This suggests that the gaplessness for the primitive cell is a finite-size effect.

<div style="text-align: right;">
  <a href="../../misc/code_snippets/Tutorials/FlatBands/tutorial_FlatBands_{8,3}-kagome_HyperBloch.nb" class="btn btn-primary"><i class="fa-solid fa-download"></i> Download Mathematica Notebook</a>
</div>

