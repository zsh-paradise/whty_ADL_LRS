﻿# ADL LRS

#### 本篇是天喻教育xapi系统部署文档，python2.7，postgres9.6


## 初始化

**Install Postgres** 参看文献https://wiki.postgresql.org/wiki/YUM_Installation 

    sudo  yum install https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-redhat96-9.6-3.noarch.rpm
 
    sudo yum install postgresql96-server
    
    sudo yum install postgresql96-devel
 
    sudo /usr/pgsql-9.6/bin/postgresql96-setup initdb

    
    admin:~$ sudo -u postgres createuser -P -s <db_owner_name>
    Enter password for new role: <db_owner_password>
    Enter it again: <db_owner_password>
    admin:~$ sudo -u postgres psql template1
    template1=# CREATE DATABASE lrs OWNER <db_owner_name>;
    template1=# \q (exits shell)
    
    修改数据库参数
    /var/lib/pgsql/9.6/data/pg_hba.conf
    # "local" is for Unix domain socket connections only
    local   all             all                                     trust
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            trust
    # IPv6 local connections:
    host    all             all             ::1/128                 trust



**Install Prerequisites**

    admin:~$ sudo apt-get install git fabric python-setuptools python-dev\
        libxml2-dev libxslt1-dev gcc
    admin:~$ sudo easy_install pip
    admin:~$ sudo pip install virtualenv

**Clone the LRS repository**

    admin:~$ cd <wherever you want to put the LRS>
    admin:~$ git clone https://github.com/adlnet/ADL_LRS.git
    admin:~$ cd ADL_LRS/

**Set the LRS configuration**

  Create a `settings.ini` file and place it in the `adl_lrs` directory. Visit the [Settings](https://github.com/adlnet/ADL_LRS/wiki/Settings) wiki page to set it up.


**Setup the environment**

    admin:ADL_LRS$ fab setup_env
    admin:ADL_LRS$ source ../env/bin/activate
    (env)admin:ADL_LRS$


**Setup the LRS**

This creates the top level folders, <b>logs</b> and <b>media</b> at the same level as the project folder, <b>ADL_LRS</b>. Throughout the readme and the other install guides for celery and nginx you will most likely want to direct any log files to the logs directory. Inside of <b>logs</b> there are directorys for <b>celery</b>, <b>supervisord</b>, <b>uwsgi</b> and <b>nginx</b>.

    (env)admin:ADL_LRS$ fab setup_lrs
    ...
    You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blank to use '<system_user_name>'):
    E-mail address:
    Password: <this can be different than your system password since this will just be for the LRS site>
    Password (again):
    Superuser created successfully.
  ...

If you get some sort of authentication error here, make sure that Django and PostgreSQL are both
using the same form of authentication (*adl_lrs/settings.py* and *pg_hba.conf*) and that the credentials
given in *settings.py* are the same as those you created.

<b>IMPORTANT:</b> You <b>MUST</b> setup celery for retrieving the activity metadata from the ID as well as voiding statements that might have come in out of order. Visit the [Using Celery](https://github.com/adlnet/ADL_LRS/wiki/Using-Celery) wiki page for installation instructions.

## Starting

While still in the ADL_LRS directory, run

    (env)dbowner:ADL_LRS$ ./manage.py runserver

This starts a lightweight development web server on the local machine. By default, the server runs on port 8000 on the IP address 127.0.0.1. You can pass in an IP address and port number explicitly. This will serve your static files without setting up Nginx but must NOT be used for production purposes. Press `CTRL + C` to stop the server


Set your site domain

  Visit the admin section of your website (/admin). Click Sites and you'll see the only entry is 'example.com' (The key for this in the DB is 1 and it maps back to the SITE_ID value in settings). Change the domain and name to the domain you're going to use. If running locally it could be localhost:8000, or if production could be lrs.adlnet.gov (DON'T include the scheme here). Once again this does not change the domain it's running on...you want to set that up first then change this value to your domain name.

Whenever you want to exit the virtual environment, just type `deactivate`

For other ways to start and run the LRS, please visit our Wiki.

## Test LRS

    (env)dbowner:ADL_LRS$ fab test_lrs

## Helpful Information

* [Test Coverage](https://github.com/adlnet/ADL_LRS/wiki/Code-Coverage)
* [Code Profiling](https://github.com/adlnet/ADL_LRS/wiki/Code-Profiling-with-cProfile)
* [Setting up Nginx and uWSGI](https://github.com/adlnet/ADL_LRS/wiki/Using-uWSGI-with-Nginx)
* [OAuth Help](https://github.com/adlnet/ADL_LRS/wiki/Using-OAuth)
* [Clearing the Database](https://github.com/adlnet/ADL_LRS/wiki/Clearing-the-Database)

## Contributing to the project
We welcome contributions to this project. Fork this repository, make changes, and submit pull requests. If you're not comfortable with editing the code, please [submit an issue](https://github.com/adlnet/ADL_LRS/issues) and we'll be happy to address it.

## License
   Copyright &copy;2016 Advanced Distributed Learning

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
