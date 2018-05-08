# bp_Container_Demo
Demonstration of Devops Flow - using vagrant/ansilbe 
1. create VM.
2. install docker
3. create linux alpine image within docker
4. install nginx with install of alpine image.


SUMMARY
--------
This code creates a local VM.  The VM is fitted with ubuntu as the os.  Docker is installed on the VM.  The docker image is linux alpine (a small variety).  Ansible is used within Vagrant to configure the VM with Docker.  Docker is instructed to create a new container based on the linux apline image.  When the alpine image is installed, nginx is also installed within the docker container.  When successful, the following website presents a static webpage: http://localhost:8888. 


PREREQS
--------
Vagrant 2.0.4
Ansible 2.5.2 
VirtualBox Version 5.2.10 r122088 (Qt5.6.3)
testinfra-1.12.0 /pytest version 3.5.1
  Note: i also installed the following: "pip install pytest requests" - to test the final webpage via pytest.
Ubuntu 14.04.5 LTS


INSTRUCTIONS
-------------
Make sure that the prereqs are installed (or available if needed)

Clone repository:
  $ git clone https://github.com/vidrir/bp_Container_Demo.git

Change directory to cloned repo:
  $ cd bp_Container_Demo
  
Start the machine:
  $ vagrant up
  
Visit resulting page: http://localhost:8888

Test the results using pytest: ./tester.sh


