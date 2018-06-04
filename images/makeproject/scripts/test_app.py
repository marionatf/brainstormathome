from boinc2docker_create_work import boinc2docker_create_work

boinc2docker_create_work("python:alpine", 
  ["python", "-c", "print(open('/root/shared/myinput.txt').read())"], 
  input_files=[("shared/myinput.txt", open("/root/project/testinput.txt").read(), [])])

