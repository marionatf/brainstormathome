FROM boinc/server_makeproject:2.1.0-b2d
COPY scripts/test_app.py /root/project/bin
COPY input_files /root/project/input_files
COPY html/project/project.inc /root/project/html/project/project.inc
COPY html/user/img /root/project/html/user/img
COPY html/user/index.php /root/project/html/user/index.php
COPY config.xml /root/project

# install app: shortsim
COPY apps/shortsim_boinc2docker/ /root/project
RUN boinc2docker_create_app --projhome /root/project /root/project/apps_boinc2docker/shortsim/boinc2docker.yml

