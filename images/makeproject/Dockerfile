FROM boinc/server_makeproject:2.1.0-b2d
COPY scripts/test_app.py /root/project/bin
COPY input_files /root/project/input_files
COPY html/project/project.inc /root/project/html/project/project.inc
COPY html/user/img /root/project/html/user/img
COPY html/user/index.php /root/project/html/user/index.php

# COPY conf/brainstorm.httpd.conf /root/project/brainstorm.httpd.conf
# COPY conf/config.xml /root/project/config.xml
# COPY html/user/schedulers.txt /root/project/html/user/schedulers.txt
COPY html/user_profile/profile_country.html /root/project/html/user_profile/profile_country.html
COPY html/user_profile/user_gallery_1.html /root/project/html/user_profile/user_gallery_1.html

