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
model := TessellationModelGraph( cgpc, true : simplify := 5 );
Export( model, "{8,8}-tess_T2.6_3.hcm" ); # export

# Supercell:
# ----------

# specify the quotient defining the supercell cell
qsc := TGQuotient( [ 3, 11 ] );

# construct symmetric supercell
cgsc := TGCellGraph( tg, qsc, 3 : simplify := 1 );
Export(cgsc, "(2,8,8)_T3.11_3.hcc");

# construct symmetric supercell
sc := TGCellSymmetric( tg, qsc, 3 );

# extend the model defined on the primitive cell to the supercell
scmodel := TGSuperCellModelGraph( model, sc : simplify := 0 );
Export( scmodel, "{8,8}-tess_T2.6_3_sc-T3.11.hcs" ); # export