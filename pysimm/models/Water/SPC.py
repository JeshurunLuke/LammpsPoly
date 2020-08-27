from pysimm import system, lmps, forcefield
from pysimm.apps.random_walk import random_walk


def SPC():
    try:
        s = system.read_pubchem_smiles('[H]O[H]')
    except:
        import os
        s = system.read_mol(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'CC.mol'))
    f = forcefield.Dreiding()
    s.apply_forcefield(f)
    for pb in s.particles:
        if pb.elem == 'H':
            pb.charge = 0.4238
        elif pb.elem == 'O':
            pb.charge = -0.8476


    lmps.quick_min(s, min_style='fire')


    return s

