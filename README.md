dj-wasabi.zabbix-server
=========

This is an role for installing and maintaining the zabbix-server. 

This is one of the 'dj-wasabi' roles which configures your whole zabbix environment. See an list for the complete list:

 * zabbix-server (https://galaxy.ansible.com/list#/roles/2070)
 * zabbix-proxy (https://galaxy.ansible.com/list#/roles/2073)
 * zabbix-javagateway (https://galaxy.ansible.com/list#/roles/2076)
 * zabbix-agent (https://galaxy.ansible.com/list#/roles/2079)

Requirements
------------

This role will work on:
* Red Hat
* Debian
* Ubuntu

So, you'll need one of those operating systems.. :-)

Role Variables
--------------

There are some variables in de default/main.yml which can (Or needs to) be changed/overriden:

* `zabbix_url`: This is the url on which the zabbix web interface is available. Default is zabbix.example.com, you should override it. For example, see "Example Playbook"

* `zabbix_version`: This is the version of zabbix. Default it is 2.4, but can be overriden to 2.2 or 2.0.

* `zabbix_timezone`: This is the timezone. The apache vhost needs this parameter. Default: Europe/Amsterdam

* `zabbix_repo`: True / False. When you already have an repository with the zabbix components, you can set it to False.

* `zabbix_vhost`: True / False. When you don't want to create an apache vhosts, you can set it to False.

* `zabbix_web`: True / False. When you down't want to install the zabbix-web component. Setting this to False, this playbook will only install the zabbix-server incl. database (if the 2 parameters below are set to True).

* `zabbix_database_creation`: True / False. When you don't want to create the database including user, you can set it to False.

* `zabbix_database_sqlload`:True / False. When you don't want to load the sql files into the database, you can set it to False.

There are some zabbix-server specific variables which will be used for the zabbix-server configuration file, these can be found in the defaults/main.yml file. There are 2 which needs some explanation:
```bash
  #database_type: mysql
  #database_type_long: mysql
  database_type: pgsql
  database_type_long: postgresql
```

There are 2 database_types which will be supported: mysql and postgresql. You'll need to comment or uncomment the database you would like to use. In example from above, the postgresql database is used. If you want to use mysql, uncomment the 2 lines from mysql and comment the 2 lines for postgresql.

Dependencies
------------

This role has 1 "hardcoded" dependency: geerlingguy.apache. This is an role which support the 3 main operating systems (Red Hat/Debian/Ubuntu). I can't find an mysql or postgresql role which also supports these 3 operating systems.

```text
You'll need to find the correct database role by yourself. I only want to use roles which supports the 3 main operating systems as well and for now I can't find one. If there is an role which supports these 3 operating systems, please let me know and I'll use it as dependency.
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: zabbix-server
      sudo: yes
      roles:
         - { role: geerlingguy.apache }
         - { role: dj-wasabi.zabbix-server, zabbix_url: zabbix.dj-wasabi.nlm database_type: mysql, database_type_long: mysql }

License
-------

GPLv3

Author Information
------------------

This is my first attempt to create an ansible role, so please send suggestion or pull requests to make this role better. 

Github: https://github.com/dj-wasabi/ansible-zabbix-server

mail: ikben [ at ] werner-dijkerman . nl
