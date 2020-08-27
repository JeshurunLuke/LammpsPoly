from pysimm import system, lmps, forcefield
from pysimm.apps.random_walk import random_walk


def monomer():
    try:
        import os
        s = system.read_mol(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'disIpro.mol'))

      #  s = system.read_pubchem_smiles('CCC(OCCSSCCN)=O')
    except:
        import os
        s = system.read_mol(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'CC(C)C(=O)OC.mol'))
    f = forcefield.Gaff()
    s.apply_forcefield(f)

    c3 = s.particles[1]
    c4 = s.particles[2]

    for b in c3.bonds:
        if b.a.elem == 'H' or b.b.elem == 'H':
            pb = b.a if b.b is c3 else b.b
            s.particles.remove(pb.tag, update=False)
            break

    for b in c4.bonds:
        if b.a.elem == 'H' or b.b.elem == 'H':
            pb = b.a if b.b is c4 else b.b
            s.particles.remove(pb.tag, update=False)
            break

    s.remove_spare_bonding()

    c3.linker = 'head'
    c4.linker = 'tail'

    lmps.quick_min(s, min_style='cg')

    s.add_particle_bonding()
    s.apply_charges(f,charges = 'gasteiger')
    for pb in s.particles:
        if pb.elem == 'N':
            pb.charge = pb.charge + 1.0

    return s


def polymer_chain(length):
    mon = monomer()
    polym = random_walk(mon, length, forcefield=forcefield.Dreiding())
    return polym