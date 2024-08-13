# load the HyperCells package
LoadPackage( "HyperCells" );

# Constuct supercell sequence on the {8,8}-lattice: 
# -------------------------------------------------

# set up (proper) triangle group
tg := ProperTriangleGroup( [ 2, 8, 8 ] );

# Primitive cell:
# ---------------

# specify the quotient defining the primitive cell
qpc := TGQuotient( [5, 12], [ 2, 8, 8 ] );

# construct symmetric primitive cell
cgpc := TGCellGraph( tg, qpc, 3 );

# associated translation group
tgGamma_pc1 := TGTranslationGroup( tg, qpc);

# elementary nearest-neighbor model
model := TessellationModelGraph( cgpc, true : simplify := 5 );
Export( model, "{8,8}-tess_T5.12_3.hcm" ); # export

# Supercells:
# -----------

sc_lst := [[9, 22], [17, 32], [33, 46], [65, 79]];

tgGamma_sc_i := tgGamma_pc1;

for sc_i_index in sc_lst do
  
  # quotient group 
  qsc_i := TGQuotient( sc_i_index );

  # construct tessellation graphs
  sc_i := TGCellSymmetric(tg, qsc_i, 3);
  scmodel_i := TGSuperCellModelGraph(model, sc_i);

  # export file
  sc_i_label := StringFormatted("-tess_T5.12_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
  scmodel_i_name := JoinStringsWithSeparator(["{8,8}", sc_i_label], "");
  Export(scmodel_i,  scmodel_i_name);

od;