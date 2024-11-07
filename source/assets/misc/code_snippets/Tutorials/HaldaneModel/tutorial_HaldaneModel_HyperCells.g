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


# Construction of NNN model:
# ---------------------------
# specify underlying model graph
model := TessellationModelGraph(cgpc);

# Adding NNN terms:
# -----------------
AddOrientedNNNEdgesToTessellationModelGraph(model);
Export(model, "{6,4}-tess-NNN_T2.2_3.hcm");


# Supercells:
# -----------

tgQAdjMat := TGQuotientSequencesAdjacencyMatrix(tg : boundByGenus := 10);;
sequence := LongestSequence(tgQAdjMat : quotient := 1);
sc_lst := sequence{[2..Length(sequence)]};

for sc_i_index in sc_lst do
    
    # find appropriate quotient group
    qsc_i := TGQuotient( sc_i_index );

    # construct tessellation graphs
    sc_i := TGCellSymmetric(tg, qsc_i, 3);
    scmodel_i := TGSuperCellModelGraph(model, sc_i);

    # export file
    sc_i_label := StringFormatted("_T2.2_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
    scmodel_i_name := JoinStringsWithSeparator(["{6,4}-tess-NNN", sc_i_label], "");
    Export(scmodel_i,  scmodel_i_name);

od;