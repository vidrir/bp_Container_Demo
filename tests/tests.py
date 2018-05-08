import requests

def test_docker_installed_and_running(host):
    docker = host.service("docker")
    assert docker.is_running
    assert docker.is_enabled

def test_nginx_processes_running(host):
    assert int(host.check_output("docker exec nginx_alpine ps aux | grep -c .*nginx:.*process")) == 2 

def test_web_page():    
    response = requests.get("http://localhost:8888")
    assert response.status_code == 200
    assert "I can get the job done!" in response.content

def test_vm_ipaddress(host):
    assert host.check_output("ifconfig | grep -c 'inet addr:192.168.33.10'") == "1"

def test_nginx_site_is_available_on_docker_host(host):
    assert host.socket("tcp://0.0.0.0:8888").is_listening

def test_docker_is_running_alpine_linux(host):
    assert host.check_output("docker exec nginx_alpine cat /etc/alpine-release") == "3.7.0"

def test_nginx_is_running_in_container(host):
    assert host.check_output("docker exec nginx_alpine pgrep '/usr/sbin/nginx'") == "1"

