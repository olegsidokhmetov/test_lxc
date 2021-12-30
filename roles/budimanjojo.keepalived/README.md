Ansible Packages Role
=====================

Role to install and configure [keepalived](https://www.keepalived.org/).

Supported OS Families
---------------------

- Ubuntu (tested)
- Arch Linux (tested)
- Redhat (tested)
- Other Linux distributions should work just fine

Role Variables
--------------

Available variables are listed below, the default values are in [defaults/main.yml](./defaults/main.yml):
```
keepalived_package_name: name of keepalived package name, default to 'keepalived' (string)
keepalived_service_name: name of keepalived service name, default to 'keepalived' (string)

## Dict of keepalived global_defs section, value can be string, int, list, dict, bool
keepalived_global_defs_options: {}

## List of keepalived vrrp_script sections
keepalived_vrrp_scripts:
- name: name of vrrp_script (string)
  options: dict of options for the section, value can be string, int, list, dict, bool

## List of keepalived vrrp_instance sections
keepalived_vrrp_instances:
- name: name of vrrp_instance (string)
  options: dict of options for the section, value can be string, int, list, dict

## List of keepalived virtual_server sections
keepalived_virtual_servers:
- name: name of virtual_server (string)
  options: dict of options for the section, value can be string, int, list, dict

## List of keepalived real_server sections
keepalived_real_servers:
- name: name of real_server (string)
  options: dict of options for the section, value can be string, int, list, dict

## List of keepalived vrrp_sync_group sections
keepalived_vrrp_sync_groups:
- name: name of vrrp_sync_group (string)
  options: dict of options for the section, value can be string, int, list, dict

## List of keepalived vrrp_instance sections
keepalived_vrrp_instances:
- name: name of vrrp_instance (string)
  options: dict of options for the section, value can be string, int, list, dict
```

Dependencies
------------

None

Example Playbook
----------------

Here is an example playbook (taken from [keepalived sample file](https://github.com/acassen/keepalived/blob/master/doc/samples/keepalived.conf.vrrp)):
```
- hosts: all

  vars:
    keepalived_global_defs_options:
      notification_email:
      - acassen
      notification_email_from: "Alexandre.Cassen@firewall.loc"
      smtp_server: 192.168.200.1
      smtp_connect_timeout: 30
      router_id: LVS_DEVEL
    keepalived_vrrp_instances:
    - name: VI_1
      options:
        state: MASTER
	interface: eth0
	garp_master_delay: 10
	smtp_alert: true
	virtual_router_id: 51
	priority: 100
	advert_int: 1
	authentication:
	  auth_type: PASS
	  auth_pass: 1111
	virtual_ipaddress:
	- 192.168.200.16
	- 192.168.200.17
	- 192.168.200.18
	- 192.168.200.18 label eth0:1
     - name: VI_2
       options:
         interface: eth0
	 smtp_alert: true
	 virtual_router_id: 50
	 priority: 50
	 advert_int: 1
	 virtual_ipaddress:
	 - 192.168.200.13
	 - 192.168.200.14
	 - 192.168.200.15
      - name: VI_3
        options:
	  state: MASTER
	  interface: eth1
	  smtp_alert: ""
	  virtual_router_id: 52
	  priority: 100
	  advert_int: 1
	  authentication:
	    auth_type: PASS
	    auth_pass: 1111
	  virtual_ipaddress:
	  - 192.168.200.13
	  - 192.168.200.14
	  - 192.168.200.15
      - name: VI_4
        options:
	  interface: eth1
	  smtp_alert: true
	  virtual_router_id: 5
	  priority: 50
	  advert_int: 1
	  virtual_ipaddress:
	  - 192.168.201.16
	  - 192.168.201.17
	  - 192.168.201.18

  roles:
  - budimanjojo.keepalived
```

License
-------

MIT License
