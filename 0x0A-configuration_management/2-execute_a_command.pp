# kills a process named killmenow.
exec { 'Kill killmenow prcess':
  command => '/usr/bin/pkill killmenow'
}
