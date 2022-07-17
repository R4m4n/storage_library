class StorageLibError(Exception):
    """
    Base class for all exceptions
    """
    pass

class InvalidDictError(StorageLibError):
    pass

class InvalidListError(StorageLibError):
    pass