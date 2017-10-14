import os

from charmhelpers.core.host import mkdir
from charmhelpers.core.templating import render

SLURM_CONFIG_TEMPLATE = 'slurm.conf'
SLURM_CONFIG_PATH = '/etc/slurm-llnl/slurm.conf'

MUNGE_KEY_TEMPLATE = 'munge.key'
MUNGE_KEY_PATH = '/etc/munge/munge.key'


def render_slurm_config(config):
    render(source=SLURM_CONFIG_TEMPLATE,
           target=SLURM_CONFIG_PATH,
           context=config,
           owner=config.get('slurm_user'),
           group=config.get('slurm_user'),
           perms=0o644)


def render_munge_key(config):
    render(source=MUNGE_KEY_TEMPLATE,
           target=MUNGE_KEY_PATH,
           context=config,
           owner='munge',
           group='munge',
           perms=0o400)


def create_spool_dir(config):
    if not os.path.isdir(config.get('slurmd_spool_dir')):
        mkdir(path=config.get('slurmd_spool_dir'),
              owner=config.get('slurm_user'),
              group=config.get('slurm_user'),
              perms=0o750)


def create_state_save_location(config):
    if not os.path.isdir(config.get('state_save_location')):
        mkdir(path=config.get('state_save_location'),
              owner=config.get('slurm_user'),
              group=config.get('slurm_user'),
              perms=0o750)
