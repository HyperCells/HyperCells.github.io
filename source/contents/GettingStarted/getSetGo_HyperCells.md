
# HyperCells


```{dropdown} Learning goals
:color: success
:icon: light-bulb

Construction of:

* the **proper triangle group** {math}`\Delta^{+}`,
* the graph representing a **primitive cell** and a **supercell**,
* the corresponding graph representations of a **nearest-neighbor tight-binding model**.

Through:

* the access of **quotient groups** {math}`\Delta^{+}/\Gamma`,
* the construction of the corresponding **translation group** {math}`\Gamma`.
```

```{dropdown}  Featured functions
:color: info
:icon: gear

<code class="code-gap">
FpGroup, ListTGQuotients, ProperTriangleGroup, TessellationModelGraph, TGCellGraph, TGCellSymmetric, TGQuotient, TGQuotientGenus, TGQuotientGroup, TGQuotientOrder, TGQuotientRelators, TGSuperCellModelGraph, TGTranslationGroup
</code>
```

In this tutorial we will see how the cell, model and supercell model graphs are constructed through the **HyperCells** package. These objects capture the tight-binding model specifications and can be used to conduct **hyperbolic band theory** analysis. Moreover, we go through the intended workflow and showcase which HyperCells objects need to be assembled in order to construct the cell, model and supercell model graphs through group theory in GAP.

## Preliminaries

To use the HyperCells package, start GAP and then load the package with:

```gap
gap> LoadPackage("HyperCells");
```

A typical workflow starts by setting up the (proper) triangle group, here we choose {math}`\Delta^{+}(2,8,8)`:

```gap
gap> tg := ProperTriangleGroup( [ 2, 8, 8 ] );
ProperTriangleGroup(2, 8, 8)
```

The returned object is of category <code class="code-gap">ProperTriangleGroup</code>. The presentation of the proper triangle group can be extracted by applying the operation <code class="code-gap">FpGroup</code>:

```gap
gap> FpGroup(tg);
<fp group on the generators [ x, y, z ]>
```

This represents a finitely presented group with rotation generators <code class="code-gap">x</code>, <code class="code-gap">y</code>, <code class="code-gap">z</code> and corresponding relators given by:

```gap
gap> GeneratorsOfGroup(FpGroup(tg));
[ x, y, z ]

gap> RelatorsOfFpGroup(FpGroup(tg));
[ x*y*z, x^2, y^8, z^8 ]
```

It is instructive to use the **HyperBloch** package in Mathematica in order to visualize how the **fundamental Schwarz triangle** <code class="code-gap">s<sub>f</sub></code> is transported in the {math}`\{8,8\}`-tesselations of the hyperbolic plane when acting upon it with the rotation generators. However, we will restrain the exact details on how to obtain it for now, a detailed discussion can be found in the [Flat-bands](../Tutorials/Flat-bands.md) and [Haldane model](../Tutorials/Haldane_model.md) tutorials. The corresponding visualization in **Poincaré disk** looks as follows:

<figure class="text-center">
  <picture> 
    <source type="image/svg+xml" srcset="../../media/figs/getSetGoHyperCells/Sym88.png">
    <img src="../../media/figs/getSetGoHyperCells/Sym88.png" class="figure-img img-fluid rounded" alt="{6,4} Lieb lattice pc" width="400"/>
  </picture>
</figure>

Next, we specify a unit cell of the lattice in terms of the quotient of the proper triangle group {math}`\Delta^{+}` with a translation group {math}`\Gamma \triangleleft \Delta^{+}`. For that we can query the included database based on the work of <a target="_blank" href="https://hypercells.github.io/HyperCells/doc/chapBib_mj.html#biBConder:2007">Marston Conder</a>, which allows us to select one of them:

```gap
gap> ListTGQuotients( [ 2, 8, 8 ] );
[ [ 2, 6 ], [ 3, 10 ], [ 3, 11 ], [ 5, 12 ], [ 5, 13 ], [ 9, 19 ], ... ]
```

In the following, we select the quotient denoted by <code class="code-gap">T2.6</code>, where the <code class="code-gap">2</code> indicates the genus of the surface on which the quotient group acts, and the <code class="code-gap">6</code> indicates the position in Conder's list of all quotients with the same genus:

```gap
gap> q := TGQuotient( [ 2, 6 ] );
TGQuotient([ 2, 6 ], [ 2, 8, 8 ], 8, 2, Action reflexible [m,n], 
    [ x^2, x * y * z, x * z * y, y^3 * z^-1 ])
```

The returned object is of category <code class="code-gap">TGQuotient</code>. Alternatively, we can access the first entry appearing for {math}`\Delta^{+}(2,8,8)` using:

```gap
gap> q := TGQuotient( 1, [ 2, 8, 8 ] );
TGQuotient([ 2, 6 ], [ 2, 8, 8 ], 8, 2, Action reflexible [m,n],
    [ x^2, x * y * z, x * z * y, y^3 * z^-1 ])
```

The <code class="code-gap">TGQuotient</code> object carries the defining information of the triangle group quotient, such as its order, the genus of the compactified unit cell it acts upon, the defining relators and other information, for example:

```gap
gap> TGQuotientOrder(q);
8

gap> TGQuotientGenus(q);
2

gap> TGQuotientRelators(q);
[ x^2, x * y * z, x * z * y, y^3 * z^-1 ]
```

Once we have the proper triangle group and the <code class="code-gap">TGQuotient</code> object, we can obtain the quotient group, which is isomorphic to the proper point group {math}`G^{+}\cong \Delta^{+}/\Gamma`:

```gap
gap> G := TGQuotientGroup( tg, q );
<fp group on the generators [ x, y, z ]>
```

or the associated translation group {math}`\Gamma`:

```gap
gap> TGTranslationGroup( tg, q );
TranslationGroup( < g1, g2, g3, g4 | g4*g3*g2*g1*g2^-1*g4^-1*g1^-1*g3^-1 > )
```

The number of generators in the translation group {math}`\Gamma` is twice the genus of the compactified unit cell.


## Cell graph

The next step is to construct the graph representing the primitive cell. This graph corresponds to a triangular tessellation of the compactified cell and is stored as an object of category <code class="code-gap">TGCellGraph</code>. In addition to the triangle group and quotient, we also need to specify the vertex at which the cell should be centered (here we choose <code class="code-gap">3</code>, corresponding to the <code class="code-gap">z</code> vertex of the fundamental Schwarz triangle):

```gap
gap> cg := TGCellGraph( tg, q, 3 : simplify := 5 );
TGCellGraph(
    TGCell( ProperTriangleGroup(2, 8, 8), [ x^2, x*y*z, x*z*y, y^3*z^-1 ] ),
    center = 3,
    vertices = [ [ 1, 1 ], [ 1, 2 ], [ 1, 3 ], [ 1, 4 ], [ 2, 1 ], [ 3, 1 ] ],
    edges = [ [ 1, 6, 1, <identity ...> ], ..., [ 6, 5, 8, g1^-1*g2*g3^-1 ] ],
    faces = [ [ [ 3, 1 ], [ 2, 1 ], [ 14, -1 ], [ 6, -1 ] ], ... ],
    boundary = [ [ <identity ...>, <identity ...>, 2, 1, 0, g1 ], ... ]
)
```

The option <code class="code-gap">simplify</code> specifies the maximum wordlength that should be checked for simplifying expressions in terms of the translation generators <code class="code-gap">g1</code>, <code class="code-gap">g2</code>, etc. The default value is <code class="code-gap">0</code> which means that no simplification is performed. 

In tandem with the option <code class="code-gap">simplify</code>, another option <code class="code-gap">simplifyMethod</code> can be passed, which specifies whether to use the default brute force approach <code class="code-gap">simplifyMethod="BruteForce"</code> or the Knuth-Bendix completion algorithm <code class="code-gap">simplifyMethod="KnuthBendix"</code> for the simplification, provided the <a target="_blank" href="https://gap-packages.github.io/kbmag/doc/chap0_mj.html">kbmag</a> package is available.

While the cell graph itself represents the compactified unit cell, potential translations associated with the edges crossing from one copy of the cell to another are stored as well. The cell graph can be exported using the <code class="code-gap">Export</code> operation.

## Model graph

With the cell graph at hand, we can derive a model graph, such as a tessellation graph, i.e., the nearest-neighbor graph of the {math}`\{8,8\}`-tesselation of the hyperbolic plane restricted to the primitive cell:

```gap
gap> model := TessellationModelGraph( cg, true : simplify := 0 );
TGCellModelGraph( 
    TGCell( ProperTriangleGroup(2, 8, 8), [ x^2, x*y*z, x*z*y, y^3*z^-1 ] ), 
    center = 3, 
    type = [ "TESS", [ 8, 8 ], [ "VEF", [ [ 3 ], [ 1 ], [ 2 ] ] ] ], 
    vertices = [ [ 3, 1 ] ], 
    edges = [[ 1, 1, [ 1, [ [ 1, 1 ], 1, 5 ] ], g1 ], [ 1, 1, [ 1, [ [ 1, 2 ], 4,  8 ] ], g4 ], 
        [ 1, 1, [ 1, [ [ 1, 3 ], 2, 6 ] ], g2 ], [ 1, 1, [ 1,  [ [ 1, 4 ], 3, 7 ] ], g3 ] ], 
    faces = [ [ [ 1, -1 ], [ 2, -1 ], [ 4, 1 ], [ 3, -1 ], [ 1, 1 ], [ 2, 1 ], 
        [ 4, -1 ], [ 3, 1 ] ] ] )
```

The result is an object of category <code class="code-gap">TGCellModelGraph</code>, which can be exported using the <code class="code-gap">Export</code> operation.

## Supercell model graph

Finally, the model graph defined on the primitive cell can be extended to a **supercell**, i.e., a cell specified by a translation subgroup {math}`\Gamma^{'}\triangleleft\Gamma` of the original translation group {math}`\Gamma`. Here, we consider the one given by the quotient <code class="code-gap">T3.11</code> (see tutorial [Supercells](../Tutorials/Supercells) for a in depth discussion) and first construct the **symmetric** cell, without simplifying the translation generators:

```gap
gap> sc := TGCellSymmetric( tg, TGQuotient( [ 3, 11 ] ), 3 );
TGCell( ProperTriangleGroup(2, 8, 8), [ x^2, x*y*z, x*z*y, y^-8 ] )
```
and then construct the supercell model graph:

```gap
gap> scmodel := TGSuperCellModelGraph( model, sc : simplify := 0 );
TGSuperCellModelGraph( 
    primitive cell = TGCell( ProperTriangleGroup(2, 8, 8), 
        [ x^2, x*y*z, x*z*y, y^3*z^-1 ] ), 
    supercell = TGCell( ProperTriangleGroup(2, 8, 8), 
        [ x^2, x*y*z, x*z*y, y^-8 ] ), 
    cell embedding = TGCellEmbedding( 
        primitive cell = TGCellTranslationGroup( < g1, g2, g3, g4 | 
            g2*g1^-1*g4^-1*g3*g2^-1*g1*g4*g3^-1 > ), 
        supercell = TGCellTranslationGroup( < g1, g2, g3, g4, g5, g6 | 
            g6*g4*g2*g1*g3*g5*g3^-1*g2^-1*g6^-1*g5^-1*g1^-1*g4^-1 > ), 
        transversal = [ <identity ...>, (x^-1*y^-1)^4*x^-1 ], 
        embedding = [ g1, g2, g3, g4, g5, g6 ] -> [ g1^-1*g4^-1, ... ] 
    ), 
    center = 3, 
    type = [ "TESS", [ 8, 8 ], [ "VEF", [ [ 3 ], [ 1 ], [ 2 ] ] ] ], 
    vertices = [ [ 3, 1, 1 ], [ 3, 1, 2 ] ], 
    edges = [ [ 1, 2, [ 1, 1, [ 1, [ [ 1, 1 ], 1, 5 ] ] ], <identity ...> ], ... ], 
    faces = [ ] 
)
```

which is returned as an object of category <code class="code-gap">TGSuperCellModelGraph</code> and can be exported using the <code class="code-gap">Export</code> operation. The vertices and edges of the supercell model graph retain information about the vertices and edges of the primitive cell model graph and the elements of the quotient group {math}`\Gamma_{pc}/\Gamma_{sc}` distinguishing the different copies of the primitive cell in the supercell.



