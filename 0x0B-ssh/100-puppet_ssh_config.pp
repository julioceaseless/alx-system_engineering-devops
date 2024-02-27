#Set up client SSH config file with Puppet

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "\
    IdentityFile ~/.ssh/school\n\
    PasswordAuthentication no\n",
}
