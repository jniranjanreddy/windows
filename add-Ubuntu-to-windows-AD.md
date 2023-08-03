## apt-get install realmd
### Source: https://ubuntu.com/server/docs/service-sssd-ad

```
apt install sssd-ad sssd-tools realmd adcli
```
```
root@nginx02:~# realm -v discover jnrit.com
 * Resolving: _ldap._tcp.jnrit.com
 * Performing LDAP DSE lookup on: 192.168.9.201
 * Successfully discovered: jnrit.com
jnrit.com
  type: kerberos
  realm-name: JNRIT.COM
  domain-name: jnrit.com
  configured: no
  server-software: active-directory
  client-software: sssd
  required-package: sssd-tools
  required-package: sssd
  required-package: libnss-sss
  required-package: libpam-sss
  required-package: adcli
  required-package: samba-common-bin
root@nginx02:~#

```
