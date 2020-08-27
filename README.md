# LammpsPol
# What does it do?

Basically in mainDreiding.py you can select the monomers you want in your polymer as well as the frequency of each monomer and the number of water molecules. Once you specify these paramaters, you can run mainDreiding.py and it will output a charge-neutral minimized system of a random copolymer with the monomers you picked. The system will be written as a lammps data file and it was written with the Dreiding Potential Paramaters! The data file known as polymer.lmps can be used to run a simulation when paired with the input file basic.in

# What do I need to do to run mainDreiding.py? (Instructions for Windows)

You need to activate the wsl for windows and the instructions are given here: https://docs.microsoft.com/en-us/windows/wsl/install-win10. Once you have followed the instructions and installed the Ubuntu terminal input the following commands into your terminal in the following order



1) sudo apt update

2) sudo apt upgrade

3) sudo apt install make

4) sudo apt install cmake

5) sudo apt install mpirun

6) sudo apt install python3

7) sudo apt install git


This should set up everything needed! Now its time you get yourself a Python IDE. I recommend Pycharm Professional Version or Visual Studios (Both Free given you have a UNC email or other university email). Now start a new project (Instructions will be straight forward once you install Pycharm Professional Version). Finally in your Ubuntu command prompt go to the folder of the project using the command:

1) cd /mnt/c/Users/(User Name)/PycharmProjects/(Project Name)


For example, In my computer to go to my python Project folder which I named Lammps3, I typed the following in the Ubuntu Command prompt:

cd /mnt/c/Users/jeshu/PycharmProjects/Lammps3


your almost done! Now you just need to set up your lammps to do so follow the following commands in your Ubuntu Command Prompt

1) git clone https://github.com/JeshurunLuke/LammpsPolymer.git
2) cd LammpsPolymer
3) python3 pysimm1/complete_install.py --lammps $PWD
4) echo "export LAMMPS_EXEC=$PWD/lammps/src/lmp_mpi" >> ~/.bashrc
5) echo "export PATH=$PATH:$PWD/lammps/src" >> ~/.bashrc
6) source ~/.bashrc
7) sudo apt install python3-pip
9) pip3 install numpy
9) pip3 install random
10) pip3 install pandas
11) pip3 install pytest

Thats it!! Everything is setup for your run!! Now you can run the python File by typing:

1) python3 mainDreiding.py

in your Ubuntu Terminal! Now if you check your folder you will see polymer.lmps and you can run your lammps simulation using 

1) lmp_mpi -in basic.in

in your Ubuntu terminal!


How to change to the polymer composition and number of water molecules?



To change the composition of your system all you need to do is open up main.py and then scroll down till you see this section:


    ##### Specifiy What Monomer that you are going to use and the frequency of each Monomer
    polist = [ba, amide, disg,disi,dise]
    monlist = [1,3,3,2,1]
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
 
Here is where you can change the monomer component and frequency for example say you want a 100mer of 50 percent peg and ba polymer all you need to do is edit polist and monlist in the following way

polist = [ba, peg]

monlist = [50,50]

Once you edit the monlist and polist you can rerun main.py again with ("python3 main.py) and polymer.lmps will be updated with the setup you specified! Thats it your good to go! Let me know if you have any questions

Credit: The pysimm package was created and done by another group. The pysimm version here is an edit version that allows for compatability with more monomers and the SPC water model. The dreiding package is more paramatized as such. The original pysimm package is here: https://github.com/polysimtools/pysimm.git 




# What do I do to run main.py? (Instructions for Mac)

With Mac you can actually go ahead and run the commands in the bottom in your command prompt without doing any prerequisite steps!!!


1) sudo apt update

2) sudo apt upgrade

3) sudo apt install make

4) sudo apt install cmake

5) sudo apt install mpirun

6) sudo apt install python3

7) sudo apt install git


This should set up everything needed! Now its time you get yourself a Python IDE. I recommend Pycharm (Professional or Community Version) or Visual Studios (Community is free and professional and visual studios are free as well given you have a university email). Now start a new project (Instructions will be straight forward once you install your Pycharm Version). Finally in your mac command prompt go to the folder of your new project using the command:

1) cd (Location of the Project Folder)


For example, In my computer to go to my python Project folder which I named Lammps3, I typed the following in the Command prompt:

cd /mnt/c/Users/jeshu/PycharmProjects/Lammps3

your almost done! Now you just need to set up your lammps to do so follow the following commands in your mac Command Prompt

1) git clone https://github.com/JeshurunLuke/LammpsPolymer.git
2) cd LammpsPolymer
3) python3 complete_install.py --lammps $PWD
4) source ~/.bashrc
5) sudo apt install python3-pip
6) pip3 install numpy
7) pip3 install random
8) pip3 install pandas
9) pip3 install pytest

Thats it!! Everything is setup for your run!! Now you can run the python File by typing:

1) python3 mainDreiding.py

in your Mac Terminal! Now if you check your folder you will see polymer.lmps and you can run your lammps simulation using 

1) lmp_mpi -in basic.in

in your Mac terminal!


How to change to the polymer composition and number of water molecules?



To change the composition of your system all you need to do is open up main.py and then scroll down till you see this section:


    ##### Specifiy What Monomer that you are going to use and the frequency of each Monomer
    polist = [ba, amide, disg,disi,dise]
    monlist = [1,3,3,2,1]
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
 
Here is where you can change the monomer component and frequency for example say you want a 100mer of 50 percent peg and ba polymer all you need to do is edit polist and monlist in the following way

polist = [ba, peg]

monlist = [50,50]

Once you edit the monlist and polist you can rerun main.py again with ("python3 main.py) and polymer.lmps will be updated with the setup you specified! Thats it your good to go! Let me know if you have any questions


Warning: The Code can take a significant amount of time to run anywhere from 40-50 min if you are doing a 100mer with 100,000 water molecules. To reduce the time you can either reduce the size of your polymer or reduce the number of water molecules. 

Credit: The pysimm package was created and done by another group. The pysimm version here is an edit version that allows for compatability with more monomers and the SPC water model. The dreiding package is more paramatized as such. The original pysimm package is here: https://github.com/polysimtools/pysimm.git 


# What about the Other Mains?
mainPcff.py, mainGaff.py, and mainGaff2.py are work in progess duplicates of the mainDreiding but with the Pcff, Gaff and Gaff2 forcefield implementation. Currently, running these programs will give you error as certain dihedrals cannot be typed.