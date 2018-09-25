from boinc2docker_create_work import boinc2docker_create_work

#--- File with all commands -->  Permission problems
#boinc2docker_create_work("python:alpine",
#              "/root/shared/myinput.txt",
#                    input_files=[("shared/myinput.txt", open("/home/boincadm/project/test.txt").read(), [])]
#             )

#-- Call more than 1 command --> Only 1st executed
#boinc2docker_create_work("python:alpine",
##              "python -c print(open('/root/shared/myinput.txt').read())",
#               "python -c print(';)');  python -c print(':)')",
#               input_files=[("shared/myinput.txt", open("/home/boincadm/project/testinput.txt").read(), [])])


#-- Tests on how to open files at input_files:
#boinc2docker_create_work("python:alpine",
#              "python -c print(open('/root/shared/myinput.txt').read())",
#               input_files=[("shared/myinput.txt", "/home/boincadm/project/testinput.txt", [])])


#-- Tests on how to send tar files
#boinc2docker_create_work(
#               image="python:alpine",
#               command="python -c print(open('/root/shared/myinput.txt').read())",
#               prerun="tar zxvf /root/shared/inputfiles.tgz -C /root/shared",
#               input_files=[('shared/inputfiles.tgz', "/home/boincadm/project/input_files/test_py/inputfiles.tgz" ,[])],
#               )
from cStringIO import StringIO
import tarfile

def add_file_to_tar(tgz,filename,data):
    info = tarfile.TarInfo(filename)
    info.size = len(data)
    tgz.addfile(info, StringIO(data))


myfileobj = StringIO()
with tarfile.open(fileobj= myfileobj, mode='w:gz') as tgz:
    # File to print
    data="""Text to be printed 
    
    :D
    
    ^^
    """
    add_file_to_tar(tgz,"myinput_print.txt",data)

    #Script
    data2="""        
        python -c 'print("Hello there")'
        python -c 'print("The angel from my nightmare")'
    """
    add_file_to_tar(tgz,"myscript.ini",data2)
 
    tgz.add(name='/home/boincadm/project/myinputTEST.py',arcname='myinputTEST.py')

boinc2docker_create_work(
               image="python:alpine",
               command="python  /root/shared/myinputTEST.py",
               prerun="tar zxvf /root/shared/inputfiles.tgz -C /root/shared",
               input_files=[('shared/inputfiles.tgz', myfileobj.getvalue() ,[]),
                   ],
               )

