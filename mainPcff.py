from pysimm import system, lmps, forcefield
from pysimm.apps.random_walk import copolymer
from pysimm.models.monomers.Pcff.pe import monomer as pe_monomer
from pysimm.models.monomers.Pcff.ps import monomer as ps_monomer
from pysimm.models.monomers.Pcff.ba import monomer as ba_monomer
from pysimm.models.monomers.Pcff.peg5 import monomer as peg_monomer
from pysimm.models.monomers.Pcff.amide import monomer as amide_monomer
from pysimm.models.monomers.Pcff.disE import monomer as dise_monomer
from pysimm.models.monomers.Pcff.disG import monomer as disg_monomer
from pysimm.models.monomers.Pcff.disI import monomer as disi_monomer
from pysimm.models.Water.SPC import SPC as water_water
from pysimm.models.Ions.BasicIons.Na import Na as pos_salt
from pysimm.models.Ions.BasicIons.Cl import Cl as neg_salt

from pysimm import system

import numpy as np
import random
import multiprocessing
import time




def run(test=False):
    # we'll make a polyethylene monomer and a polystyrene monomer from the pysimm models database
    pe = pe_monomer()
    ps = ps_monomer()
    ba = ba_monomer()
    H20 = water_water()
    dise = dise_monomer()
    disg = disg_monomer()
    disi = disi_monomer()
    amide = amide_monomer()
    peg = peg_monomer()
    Na = pos_salt()
    Cl = neg_salt()




    # we'll instantiate a Dreiding forcefield object for use later
    f = forcefield.Pcff()

    # the monomers do not have any charges, so we will derive partial charges using the gasteiger algorithm
    pe.apply_charges(f, charges='gasteiger')
    ps.apply_charges(f, charges='gasteiger')
    #H20.apply_charges(f,charges = 'gasteiger')
    ba.apply_charges(f,charges = 'gasteiger')
    peg.apply_charges(f,charges = 'gasteiger')
    amide.apply_charges(f,charges = 'gasteiger')
    dise.apply_charges(f,charges='gasteiger')


    # the buckingham potential isn't great at small distances, and therefore we use the LJ potential while growing the polymer
    pe.pair_style = 'lj/cut'
    ps.pair_style = 'lj/cut'
    H20.pair_style = 'lj/cut'
    ba.pair_style = 'lj/cut'
    dise.pair_style = 'lj/cut'
    disg.pair_style = 'lj/cut'
    peg.pair_style = 'lj/cut'
    amide.pair_style = 'lj/cut'
    disi.pair_style = 'lj/cut'
    Na.pair_style = 'lj/cut'
    Cl.pair_style = 'lj/cut'





    ##### Specifiy What Monomer that you are going to use and the frequency of each Monomer
    polist = [ba, amide, disg,disi,dise]
    monlist = [2,2,1,1,1]
    n_molecules = 10000 # Number of Water Molecules Try to keep it at 10,000

    ##Current Monomers available
    # PEG5 : peg
    # Butyl Acrylate : ba
    # amide monomer: amide
    # Ethelyne: pa
    # Polystyrene: ps
    # MethylAcrylate: pmma
    # disulfideG: disg
    # disulfideI: disi
    # disulfideE: dise
    ####################################################################################




    pattern = shuffle(monlist, polist)

    # run the copolymer random walk method with 10 total repeat units, using an alternating pattern
    z = np.ones(len(pattern))
    setter = []
    for elem in range(0, len(z)):
        setter.append(int(z[elem]))
    print(setter)
    polymer = copolymer(pattern, len(pattern), pattern=setter, forcefield=f)

    polymer.write_xyz('polymernonsolvated.xyz')


    charge = 0
    for pb in polymer.particles:
        charge = charge + pb.charge
    print("The System has: " + str(charge) + " charge")

    numSa = round(charge)
    if charge<0:
        salt = 'Na'
        charg = +1
    else:
        salt = 'Cl'
        charg = -1



    partition = n_molecules/(abs(numSa)+1)
    if round(charge) == 0:
        system.replicate([H20], n_molecules, s_=polymer, density=0.6)
    else:
        for iters in range(0, abs(numSa)+1):

            system.replicate([H20], abs(int(partition)),s_ = polymer, density=0.6)
            if iters == abs(numSa):
                lmps.quick_min(polymer, min_style='sd')
                break
            m = polymer.molecules.add(system.Molecule())
            dreiding_salt_ = polymer.particle_types.add(f.particle_types.get(salt)[0].copy())
            polymer.particles.add(system.Particle(type=dreiding_salt_, x=polymer.dim.dx/2, y=polymer.dim.dy/2, z=polymer.dim.dz/2, charge=charg, molecule=m))
            lmps.quick_min(polymer, min_style='sd')



    charge = 0
    for pb in polymer.particles:
        charge = charge + pb.charge
    print("The System has: " + str(charge) + " charge")



    # write a few different file formats
    polymer.write_xyz('polymersolvated.xyz')
    # polymer.write_yaml('polymer.yaml')
    polymer.write_lammps('polymer.lmps')
    # polymer.write_chemdoodle_json('polymer.json')


def shuffle(plist, baser):
    returner = []
    x = np.arange(1, len(plist) + 1)
    monlist = []
    total = sum(plist)
    for elem in range(0, total):
        weight = []
        for e in range(0, len(x)):
            weight.append(plist[e] / sum(plist))
        choice = random.choices(x, weights=weight, k=1)

        monlist.append(choice[0])
        plist[choice[0] - 1] = plist[choice[0] - 1] - 1
    for elem in range(0, len(monlist)):
        returner.append(baser[monlist[elem] - 1])

    return returner

run()