# Increases maximum number of file descriptors
# to allow Nginx handle more concurrent connections.


# Uncomment the ULIMIT Value
exec { 'modify-nginx':
  command => 'sed -i "s/^#[[:space:]]*ULIMIT=\"-n [0-9]*\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

#restart Nginx

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
