# load the HyperCells package
LoadPackage( "HyperCells" );

# Function to extract a particular sequence of supercells:
# --------------------------------------------------------

getMthSupercellQuotient := function(tg, tgGamma, n1)
        local tgGamma_n, Gamma1, qn, signat, switch, 
        i, D, rels, G, Gplus, a, b, c, DELTA, 
        embDDELTA, relsfull;


  # signature (2, q, p)
  signat := Signature(tg);

  # presentation of the proper triangle group  
  D := FpGroup(tg);

  # translation group in terms of generators x, y, z
  Gamma1 := AsTGSubgroup(tgGamma);
	
  # presentation of the (full) triangle group
  DELTA := FpGroup(TriangleGroup(Signature(tg)));
  a := DELTA.1;; b := DELTA.2;; c := DELTA.3;

  # embedding homomorphism of D in DELTA
  embDDELTA := GroupHomomorphismByImagesNC(D, DELTA,
      GeneratorsOfGroup(D), [a*b, b*c, c*a]);

  i := n1;
  switch := false;
  while switch = false do
                
    qn := TGQuotient(i, signat);
    tgGamma_n := TGTranslationGroup(tg, qn);
    switch := IsSubgroup(Gamma1, AsTGSubgroup(tgGamma_n));
    if switch then
		
      # proper point group
      rels := TGQuotientRelators(tg, qn);
      Gplus := D / rels;
      
      # (full) point group
      relsfull := List(rels, r -> Image(embDDELTA, r));
      G := DELTA / relsfull;
      
      # ensure that quotient is mirror symmetric
      if not Order(G) = 2 * Order(Gplus) then
        switch := false;
      fi; 
     fi;
  
   i := i + 1;
  od;

 return [qn, tgGamma_n, i];
end;;


# Constuct supercell sequence {8,8}-lattice: 
# -------------------------------------------

# set up (proper) triangle group
tg := ProperTriangleGroup( [ 2, 8, 8 ] );

# Primitive cell:
# ---------------

# specify the quotient defining the primitive cell
qpc := TGQuotient( 1, [ 2, 8, 8 ] );

# construct symmetric primitive cell
cgpc := TGCellGraph( tg, qpc, 3 : simplify := 5 );

# associated translation group
tgGamma_pc1 := TGTranslationGroup( tg, qpc );

# elementary nearest-neighbor model
model := TessellationModelGraph( cgpc, true : simplify := 5 );
Export( model, "{8,8}-tess_T2.6_3.hcm" ); # export

# Supercells:
# -----------

n0 := 2;
tgGamma_sc_i := tgGamma_pc1;

for i in [1 .. 6] do
  
  # find appropriate quotient group
  qANDtgGamma_sc_i := getMthSupercellQuotient(tg, tgGamma_sc_i, n0);
  qsc_i := qANDtgGamma_sc_i[1];;
  tgGamma_sc_i := qANDtgGamma_sc_i[2];; 
  n0 := qANDtgGamma_sc_i[3];;

  # construct tessellation graphs
  sc_i := TGCellSymmetric(tg, qsc_i, 3);
  scmodel_i := TGSuperCellModelGraph(model, sc_i);

  # export file
  sc_i_index := TGQuotientName(qsc_i);
  sc_i_label := StringFormatted("-tess_T2.6_3_sc-T{}.{}.hcs", sc_i_index[1], sc_i_index[2]);
  scmodel_i_name := JoinStringsWithSeparator(["{8,8}", sc_i_label], "");
  Export(scmodel_i,  scmodel_i_name);

od;


