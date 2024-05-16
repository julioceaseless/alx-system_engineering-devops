# Change OS config so that it is possible to login with the holberton
# user and open file without any error

exec {'replacement-1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replacement-2'],
}

exec {'replacement-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
