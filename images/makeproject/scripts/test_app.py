from boinc2docker_create_work import boinc2docker_create_work

# boinc2docker_create_work("python:alpine", 
#  ["python", "-c", "print(open('/root/shared/myinput.txt').read())"], 
#  input_files=[("shared/myinput.txt", open("/root/project/testinput.txt").read(), [])])

cinput_path="/root/shared/"
coutput_path="/root/shared/results/"

boinc2docker_create_work("claughton/gromacs2018:latest", 
   ["pdb2gmx", "-f", "/root/shared/E2Bwt.pdb", "-o", "/root/shared/results/E2Bwt.gro", "-p", "/root/shared/results/E2Bwt.top", "-ignh", "-ff", "gromos53a6", "-water", "spc"], 
   input_files=[("shared/E2Bwt.pdb", open("/root/project/input_files/E2Bwt.pdb").read(), [])],
   )

# boinc2docker_create_work("claughton/gromacs2018:latest", 
#    ["mdrun", "-deffnm", "/root/shared/E2Bwt-EM-vacuum", "-c", "E2Bwt-EM-vacuum.gro"], 
#    input_files=[("shared/E2Bwt-EM-vacuum.tpr", open("/root/project/input_files/E2Bwt-EM-vacuum.tpr").read(), [])],
#    )



# pdb2gmx -f E2Bwt.pdb -o E2Bwt.gro -p E2Bwt.top -ignh -ff gromos53a6 -water spc
# grompp -v -f minim.mdp -c E2Bwt.gro -p E2Bwt.top -o E2Bwt-EM-vacuum.tpr 
# mdrun -deffnm E2Bwt-EM-vacuum -c E2Bwt-EM-vacuum.gro



# Check output
# Script to create WU when other WI ends