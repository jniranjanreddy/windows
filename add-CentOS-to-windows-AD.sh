## How to add a Host to windows Active Directory
yum install sssd realmd oddjob oddjob-mkhomedir adcli samba-common samba-common-tools krb5-workstation openldap-clients policycoreutils-python -y
realm discover jnrlabs.com
realm join --user=administrator@jnrlabs.com jnrlabs.com
