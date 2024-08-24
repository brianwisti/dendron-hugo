---
created: '2024-02-22 17:40:36'
date: 2014-08-06 00:00:00+00:00
description: ''
fname: pub.post.2014.08.connect-to-mongodb-on-a-vagrant-box-from-the-host
id: voeg1d76wxs24asxge3mk9x
redirects:
- /tools/2014/08/06_mongo-vagrant-connect.html
- /post/2014/mongo-vagrant-connect/
- /2014/08/06/connect-to-mongodb-on-a-vagrant-box-from-the-host/
slug: connect-to-mongodb-on-a-vagrant-box-from-the-host
tags:
- vagrant
- mongodb
- tools
title: Connect to Mongodb on a Vagrant Box from the Host
updated: '2024-08-07 18:40:54'
---

![Robomongo showing server status as JSON text](assets/img/2014/cover-2014-08-06.png)

[Trusty Mongo Mojo Box]({{< relref "/post/2014/08/trusty-mongo-mojo-box.md" >}}) ended with a reusable Vagrant box for MongoDB and [Perl]({{< relref "/card/perl.md" >}}) Mojolicious experiments. That project is okay as it is right now, but I would like to get at MongoDB from the host system.
<!--more-->

It is not painfully difficult, but it would be easy for me to forget. That is why I made a post out of it.

Adjust the Vagrantfile so that the MongoDB guest port is forwarded to a host port.

``` ruby
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Use Ubuntu 14.04 64 bit
  config.vm.box = "ubuntu/trusty64"

  # Install system requirements
  config.vm.provision "shell", path: "bootstrap/system.sh"
  
  # Configure guest services to be accessible on host
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  config.vm.network "forwarded_port", guest: 27017, host: 27017
end
```

Inside the box, comment out the `bind_ip` line from `/etc/mongod.conf`.

``` bash
# Listen to local interface only. Comment out to listen on all interfaces.
# bind_ip = 127.0.0.1
```

Restart the `mongod` service.

```bash
sudo service mongod restart
```

Connect to Mongo from the host using whatever interface you prefer. I have been enjoying [Robomongo](http://robomongo.org/).