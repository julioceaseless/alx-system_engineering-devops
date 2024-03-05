# Update package information
exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
  path    => ['/usr/bin', '/bin'],
}

# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Create a basic HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Add the custom HTTP header to nginx
file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

# Ensure Nginx is running
service { 'nginx':
  ensure => running,
}
