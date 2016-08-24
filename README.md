Table of Contents

1. [Overview](#overview)
2. [Requirements for this role](#requirements)
   * [List of Operating systems](#operating-systems)
   * [List supported Zabbix versions](#zabbix-version)
3. [Installing this role](#installation)
4. [Overview of variables which can be used](#role-variables)
   * [Main variables](#main-variables)
   * [Zabbix 3 variables](#zabbix-3)
   * [Database variables](#databases)
4. [Dependencies](#dependencies)
5. [Example of using this role](#example-playbook)
   * [ Vars in role configuration](#vars-in-role-configuration)
   * [Combination of group_vars and playbook](#combination-of-group_vars-and-playbook)
6. [Test Kitchen](#test-kitchen)
7. [Extra information](#extra-information)
8. [License](#license)
9. [Author Information](#author-information)

#Overview

Build Status:

[![Build Status](https://travis-ci.org/dj-wasabi/ansible-zabbix-server.svg?branch=master)](https://travis-ci.org/dj-wasabi/ansible-zabbix-server)

This is an role for installing and maintaining the zabbix-server. 

This is one of the 'dj-wasabi' roles which configures your whole zabbix environment. See an list for the complete list:

 * zabbix-server (https://galaxy.ansible.com/dj-wasabi/zabbix-server/)
 * zabbix-proxy (https://galaxy.ansible.com/dj-wasabi/zabbix-proxy/)
 * zabbix-javagateway (https://galaxy.ansible.com/dj-wasabi/zabbix-javagateway/)
 * zabbix-agent (https://galaxy.ansible.com/dj-wasabi/zabbix-agent/)

#Requirements
##Operating systems

This role will work on the following operating systems:

 * Red Hat
 * Debian
 * Ubuntu

So, you'll need one of those operating systems.. :-)
Please sent Pull Requests or suggestions when you want to use this role for other Operating systems.

##Zabbix Versions

See the following list of supported Operating systems with the Zabbix releases:

Zabbix 3.0:

  * CentOS 5.x, 6.x, 7.x
  * Amazon 5.x, 6.x, 7.x
  * RedHat 5.x, 6.x, 7.x
  * OracleLinux 5.x, 6.x, 7.x
  * Scientific Linux 5.x, 6.x, 7.x
  * Ubuntu 14.04
  * Debian 7, 8

Zabbix 2.4:

  * CentOS 6.x, 7.x
  * Amazon 6.x, 7.x
  * RedHat 6.x, 7.x
  * OracleLinux 6.x, 7.x
  * Scientific Linux 6.x, 7.x
  * Ubuntu 12.04 14.04
  * Debian 7

Zabbix 2.2:

  * CentOS 5.x, 6.x
  * RedHat 5.x, 6.x
  * OracleLinux 5.x, 6.x
  * Scientific Linux 5.x, 6.x
  * Ubuntu 12.04
  * Debian 7
  * xenserver 6

#Installation

Installing this role is very simple: `ansible-galaxy install dj-wasabi.zabbix-server`

#Role Variables

## Main variables
There are some variables in de default/main.yml which can (Or needs to) be changed/overriden:

* `zabbix_url`: This is the url on which the zabbix web interface is available. Default is zabbix.example.com, you should override it. For example, see "Example Playbook"

* `zabbix_version`: This is the version of zabbix. Default it is 3.0, but can be overriden to 2.4, 2.2 or 2.0.

* `zabbix_timezone`: This is the timezone. The apache vhost needs this parameter. Default: Europe/Amsterdam

* `zabbix_repo`: Default: _zabbix_
  * _epel_ install agent from EPEL repo
  * _zabbix_ (default) install agent from Zabbix repo
  * _other_ install agent from pre-existing or other repo

* `zabbix_vhost`: True / False. When you don't want to create an apache vhosts, you can set it to False.

* `zabbix_web`: True / False. When you down't want to install the zabbix-web component. Setting this to False, this playbook will only install the zabbix-server incl. database (if the 2 parameters below are set to True).

* `zabbix_database_creation`: True / False. When you don't want to create the database including user, you can set it to False.

* `zabbix_database_sqlload`:True / False. When you don't want to load the sql files into the database, you can set it to False.

* `server_dbencoding`: The encoding for the MySQL database. Default set to `utf8`

* `server_dbcollation`: The collation for the MySQL database. Default set to `utf8_bin` 

## Zabbix 3

These variables are specific for Zabbix 3.0

* `server_tlscafile`: Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification.

* `server_tlscrlfile`: Full pathname of a file containing revoked certificates.

* `server_tlscertfile`: Full pathname of a file containing the agent certificate or certificate chain.

* `server_tlskeyfile`: Full pathname of a file containing the agent private key.

## Database

There are some zabbix-server specific variables which will be used for the zabbix-server configuration file, these can be found in the defaults/main.yml file. There are 2 which needs some explanation:
```bash
  #database_type: mysql
  #database_type_long: mysql
  database_type: pgsql
  database_type_long: postgresql
```

There are 2 database_types which will be supported: mysql and postgresql. You'll need to comment or uncomment the database you would like to use. In example from above, the postgresql database is used. If you want to use mysql, uncomment the 2 lines from mysql and comment the 2 lines for postgresql.

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
         - { role: geerlingguy.apache }
         - { role: dj-wasabi.zabbix-server, zabbix_url: zabbix.dj-wasabi.nl, database_type: mysql, database_type_long: mysql }


# Test Kitchen

This roles is configured to be tested with Test Kitchen. You can find on this page some more information regarding Test Kitchen: http://werner-dijkerman.nl/2015/08/20/using-test-kitchen-with-docker-and-serverspec-to-test-ansible-roles/

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
