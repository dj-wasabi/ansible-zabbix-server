#ansible-zabbix-server Release

Below an overview of all changes in the releases.

Version (Release date)

0.6.0   (2016-08-24)

  * Removed Test Kitchen tests, added molecule tests
  * Added collation and encoding for MySQL databases #23
  * Add SELinux specifics #19 (By pull request: mescanef (Thanks!))
  * Fixes in the README.md file #18 (By pull request: mescanef (Thanks!))
  * Fix for: zabbix_repo - inconsistent use between server and agent roles. #17
  * Fix for: apache 2.2. and 2.4 #15

0.5.1   (2016-04-03)

  * Fix for: zabbix_server.conf file mode #14
  * Fix for: Support for v3+ Server Configuration #13

0.5.0   (2016-03-28)

  * Zabbix 3.0
  * MySQL database creation on other host (delegation)

0.4.0   (2016-02-05)

  * fix #2: server_dbhost allows for remote database but role does not fully support setting up on remote db #11 (By pull request: lhoss (Thanks!))
  * Added basic travis test
  * Fixed installation on Debian / Ubuntu for installing mysqldb-python package.

0.3.0   (2015-11-24)

  * Add test-kitchen #7 (By pull request: kostyrevaa (Thanks!))
  * Force apt cache update after installing Zabbix's gpg key #8 (By pull request: SAL-e (Thanks!))
  * tasks/mysql.yml - [add] install mysql client on RHEL base 7 #9 (By pull request: clopnis (Thanks!))
  * Updated test-kitchen tests
  * Added BATS tests
  * Added CHANGELOG.md file

0.2.1   (2015-06-30)

  * Fix unzip schema files for RedHat #5 (By pull request: kostyrevaa (Thanks!))
  * Fix missed required space #6 (By pull request: kostyrevaa (Thanks!))

0.2.0   (2015-03-20)

  * Various fixes #3 (By pull request: srvg (Thanks!))
  * Add optional configuration for Apache virtualhost aliases #4 (By pull request: srvg (Thanks!))

0.1.0   (2015-02-01)

  * Two minor changes for installation #1 (By pull request: drmikecrowe (Thanks!))

0.0.1   (2014-10-31)

  * Initial creation