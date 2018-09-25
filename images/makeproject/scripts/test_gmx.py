from boinc2docker_create_work import boinc2docker_create_work
from cStringIO import StringIO
import tarfile

def add_file_to_tar(tgz,filename,data):
    info = tarfile.TarInfo(filename)
    info.size = len(data)
    tgz.addfile(info, StringIO(data))

#     Mdrun
# ----------------
# mdrun produces at least four output files. 
#   A single log file (-g) is written. 
#   The trajectory file (-o), contains coordinates, velocities and optionally forces. 
#   The structure file (-c) contains the coordinates and velocities of the last step. 
#   The energy file (-e) contains energies, the temperature, pressure, etc, a lot of these things are also printed in the log file.

myfileobj = StringIO()
with tarfile.open(fileobj= myfileobj, mode='w:gz') as tgz: 
    tgz.add(name='/home/boincadm/project/input_files/test_gromacs/topol.tpr',arcname='topol.tpr')


boinc2docker_create_work(
               image="claughton/gromacs2018:latest",
               command="mdrun -s /root/shared/topol.tpr -g /root/shared/results/md.log -o /root/shared/results/traj_comp.trr -c /root/shared/results/coords.pdb -e /root/shared/results/energy.txt -nb cpu -pme cpu -pmefft cpu",
#              command=["pdb2gmx", "-f", "/root/shared/E2Bwt.pdb", "-o", "/root/shared/results/E2Bwt.gro", "-p", "/root/shared/results/E2Bwt.top", "-ignh", "-ff", "gromos53a6", "-water", "spc"],
#               appname="testsim",
               prerun="tar zxvf /root/shared/inputfiles.tgz -C /root/shared",
               input_files=[('shared/inputfiles.tgz', myfileobj.getvalue() ,[]),
                   ],
               )

