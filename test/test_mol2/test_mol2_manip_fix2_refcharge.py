from pyprot.mol2.mol2_manip import fix2ref_charge 

ref_mol2 = """@<TRIPOS>MOLECULE
test_mol1
   34    35     0     0     0
SMALL
USER_CHARGES

mmff94s_NoEstat = 53.58
@<TRIPOS>ATOM
      1 C1          0.1446   -2.8193    3.9343 C.ar      1 <0>        -0.0646
      2 C2          0.5814   -4.5093    2.2638 C.ar      1 <0>        -0.0385
      3 C3          0.3929   -3.7512    4.9420 C.ar      1 <0>        -0.1562
      4 C4          0.8299   -5.4411    3.2715 C.ar      1 <0>        -0.1542
      5 C5          0.2388   -3.1984    2.5951 C.ar      1 <0>        -0.1413
@<TRIPOS>BOND
      1    1    3 test
      2    1    5 ar
      3    2    4 ar
      30   10   29 1
      31   11   30 1""".split('\n')


fix_mol2 = """@<TRIPOS>MOLECULE
test_mol2
   34    35     0     0     0
SMALL
USER_CHARGES

mmff94s_NoEstat = 53.58
@<TRIPOS>ATOM
      1 C1          0.1446   -2.8193    3.9343 C.ar      1 <0>        -0.0000
      2 C2          0.5814   -4.5093    2.2638 C.ar      1 <0>        -0.0000
      3 C3          0.3929   -3.7512    4.9420 C.ar      1 <0>        -0.0000
      4 C4          0.8299   -5.4411    3.2715 C.ar      1 <0>        -0.0000
      5 C5          0.2388   -3.1984    2.5951 C.ar      1 <0>        -0.0000
@<TRIPOS>BOND
     1    1    3 ar
     2    1    5 hello
     3    2    4 ar
    30   10   29 1
    31   11   30 1""".split('\n')

result = """@<TRIPOS>MOLECULE
test_mol2
   34    35     0     0     0
SMALL
USER_CHARGES

mmff94s_NoEstat = 53.58
@<TRIPOS>ATOM
      1 C1          0.1446   -2.8193    3.9343 C.ar      1 <0>        -0.0646
      2 C2          0.5814   -4.5093    2.2638 C.ar      1 <0>        -0.0385
      3 C3          0.3929   -3.7512    4.9420 C.ar      1 <0>        -0.1562
      4 C4          0.8299   -5.4411    3.2715 C.ar      1 <0>        -0.1542
      5 C5          0.2388   -3.1984    2.5951 C.ar      1 <0>        -0.1413
@<TRIPOS>BOND
     1    1    3 ar
     2    1    5 hello
     3    2    4 ar
    30   10   29 1
    31   11   30 1"""


def test_fix2ref_charge():
    out = fix2ref_charge(ref_mol2, fix_mol2, ref_col=-1, fix_col=-1)
    assert '\n'.join(out) == result


