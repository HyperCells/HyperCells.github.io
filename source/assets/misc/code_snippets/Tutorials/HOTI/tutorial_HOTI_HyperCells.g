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

# Supercells:
# -----------
tgQSS := TGQuotientSequencesStructure(tg : boundByGenus := 10);;
sequence := GetLongestSequence(tgQSS : quotient := 1);
sc_lst := sequence{[2..Length(sequence)]};

for sc_i_index in sc_lst do
    qsc_i := TGQuotient( sc_i_index );

    sc_i := TGCellSymmetric(tg, qsc_i, 3);
    scmodel_i := TGSuperCellModelGraph(model, sc_i);

    sc_i_label := StringFormatted("_T2.2_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
    scmodel_i_name := JoinStringsWithSeparator(["{6,4}-tess-NN", sc_i_label], "");
    Export(scmodel_i,  scmodel_i_name); # export file
od;