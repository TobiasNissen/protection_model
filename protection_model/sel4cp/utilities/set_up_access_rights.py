import sys
from pathlib import Path

from .system_parser import parse_system
from .access_rights_parser import parse_access_rights
from .access_rights_prompter import get_access_rights
from ...utilities.elf_patcher import patch_elf

def set_up_access_rights():
    num_args = len(sys.argv)
    if num_args != 3 and num_args != 4:
        sys.exit(f"Usage: python3 set_up_access_rights.py <target_ELF_file> <system_configuration_file> [<ELF_access_rights_file>]")
    
    target_elf = Path(sys.argv[1])
    system_file = Path(sys.argv[2])
    
    system_description = parse_system(system_file)
   
    if num_args == 4: # read the access rights from the provided file.
        elf_access_rights_file = Path(sys.argv[3])
        access_rights = parse_access_rights(elf_access_rights_file, system_description)
    else: # get the access rights interactively from the user.
        access_rights = get_access_rights(system_description)
    
    patch_elf(target_elf, access_rights)

    
    
    
    
