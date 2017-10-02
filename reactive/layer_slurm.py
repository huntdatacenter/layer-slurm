from charms.reactive import when
from charms.reactive import when_not
from charms.reactive import set_state
from charms.reactive import remove_state

from charmhelpers import fetch
from charmhelpers.core import hookenv
from charmhelpers.core import host

SLURM_PACKAGE = 'slurm-wlm'
SLURMD_SERVICE = 'slurmd'
SLURMCTLD_SERVICE = 'slurmctld'
MUNGE_SERVICE = 'munge'


@when_not('slurm.installed')
def install_slurm():
    hookenv.status_set('maintenance', 'installing slurm packages')
    packages = [SLURM_PACKAGE]
    fetch.apt_install(packages)
    # Set Slurm version
    hookenv.application_version_set(
        fetch.get_upstream_version(SLURM_PACKAGE))
    set_state('slurm.installed')


@when('slurmd.stop')
def stop_slurmd():
    host.service_stop(SLURMD_SERVICE)
    remove_state('slurmd.stop')


@when('slurmd.restart')
def restart_slurmd():
    host.service_restart(SLURMD_SERVICE)
    remove_state('slurmd.restart')


@when('slurmd.disable')
def disable_slurmd():
    host.service_pause(SLURMD_SERVICE)
    remove_state('slurmd.disable')


@when('slurmctld.stop')
def stop_slurmctld():
    host.service_stop(SLURMCTLD_SERVICE)
    remove_state('slurmctld.stop')


@when('slurmctld.restart')
def restart_slurmctld():
    host.service_restart(SLURMCTLD_SERVICE)
    remove_state('slurmctld.restart')


@when('slurmctld.disable')
def disable_slurmctld():
    host.service_pause(SLURMCTLD_SERVICE)
    remove_state('slurmctld.disable')


@when('munge.restart')
def restart_munge():
    host.service_restart(MUNGE_SERVICE)
    remove_state('munge.restart')
