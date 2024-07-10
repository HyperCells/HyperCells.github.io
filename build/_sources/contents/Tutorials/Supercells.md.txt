# Supercells

```{admonition} Learning goals
:class: hint

* Access of supercell sequences through:
   * custom functions and
   * subgroup tree graphs.
<br></br>
* Construction of:
   * subgroup tree graphs and
   * model graphs on supercells.
<br></br>
* Application of the supercell method. 
```

As usual, let us construct the proper triangle group, the quotient group for the primitive cell and additionally the corresponding translation group for the {8,8}-lattice in **GAP**:

```gap
# load the HyperCells package
LoadPackage( "HyperCells" );

# set up (proper) triangle group
tg := ProperTriangleGroup( [ 2, 8, 8 ] );

# specify the quotient defining the primitive cell
qpc := TGQuotient( 1, [ 2, 8, 8 ] );

# associated translation group
tgGamma_pc1 := TGTranslationGroup( tg, qpc );
```

## Accessing supercell sequences

In order to use the supercell method for hyperbolic lattices on tight-binding models, we need to identify appropriate sequences of supercells. A usual workflow starts by constructing a **subgroup tree graph**, which shows the normal subgroup relations between any given translation group extracted from quotient groups in  <a target="_blank" href="https://patrick-lenggenhager.github.io/HyperCells/doc/chapBib_mj.html#biBConder:2007">Marston Conder's</a> list. In this tutorial we will look at two approaches to construct supercell sequences which consist of constructing a custom function and a subgroup tree graph. 

```{admonition} Skip to subsection [Subgroup tree graph approach](#subgroup-tree-graph-approach)
:class: seealso

On a first read, one may want to skip the subsection "Custom function approach" and resume at the subsection "Subgroup tree graph approach".
```

### Custom function approach

Supercell sequences are restricted to consecutive translation groups  <code class="code-gap" style="font-size:1.1em;">&#915;<sup>(m+1)</sup> </code> that are normal subgroups of <code class="code-gap" style="font-size:1.1em;">&#915;<sup>(m)</sup> </code> and <code class="code-gap" style="font-size:1.1em;">&#916;<sup>+</sup> </code>. In addition, the application of the supercell method requires that supercells are symmetric aggregates of primitive cells. Thus, restricting the selection of quotient groups to those with group action called  **reflexible**, i.e. the order of the **point group** <code class="code-gap" style="font-size:1.1em;">G<sup>(m)</sup> </code> and the **proper point group** <code class="code-gap" style="font-size:1.1em;">G<sup>+(m)</sup> </code> are <code class="code-gap" style="font-size:1.1em;">|G<sup>(m)</sup>| = 2 |G<sup>+(m)</sup>| </code>.

As such, a possible function to retrive a particular supercell sequence is given by:

```gap
getMthSupercellQuotient := function(tg, tgGamma, n1)
        local tgGamma_n, Gamma1, qn, signat, switch, 
        i, D, rels, G, Gplus, a, b, c, DELTA, 
        embDDELTA, relsfull;


  # signature (2, q, p)
  signat := Signature(tg);

  # presentation of the proper triangle group  
  D := FpGroup(tg);

  # translation group in terms of generators x, y, z
  Gamma1 := AsTGSubgroup(tgGamma);
	
  # presentation of the (full) triangle group
  DELTA := FpGroup(TriangleGroup(Signature(tg)));
  a := DELTA.1;; b := DELTA.2;; c := DELTA.3;

  # embedding homomorphism of D in DELTA
  embDDELTA := GroupHomomorphismByImagesNC(D, DELTA,
      GeneratorsOfGroup(D), [a*b, b*c, c*a]);

  i := n1;
  switch := false;
  while switch = false do
                
    qn := TGQuotient(i, signat);
    tgGamma_n := TGTranslationGroup(tg, qn);
    switch := IsSubgroup(Gamma1, AsTGSubgroup(tgGamma_n));
    if switch then
		
      # proper point group
      rels := TGQuotientRelators(tg, qn);
      Gplus := D / rels;
      
      # (full) point group
      relsfull := List(rels, r -> Image(embDDELTA, r));
      G := DELTA / relsfull;
      
      # ensure that quotient is mirror symmetric
      if not Order(G) = 2 * Order(Gplus) then
        switch := false;
      fi; 
     fi;
  
   i := i + 1;
  od;

 return [qn, tgGamma_n, i];
end;;
```

This function takes as arguments a <code class="code-gap" style="font-size:1.1em;">ProperTriangleGroup</code> (<a target="_blank" href="https://patrick-lenggenhager.github.io/HyperCells/doc/chap2_mj.html#X84E92102876317DE">see 2.3</a>) and a <code class="code-gap" style="font-size:1.1em;">TGTranslationGroup</code> (see 2.2 (href ???)). The integer <code class="code-gap" style="font-size:1.1em;">n1</code> is the first index of the quotient groups in the list <code class="code-gap" style="font-size:1.1em;">ListTGQuotients( [ 2, 8, 8 ] )</code> that will be checked to satisfy the conditions stated above. Let us apply this function in order to retrive a first supercell:

```gap
qANDtgGamma_sc1 := getMthSupercellQuotient(tg, tgGamma_pc1, 2);
```

The first supercell in this sequence is given by:

```gap
gap> qsc_3_11 := qANDtgGamma_sc1[1];;
gap> TGQuotientName(qsc_3_11);
[ 3, 11 ]
```

The <code class="code-gap" style="font-size:1.1em;">TGQuotientName</code> returns the label given in M. Conder's list, where 3 is the genus of the Rieman surface the quotient acts upon and 11 the index in the list. Let us retrive the next 5 supercells, together with the corresponding  tessellation graphs, i.e., the nearest-neighbor graphs of the {8,8} tessellation of the hyperbolic plane:


```gap
# elementary nearest-neighbor model
model := TessellationModelGraph( cgpc, true : simplify := 5 );
Export( model, "{8,8}-tess_T2.6_3.hcm" ); # export

n0 := 2;
tgGamma_sc_i := tgGamma_pc1;

for i in [1 .. 6] do

  # find appropriate quotient group
  qANDtgGamma_sc_i := getMthSupercellQuotient(tg, tgGamma_sc_i, n0);
  qsc_i := qANDtgGamma_sc_i[1];;
  tgGamma_sc_i := qANDtgGamma_sc_i[2];; 
  n0 := qANDtgGamma_sc_i[3];;

  # construct tessellation graphs
  sc_i := TGCellSymmetric(tg, qsc_i, 3);
  scmodel_i := TGSuperCellModelGraph(model, sc_i);

  # export file
  sc_i_index := TGQuotientName(qsc_i);
  sc_i_label := StringFormatted("-tess_T2.6_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
  scmodel_i_name := JoinStringsWithSeparator(["{8,8}", sc_i_label], "");
  Export(scmodel_i,  scmodel_i_name);

od;
```

The sequence of quotient groups is <code class="code-gap" style="font-size:1.1em;">T2.6</code>, <code class="code-gap" style="font-size:1.1em;">T3.11</code>, <code class="code-gap" style="font-size:1.1em;">T5.13</code>, <code class="code-gap" style="font-size:1.1em;">T17.29</code>, <code class="code-gap" style="font-size:1.1em;">T33.44</code> and <code class="code-gap" style="font-size:1.1em;">T65.78</code>.

<div class="flex ">
  <a href="../../../source/assets/misc/code_snippets/Tutorials/Supercells/tutorial_Supercells_HyperCells_pc_sc_files.zip" download class="btn btn-primary" class="flex-child">Download generated files</a>
  <a href="../../../source/assets/misc/code_snippets/Tutorials/Supercells/tutorial_Supercells_HyperCells.g" download class="btn btn-primary" class="flex-child">Download GAP Code</a>
</div>

### Subgroup tree graph approach

Identifying sequences of supercells through custom functions might be cumbersome. The built-in function to construct subgroup relations of the translation groups provides efficient access to all sequences which are normal subgroups of <code class="code-gap" style="font-size:1.1em;">&#916;<sup>+</sup> </code> and obey the normal subgroup relation <code class="code-gap" style="font-size:1.1em;">&#916;<sup>+</sup> &#8883; &#915;<sup>(1)</sup> &#8883; &#915;<sup>(2)</sup> &#8883; ... &#915;<sup>(m)</sup> &#8883; ... </code> given in <a target="_blank" href="https://patrick-lenggenhager.github.io/HyperCells/doc/chapBib_mj.html#biBConder:2007">Marston Conder</a> list. It can be used to build advanced custom functions as well as to visualize appropriate sequences in subgroup tree graphs. Let us visualize the subgroup relations of the {8,8}-lattice by constructing the adjacency matrix of normal subgroup relations between any pairwise disctinct translation group in **GAP**:

```gap
adjMat88 := subgroupAdjacencyMatrix([2,8,8]);
ExportAdjMat(adjMat88, "SubgroupAdjMat88.g");
```

<div style="text-align: right;">
  <a href="../../../source/assets/misc/code_snippets/Tutorials/Supercells/tutorial_Supercells_HyperCells_SubgroupAdjMat88.g" download class="btn btn-primary">Download generated file</a>
</div>
<br>

Next, in **Mathematica** we import the adjacency matrix:

```Mathematica
(* Preliminaries *)
<< PatrickMLenggenhager`HyperBloch`
SetDirectory[NotebookDirectory[]];

(* Import adjacency matrix *)
adjM88 = ImportAdjMatrixString[Import["SubgroupAdjMat88.g"], 
  scaleLayer -> 1/1.03, justHighlightVertexLabelSm -> True]; 

(* Set genus limit *)
limiter = Position[adjM88["GenusList"], n_ /; n < 20][[-1, 1]];
limiterHL = Position[adjM88["HighlightSm"][[;; , 2]], n_ /; n < 20][[-1, 1]];

(* Calculate nearest-neighbor relations *)
NNadjM88 = adjM88["adjMatrix"][[;; limiter, ;; limiter]] - 
  Sign@MatrixPower[adjM88["adjMatrix"][[;; limiter, ;; limiter]], 2];
```

and visualize the subgroup relations up to genus 20 of the closed Riemann surfaces that the corrsponding quotient groups act upon:

```Mathematica
AdjacencyGraph[NNadjM88, 
  GraphLayout -> {
    "LayeredDigraphEmbedding", "RootVertex" -> 1, "Tolerance" -> 0.01, 
    "VertexLayerPosition" -> -1.72 adjM88["vertexLayerPosition"][[;; limiter]]
  }, 
  VertexLabels -> adjM88["vertexLabels" ][[;; limiter]], AspectRatio -> 0.5, 
  ImageSize -> Scaled[1], VertexSize -> 0.35, 
  GraphHighlight -> adjM88["HighlightSm"][[;; limiterHL]][[;; , 1]],
  EdgeShapeFunction -> edge
]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../../source/assets/media/figs/Tutorials/Supercells/SubgroupTreegraph.png">
    <img src="../../../source/assets/media/figs/Tutorials/Supercells/SubgroupTreegraph.png" class="figure-img img-fluid rounded" alt="SubgroupTreegraph {8,8}-lattice" width="1000"/>
  </picture>
</figure>

Every vertex corresponds to a normal subgroup <code class="code-gap" style="font-size:1.1em;">&#915;<sup>(m)</sup></code>. They are labeled by a corresponding quotient group <code class="code-gap" style="font-size:1.1em;">&#916;<sup>+</sup>/&#915;<sup>(m)</sup></code>, denoted as <code class="code-gap" style="font-size:1.1em;">Tg.n</code>, where <code class="code-gap" style="font-size:1.1em;">g</code> is the genus of the corresponding closed Riemann surface up to genus 20 and <code class="code-gap" style="font-size:1.1em;">n</code> is the <code class="code-gap" style="font-size:1.1em;">n</code>'th quotient group with that genus. Vertices highlighted in red indicate that Schwarz triangles can be assembled mirror symmetrically, given an appropriate choice of representatives in the right transversal. Blue vertices do not admit a mirror-symmetric unit cell, and they cannot be analyzed with the present version of the HyperCells package. Pairwise distinct vertices <code class="code-gap" style="font-size:1.1em;"> &#915;<sup>(m)</sup></code>,<code class="code-gap" style="font-size:1.1em;"> &#915;<sup>(m+1)</sup></code> connected by a directed edge obey the normal subgroup relation <code class="code-gap" style="font-size:1.1em;"> &#915;<sup>(m)</sup> &#8883; &#915;<sup>(m+1)</sup></code>. 

We choose to construct the supercell sequence  <code class="code-gap" style="font-size:1.1em;">T2.6</code>, <code class="code-gap" style="font-size:1.1em;">T3.11</code>, <code class="code-gap" style="font-size:1.1em;">T5.13</code>, <code class="code-gap" style="font-size:1.1em;">T17.29</code>, <code class="code-gap" style="font-size:1.1em;">T33.44</code> and <code class="code-gap" style="font-size:1.1em;">T65.78</code> by manually extracting the sequence following the subgroup tree graph shown above. The corresponding  tessellation graphs, i.e. the nearest-neighbor graphs of the {8,8} tessellation of the hyperbolic plane in **GAP**, are extracted as follows:

```gap
# load the HyperCells package
LoadPackage( "HyperCells" );

# Constuct supercell sequence on the {8,8}-lattice: 
# -------------------------------------------------

# set up (proper) triangle group
tg := ProperTriangleGroup( [ 2, 8, 8 ] );

# Primitive cell:
# ---------------

# specify the quotient defining the primitive cell
qpc := TGQuotient( 1, [ 2, 8, 8 ] );

# construct symmetric primitive cell
cgpc := TGCellGraph( tg, qpc, 3 : simplify := 5 );

# associated translation group
tgGamma_pc1 := TGTranslationGroup( tg, qpc );

# elementary nearest-neighbor model
model := TessellationModelGraph( cgpc, true : simplify := 5 );
Export( model, "{8,8}-tess_T2.6_3.hcm" ); # export

# Supercells:
# -----------

sc_lst := [[3, 11], [5, 13], [17, 29], [33, 44], [65, 78]];

tgGamma_sc_i := tgGamma_pc1;

for sc_i_index in sc_lst do
  
  # find appropriate quotient group
  qsc_i := TGQuotient( sc_i_index );

  # construct tessellation graphs
  sc_i := TGCellSymmetric(tg, qsc_i, 3);
  scmodel_i := TGSuperCellModelGraph(model, sc_i);

  # export file
  sc_i_label := StringFormatted("-tess_T2.6_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
  scmodel_i_name := JoinStringsWithSeparator(["{8,8}", sc_i_label], "");
  Export(scmodel_i,  scmodel_i_name);

od;
```

<div class="flex ">
  <a href="../../../source/assets/misc/code_snippets/Tutorials/Supercells/tutorial_Supercells_HyperCells_pc_sc_files.zip" download class="btn btn-primary" class="flex-child">Download generated files</a>
  <a href="../../../source/assets/misc/code_snippets/Tutorials/Supercells/tutorial_Supercells_HyperCells_sc.g" download class="btn btn-primary" class="flex-child">Download GAP Code</a>
</div>

## The supercell method, example

We are now ready to apply the supercell method in **Mathematica** using the HyperBloch package. The generated files need to be imported:

```Mathematica
(* Import primitive cell model *)
pcmodel = 
  ImportModelGraphString[Import[
    FileNameJoin[{"data", "cells", "{8,8}-tess_T2.6_3.hcm"}] ]];

(* Import supercell models *)
scmodels = Association[# ->
  ImportSupercellModelGraphString[
    Import[FileNameJoin[
      {"data", "cells", ToString@StringForm["{8,8}-tess_T2.6_3_sc-``.hcs", #]}]]
  ] & /@ cells[[2 ;;]]];
```

and the corresponding Abelian Bloch Hamiltonians for the nearest-neighbor tight-binding model needs to be constructed:

```Mathematica
(* Hamiltonian for the primitive cell *)
Hpc = AbelianBlochHamiltonian[pcmodel, 1, 0 &, -1 &];

(* Hamiltonian for the supercells *)
Hscs = Association[# ->
    AbelianBlochHamiltonian[scmodels[#], 1, 0 &, -1 &,
       PCModel -> pcmodel, CompileFunction -> True]
  &/@ supercells];

(* All *)
Hclst = Join[Association["T2.6" -> Hpc], Hscs]
```

This captures some of the higher-dimensional irreducible representations on the original primitive cell, and computing the resulting DOS can be done as follows:

```Mathematica
ComputeEigenvalues[cfH_, Npts_, Nruns_, genus_] :=
 Flatten@ParallelTable[
  Flatten@Table[
    Eigenvalues[cfH @@ RandomReal[{-Pi, Pi}, 2 genus]], 
    {i, 1, Round[Npts/Nruns]}],
  {j, 1, Nruns}, Method -> "FinestGrained"]

(* Labels and genus list *)
cells = {"T2.6", "T3.11", "T5.13", "T9.20", "T17.29", "T33.44", "T65.78"}; 
genusLst = {2, 3, 5, 9, 17, 33, 65};

(* Compute the Eigenvalues *)
evals = Association[cells[[#]] -> 
  ComputeEigenvalues[Hclst[cells[[#]]], 5*10^4, 32, genusLst[[#]]] &/@ Range[7]];
```

We can nicely observe the convergence of the DOS:

```Mathematica
SmoothHistogram[evals, 0.05, "PDF", Frame -> True, FrameStyle -> Black, 
                FrameLabel -> {"Energy E", "Density of states"}, 
                PlotRange -> All, ImageSize -> 500, LabelStyle -> 20,
                PlotLabel -> "k sampling: 5*10^4", PlotStyle -> 
                (ColorData["SunsetColors", "ColorFunction"] /@ (1-Range[1, 7]/7.)),
                ImagePadding -> {{Automatic, 10}, {Automatic, 10}}]
```

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../../source/assets/media/figs/Tutorials/Supercells/dos_88_scm1.png">
    <img src="../../../source/assets/media/figs/Tutorials/Supercells/dos_88_scm1.png" class="figure-img img-fluid rounded" alt="{8,8}-lattice NN-TB model DOS 1st supercell sequence" width="600"/>
  </picture>
</figure>

<div style="text-align: right;">
  <a href="../../../source/assets/misc/code_snippets/Tutorials/Supercells/tutorial_Supercells_HyperBloch.nb" download class="btn btn-primary">Download Mathematica Notebook</a>
</div>
<br>
