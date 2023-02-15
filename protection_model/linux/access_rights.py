from ..base.access_right import AccessRight
from ..utilities.serialization import serialize_16_bit_int


class LinuxAccessRight(AccessRight):
    def serialize_type_id(self) -> bytes:
        return serialize_16_bit_int(self.type_id)
        
    def serialize_metadata(self) -> bytes | None:
        return None
        
    def __init__(self, syscall_number: int):
        if syscall_number < 0 or syscall_number > 450:
            raise ValueError(f"The system call number must be in " \
                              "the range [0, 450], " \ 
                              "got: {syscall_number}")
        self.type_id = syscall_number
        

