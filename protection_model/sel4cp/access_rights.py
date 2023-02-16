from ..base.access_right import AccessRight
from ..utilities.serialization import serialize_8_bit_int, serialize_64_bit_int
from .constants import SCHEDULING_TYPE_ID, CHANNEL_TYPE_ID, MEMORY_REGION_TYPE_ID, IRQ_TYPE_ID


class SeL4CPAccessRight(AccessRight):
    def serialize_type_id(self) -> bytes:
        return serialize_8_bit_int(self.type_id)
    
    
class SchedulingAccessRight(SeL4CPAccessRight):
    def __init__(self, priority: int, mcp: int, budget: int, period: int):
        self.type_id = SCHEDULING_TYPE_ID
        self.priority = priority
        self.mcp = mcp
        self.budget = budget
        self.period = period
        
    def serialize_metadata(self) -> bytes:
        return serialize_8_bit_int(self.priority) + \
               serialize_8_bit_int(self.mcp) + \
               serialize_64_bit_int(self.budget) + \
               serialize_64_bit_int(self.period)
    
    
class ChannelAccessRight(SeL4CPAccessRight):    
    def __init__(self, target_pd_id: int, target_pd_channel_id: int, own_channel_id: int):
        self.type_id = CHANNEL_TYPE_ID
        self.target_pd_id = target_pd_id # the id of the targeted PD.
        self.target_pd_channel_id = target_pd_channel_id # the ID used by the targeted PD for the channel.
        self.own_channel_id = own_channel_id # the ID used by the current PD for the channel.
        
    def serialize_metadata(self) -> bytes:
        return serialize_8_bit_int(self.target_pd_id) + \
               serialize_8_bit_int(self.target_pd_channel_id) + \
               serialize_8_bit_int(self.own_channel_id)


class MemoryRegionAccessRight(SeL4CPAccessRight):
    def __init__(self, memory_region_page_cap_index: int, vaddr: int, size: int, perms: int, cached: bool):
        self.type_id = MEMORY_REGION_TYPE_ID
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
    def __init__(self, parent_irq_channel_id: int, own_irq_channel_id: int):
        self.type_id = IRQ_TYPE_ID
        self.parent_irq_channel_id = parent_irq_channel_id
        self.own_irq_channel_id = own_irq_channel_id
        
    def serialize_metadata(self) -> bytes:
        return serialize_8_bit_int(self.parent_irq_channel_id) + \
               serialize_8_bit_int(self.own_irq_channel_id)


