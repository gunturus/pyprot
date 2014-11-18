"""
Sebastian Raschka 2014

Unit tests for  mol2_atom_dict function in mol2filter.py

"""

from pyprot.mol2filter import create_atom_dict

def test_create_atom_dict():
    d1 = create_atom_dict(group_charge_pairs=['O.2,-1.12,-0.792', 'O.3,-0.595,-0.315'] ,atom_dict=None)
    assert d1 == {'O.2':[-1.12, -0.792], 'O.3':[-0.595, -0.315]}
    
    d2 = create_atom_dict(group_charge_pairs=['O.2,-1.12,-0.792', 'O.4,-0.595,-0.315'] ,atom_dict=d1)
    assert d2 == {'O.2':[-1.12, -0.792], 'O.3':[-0.595, -0.315], 'O.4':[-0.595, -0.315]}
