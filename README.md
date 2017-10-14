# Overview
[![Travis](https://travis-ci.org/hunt-genes/layer-slurm.svg?branch=master)](https://travis-ci.org/hunt-genes/layer-slurm) [![license](https://img.shields.io/github/license/hunt-genes/layer-slurm.svg)](./copyright)

This layer provides the base Slurm install for Slurm charms.

# Usage

To create a charm layer using this base layer, you need only include it in
a `layer.yaml` file:

```yaml
include: ['layer:slurm']
```

# Reactive States

This layer will set the following states:

* **`slurm.installed`** Slurm packages are installed.

* **`slurmd.stop`** Stops the `slurmd` service.

* **`slurmd.restart`** Restarts the `slurmd` service.

* **`slurmd.disable`** Disables the `slurmd` service.

* **`slurmctld.stop`** Stops the `slurmctld` service.

* **`slurmctld.restart`** Restarts the `slurmctld` service.

* **`slurmctld.disable`** Disables the `slurmctld` service.

* **`munge.restart`** Restarts the `munge` service.
