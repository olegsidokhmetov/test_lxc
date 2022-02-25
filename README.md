# Deploy Jitsi

Playbook para desplegar a partir de una plantilla lxc varios servidores Jitsi.
El playbook se divide en 3 tipos de tareas diferentes

* **pre-jitsi** 
* **jitsi**
* **post-jitsi**

### Pre-jitsi
- Despliege de contenedores en distintos nodos LXD a partir de una plantilla con previamente securizada a nivel de usuarios.

Si desea instalar sólo contenedores `LXD` y la instalación keepalived con la configuración ejecute el rol usando playbook `ini.yaml` de la carpeta `/etc/ansible/playbooks`. 
```
---

 - hosts: devel-lxd01
   gather_facts: false
   vars_files:
   - /etc/ansible/roles/make_jitsi/lxd_qs/vars/main.yml
   - /etc/ansible/roles/make_jitsi/lxd_qs/defaults/main.yml
   
   roles:
     - role: "/etc/ansible/roles/make_jitsi/lxd_qs"
```

```
Paso:
1-Creating_container.yaml
```

- Configuración de red
```
Paso:
2-Send_netplan_config_to_containers.yaml
```
```
Si está utilizando un proxy, incluya esta tarea en su rol
3-Add_proxy_setiings_in_LXC_container.yaml
```

- Update y upgrade del SO
```
Paso:
4-Update_upgrade_OS.yaml
```

- Instalación de dependencias y software keepalived
```
Paso:
5-Install_dependencias_and_keepalived.yaml
```

- Configuración keepalived
```
6-Configuration_keepalived.yaml
```

