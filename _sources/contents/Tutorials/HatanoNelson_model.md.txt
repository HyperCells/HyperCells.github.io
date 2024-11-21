# Hatano-Nelson model

```{dropdown} Learning goals
:color: success
:icon: light-bulb

Construction of **non-Hermitian** Abelian Bloch Hamiltonians of:

* a tight-binding model with Hermiticity-breaking gains and losses
* and a variant of the Hatano-Nelson model for the {math}`\{6,4\}`-lattice.
```

```{dropdown}  Featured functions
:color: info
:icon: gear

**HyperCells:**

<code class="code-gap">
Export, LongestSequence, ProperTriangleGroup, TGCellSymmetric, TessellationModelGraph, TGQuotient,  TGQuotientSequencesStructure,   TGSuperCellModelGraph
</code>
<br></br>

**HyperBloch:**

<code class="code-Mathematica">
AbelianBlochHamiltonian, GetCellGraphEdge, ImportCellGraphString, ImportModelGraphString, ImportSupercellModelGraphString, NonReciprocalAbelianBlochHamiltonian, ShowCellBoundary, ShowCellGraphFlattened, VisualizeModelGraph
</code>
```

```{dropdown}  Needed functions
:color: warning
:icon: tools

**Mathematica:**

In previous tutorials, such as [Getting started with the HyperBloch package](../GettingStarted/getSetGo_HyperBloch.md) and HyperBloch [Supercells](./Supercells.md) tutorial etc., we have calculated the density of states of various nearest-neighbor tight-binding models via exact diagonalization and random samples. We predefine a function in order to calculate the eigenvalues for the (non-reciprocal) Abelian Bloch Hamiltonians that we will construct. We  take advantage of the independence of different momentum sectors and parallelize the computation, where we partition the set of <code class="code-Mathematica">Npts</code> into <code class="code-Mathematica">Nruns</code> subsets:

```Mathematica
ComputeEigenvalues[cfH_, Npts_, Nruns_, genus_] :=
 Flatten@ParallelTable[
   Flatten@Table[
     Eigenvalues[cfH @@ RandomReal[{-Pi, Pi}, 2 genus]], 
    {i, 1, Round[Npts/Nruns]}], {j, 1, Nruns}, 
  Method -> "FinestGrained"]
```


The HyperBloch package provides a framework for the construction of Abelian Bloch Hamiltonians of Hermitian as well as **non-Hermitian systems**. In principle, the workflow for the construction of non-Hermitian compared to Hermitian models is unchanged. However, particular attention is required when assigning coupling constants. In this tutorial we will see how non-Hermitian hyperbolic lattice models can be set up through the construction of nearest-neighbor tight-binding models on the {math}`\{6,4\}`-lattice. Specifically, we will consider Hermiticity-breaking terms, such as gains and losses, and a variant of the **Hatano-Nelson model**.


## Prerequisits

In order to construct the Abelian Bloch Hamiltonian for the two non-Hermitian models, we need to create the necessary files using the HyperCells package in **GAP**: 

```gap
# load the HyperCells package
LoadPackage( "HyperCells" );
tg := ProperTriangleGroup( [ 2, 4, 6 ] );

# Primitive cell:
# ---------------
qpc := TGQuotient( 1, [ 2, 4, 6 ] );
cgpc := TGCellGraph( tg, qpc, 3 : simplify := 5 );
Export( cgpc, "(2,4,6)_T2.2_3.hcc" ); # export

# specify underlying model graph
model := TessellationModelGraph(cgpc);
Export(model, "{6,4}-tess-NN_T2.2_3.hcm");
```

We choose a supercell sequence by following the central concepts discussed in the tutorial [Supercells](./Supercells.md) and [Coherent sequences](./Coherent_SC_sequences.md). The model specifications are inherited by subsequent supercell model graphs:

```gap
# Supercells:
# -----------
tgQS := TGQuotientSequencesStructure(tg : boundByGenus := 10);;
sequence := LongestSequence(tgQS : quotient := 1);
sc_lst := sequence{[2..Length(sequence)]};

for sc_i_index in sc_lst do
    qsc_i := TGQuotient( sc_i_index );

    sc_i := TGCellSymmetric(tg, qsc_i, 3);
    scmodel_i := TGSuperCellModelGraph(model, sc_i);

    sc_i_label := StringFormatted("_T2.2_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
    scmodel_i_name := JoinStringsWithSeparator(["{6,4}-tess-NN", sc_i_label], "");
    Export(scmodel_i,  scmodel_i_name); # export file
od;
```

<div class="flex ">
  <a href="../../misc/code_snippets/Tutorials/HatanoNelsonModel/tutorial_HatanoNelsonModel_HyperCells_pc_sc_files.zip" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download generated files</a>
  <a href="../../misc/code_snippets/Tutorials/HatanoNelsonModel/tutorial_HatanoNelsonModel_HyperCells.g" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download GAP Code</a>
</div>
<br>

As usual, we load the HyperBloch package, set the working directory of the files we have created through the HyperCells package, define a list of available unit cells together with the corresponding genera of the compactified unit cells and import the cell, model and supercell model graph:

```Mathematica
(* Preliminaries *)
<< PatrickMLenggenhager`HyperBloch`
SetDirectory[NotebookDirectory[]];

(* Labels and genera *)
cells = {"T2.2", "T5.4", "T9.3"}; 
genusLst = {2, 5, 9};

(* Import cell and model graph of the primitive cell *)
pcell = ImportCellGraphString[Import["(2,4,6)_T2.2_3.hcc"]];
pcmodel = ImportModelGraphString[Import["{6,4}-tess-NN_T2.2_3.hcm"]];

(* Import supercell model graph *)
scmodels = Association[# -> 
    ImportSupercellModelGraphString[Import["{6,4}-tess-NN_T2.2_3_sc-" <> # <> ".hcs"]] 
  &/@cells[[2 ;;]]];
```

It is instructive to visualize the {math}`\{6,4\}`-tesselation model graph in order to properly assign the coupling constants:

```Mathematica
VisualizeModelGraph[pcmodel,
	CellGraph -> pcell,
	Elements -> <|
		ShowCellGraphFlattened -> {},
		ShowCellBoundary -> {ShowEdgeIdentification -> True}
	|>, 
  ImageSize -> 300,
  NumberOfGenerations -> 3]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HatanoNelson/{6,4}-tess-NN_pc_T2.2.png">
    <img src="../../media/figs/Tutorials/HatanoNelson/{6,4}-tess-NN_pc_T2.2.png" class="figure-img img-fluid rounded" alt="Tessellation model {6,4}-lattice" width="380"/>
  </picture>
</figure>


## Non-Hermitian on-site terms

We choose to endow the {math}`\{6,4\}`-lattice with gains and losses by introducing a **staggered complex on-site potential**. Since the hyperbolic hexagons have an even number of sides the lattice can be considered as bipartite such that a sublattice mass can be realized with {math}`\pm (M + i \eta)`. It is instructive to take a look at the list of vertices in the model graph in order to identify the sub-lattices:

```Mathematica
VertexList@pcmodel["Graph"]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HatanoNelson/vertices_{6,4}-tess-NN_pc_T2.2.png">
    <img src="../../media/figs/Tutorials/HatanoNelson/vertices_{6,4}-tess-NN_pc_T2.2.png" class="figure-img img-fluid rounded" alt="Vertices tessellation model {6,4}-lattice" width="500"/>
  </picture>
</figure>

Comparing the list of vertices with the model representation we have previously visualized, we can assign the staggered on-site potential as follows:

```Mathematica
mVec = (M + I eta) {1, -1, -1, 1, 1, -1}; 
onsitePC = AssociationThread[VertexList@pcmodel["Graph"] -> mVec];
```

The non-Hermitian Abelian Bloch Hamiltonians with complex staggered on-site potentials can be constructed through the <code class="code-Mathematica">AbelianBlochHamiltonian</code> function, where we set the nearest-neighbor hopping amplitudes to <code class="code-Mathematica">-1</code>:

```Mathematica
Hpc = AbelianBlochHamiltonian[pcmodel, 1, onsitePC, -1 &, CompileFunction -> True];
```
and correspondingly for the supercells:

```Mathematica
Hsclst = Association[# -> 
    AbelianBlochHamiltonian[scmodels[#], 1, onsitePC, -1 &, PCModel -> pcmodel, CompileFunction -> True] 
  &/@cells[[2 ;;]]];
```

For convenience, let us collect the constructed Hamiltonians in one Association:

```Mathematica
Hclst = Join[Association[cells[[1]] -> Hpc], Hsclst];
```

The supercell method can be applied as usual, where we use the function ComputeEigenvalues, which can be found in the dropdown menu **Needed function** above:

```Mathematica
evals = Association[# -> 
    ComputeEigenvalues[Hclst[#] /. {M -> 0.1, Eta -> 1}, 10^4, 32, genusLst[#]] 
  &/@cells];
```

The complex spectrum can be visualized by using the built-in function <code class="code-Mathematica">ComplexListPlot</code> of Mathematica. However, this might take a few minutes to be displayed. As such let us thin down our data sets by taking smaller subsets through random samples:

```Mathematica
ComplexRandomThinning[evs_, Npts_] := Module[{keys},
  keys = Keys[evs];
  Association[
   Table[key -> RandomSample[Flatten[evs[key]], Npts],
    {key, keys}]]]
```

The complex spectrum exhibits a **line gap**:

```Mathematica
(* color maps *)
cLst = (ColorData["SunsetColors", "ColorFunction"] /@ (1 - Range[1, 3]/3.));

ComplexListPlot[ComplexRandomThinning[evals, 1000],
 AspectRatio -> 1/1.5, Frame -> True, FrameLabel -> {"Re{E}", "Im{E}"},
 FrameStyle -> Directive[Black, 30], ImageSize -> 500, LabelStyle -> 20, 
 PlotMarkers -> {"\[FilledCircle]", Scaled[0.015]},
 PlotRange -> {{-4, 4}, {-1.1, 1.1}}, PlotStyle -> cLst]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HatanoNelson/spec_complex_64_onsite.png">
    <img src="../../media/figs/Tutorials/HatanoNelson/spec_complex_64_onsite.png" class="figure-img img-fluid rounded" alt="Complex spectra, on-site, {6,4}-lattice" width="500"/>
  </picture>
</figure>


## {math}`\{6,4\}`-Hatano-Nelson model

Other Hermiticity-breaking terms, aside from gains and losses, are for example non-reciprocal hopping amplitudes, most prominently used in the Hatano-Nelson model for a Euclidean one dimensional system with asymmetric hopping terms. A possible variant of the Hatano-Nelson model for the {math}`\{6,4\}`-lattice consists of (weakly) coupled 1 dimensional chains with asymmetric hopping amplitudes and zero on-site potential. Each chain follows a hyperbolic geodesic and consists of a particular pair of vertices connected through directed edges in the model graph. Let us take a look at the list of edges in order to construct it:

```Mathematica
EdgeList@pcmodel["Graph"]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HatanoNelson/edges_{6,4}-tess-NN_pc_T2.2.png">
    <img src="../../media/figs/Tutorials/HatanoNelson/edges_{6,4}-tess-NN_pc_T2.2.png" class="figure-img img-fluid rounded" alt="Vertices tessellation model {6,4}-lattice" width="1000"/>
  </picture>
</figure>

 We choose to asymmetrically couple the vertices  <code class="code-Mathematica">{{2,1},{2,2}}</code>, <code class="code-Mathematica">{{2,3},{2,5}}</code> and <code class="code-Mathematica">{{2,4},{2,6}}</code>. It is helpful to visualize the corresponding directed edges in the model graph by first defining the list:

```Mathematica
edgesInChains = {
    DirectedEdge[{2,1}, {2,2}], DirectedEdge[{2,2}, {2,1}], 
    DirectedEdge[{2,3}, {2,5}], DirectedEdge[{2,5}, {2,3}], 
    DirectedEdge[{2,4}, {2,6}], DirectedEdge[{2,6}, {2,4}]}
```

We can make use of the option <code class="code-Mathematica">EdgeFilter</code> within the option <code class="code-Mathematica">ShowCellGraphFlattened</code> in the function <code class="code-Mathematica">VisualizeModelGraph</code> in order to visualize the corresponding one dimensional chains. Therefore, the graph representation of the Hatano-Nelson with decoupled one dimensional chains on the primitive cell looks as follows:

```Mathematica
HNgraph = VisualizeModelGraph[pcmodel,
 CellGraph -> pcell,
 Elements -> <|
   ShowCellGraphFlattened -> {EdgeFilter -> (MemberQ[edgesInChains, #[[{1, 2}]]] &)},
   ShowCellBoundary -> {ShowEdgeIdentification -> True}
   |>,
  ImageSize -> 300,
  NumberOfGenerations -> 3]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HatanoNelson/1DChains_{6,4}-tess-NN_pc_T2.2.png">
    <img src="../../media/figs/Tutorials/HatanoNelson/1DChains_{6,4}-tess-NN_pc_T2.2.png" class="figure-img img-fluid rounded" alt="Vertices tessellation model {6,4}-lattice" width="380"/>
  </picture>
</figure>

It is instructive to also visualize the equivalent (translated) inter-cell edges starting outside the cell and ending inside. First, let us extract the inter-cell edges. Each inter-cell edge is associated with a non-trivial translation:

```Mathematica
pcmodel["EdgeTranslations"]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HatanoNelson/EdgeTranslations.png">
    <img src="../../media/figs/Tutorials/HatanoNelson/EdgeTranslations.png" class="figure-img img-fluid rounded" alt="EdgeTranslations {6,4}-tess model" width="700"/>
  </picture>
</figure>

In addition, we restrict the list to the edges present in the Hatano-Nelson chains specified in our previously defined list:

```Mathematica
intercedges = Select[
    Transpose[{EdgeList@pcmodel["Graph"], pcmodel["EdgeTranslations"]}], 
    MemberQ[edgesInChains, #[[1, {1, 2}]]] && #[[2]] != "1" &][[;;, 1]
  ];
```

We can use the function <code class="code-Mathematica">GetCellGraphEdge</code> and its option <code class="code-Mathematica">ShowEquivalentEdge</code> in order visualize specific edges and equivalent (translated) inter-cell edges in the Poincaré disk:

```Mathematica
Show[HNgraph,
 Graphics[{AbsoluteThickness[2],
    GetCellGraphEdge[pcmodel, #, ShowEquivalentEdge -> True] /. Line -> Arrow}] 
  &/@intercedges]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HatanoNelson/1DChains_complete_{6,4}-tess-NN_pc_T2.2.png">
    <img src="../../media/figs/Tutorials/HatanoNelson/1DChains_complete_{6,4}-tess-NN_pc_T2.2.png" class="figure-img img-fluid rounded" alt="Vertices tessellation model {6,4}-lattice" width="380"/>
  </picture>
</figure>

The visualization enables us to ensure we construct the corresponding Abelian Bloch Hamiltonian consistently. The hopping amplitudes can be assigned by inspecting the list of edges in the model graph, however, we may as well choose to proceed programmatically by filtering through the list:

```Mathematica
hoppingVecHatanoNelson = If[MemberQ[edgesInChains, #[[{1, 2}]]], 1, 0] 
  &/@EdgeList[pcmodel["Graph"]];
```

In addition, we define another vector which we will use to (weakly) couple the Hatano-Nelson chains by symmetric hopping amplitudes:

```Mathematica
hoppingVecPerturbation = If[MemberQ[edgesInChains, #[[{1, 2}]]], 0, 1]
  &/@EdgeList[pcmodel["Graph"]];
```

Through the multiplication of the vector <code class="code-Mathematica">hoppingVecHatanoNelson</code> with the hopping amplitudes {math}`(t \pm \gamma)` in the canonical and opposite to the canonical direction, respectively, we are able to realize the Hatano-Nelson chains. These chains can be coupled by adding the vector <code class="code-Mathematica">hoppingVecPerturbation</code> multiplied by the hopping amplitude {math}`\delta`:

```Mathematica
(* Canonical direction *)
hoppingVecCanonical = (t + gamma) hoppingVecHatanoNelson + delta  hoppingVecPerturbation;
hoppingsPCCanonical = AssociationThread[EdgeList@pcmodel["Graph"] -> hoppingVecCanonical];

(* Opposite to the canonical direction *)
hoppingVecOpposite = (t - gamma) hoppingVecHatanoNelson + delta hoppingVecPerturbation;
hoppingsPCOpposite = AssociationThread[EdgeList@pcmodel["Graph"] -> hoppingVecOpposite];
```
The non-reciprocal Abelian Bloch Hamiltonians for the primitive cell and supercells are constructed as follows: 

```Mathematica
(* Hamiltonian for the primitive cell *)
Hpc = NonReciprocalAbelianBlochHamiltonian[pcmodel, 1, 0 &, 
  hoppingsPCCanonical, hoppingsPCOpposite, CompileFunction -> True];

(* Hamiltonians for the supercells *)
Hsclst = Association[# -> 
  NonReciprocalAbelianBlochHamiltonian[scmodels[#], 1, 0 &, 
    hoppingsPCCanonical, hoppingsPCOpposite, PCModel -> pcmodel, CompileFunction -> True]
  &/@cells[[2 ;;]]];

(* All *)
Hclst = Join[Association[cells[[1]] -> Hpc], Hsclst];
```

The complex spectrum exhibits a **point gap**:

```Mathematica
evals = Association[# -> 
  ComputeEigenvalues[Hclst[#] /. {t -> 0.5, gamma -> 0.5, delta -> 0.1}, 10^4,
        32, genusLst[#]] & /@ cells];


ComplexListPlot[ComplexRandomThinning[evals, 1000],
 AspectRatio -> 1/1.5, Frame -> True, FrameLabel -> {"Re{E}", "Im{E}"},
 FrameStyle -> Directive[Black, 30], ImageSize -> 500, LabelStyle -> 20, 
 PlotMarkers -> {"\[FilledCircle]", Scaled[0.015]},
 PlotRange -> {{-4, 4}, {-1.1, 1.1}}, PlotStyle -> cLst]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HatanoNelson/spec_complex_64_HatanoNelsonModel.png">
    <img src="../../media/figs/Tutorials/HatanoNelson/spec_complex_64_HatanoNelsonModel.png" class="figure-img img-fluid rounded" alt="Complex spectra, on-site, {6,4}-lattice" width="500"/>
  </picture>
</figure>

<div style="text-align: right;">
  <a href="../../misc/code_snippets/Tutorials/HatanoNelsonModel/tutorial_HatanoNelsonModel_HyperBloch.nb" class="btn btn-primary"><i class="fa-solid fa-download"></i> Download Mathematica Notebook</a>
</div>
