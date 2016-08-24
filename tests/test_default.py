from testinfra.utils.ansible_runner import AnsibleRunner
import pytest
import requests

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_zabbiserver_running_and_enabled(Service):
    zabbix = Service("zabbix-server")
    assert zabbix.is_enabled
    assert zabbix.is_running


@pytest.mark.parametrize("server, web", [
    ("zabbix-server-pgsql", "zabbix-web-pgsql"),
    ("zabbix-server-mysql", "zabbix-web-mysql"),
])
def test_zabbix_package(Package, TestinfraBackend, server, web, SystemInfo):
    host = TestinfraBackend.get_hostname()
    host = host.replace("-centos", "")
    host = host.replace("-debian", "")

    if host == server:
        zabbix_server = Package(server)
        zabbix_web = Package(web)
        assert zabbix_server.is_installed
        assert zabbix_web.is_installed

        if SystemInfo.distribution == 'debian':
            assert zabbix_server.version.startswith("1:3.0")
            assert zabbix_web.version.startswith("1:3.0")
        elif SystemInfo.distribution == 'centos':
            assert zabbix_server.version.startswith("3.0")
            assert zabbix_web.version.startswith("3.0")


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


def test_zabbix_web(File):
    zabbix_web = File("/etc/zabbix/web/zabbix.conf.php")
    assert zabbix_web.user == "zabbix"
    assert zabbix_web.group == "zabbix"
    assert zabbix_web.mode == 0o644


# def test_http_status():
#     zabbix = requests.get('http://zabbix.example.com')
#     zabbix_status_code = zabbix.status_code
#     assert zabbix_status_code == 200
#
#
# def test_http_api_login():
#     data_login = '{"params": {"password":"zabbix", "user":"Admin"}, "jsonrpc":"2.0", "method":"user.login", "id":0}'
#     headers = {'Content-Type': 'application/json-rpc'}
#     zabbix = requests.post('http://zabbix.example.com/api_jsonrpc.php', data=data_login, headers=headers, timeout=30)
#     zabbix_api_status = zabbix.status_code
#     zabbix_api_json = zabbix.json()
#     assert zabbix_api_status == 200
#     assert zabbix_api_json['id'] == 0
#
#     zabbix_api_token = zabbix_api_json['result']
#     data_search = '''{"jsonrpc": "2.0","method": "host.get","params":
#     {"output": "extend","filter": {"host": ["Zabbix server"]}},"auth":"''' + zabbix_api_token + '''","id": 1}'''
#     zabbix = requests.post('http://zabbix.example.com/api_jsonrpc.php', data=data_search, headers=headers, timeout=30)
#     zabbix_api_search_status = zabbix.status_code
#     zabbix_api_search_json = zabbix.json()
#     assert zabbix_api_search_status == 200
#     assert zabbix_api_search_json['result'][0]['host'] == 'Zabbix server'
