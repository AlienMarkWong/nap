!-----------------------------------------------------------------------
!  Parameters for EAM Al by Mishin et al.
!  Cutoff radius should be 6.2872 Ang.
!  See Mishin et al. PRB 59(5) (1999) 3393--3407.
!-----------------------------------------------------------------------
      real(8),parameter:: am_al = 26.9815d0
      real(8),parameter:: rc_eam= 6.2872d0

      integer,parameter:: neamd = 25
      real(8):: rtbl(1:neamd)=(/ &
           2.0000, &
           2.1786, &
           2.3573, &
           2.5359, &
           2.7145, &
           2.8932, &
           3.0718, &
           3.2504, &
           3.4291, &
           3.6077, &
           3.7863, &
           3.9650, &
           4.1436, &
           4.3222, &
           4.5009, &
           4.6795, &
           4.8581, &
           5.0368, &
           5.2154, &
           5.3940, &
           5.5727, &
           5.7513, &
           5.9299, &
           6.1086, &
           6.2872 /)

      real(8):: rhotbl(1:neamd)=(/ &
           0.000, &
           0.050, &
           0.100, &
           0.150, &
           0.200, &
           0.250, &
           0.300, &
           0.350, &
           0.400, &
           0.450, &
           0.500, &
           0.550, &
           0.600, &
           0.650, &
           0.700, &
           0.750, &
           0.800, &
           0.850, &
           0.900, &
           0.950, &
           0.975, &
           1.000, &
           1.025, &
           1.050, &
           1.100 /)

      real(8):: rhoprm(1:4,1:neamd-1)= reshape([ &
          2.6945853E-01, -3.1498256E-01,  1.6548997E-01, -2.7581661E-02, &
          3.7410415E-01, -4.5908283E-01,  2.3163349E-01, -3.7701849E-02, &
          2.9691897E-01, -3.6085370E-01,  1.8996330E-01, -3.1809488E-02, &
          5.2723844E-01, -6.3332438E-01,  2.9740866E-01, -4.5932726E-02, &
         -8.6143366E-01,  9.0140257E-01, -2.6797242E-01,  2.3494558E-02, &
         -2.0630296E+00,  2.1473544E+00, -6.9862079E-01,  7.3110712E-02, &
         -1.4881488E+00,  1.5859108E+00, -5.1584731E-01,  5.3277228E-02, &
         -2.5300722E+00,  2.5475679E+00, -8.1170537E-01,  8.3617910E-02, &
          3.1382971E-01,  5.9537296E-02, -8.6141639E-02,  1.3087865E-02, &
          2.3025935E+00, -1.5942286E+00,  3.7225732E-01, -2.9265892E-02, &
          1.7192622E+00, -1.1320376E+00,  2.5018802E-01, -1.8519315E-02, &
          1.8389770E+00, -1.2226163E+00,  2.7303258E-01, -2.0439833E-02, &
          1.9498138E+00, -1.3028630E+00,  2.9239899E-01, -2.1997771E-02, &
         -8.5074437E-02,  1.0953454E-01, -3.4378466E-02,  3.2037052E-03, &
          9.9254577E-01, -6.0873528E-01,  1.2520513E-01, -8.6149383E-03, &
          4.8974785E-01, -2.8639448E-01,  5.6321535E-02, -3.7081749E-03, &
          1.3972767E+00, -8.4681657E-01,  1.7167982E-01, -1.1623360E-02, &
         -2.0134672E+00,  1.1846779E+00, -2.3165057E-01,  1.5068878E-02, &
          2.0415698E+00, -1.1478586E+00,  2.1558962E-01, -1.3515711E-02, &
         -6.9671486E-01,  3.7510288E-01, -6.6753989E-02,  3.9322935E-03, &
          3.8237511E-01, -2.0581300E-01,  3.7489176E-02, -2.3030541E-03, &
         -4.4055168E+00,  2.2916529E+00, -3.9675455E-01,  2.2864805E-02, &
          4.3122992E+00, -2.1187837E+00,  3.4700784E-01, -1.8943792E-02, &
         -7.0583196E-02,  3.3697607E-02, -5.3611582E-03,  2.8423666E-04], &
         [4,neamd-1])

      real(8):: vprm(1:4,1:neamd-1)= reshape([ &
        -1.1770531E+01,  2.5540544E+01, -1.4236446E+01,  2.3727410E+00, &
        -1.6115169E+01,  3.1523246E+01, -1.6982568E+01,  2.7929072E+00, &
         3.2160069E+01, -2.9913871E+01,  9.0799253E+00, -8.9245225E-01, &
         5.3684142E+01, -5.5377107E+01,  1.9121030E+01, -2.2123130E+00, &
         2.9391314E+01, -2.8529258E+01,  9.2304977E+00, -9.9778212E-01, &
         2.1401328E+01, -2.0244328E+01,  6.3669107E+00, -6.6786058E-01, &
         8.9076204E+00, -8.0426480E+00,  2.3947509E+00, -2.3682560E-01, &
         3.2023953E+00, -2.7769344E+00,  7.7473076E-01, -7.0690131E-02, &
         1.1198171E+01, -9.7721596E+00,  2.8146903E+00, -2.6898896E-01, &
         1.6128404E+00, -1.8014327E+00,  6.0532506E-01, -6.4854724E-02, &
        -2.1080867E+01,  1.6179478E+01, -4.1436146E+00,  3.5322623E-01, &
         8.1972955E-01, -3.9096079E-01,  3.5562783E-02,  1.8872240E-03, &
         2.8851507E+00, -1.8863425E+00,  3.9645227E-01, -2.7144656E-02, &
        -7.8220904E-01,  6.5913883E-01, -1.9247959E-01,  1.8274488E-02, &
        -1.4128089E+00,  1.0794547E+00, -2.8586444E-01,  2.5190501E-02, &
         1.1602494E+01, -7.2645800E+00,  1.4972395E+00, -1.0182477E-01, &
         1.0595405E+01, -6.6426769E+00,  1.3692258E+00, -9.3041252E-02, &
         7.3118242E+00, -4.6869225E+00,  9.8093278E-01, -6.7344180E-02, &
        -3.6697759E+00,  1.6299084E+00, -2.3025543E-01,  1.0066834E-02, &
        -3.5805448E+00,  1.5802805E+00, -2.2105485E-01,  9.4982648E-03, &
        -1.1919642E+01,  6.0695393E+00, -1.0266354E+00,  5.7684397E-02, &
        -3.1965244E+01,  1.6525750E+01, -2.8446958E+00,  1.6305538E-01, &
         2.1957340E+01, -1.0754264E+01,  1.7557213E+00, -9.5544662E-02, &
         2.2160090E+00, -1.0590808E+00,  1.6858471E-01, -8.9379855E-03], &
         [4,neamd-1])

      real(8):: fprm(1:4,1:neamd-1)= reshape([ &
         0.0000000E+00, -1.3083710E+01,  0.0000000E+00,  2.7988383E+02, &
         5.0712875E-02, -1.6126482E+01,  6.0855450E+01, -1.2581916E+02, &
        -5.8499112E-02, -1.2850122E+01,  2.8091853E+01, -1.6607177E+01, &
         4.1215095E-02, -1.4844407E+01,  4.1387081E+01, -4.6152128E+01, &
        -2.4127424E-02, -1.3864269E+01,  3.6486392E+01, -3.7984313E+01, &
         1.2221156E-02, -1.4300452E+01,  3.8231124E+01, -4.0310622E+01, &
        -1.0552892E+00, -3.6253480E+00,  2.6474447E+00, -7.7320031E-01, &
        -1.0628619E+00, -3.5604389E+00,  2.4619903E+00, -5.9657702E-01, &
        -1.0472514E+00, -3.6775179E+00,  2.7546878E+00, -8.4049161E-01, &
        -1.0471635E+00, -3.6781041E+00,  2.7559904E+00, -8.4145653E-01, &
        -1.0781353E+00, -3.4922734E+00,  2.3843291E+00, -5.9368228E-01, &
        -1.0465020E+00, -3.6648183E+00,  2.6980470E+00, -7.8381437E-01, &
        -1.3300569E+00, -2.2470439E+00,  3.3508961E-01,  5.2893974E-01, &
        -1.2584116E+00, -2.5777148E+00,  8.4381410E-01,  2.6805539E-01, &
        -1.4404702E+00, -1.7974633E+00, -2.7083086E-01,  7.9883871E-01, &
        -1.3298340E+00, -2.2400083E+00,  3.1922919E-01,  5.3658979E-01, &
        -1.1855587E+00, -2.7810407E+00,  9.9551957E-01,  2.5480213E-01, &
        -1.5475237E+00, -1.5035171E+00, -5.0744927E-01,  8.4420168E-01, &
        -1.2006578E+00, -2.6597367E+00,  7.7723917E-01,  3.6839115E-01, &
        -7.2627326E-01, -4.1577932E+00,  2.3541407E+00, -1.8490765E-01, &
        -2.7070932E+00,  1.9370375E+00, -3.8969677E+00,  1.9522234E+00, &
         6.8691162E+00, -2.6791591E+01,  2.4831661E+01, -7.6239860E+00, &
         2.3809518E+00, -1.3655500E+01,  1.2015962E+01, -3.4562792E+00, &
         7.0904855E+00, -2.7111311E+01,  2.4831020E+01, -7.5245515E+00], &
         [4,neamd-1])
