# load the HyperCells package
LoadPackage( "HyperCells" );

# set up (proper) triangle group
tg := ProperTriangleGroup( [ 2, 4, 6 ] );

# Primitive cell:
# ---------------

# specify the quotient defining the primitive cell
qpc := TGQuotient( 1, [ 2, 4, 6 ] );

# construct symmetric primitive cell
cgpc := TGCellGraph( tg, qpc, 3 : simplify := 5 );
Export( cgpc, "(2,4,6)_T2.2_3.hcc" ); # export


# Lieb lattice:
# -------------
# elementary nearest-neighbor model
model_Lieb := LiebModelGraph( cgpc );
Export( model_Lieb, "{6,4}-Lieb_T2.2_3.hcm" ); # export



# Supercells:
# -----------

sc_lst := [[5, 4], [9, 3]];


for sc_i_index in sc_lst do
    
    # find appropriate quotient group
    qsc_i := TGQuotient( sc_i_index );

    # construct tessellation graphs
    sc_i := TGCellSymmetric(tg, qsc_i, 3);
    scmodel_i := TGSuperCellModelGraph(model_Lieb, sc_i);

    # export file
    sc_i_label := StringFormatted("_T2.2_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
    scmodel_i_name := JoinStringsWithSeparator(["{6,4}-Lieb", sc_i_label], "");
    Export(scmodel_i,  scmodel_i_name);

od;