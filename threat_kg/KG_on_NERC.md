# Use NERC OpenStack for Knowledge Graph Work
This document is a brief guide for setting up the development environment for knowledge graph work on New England Research Cloud (NERC). Specifically, NERC OpenStack will be used to create virtual machines (VMs) with powerful GPUs, which are ideal for GPU-intensive work such as knowledge graph embedding. For example, we use NERC for our [threat knowledge graph](https://github.com/nislab/threat-knowledge-graph) research project.

See also [NREC's official documentation](https://nerc-project.github.io/nerc-docs/openstack/).



## Launch new VMs
First, make sure to [get resource allocation from NERC](https://nerc-project.github.io/nerc-docs/get-started/user-onboarding-on-NERC/) for your research project. 

Log into the [OpenStack Dashboard](https://stack.nerc.mghpcc.org/) (via OpenID Connect). An overview page of the project will show up.

To prepare for launching new VMs, [create a Key Pair](https://nerc-project.github.io/nerc-docs/openstack/access-and-security/create-a-key-pair/) to set up a public ssh key. An ssh key pair is required to log in. Key pairs can be uploaded to NERC OpenStack Dashboard, and can be found under "project / compute / key pairs". Next, add rules in the [Security Groups](https://nerc-project.github.io/nerc-docs/openstack/access-and-security/security-groups/#allowing-ssh) to allow ssh using Port 22 access to the instance. The added rules will show under "project / network / security groups".

Follow instructions on [this page](https://nerc-project.github.io/nerc-docs/openstack/create-and-connect-to-the-VM/launch-a-VM/) to launch new VMs. VMs can be created with different *flavors*, which define hardware configurations of vCPU, GPU, RAM, Disk, etc. See all available flavors [here](https://nerc-project.github.io/nerc-docs/openstack/create-and-connect-to-the-VM/flavors/).

Connect to created VMs via SSH following [this page](https://nerc-project.github.io/nerc-docs/openstack/create-and-connect-to-the-VM/ssh-to-the-VM/). Specifically, if all the steps above are followed, one thing left to do is to [assign a floating IP](https://nerc-project.github.io/nerc-docs/openstack/create-and-connect-to-the-VM/assign-a-floating-IP/) to the instances. Details of the created VMs can be found under "project / compute / instances".

Now, the VMs are ready to be accessed remotely. Start the VM on the OpenStack Dashboard under "project / compute / instances", then SSH into it, for example, if the VM use Ubuntu images and its assigned IP is 199.xx.xx.xx, it can be accessed by
    
    ssh ubuntu@199.xx.xx.xx

Once connected to the VM, you can set a password, add other SSH keys to the instance, and add other users to the instance. See guide [here](https://nerc-project.github.io/nerc-docs/openstack/create-and-connect-to-the-VM/ssh-to-the-VM/).

Note: the VMs are charged for running time. When not in use, the VMs can be shut off under "project / compute / instances / more actions / shut off instances" on the OpenStack Dashboard. See more pricing information [here](https://nerc-project.github.io/nerc-docs/get-started/cost-billing/how-pricing-works/).

## Configure VM environments

Next, configure the environments for knowledge graph work. For illustration, we assume TensorFlow v1.15 and [AmpliGraph v1.4.0](https://docs.ampligraph.org/en/1.4.0/index.html) (an open source Python library for knowledge graphs) are used. Other Python libraries for knowledge graphs include [PyKEEN](https://pykeen.readthedocs.io/en/stable/index.html), [DGL-KE](https://aws-dglke.readthedocs.io/en/latest/index.html), and so on.

The following parts assume using a VM equipped with Nvidia GPU. If using CPU-only VM, setting up environments is relatively straightforward, without need for CUDA related stuff.

Install CUDA driver. See driver installer section on [this page](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local). You should now be able to monitor GPU status with command `nvidia-smi`, see [its documentation](https://developer.download.nvidia.com/compute/DCGM/docs/nvidia-smi-367.38.pdf). 

[Install conda](https://docs.anaconda.com/free/anaconda/install/linux/) and [create a conda environment](https://docs.conda.io/projects/conda/en/4.6.0/user-guide/tasks/manage-environments.html) for your work. Then install compatible versions of CUDA Toolkit and cuDNN. For example, for TensorFlow v1.15, CUDA Toolkit v10.0 and cuDNN v7.3.1 should work:
```
conda create -n demo python=3.7
conda activate demo
conda install cudatoolkit=10.0
conda install cudnn=7.3.1
```

Install [Jupyter](https://jupyter.org/install), TensorFlow v1.15, and AmpliGraph v1.4.0:
```
pip install notebook
pip install tensorflow-gpu=1.15
pip install ampligraph==1.4.0
```
See also [AmpliGraph documentation on installation](https://docs.ampligraph.org/en/1.4.0/install.html).

Note: one additional step you might need to do for this version of tensorflow is downgrading protobuf using pip
```
pip install protobuf==3.20.*
```

Once all the steps above are completed, the VMs are ready for knowledge graph embedding, evaluation, prediction, etc. 
