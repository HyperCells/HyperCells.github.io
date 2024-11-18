# load the HyperCells package
LoadPackage( "HyperCells" );


# --------------
# Preliminaries:
# --------------

# (Proper) triangle group:
# ------------------------

# TriangleGroup obj. and group
fulltg := TriangleGroup( [ 2, 4, 6 ] );
DELTA := FpGroup(fulltg);

# ProperTriangleGroup obj. and group
tg := ProperTriangleGroup( [ 2, 4, 6 ] );
D := FpGroup(tg);


# ---------------------------
# Point-group matrix example:
# ---------------------------

# specify the quotient defining the primitive cell
qpc := TGQuotient( 1, [ 2, 4, 6 ] );

# get the PGMatricesOfGenerators
pgMatGs := PGMatricesOfGenerators(fulltg, tg, qpc);

# symmety
symName := "c";;
symmetry := DELTA.3;

# get the corresponding point-group matrix
EvaluatePGMatrix(symmetry, pgMatGs);


# ---------------------------
# Construct PGMatrices obj.s:
# ---------------------------

# symmety
symName := "z";;
symmetry := D.3;

# Quotient T2.2 (primitive cell):
# -------------------------------

# get the PGMatricesOfGenerators
pgMatGs := PGMatricesOfGenerators(fulltg, tg, qpc : sparse := true);

# construct and export the PGMatrices
pgMat_T2_2 := PGMatrices(symmetry, pgMatGs : symNames := symName);
Export(pgMat_T2_2, "(2,4,6)-T2.2-pgMat_z_sparse.hcpgm");


# Quotients T5.4, T9.3 (supercells):
# ---------------------------------
tgQSS := TGQuotientSequencesStructure(tg : boundByGenus := 10);;
sequence := LongestSequence(tgQSS : quotient := 1);
sc_lst := sequence{[2..Length(sequence)]};

for sc_i_index in sc_lst do
    qsc_i := TGQuotient( sc_i_index );

    # get the PGMatricesOfGenerators
    pgMatGs := PGMatricesOfGenerators(fulltg, tg, qsc_i : sparse := true);

    # construct and export the PGMatrices
    pgMat_sc_i := PGMatrices(symmetry, pgMatGs : symNames := symName);

    sc_i_label := StringFormatted("(2,4,6)-T{}.{}-pgMat_z_sparse.hcpgm", sc_i_index[1], sc_i_index[2]);
    Export(pgMat_sc_i, sc_i_label);
od;

