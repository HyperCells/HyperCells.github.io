# load the HyperCells package
LoadPackage( "HyperCells" );

# set up (proper) triangle group
tg := ProperTriangleGroup( [ 2, 3, 8 ] );

# Primitive cell:
# ---------------

# specify the quotient defining the primitive cell
qpc := TGQuotient( 1, [ 2, 3, 8 ] );

# construct symmetric primitive cell
cgpc := TGCellGraph( tg, qpc, 3 : simplify := 5 );
Export( cgpc, "(2,3,8)_T2.1_3.hcc" ); # export
 

# Kagome lattice:
# ---------------
model_kagome := KagomeModelGraph( cgpc );
Export( model_kagome, "{8,3}-kagome_T2.1_3.hcm" ); # export


# Supercells:
# -----------
tgQAdjMat := TGQuotientSequencesAdjacencyMatrix(tg : boundByGenus := 20);;
sequence := LongestSequence(tgQAdjMat : quotient := 1);
sc_lst := sequence{[2..Length(sequence)]};

for sc_i_index in sc_lst do
    
    # find appropriate quotient group
    qsc_i := TGQuotient( sc_i_index );

    # construct tessellation graphs
    sc_i := TGCellSymmetric(tg, qsc_i, 3);
    scmodel_i := TGSuperCellModelGraph(model_kagome, sc_i);

    # export file
    sc_i_label := StringFormatted("_T2.1_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
    scmodel_i_name := JoinStringsWithSeparator(["{8,3}-kagome", sc_i_label], "");
    Export(scmodel_i,  scmodel_i_name);

od;
