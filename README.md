Role Name
=========

This installs a traefik running on docker

Requirements
------------

Docker running on the host, publically accessible tcp/80 and tcp/443

Role Variables
--------------

reverseproxy_le_email: email address used for Letsencrypt registration
reverseproxy_default_vhost: required variable for now to indicate the default virtualhost.

Dependencies
------------

Example Playbook
----------------

    - hosts: traefik:&docker
      roles:
         - docker
         - traefik

License
-------

BSD

Author Information
------------------

Dieter Verhelst - dieter@werus.be
