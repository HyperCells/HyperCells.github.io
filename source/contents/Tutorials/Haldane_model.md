# Haldane model

```{dropdown} Learning goals
:color: success
:icon: light-bulb

Construction of:

* next-nearest-neighbor model graphs,
* Abelian Bloch Hamiltonians with orientated couplings,
* point-group matrices and symmetry analysis.
```

```{dropdown}  Featured functions
:color: info
:icon: gear

**HyperCells:**

<code class="code-gap">
ProperTriangleGroup, TGQuotient, TGCellGraph, Export, TessellationModelGraph, AddOrientedNNNEdgesToTessellationModelGraph, TGQuotientSequencesAdjacencyMatrix, LongestSequence, TGCellSymmetric, TGSuperCellModelGraph, TriangleGroup, FpGroup, EvaluatePGMatrix, PGMatrices, PGMatricesOfGenerators
</code>
<br></br>

**HyperBloch:**

<code class="code-gap">
ImportCellGraphString, ImportModelGraphString, ImportSupercellModelGraphString, VisualizeModelGraph, ShowCellGraphFlattened, ShowCellBoundary, EdgeFilter, AbelianBlochHamiltonian, ImportPGMatricesString
</code>
```

```{dropdown}  Needed functions
:color: warning
:icon: tools

**Mathematica:**

In previous tutorials, such as [Getting started with the HyperBloch package](../GettingStarted/getSetGo_HyperBloch.md) and HyperBloch [Supercells](./Supercells.md) tutorial etc., we have calculated the density of states of various nearest-neighbor tight-binding models via exact diagonalization and random samples. We predefine a function in order to calculate the eigenvalues for the Abelian Bloch Hamiltonians that we will construct. We  take advantage of the independence of different momentum sectors and parallelize the computation, where we partition the set of *Npts* into *Nruns* subsets:

```Mathematica
ComputeEigenvalues[cfH_, Npts_, Nruns_, genus_] :=
 Flatten@ParallelTable[
   Flatten@Table[
     Eigenvalues[cfH @@ RandomReal[{-Pi, Pi}, 2 genus]], {i, 1, 
      Round[Npts/Nruns]}],
   {j, 1, Nruns}, Method -> "FinestGrained"]
```


In the previous tutorials, [Supercells](./Supercells.md) and [Flat-bands](./Flat-bands.md), we have considered nearest-neighbor tight-binding models through the construction of tessellation model graphs.
The HyperCells package enables the construction of extended tessellation model graphs which are comprised not only of nearest-neighbor but also **next-nearest-neighbor terms**. In this tutorial we will see how we can extend tessellation model graphs through the construction of next-nearest-neighbor tight-binding models on the {math}`\{6,4\}`-lattice. Specifically, we will consider next-nearest-neighbor terms as small perturbations as well as a variant of the Haldane model. Additionally, we will showcase how **hyperbolic lattice symmetries** can be analyzed in Abelian hyperbolic band theory through the construction of **point-group matrices**.


## Next-nearest-neighbor model graph

Next-nearest-neighbor terms can be added through a minor modification of the usual workflow. We start by constructing the cell graph for the primitive cell in **GAP**:

```gap
# load the HyperCells package
LoadPackage( "HyperCells" );
tg := ProperTriangleGroup( [ 2, 4, 6 ] );

# Primitive cell:
# ---------------
qpc := TGQuotient( 1, [ 2, 4, 6 ] );
cgpc := TGCellGraph( tg, qpc, 3 : simplify := 5 );
Export( cgpc, "(2,4,6)_T2.2_3.hcc" ); # export
```

In order to add next-nearest-neighbor terms, a tessellation model graph needs to be specified beforehand. As such, let us construct the nearest-neighbor graph of the {math}`\{6,4\}`-tessellation of the hyperbolic plane on the primitive cell and decorate it with next-nearest-neighbor (NNN) terms through the function <code class="code-gap">AddOrientedNNNEdgesToTessellationModelGraph</code>:

```gap
# Construction of NNN model:
# ---------------------------
# specify underlying model graph
model := TessellationModelGraph(cgpc);

# Adding NNN terms:
# -----------------
AddOrientedNNNEdgesToTessellationModelGraph(model);
Export(model, "{6,4}-tess-NNN_T2.2_3.hcm");
```

We choose a supercell sequence by following the central concepts discussed in the tutorial [Supercells](./Supercells.md) and [Coherent sequences](./Coherent_SC_sequences.md). The model specifications are inherited by subsequent supercell model graphs:

```gap
# Supercells:
# -----------
tgQAdjMat := TGQuotientSequencesAdjacencyMatrix(tg : boundByGenus := 10);;
sequence := LongestSequence(tgQAdjMat : quotient := 1);
sc_lst := sequence{[2..Length(sequence)]};

for sc_i_index in sc_lst do
    qsc_i := TGQuotient( sc_i_index );

    sc_i := TGCellSymmetric(tg, qsc_i, 3);
    scmodel_i := TGSuperCellModelGraph(model, sc_i);

    sc_i_label := StringFormatted("_T2.2_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
    scmodel_i_name := JoinStringsWithSeparator(["{6,4}-tess-NNN", sc_i_label], "");
    Export(scmodel_i,  scmodel_i_name); # export file
od;
```

<div class="flex ">
  <a href="../../misc/code_snippets/Tutorials/HaldaneModel/tutorial_HaldaneModel_HyperCells_pc_sc_files.zip" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download generated files</a>
  <a href="../../misc/code_snippets/Tutorials/HaldaneModel/tutorial_HaldaneModel_HyperCells.g" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download GAP Code</a>
</div>
<br>

## {math}`\{6,4\}`-NNN tight-binding model:

Before we construct the Haldane model on the {math}`\{6,4\}`-lattice, let us consider a more fundamental model in order to get familiar with the procedures to assign coupling constants for next-nearest-neighbor (supercell) model graphs. As such, let us construct an elementary next-nearest-neighbor hopping model.

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
pcmodel = ImportModelGraphString[Import["{6,4}-tess-NNN_T2.2_3.hcm"]];

(* Import supercell model graph *)
scmodels = Association[# -> 
  ImportSupercellModelGraphString[ 
    Import["{6,4}-tess-NNN_T2.2_3_sc-" <> # <> ".hcs"]] 
  &/@ cells[[2 ;;]]];
```

Let us visualize the NN and NNN-terms of the graph representation for the next-nearest-neighbor tight-binding model on the primitive cell. They are stored as directed edges, which can be extracted from the model graph as follows:

```Mathematica
EdgeList@pcmodel["Graph"]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HaldaneModel/{6,4}-tess-NNN-EdgeList_snippet.png">
    <img src="../../media/figs/Tutorials/HaldaneModel/{6,4}-tess-NNN-EdgeList_snippet.png" class="figure-img img-fluid rounded" alt="{6,4} pcmodel EdgeList" width="700"/>
  </picture>
</figure>

The first entry in the edge tags (the nested list above the arrow) indicate the if the edge connects nearest-neighbors or next-nearest-neighbor sites, where 1 and 2 denote NN and NNN-vertices, respectively. We can visualize the corresponding edges by using the optional argument *EdgeFilter* of the function <code class="code-gap">ShowCellGraphFlattened</code>. This enables us to visualize edges connecting NN-vertices or NNN-vertices separately:

```Mathematica
Row[
 Table[
  Module[{filterFunction},
   filterFunction[edge_, j_] := If[j < 3, edge[[3, 1]] == j, edge[[3, 1]] < j];
   VisualizeModelGraph[pcmodel, 
      CellGraph -> pcell, 
      Elements -> <|
        ShowCellBoundary -> {ShowEdgeIdentification -> True},
        ShowCellGraphFlattened -> {EdgeFilter -> (filterFunction[#, j] &)}
      |>,
      ImageSize -> 300, NumberOfGenerations -> 3]],
  {j, 3}]]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HaldaneModel/{6,4}-tess-NNN_pc_T2.2.png">
    <img src="../../media/figs/Tutorials/HaldaneModel/{6,4}-tess-NNN_pc_T2.2.png" class="figure-img img-fluid rounded" alt="{6,4} NNN model  pc" width="1000"/>
  </picture>
</figure>

In order to construct the Abelian Bloch Hamiltonian let us recall the general startegy to endow the model graphs with coupling constants, see [Getting started with the HyperBloch package](../GettingStarted/getSetGo_HyperBloch.md). The list of edges, accessed through calling ``EdgeList@pcmodel["Graph"]``, allows us to associate distinct hopping amplitudes <code class="code-gap">h1</code> and <code class="code-gap">h2</code> with the NN and NNN-terms, respectively. It contains 12 directed edges connecting NN-vertices followed by 24 directed edges connecting NNN-vertices, thus:

```Mathematica
(* NN-terms *)
nnVec = ConstantArray[h1, 12];

(* NNN-terms *)
nnnVec = ConstantArray[h2 , 24];
```

The hopping amplitudes can be assigned through an Association, with edges as keys and hopping amplitudes as values:

```Mathematica
(* Construct association *)
hoppingVec = Join[nnVec, nnnVec];
hoppingsPC = AssociationThread[EdgeList@pcmodel["Graph"] -> hoppingVec];
```

The corresponding Hamiltonians are given by:

```Mathematica
(* Hamiltonian for the primitive cell *)
Hpc = AbelianBlochHamiltonian[pcmodel, 1, 0 &, hoppingsPC, CompileFunction -> True];

(* Hamiltonians for the supercells *)
Hsclst = Association[# -> 
    AbelianBlochHamiltonian[scmodels[#], 1, 0 &, hoppingsPC, PCModel -> pcmodel, CompileFunction -> True] 
  &/@ cells[[2 ;;]]];

(* All *)
Hclst = Join[Association[cells[[1]] -> Hpc], Hsclst];
```

As usual, we compute the density of states of this sequence of supercells by random samples in the Brioullin zone, where we use the function <code class="code-gap">ComputeEigenvalues</code>, which can be found in the dropdown menu **Needed function** above. We choose to treat the next-nearest-neighbor contributions as a weak coupling between sites, as such we set <code class="code-gap">h1</code> to {math}`1` and <code class="code-gap">h2</code> to {math}`0.05`:

```Mathematica
(* Eigenvalues *)
evals = Association[# -> ComputeEigenvalues[Hclst[#] /. {h1 -> 1, h2 -> 0.05}, 10^4, 32, genusLst[#]]&/@cells];

(* Color maps *)
cLst = (ColorData["SunsetColors", "ColorFunction"] /@ (1 - Range[1, 3]/3.));

(* Visualize *)
SmoothHistogram[evals, 0.01, "PDF",
  Frame -> True, FrameLabel -> {"Energy E", "Density of states"} FrameStyle -> Black, 
  ImageSize -> 500, ImagePadding -> {{Automatic, 10}, {Automatic, 10}}, LabelStyle -> 20,
  PlotLabel -> "k sampling: 10^4", PlotRange -> All, PlotStyle -> cLst]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HaldaneModel/dos_tess-NNN-64_scm.png">
    <img src="../../media/figs/Tutorials/HaldaneModel/dos_tess-NNN-64_scm.png" class="figure-img img-fluid rounded" alt="{6,4} NNN DOS" width="500"/>
  </picture>
</figure>

## Haldane model

The next-nearest-neighbor tight-binding model can easily be extended to a Haldane model. The directed edges for the NNN-terms are oriented such that a **Peierls substitution** can be performed by multiplying the previously defined constant vector ``nnnVec`` by a phase **{math}`e^{i\phi}`** . The resulting {math}`\{6,4\}`-lattice is threaded by **local magnetic fluxes** with net zero flux per hyperbolic hexagon:

```Mathematica
(* NNN-terms *)
phase = Exp[I Phi];
nnnVec = phase * nnnVec;

(* Construct association *)
hoppingVec = Join[nnVec, nnnVec];
hoppingsPC = AssociationThread[EdgeList@pcmodel["Graph"] -> hoppingVec];
```

Since the hyperbolic hexagons have an even number of sides the lattice can be considered as bipartite such that a sublattice mass can be realized by a **staggered on-site potential** **{math}`\pm m`**. It is instructive to take a look at the list of vertices in the model graph:

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
mVec = m {1, -1, -1, 1, 1, -1};
onsitePC = AssociationThread[VertexList@pcmodel["Graph"] -> mVec];
```

The Abelian Bloch Hamiltonians are given by:

```Mathematica
(* Hamiltonian for the primitive cell *)
Hpc = AbelianBlochHamiltonian[pcmodel, 1, onsitePC, hoppingsPC, CompileFunction -> True];

(* Hamiltonians for the supercells *)
Hsclst = Association[# -> 
    AbelianBlochHamiltonian[scmodels[#], 1, onsitePC, hoppingsPC, PCModel -> pcmodel, CompileFunction -> True] 
  &/@ cells[[2 ;;]]];

(* All *)
Hclst = Join[Association[cells[[1]] -> Hpc], Hsclst];
```

The density of states can be computed as usual:

```Mathematica
(* Eigenvalues *)
evals = Association[# -> 
    ComputeEigenvalues[Hclst[#] /. {h1 -> 1, h2 -> 0.5, m -> 0, Phi -> Pi/2}, 10^4, 32, genusLst[#]]
  &/@cells];

(* Visualize *)
SmoothHistogram[evals, 0.01, "PDF",
  Frame -> True, FrameLabel -> {"Energy E", "Density of states"} FrameStyle -> Black, 
  ImageSize -> 500, ImagePadding -> {{Automatic, 10}, {Automatic, 10}}, LabelStyle -> 20,
  PlotLabel -> "k sampling: 10^4", PlotRange -> All, PlotStyle -> cLst]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HaldaneModel/dos_Haldane-64_scm.png">
    <img src="../../media/figs/Tutorials/HaldaneModel/dos_Haldane-64_scm.png" class="figure-img img-fluid rounded" alt="{6,4} Haldane DOS" width="500"/>
  </picture>
</figure>

The application of the supercell method reveals spurious feature in the density of states of the primitive cell when using the Abelian Hyperbolic band theory. Some of the Abelian states lie outside the energy range with finite density in the thermodynamic limit and thus the band touching at zero energy is a finite sized effect.

<div style="text-align: right;">
  <a href="../../misc/code_snippets/Tutorials/HaldaneModel/tutorial_HaldaneModel_HyperBloch.nb" class="btn btn-primary"><i class="fa-solid fa-download"></i> Download Mathematica Notebook</a>
</div>


## Point group matrices

Symmetry elements of triangle groups might act non-trivially on hyperbolic momenta. As such, the degrees of freedom of observables and **topological invariants**, like the **first Chern numbers** in momentum space, might be contstrained by the hyperbolic lattice symmetries of underlying models. We can determine how hyperbolic momenta transform as hyperbolic lattice symmetry transformations act on Abelian states. This can be extracted by constructing **point-group matrices**. 

Point-group matrices can be constructed by specifying the hyperbolic lattice symmetries in terms of generators of the (full) triangle group {math}`\Delta(2,q,p)`. Let us visualize the action of the symmetry generators on the fundamental Schwarz triangle <code class="code-gap">s<sub>f</sub></code> of the {math}`\{6,4\}`-tesselation of the hyperbolic plane:

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HaldaneModel/Sym64.png">
    <img src="../../media/figs/Tutorials/HaldaneModel/Sym64.png" class="figure-img img-fluid rounded" alt="symmeries of the {6,4}-tesselation" width="400"/>
  </picture>
</figure>

For example, the generator <code class="code-gap">z</code> of the proper triangle group {math}`\Delta^{+}` is a composition of two reflection generators <code class="code-gap">c\*a</code> of {math}`\Delta`. The fundamental Schwarz triangle is  rotated by {math}`2 \pi/6` in counter clockwise direction to an adjacent copy under the action of the operator <code class="code-gap">z</code>. We can construct the operator as follows:

```gap
# proper triangle group 
D := FpGroup(tg);

# symmetry
z := D.3;
symmetry := z;
symName := "z";
```

Point-group matrices define representations of point groups {math}`G^{(m)}\cong\Delta/\Gamma^{(m)}`. This implies that it is sufficient to construct the point-group matrices for a minimal set of operators, such that matrix multiplications can be performed in order to construct the point-group matrices of other elements in the point group. As such, we first need to construct the point-group matrices for the rotation generators of the triangle group group for any given unit cell identified through a corresponding triangle group quotient {math}`\Delta/\Gamma^{(m)}`. 

They can be computed through the function <code class="code-gap">PGMatricesOfGenerators</code>, which takes the triangle group, proper triangle group and a triangle group quotient as arguments. As such, we first need to construct the triangle group:

```gap
# TriangleGroup obj.
fulltg := TriangleGroup( [ 2, 4, 6 ] );
```

Next, let us construct the point-group matrices of the triangle generators for the primitive cell:

```gap
# get the PGMatricesOfGenerators
pgMatGs := PGMatricesOfGenerators(fulltg, tg, qpc);
```

The point-group matrix for the symmetry <code class="code-gap">z</code> can now be evaluated through the function <code class="code-gap">EvaluatePGMatrix</code>:

```gap
gap>  EvaluatePGMatrix(z, pgMatGs);
[ [  0, -1,  0,  0 ], 
  [  0,  0, -1,  0 ], 
  [  0,  1,  0, -1 ], 
  [  1,  0,  0,  0 ] ]
```

Let us construct a particular point-group matrix for a symmetry analysis {math}`\{6,4\}`-Haldane model. In principle, there are two sets of symmetry operations that leave the model invariant, which are dictated by the configuration of the coupling constants, i.e, if the staggered on-site potential is non-zero or not. However, we will focus on a particular symmetry transformation that is common among them. 

The model is left invariant under a reflection <code class="code-gap">c</code> composed with time reversal <code class="code-gap">T</code> (note that an anti-unitary symmetry transformation, like time reversal, leads to an overall sign change of the point-group matrix, which we will consider later).

We have already constructed the corresponding point-group matrix through the function <code class="code-gap">PGMatricesOfGenerators</code>. However, let us choose to construct it once more as a sparse representation by passing the option <code class="code-gap">sparse</code>:

```gap
# get the PGMatricesOfGenerators
pgMatGs := PGMatricesOfGenerators(fulltg, tg, qpc : sparse := true);
```

A set of point-group matrices can only be exported by first calling the function <code class="code-gap">PGMatrices</code>. We choose to export the point-group matrices for <code class="code-gap">c</code> and <code class="code-gap">z</code>. However, we only need to specify the <code class="code-gap">z</code>, since the point-group matrices of the triangle group generators will be inherited:

```gap
# construct and export the PGMatrices
pgMat_T2_2 := PGMatrices(symmetry, pgMatGs : symNames := symName);
Export(pgMat_T2_2, "(2,4,6)-T2.2-pgMat_z_sparse.hcpgm");
```

We can repeat the procedure for the chosen supercell sequence:

```gap
# Quotients T5.4, T9.3 (supercells):
# ---------------------------------
for sc_i_index in sc_lst do
  qsc_i := TGQuotient( sc_i_index );

  # get the PGMatricesOfGenerators
  pgMatGs := PGMatricesOfGenerators(fulltg, tg, qsc_i : sparse := true);

  # construct and export the PGMatrices
  pgMat_sc_i := PGMatrices(symmetry, pgMatGs : symNames := symName);

  sc_i_label := StringFormatted("(2,4,6)-T{}.{}-pgMat_z_sparse.hcpgm", sc_i_index[1], sc_i_index[2]);
  Export(pgMat_sc_i, sc_i_label);
od;
```

<div class="flex ">
  <a href="../../misc/code_snippets/Tutorials/HaldaneModel/tutorial_HaldaneModel_PGMatrices_HyperCells_pc_sc_files.zip" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download generated files</a>
  <a href="../../misc/code_snippets/Tutorials/HaldaneModel/tutorial_HaldaneModel_PGMatrices_HyperCells.g" class="btn btn-primary" class="flex-child"><i class="fa-solid fa-download"></i> Download GAP Code</a>
</div>

### Application

Point-group matrices can be used to conduct symmetry analysis on any given (supercell) model graph. Let us perform a symmetry transformation for the variant of the Haldane model we have considered above, in order to see how the corresponding spectra are effected.

The point-group matrices can be imported analogously to (supercell) model graphs. As such, the <code class="code-gap">Import</code> function is used to read the file, while the <code class="code-gap">ImportPGMatricesString</code> function is used to parse the string and construct the point-group matrices:

```Mathematica
pgMatSc = Association[# -> ImportPGMatricesString[Import["(2,4,6)-" <> # <> "-pgMat_z_sparse.hcpgm"]]&/@cells];
```

The spectrum of the Haldane model should be left invariant under the hyperbolic lattice symmetry transformation <code class="code-gap">c</code>. This can easily be verified by an explicit transformation of the hyperbolic momenta through the following modification of the function defined in the dropdown menu **Needed function** above:

```Mathematica
ComputeEigenvalues[cfH_, pgMat_, Npts_, Nruns_, genus_] :=
 Flatten@ParallelTable[
   Flatten@Table[
     Eigenvalues[cfH @@ (Dot[-pgMat,RandomReal[{-Pi, Pi}, 2 genus]])], 
     {i, 1, Round[Npts/Nruns]}],
   {j, 1, Nruns}, Method -> "FinestGrained"]
```

where we have multiplied the point-group matrix <code class="code-gap">pgMat</code> by <code class="code-gap">-1</code> in order to account for the anti-unitarity of the transformation. The point-group matrices can be extracted by using the corresponding symmetry names as keys. We compute the Eigenvalues with a set of {math}`10^4` random samples in momentum space, partitioned into {math}`32` subsets as before and pass the point-group matrix for the symmetry transformation <code class="code-gap">cT</code> to the function:

```Mathematica
evals = Association[# -> 
  ComputeEigenvalues[Hclst[#] /. {h1 -> 1, h2 -> 0.5, m -> 0, Phi -> Pi/2}, 
    -pgMatSc[#]["c"], 10^4, 32, genusLst[#]] 
  & /@ cells];
```

The resulting density of states is unchanged (aside from negligible changes due to random sampling in combination with a relatively small sample size):

```Mathematica
SmoothHistogram[evals, 0.01, "PDF",
  Frame -> True, FrameLabel -> {"Energy E", "Density of states"} FrameStyle -> Black, 
  ImageSize -> 500, ImagePadding -> {{Automatic, 10}, {Automatic, 10}}, LabelStyle -> 20,
  PlotLabel -> "Mc k sampling: 10^4", PlotRange -> All, PlotStyle -> cLst]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/Tutorials/HaldaneModel/dos_Haldane-64_scm_PGMatrices.png">
    <img src="../../media/figs/Tutorials/HaldaneModel/dos_Haldane-64_scm_PGMatrices.png" class="figure-img img-fluid rounded" alt="{6,4} Haldane DOS, PGMatrix c" width="500"/>
  </picture>
</figure>

<div style="text-align: right;">
  <a href="../../misc/code_snippets/Tutorials/HaldaneModel/tutorial_HaldaneModel_HyperBloch.nb" class="btn btn-primary"><i class="fa-solid fa-download"></i> Download Mathematica Notebook</a>
</div>
