## How to add a Host to windows Active Directory
```
yum install sssd realmd oddjob oddjob-mkhomedir adcli samba-common samba-common-tools krb5-workstation openldap-clients policycoreutils-python -y
realm discover jnrlabs.com
realm join --user=administrator@jnrlabs.com jnrlabs.com
```

```
root@minikube01 ~ # realm discover jnrlabs.com
jnrlabs.com
  type: kerberos
  realm-name: JNRLABS.COM
  domain-name: jnrlabs.com
  configured: no
  server-software: active-directory
  client-software: sssd
  required-package: oddjob
  required-package: oddjob-mkhomedir
  required-package: sssd
  required-package: adcli
  required-package: samba-common-tools
root@minikube01 ~ # realm join --user=administrator@jnrlabs.com jnrlabs.com
Password for administrator@jnrlabs.com:
root@minikube01 ~ #

root@minikube01 ~ # realm list
jnrlabs.com
  type: kerberos
  realm-name: JNRLABS.COM
  domain-name: jnrlabs.com
  configured: kerberos-member
  server-software: active-directory
  client-software: sssd
  required-package: oddjob
  required-package: oddjob-mkhomedir
  required-package: sssd
  required-package: adcli
  required-package: samba-common-tools
  login-formats: %U@jnrlabs.com
  login-policy: allow-realm-logins
```
