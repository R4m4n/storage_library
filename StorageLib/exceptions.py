# Exception module:
# Containing the custom exceptions to be raised is case of some error
# Or when certain condition is not matched.

class StorageLibError(Exception):
    """
    Base class for all exceptions
    """
    pass

class InvalidDictError(StorageLibError):
    """
    Raised when the passed data is supposed to be strictly dict 
    and does not match the dict instance.

    Subclass of StorageLibError
    """
    pass

class InvalidListError(StorageLibError):
    """
    Raised when the passed data is supposed to be strictly list 
    and does not match the list instance.

    Subclass of StorageLibError
    """
    pass