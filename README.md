Table of Contents

1. [Overview](#overview)
2. [Upgrades](#upgrades)
   * [Release 1.0.0](#100)
3. [Requirements for this role](#requirements)
   * [List of Operating systems](#operating-systems)
   * [List supported Zabbix versions](#zabbix-version)
4. [Installing this role](#installation)
5. [Overview of variables which can be used](#role-variables)
   * [Main variables](#main-variables)
   * [Zabbix 3 variables](#zabbix-3)
   * [Database variables](#databases)
6. [Dependencies](#dependencies)
7. [Example of using this role](#example-playbook)
   * [ Vars in role configuration](#vars-in-role-configuration)
   * [Combination of group_vars and playbook](#combination-of-group_vars-and-playbook)
8. [Molecule](#molecule)
9. [Extra information](#extra-information)
10. [License](#license)
11. [Author Information](#author-information)

#Overview

Build Status:

[![Build Status](https://travis-ci.org/dj-wasabi/ansible-zabbix-server.svg?branch=master)](https://travis-ci.org/dj-wasabi/ansible-zabbix-server)

This is an role for installing and maintaining the zabbix-server.

This is one of the 'dj-wasabi' roles which configures your whole zabbix environment. See an list for the complete list:

 * zabbix-web (https://galaxy.ansible.com/dj-wasabi/zabbix-web/)
 * zabbix-server (https://galaxy.ansible.com/dj-wasabi/zabbix-server/)
 * zabbix-proxy (https://galaxy.ansible.com/dj-wasabi/zabbix-proxy/)
 * zabbix-javagateway (https://galaxy.ansible.com/dj-wasabi/zabbix-javagateway/)
 * zabbix-agent (https://galaxy.ansible.com/dj-wasabi/zabbix-agent/)

#Upgrades
##1.0.0

With this 1.0.0 release, the following is changed:

* This repository will only contain all the actions that are needed for correct configuring a Zabbix Server. All tasks regarding the frontend/webui of Zabbix has been transferred to the `dj-wasabi.zabbix-web` role.
* All properties starts with `zabbix_` now. Example, property named `server_dbuser` is now `zabbix_server_dbuser`.


# Requirements
## Operating systems

This role will work on the following operating systems:

 * Red Hat
 * Debian
 * Ubuntu

So, you'll need one of those operating systems.. :-)
Please sent Pull Requests or suggestions when you want to use this role for other Operating systems.

## Zabbix Versions

See the following list of supported Operating systems with the Zabbix releases.

### Zabbix 3.2

  * CentOS 7.x
  * Amazon 7.x
  * RedHat 7.x
  * OracleLinux 7.x
  * Scientific Linux 7.x
  * Ubuntu 14.04, 16.04
  * Debian 7, 8

### Zabbix 3.0

  * CentOS 5.x, 6.x, 7.x
  * Amazon 5.x, 6.x, 7.x
  * RedHat 5.x, 6.x, 7.x
  * OracleLinux 5.x, 6.x, 7.x
  * Scientific Linux 5.x, 6.x, 7.x
  * Ubuntu 14.04
  * Debian 7, 8

### Zabbix 2.4

  * CentOS 6.x, 7.x
  * Amazon 6.x, 7.x
  * RedHat 6.x, 7.x
  * OracleLinux 6.x, 7.x
  * Scientific Linux 6.x, 7.x
  * Ubuntu 12.04 14.04
  * Debian 7

### Zabbix 2.2

  * CentOS 5.x, 6.x
  * RedHat 5.x, 6.x
  * OracleLinux 5.x, 6.x
  * Scientific Linux 5.x, 6.x
  * Ubuntu 12.04
  * Debian 7
  * xenserver 6

#Installation

Installing this role is very simple: `ansible-galaxy install dj-wasabi.zabbix-server`

Please be aware that this role only installs the Zabbix Server and not the Zabbix Web. If you do want to have a Zabbix Web, please execute the following command: `ansible-galaxy install dj-wasabi.zabbix-web`  

#Role Variables

## Main variables

The following is an overview of all available configuration default for this role.

### Overall Zabbix

* `zabbix_version`: This is the version of zabbix. Default: 3.2. Can be overridden to 2.0, 2.4, 2.2 or 2.0.
* `zabbix_repo_yum`: A list with Yum repository configuration.
* `zabbix_repo`: Default: _zabbix_
  * _epel_ install agent from EPEL repo
  * _zabbix_ (default) install agent from Zabbix repo
  * _other_ install agent from pre-existing or other repo

### Zabbix Server

* `zabbix_server_name`: The name of the Zabbix Server.
* `zabbix_server_database`: The type of database used. Can be: mysql or pgsql
* `zabbix_server_database_long`: The type of database used, but long name. Can be: mysql or postgresql
* `zabbix_server_hostname`: The hostname on which the zabbix-server is running. Default set to: {{ inventory_hostname }}
* `zabbix_server_listenport`: On which port the Zabbix Server is available. Default: 10051
* `zabbix_server_dbhost`: The hostname on which the database is running.
* `zabbix_server_dbname`: The database name which is used by the Zabbix Server.
* `zabbix_server_dbuser`: The database username which is used by the Zabbix Server.
* `zabbix_server_dbpassword`: The database user password which is used by the Zabbix Server.
* `zabbix_server_dbport`: The database port which is used by the Zabbix Server.
* `zabbix_database_creation`: True / False. When you don't want to create the database including user, you can set it to False.
* `zabbix_database_sqlload`:True / False. When you don't want to load the sql files into the database, you can set it to False.
* `zabbix_server_dbencoding`: The encoding for the MySQL database. Default set to `utf8`
* `zabbix_server_dbcollation`: The collation for the MySQL database. Default set to `utf8_bin`
* `zabbix_server_tlscafile`: Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification.
* `zabbix_server_tlscrlfile`: Full pathname of a file containing revoked certificates.
* `zabbix_server_tlscertfile`: Full pathname of a file containing the agent certificate or certificate chain.
* `zabbix_server_tlskeyfile`: Full pathname of a file containing the agent private key.

## Database

There are some zabbix-server specific variables which will be used for the zabbix-server configuration file, these can be found in the defaults/main.yml file. There are 3 which needs some explanation:
```bash
  #database_type: mysql
  #database_type_long: mysql
  database_type: pgsql
  database_type_long: postgresql
  [...]
  server_dbport: 5432
```

There are 2 database_types which will be supported: mysql and postgresql. You'll need to comment or uncomment the database you would like to use and adjust the port number (`server_dbport`) accordingly (`5432` is the default postgresql port). In example from above, the postgresql database is used. If you want to use mysql, uncomment the 2 lines from mysql and comment the 2 lines for postgresql and change the database port to the mysql one (default mysql port is `3306`).

# Dependencies

This role has 1 "hardcoded" dependency: geerlingguy.apache. This is an role which support the 3 main operating systems (Red Hat/Debian/Ubuntu). I can't find an mysql or postgresql role which also supports these 3 operating systems.

```text
You'll need to find the correct database role by yourself. I only want to use roles which supports the 3 main operating systems as well and for now I can't find one. If there is an role which supports these 3 operating systems, please let me know and I'll use it as dependency.
```

# Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: zabbix-server
      become: yes
      roles:
         - { role: dj-wasabi.zabbix-server, database_type: mysql, database_type_long: mysql }


# Molecule

This roles is configured to be tested with Molecule. You can find on this page some more information regarding Molecule:

* http://werner-dijkerman.nl/2016/07/10/testing-ansible-roles-with-molecule-testinfra-and-docker/
* http://werner-dijkerman.nl/2016/07/27/extending-ansible-role-testing-with-molecule-by-adding-group_vars-dependencies-and-using-travis-ci/
* http://werner-dijkerman.nl/2016/07/31/testing-ansible-roles-in-a-cluster-setup-with-docker-and-molecule/

# Contributors

The following have contributed to this Ansible role (List of Fame):

  * drmikecrowe
  * srvg
  * kostyrevaa
  * clopnis
  * SAL-e
  * lhoss
  * mescanef

# License

GPLv3

# Author Information

This is my first attempt to create an ansible role, so please send suggestion or pull requests to make this role better.

Github: https://github.com/dj-wasabi/ansible-zabbix-server

mail: ikben [ at ] werner-dijkerman . nl
