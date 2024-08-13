# load the HyperCells package
LoadPackage( "HyperCells" );


# Set up triangle group:
# ----------------------

# set up ProperTriangleGroup obj.
tg := ProperTriangleGroup( [ 2, 4, 6 ] );

# set up (full) triangle group 
DELTA := FpGroup(TriangleGroup([2, 4, 6]));


# Symmetries:
# -----------

symNames := "c";
symmetries := DELTA.3;


# Primitive cell:
# ---------------

# specify the quotient defining the primitive cell
qpc := TGQuotient( 1, [ 2, 4, 6 ] );

# construct symmetric primitive cell
cgpc := TGCellGraph( tg, qpc, 3 : simplify := 5 ); # or TGCellSymmetric( tg, qpc, 3 );

# Primitive cell:
# ---------------

# construct and export PGMatrices
pgMat_T2_2 := PGMatrix(DELTA, GetTGCell(cgpc), 1, symmetries : symNames := symNames, sparse := true);
ExportPGMatrix(pgMat_T2_2, "(2,4,6)_T2.2_3_PGMatrix_c.g");

# Supercells:
# -----------
tgQAdjMat := TGQuotientSequencesAdjacencyMatrix(tg : boundByGenus := 10);;
sequence := GetLongestSequence(tgQAdjMat : quotient := 1);
sc_lst := sequence{[2..Length(sequence)]};

for sc_i_index in sc_lst do
    qsc_i := TGQuotient( sc_i_index );

    # construct TGcell 
    csc_i := TGCellSymmetric( tg, qsc_i, 3 );

    # construct and export PGMatrices
    pgMat_sc_i := PGMatrix(DELTA, csc_i, sc_i_index, symmetries : symNames := symNames, sparse := true);

    sc_i_label := StringFormatted("(2,4,6)_T{}.{}_3_PGMatrix_c.g", sc_i_index[1], sc_i_index[2]);
    ExportPGMatrix(pgMat_sc_i, sc_i_label);
od;

