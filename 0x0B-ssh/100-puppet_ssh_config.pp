# Configuration of SSH client config file
file { 'config file':
  ensure  => 'present',
  path    => '/root/alx-system_engineering-devops/0x0B-ssh/config',
  content => 'Host 333419-web-01
		HostName 34.203.75.238
		PasswordAuthentication no
		IdentityFile ~/.ssh/school',
}
