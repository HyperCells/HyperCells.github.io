# load the HyperCells package
LoadPackage( "HyperCells" );

# set up (proper) triangle group
tg := ProperTriangleGroup( [ 2, 8, 8 ] );;

# Construct the quotient sequences adjacency matrix:
# --------------------------------------------------
# caution, this may take a few minutes
tgQSAdjMat := TGQuotientSequencesAdjacencyMatrix(tg : sparse := true, boundByGenus := 66);;
Export(tgQSAdjMat, "(2,8,8)-adjMat-BBG_66_sparse.hcqs");

