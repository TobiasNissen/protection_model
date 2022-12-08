from ..base.access_right import AccessRight
from ..utilities.serialization import serialize_8_bit_int, serialize_64_bit_int


class SeL4CPAccessRight(AccessRight):
    def serialize_type_id(self) -> bytes:
        return serialize_8_bit_int(self.type_id)
    
    
class SchedulingAccessRight(SeL4CPAccessRight):
    priority: int
    budget: int
    period: int
    
    def __init__(self, priority: int, budget: int, period: int):
        self.type_id = 0
        self.priority = priority
        self.budget = budget
        self.period = period
        
    def serialize_metadata(self) -> bytes:
        return serialize_8_bit_int(self.priority) + \
               serialize_64_bit_int(self.budget) + \
               serialize_64_bit_int(self.period)
    
    
class ChannelAccessRight(SeL4CPAccessRight):
    target_pd_id: int           # the id of the targeted PD.
    target_pd_channel_id: int   # the ID used by the targeted PD for the channel
    own_channel_id: int         # the ID used by the current PD for the channel.
    
    def __init__(self, target_pd_id: int, target_pd_channel_id: int, own_channel_id: int):
        self.type_id = 1
        self.target_pd_id = target_pd_id
        self.target_pd_channel_id = target_pd_channel_id
        self.own_channel_id = own_channel_id
        
    def serialize_metadata(self) -> bytes:
        return serialize_8_bit_int(self.target_pd_id) + \
               serialize_8_bit_int(self.target_pd_channel_id) + \
               serialize_8_bit_int(self.own_channel_id)


class MemoryRegionAccessRight(SeL4CPAccessRight):
    memory_region_page_cap_index: int
    vaddr: int
    size: int
    perms: int
    cached: bool
    
    def __init__(self, memory_region_page_cap_index: int, vaddr: int, size: int, perms: int, cached: bool):
        self.type_id = 2
        self.memory_region_page_cap_index = memory_region_page_cap_index
        self.vaddr = vaddr
        self.size = size
        self.perms = perms
        self.cached = cached
    
    def serialize_metadata(self) -> bytes:
        return serialize_64_bit_int(self.memory_region_page_cap_index) + \
               serialize_64_bit_int(self.vaddr) + \
               serialize_64_bit_int(self.size) + \
               serialize_8_bit_int(self.perms) + \
               serialize_8_bit_int(self.cached)


class IrqAccessRight(SeL4CPAccessRight):
    parent_irq_channel_id: int
    own_irq_channel_id: int
    
    def __init__(self, parent_irq_channel_id: int, own_irq_channel_id: int):
        self.type_id = 3
        self.parent_irq_channel_id = parent_irq_channel_id
        self.own_irq_channel_id = own_irq_channel_id
        
    def serialize_metadata(self) -> bytes:
        return serialize_8_bit_int(self.parent_irq_channel_id) + \
               serialize_8_bit_int(self.own_irq_channel_id)


