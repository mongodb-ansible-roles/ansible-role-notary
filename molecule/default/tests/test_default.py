import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nodejs(host):
    cmd = host.run("/usr/local/bin/notary-client.py -h")
    assert cmd.rc == 0

    assert host.file("/usr/local/bin/notary-client.py").exists
