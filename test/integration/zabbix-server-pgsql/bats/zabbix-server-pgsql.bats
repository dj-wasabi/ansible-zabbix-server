#!/usr/bin/env bats

@test "Validate status code for login page, should be \"200\"" {
  run curl -s -o /dev/null -w "%{http_code}" http://zabbix.example.com/index.php
  [[ $output = "200" ]]
}

@test "Validate login page and search for \"Username\"" {
  run curl -s http://zabbix.example.com/index.php
  [[ $output =~ ">Username<" ]]
}

@test "Validate if we can login with default credentials via API" {
  run curl -s -X POST -H 'Content-Type: application/json-rpc' -d '{"params": {"password": "zabbix", "user": "Admin"}, "jsonrpc": "2.0", "method": "user.login", "id": 0}' http://zabbix.example.com/api_jsonrpc.php
  [[ $output =~ "result" ]]
}