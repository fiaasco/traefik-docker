[![Build Status](https://travis-ci.com/fiaasco/traefik-docker.svg?branch=master)](https://travis-ci.com/fiaasco/traefik-docker)

Role Name
=========

This installs a traefik running on docker

Requirements
------------

Docker running on the host, publically accessible tcp/80 and tcp/443

Role Variables
--------------

traefik_le_email: email address used for Letsencrypt registration
traefik_vhost: required variable for now to indicate the default virtualhost.

Dependencies
------------

Example Playbook
----------------

    - hosts: traefik:&docker
      roles:
         - fiaasco.docker
         - fiaasco.traefik-docker

License
-------

BSD

Author Information
------------------

Dieter Verhelst - dieter@werus.be
