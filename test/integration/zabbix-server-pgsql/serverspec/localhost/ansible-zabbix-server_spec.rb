require 'serverspec'
require 'spec_helper'

describe 'Zabbix Server Packages' do
    describe package('zabbix-server-pgsql') do
        it { should be_installed }
    end
    describe package('zabbix-web-pgsql'), :if => os[:family] == 'redhat' do
        it { should be_installed }
    end
    describe package('zabbix-server') do
        it { should be_installed }
    end
    describe package('zabbix-web'), :if => os[:family] == 'redhat' do
        it { should be_installed }
    end
    describe package('zabbix-frontend-php') , :if => os[:family] == 'debian' do
        it { should be_installed }
    end
end

describe 'Zabbix Server Services' do
    describe service('zabbix-server') do
        it { should be_enabled }
        it { should be_running }
    end

    describe port(10051) do
        it { should be_listening }
    end
end

describe 'Zabbix Server Configuration' do
    describe file('/etc/zabbix/zabbix_server.conf') do
        it { should be_file}
        it { should be_owned_by 'zabbix'}
        it { should be_grouped_into 'zabbix'}

        it { should contain "ListenPort=10051" }
        it { should contain "DBHost=localhost" }
        it { should contain "DBName=zabbix-server" }
        it { should contain "DBUser=zabbix-server" }
        it { should contain "DBPassword=zabbix-server" }
    end
end

describe 'Zabbix Server Web Configuration' do
    describe file('/etc/zabbix/web/zabbix.conf.php') do
        it { should be_file}
        it { should be_owned_by 'zabbix'}
        it { should be_grouped_into 'zabbix'}

        it { should contain "$DB['TYPE']     = 'POSTGRESQL';" }
        it { should contain "$DB['SERVER']   = 'localhost';" }
        it { should contain "$DB['DATABASE'] = 'zabbix-server';" }
        it { should contain "$DB['USER']     = 'zabbix-server';" }
        it { should contain "$DB['PASSWORD'] = 'zabbix-server';" }

        it { should contain "$ZBX_SERVER      = 'localhost';" }
        it { should contain "$ZBX_SERVER_PORT = '10051';" }
        it { should contain "$ZBX_SERVER_NAME = 'localhost';" }
    end

end

describe 'Zabbix Server dependencies' do
    describe package('httpd'), :if => os[:family] == 'redhat' do
        it { should be_installed }
    end

    describe package('apache2'), :if => os[:family] == 'debian' do
        it { should be_installed }
    end
end
