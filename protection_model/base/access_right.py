from abc import ABC, abstractmethod

class AccessRight(ABC):
    """
        An abstract access right in a protection model.
        
        Each concrete subclass should have a unique type id.
    """
    type_id: int
    
    def serialize(self) -> bytes:
        """
            Serializes this access right.
        """
        return self.serialize_type_id() + self.serialize_metadata()
        
        
    @abstractmethod
    def serialize_type_id(self) -> bytes:
        """
            Serializes the type id of this access right.
            
            All access rights in a protection model must use
            the same number of bytes to represent the type id.
            
            Consider creating an abstract base class for the 
            protection model which implements this method and
            leaves the implementation of `serialize_metadata`
            to concrete subclasses.
        """
        pass
        
        
    @abstractmethod
    def serialize_metadata(self) -> bytes:
        """
            Serializes the metadata of this access right.
        """
        pass
    
    
