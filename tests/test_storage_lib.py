""" Test all the create functions in StorageLib """

# Import module
from StorageLib import storage_lib

#-----------------------------------------------------------------------------
# Insert Tests
#-----------------------------------------------------------------------------

def test_insert():
    """
    Inserts passed record to the function in the storage source.
    A dict value is passed which will be stored in the storage source.
    """
    assert storage_lib.insert({'key': 'value'})

def test_insert_many():
    """
    Inserts passed multiple records to the function in the storage source.
    A list of dict value is passed which will be stored in the storage source.
    """
    assert storage_lib.insert_many([{'key1': 'value1'},{'key2': 'value2'}])

def test_get_all_with_limit():
    """
    Returns all the records in the storage source with a limit passed.
    limit will return certain number of records.
    """
    data = storage_lib.get(limit = 4)
    assert len(data) == 4

def test_get_with_filter():
    """
    Returns all the records in the storage source with a filter passed.
    filter expression will only fetch the records matching to the key value pair.
    """
    data = storage_lib.get({'key': 'value'})
    assert isinstance(data, list)


#-----------------------------------------------------------------------------
# Query tests
#-----------------------------------------------------------------------------

def test_get_all():
    """
    Returns all the records in the storage source.
    """
    data = storage_lib.get()
    assert isinstance(data, list)

def test_get_one():
    """
    Returns the first records in the storage source.
    filter expression will only fetch the records matching to the key value pair.
    """
    data = storage_lib.get_one()
    assert isinstance(data, dict)

def test_get_one_with_filter():
    """
    Returns the first records in the storage source with a filter passed.
    filter expression will only fetch the record matching to the key value pair.
    """
    data = storage_lib.get_one({'key': 'value'})
    assert isinstance(data, dict)


#-----------------------------------------------------------------------------
# Update tests
#-----------------------------------------------------------------------------

def test_update():
    """
    Updates all the records in the storage source with a filter passed.
    """
    data = storage_lib.update({'key': 'value1'})
    assert data

def test_update_with_filter():
    """
    Updates all records in the storage source matching the filter passed.
    """
    data = storage_lib.update({'key': 'value1'}, {'key': 'value2'})
    assert data

def test_update_one():
    """
    Updates the first record in the storage source.
    """
    data = storage_lib.update_one({'key1': 'value1'})
    assert data

def test_update_one_with_filter():
    """
    Updates the first record in the storage source matching the filter passed.
    """
    data = storage_lib.update_one({'key': 'value_t'}, {'key1': 'value2'})
    assert data


#-----------------------------------------------------------------------------
# Delete tests
#-----------------------------------------------------------------------------

def test_delete():
    """
    Deletes all the records in the storage source.
    """
    data = storage_lib.delete()
    assert data

def test_delete_with_filter():
    """
    Deletes all the records in the storage source matching the filter passed.
    """
    data = storage_lib.delete({'key': 'value1'})
    assert data

def test_delete_one():
    """
    Deletes the first record in the storage source.
    """
    data = storage_lib.delete_one({'key1': 'value1'})
    assert data

def test_delete_one_with_filter():
    """
    Deletes the first record in the storage source matching the filter passed.
    """
    data = storage_lib.delete_one({'key': 'value_t'})
    assert data