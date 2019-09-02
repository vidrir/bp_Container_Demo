VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  #config.vm.box = "ubuntu/trusty64"
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "forwarded_port", guest: 8888, host: 8888
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provision "file", source: "./container", destination: "/tmp"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end 
