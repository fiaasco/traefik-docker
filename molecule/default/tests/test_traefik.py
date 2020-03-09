import os
import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_traefik_container(host):
    command = host.run("docker ps")
    assert "traefik" in command.stdout


@pytest.mark.parametrize('volume', ['traefik_logs', 'traefik_letsencrypt'])
def test_traefik_volumes(host, volume):
    command = host.run("docker volume ls")
    assert (volume) in command.stdout
