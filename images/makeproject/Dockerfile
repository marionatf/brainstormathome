FROM boinc/server_makeproject:3.0.1-b2d

USER $BOINC_USER 

# Config
COPY --chown=1000  conf/brainstorm.httpd.conf $PROJECT_ROOT/brainstorm.httpd.conf
COPY  --chown=1000 conf/config.xml $PROJECT_ROOT/config.xml
COPY  --chown=1000 conf/schedulers.txt $PROJECT_ROOT/html/user/schedulers.txt

#HTML
#COPY html $PROJECT_ROOT/html
COPY  --chown=1000 html/project/project.inc $PROJECT_ROOT/html/project/project.inc
COPY  --chown=1000 html/user/img $PROJECT_ROOT/html/user/img
COPY  --chown=1000 html/user/index.php $PROJECT_ROOT/html/user/index.php
COPY  --chown=1000 html/user/join.php  $PROJECT_ROOT/html/user/join.php
COPY  --chown=1000 html/user_profile/profile_country.html $PROJECT_ROOT/html/user_profile/profile_country.html
COPY  --chown=1000 html/user_profile/user_gallery_1.html $PROJECT_ROOT/html/user_profile/user_gallery_1.html
COPY  --chown=1000 html/inc/host.inc $PROJECT_ROOT/html/inc/host.inc
COPY  --chown=1000 html/inc/bootstrap.inc $PROJECT_ROOT/html/inc/bootstrap.inc

# Apps
COPY  --chown=1000 scripts/test_app.py $PROJECT_ROOT/bin
COPY  --chown=1000 input_files $PROJECT_ROOT/input_files

COPY  --chown=1000  apps/testsim_boinc2docker/ $PROJECT_ROOT
RUN boinc2docker_create_app --projhome $PROJECT_ROOT $PROJECT_ROOT/apps_boinc2docker/testsim/boinc2docker.yml

COPY  --chown=1000  apps/nmda_boinc2docker/ $PROJECT_ROOT
RUN boinc2docker_create_app --projhome $PROJECT_ROOT $PROJECT_ROOT/apps_boinc2docker/nmda/boinc2docker.yml
