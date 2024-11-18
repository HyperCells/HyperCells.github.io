# load the HyperCells package
LoadPackage( "HyperCells" );

# set up (proper) triangle group
tg := ProperTriangleGroup( [ 2, 8, 8 ] );;

# Construct the quotient sequences adjacency matrix:
# --------------------------------------------------
tgQSS := TGQuotientSequencesStructure(tg : sparse := true, boundByGenus := 66);;
Export(tgQSS, "(2,8,8)-QSS-BBG_66_sparse.hcqs");

