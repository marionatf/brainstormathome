from boinc2docker_create_work import boinc2docker_create_work
from cStringIO import StringIO
import tarfile

def add_file_to_tar(tgz,filename,data):
    info = tarfile.TarInfo(filename)
    info.size = len(data)
    tgz.addfile(info, StringIO(data))


myfileobj = StringIO()
with tarfile.open(fileobj= myfileobj, mode='w:gz') as tgz: 
    tgz.add(name='/home/boincadm/project/input_files/test_gromacs/lisozime/md_0_1.tpr',arcname='md_0_1.tpr')


boinc2docker_create_work(
               image="claughton/gromacs2018:latest",
               command= "mdrun -v -s  /root/shared/md_0_1.tpr -g /root/shared/results/md_0_1.log -o /root/shared/results/md_0_1.trr -c /root/shared/results/md_0_1.gro -e /root/shared/results/md_0_1.edr -cpo /root/shared/results/md_0_1.cpt",
#               appname="testsim",
               prerun="tar zxvf /root/shared/inputfiles.tgz -C /root/shared",
               input_files=[('shared/inputfiles.tgz', myfileobj.getvalue() ,[]),
                   ],
               )

