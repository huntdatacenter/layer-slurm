from charmhelpers.fetch import apt_install
from charmhelpers.fetch import get_upstream_version
from charmhelpers.core.hookenv import status_set
from charmhelpers.core.hookenv import application_version_set

from charms.reactive import when_not
from charms.reactive import set_state

# Packages
SLURM_PACKAGE = 'slurm-wlm'


@when_not('slurm.installed')
def install_slurm():
    status_set('maintenance', 'installing slurm packages')

    # Install packages
    packages = [SLURM_PACKAGE]
    apt_install(packages)

    # Set Slurm version
    application_version_set(
        get_upstream_version(SLURM_PACKAGE))

    set_state('slurm.installed')
