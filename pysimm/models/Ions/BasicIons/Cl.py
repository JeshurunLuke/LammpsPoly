from pysimm import system, lmps, forcefield

def Cl():
    s = system.System()
    m = s.molecules.add(system.Molecule())
    f = forcefield.Dreiding()
    dreiding_Na_ = s.particle_types.add(f.particle_types.get('Cl')[0].copy())
    s.particles.add(system.Particle(type=dreiding_Na_, x=0, y=0, z=0, charge=-1, molecule=m))
    s.apply_forcefield(f)
    s.pair_style = 'lj/cut'

    lmps.quick_min(s, min_style='fire')
    return s