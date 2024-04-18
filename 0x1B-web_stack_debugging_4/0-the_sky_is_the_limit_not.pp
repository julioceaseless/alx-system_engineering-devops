# Increases maximum number of file descriptors
# to allow Nginx handle more concurrent connections.


# delete existing ULIMIT and add another line
exec { 'modify-nginx':
  command => 'sed -i "/^#*[[:space:]]*ULIMIT=/d; $aULIMIT=\"-n 4096\"" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

#restart Nginx

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
