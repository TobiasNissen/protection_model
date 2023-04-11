# Overview
This repository serves as the base for the protection models of different operating systems.
Furthermore, utilities for patching ELF files with access rights are provided.

The function `patch_elf` in the `protection_model/utilities
/elf_patcher.py` file can be used to patch an ELF file with an access right table, given a list of access rights and a target ELF file.

A protection model is provided for both Linux and the seL4 Core Platform (seL4CP) in the directories `protection_model/linux` and `protection_model/sel4cp`, respectively. For each of these operating systems, a utility script is included and exposed by this library, which allows ELF files to patched for each of these operating systems. These utility scripts are installed as `linux_set_up_access_rights` and `sel4cp_set_up_access_rights`, respectively, and they use the `patch_elf` function internally.

# Build
To build this repository as a Python package, run the command: 
```
python3 -m flit build --format wheel
```
This outputs the file `dist/protection_model-1.0.0-py2.py3-none-any.whl`.

To install this module from the generated wheel file, run:
```
pip3 install dist/protection_model-1.0.0-py2.py3-none-any.whl
```
If you have already installed this module, run:
```
pip3 install --force-reinstall dist/protection_model-1.0.0-py2.py3-none-any.whl
```
instead to force reinstallation.

Note that the installed module contains scripts, which might be added to a directory that is not included in the `PATH` environment variable. If the scripts are e.g. added to the directory `/home/ttn/.local/bin` and this directory is not in the `PATH` environment variable, the script can be made available by updating the `PATH` with: `export PATH=/home/ttn/.local/bin:$PATH`.


NB: The `build` tool can be installed on Ubuntu by running the command: `pip3 install --upgrade build`.
