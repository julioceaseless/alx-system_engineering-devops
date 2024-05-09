# Troubleshoot Apache 500 error

exec { 'wordpress-debug':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
