# Installing flask from pip3
exec { 'Intall Flask with pip3':
  command => 'pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin'
}
