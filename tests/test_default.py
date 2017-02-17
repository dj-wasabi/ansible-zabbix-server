from testinfra.utils.ansible_runner import AnsibleRunner
import pytest

testinfra_hosts = AnsibleRunner('inventory').get_hosts('all')


def test_zabbiserver_running_and_enabled(Service, SystemInfo):
    if SystemInfo.distribution == 'centos':
        zabbix = Service("zabbix-server")
        assert zabbix.is_enabled
        assert zabbix.is_running


@pytest.mark.parametrize("server, redhat, debian", (
        ("zabbix-server-pgsql", "zabbix-web-pgsql", "zabbix-frontend-php"),
        ("zabbix-server-mysql", "zabbix-web-mysql", "zabbix-frontend-php"),
))
def test_zabbix_package(Package, TestinfraBackend, server, redhat, debian, SystemInfo):
    host = TestinfraBackend.get_hostname()
    host = host.replace("-centos", "")
    host = host.replace("-debian", "")
    host = host.replace("-ubuntu", "")

    if host == server:
        if SystemInfo.distribution in ['debian', 'ubuntu']:
            zabbix_server = Package(server)
            zabbix_web = Package(debian)
            assert zabbix_server.version.startswith("1:3.2")
            assert zabbix_web.version.startswith("1:3.2")
        elif SystemInfo.distribution == 'centos':
            zabbix_server = Package(server)
            zabbix_web = Package(redhat)
            assert zabbix_server.version.startswith("3.2")
            assert zabbix_web.version.startswith("3.2")

        assert zabbix_server.is_installed
        assert zabbix_web.is_installed


def test_socket(Socket):
    assert Socket("tcp://0.0.0.0:10051").is_listening


def test_zabbix_server_dot_conf(File):
    zabbix_server_conf = File("/etc/zabbix/zabbix_server.conf")
    assert zabbix_server_conf.user == "zabbix"
    assert zabbix_server_conf.group == "zabbix"
    assert zabbix_server_conf.mode == 0o644

    assert zabbix_server_conf.contains("ListenPort=10051")
    assert zabbix_server_conf.contains("DBHost=localhost")
    assert zabbix_server_conf.contains("DebugLevel=3")


def test_zabbix_include_dir(File):
    zabbix_include_dir = File("/etc/zabbix/zabbix_server.conf.d")
    assert zabbix_include_dir.is_directory
    assert zabbix_include_dir.user == "zabbix"
    assert zabbix_include_dir.group == "zabbix"
    # assert zabbix_include_dir.mode == 0o644


def test_zabbix_web(File, SystemInfo):
    zabbix_web = File("/etc/zabbix/web/zabbix.conf.php")

    if SystemInfo.distribution in ['debian', 'ubuntu']:
        assert zabbix_web.user == "www-data"
        assert zabbix_web.group == "www-data"
    elif SystemInfo.distribution == 'centos':
        assert zabbix_web.user == "apache"
        assert zabbix_web.group == "apache"
    assert zabbix_web.mode == 0o644
