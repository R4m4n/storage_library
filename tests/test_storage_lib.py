from StorageLib import storage_lib


def test_insert():
    assert storage_lib.insert({'key': 'value'})


def test_insert_many():
    assert storage_lib.insert_many([{'key1': 'value1'},{'key2': 'value2'}])


def test_get_all():
    data = storage_lib.get()
    assert isinstance(data, list)

def test_get_all_with_limit():
    data = storage_lib.get(limit = 4)
    assert isinstance(data, list)

def test_get_with_filter():
    data = storage_lib.get({'key': 'value'})
    assert isinstance(data, list)

def test_get_one():
    data = storage_lib.get_one()
    assert isinstance(data, dict)

def test_get_one_with_filter():
    data = storage_lib.get_one({'key': 'value'})
    assert isinstance(data, dict)

def test_update():
    data = storage_lib.update({'key': 'value1'})
    assert data

def test_update_with_filter():
    data = storage_lib.update({'key': 'value1'}, {'key': 'value2'})
    assert data

def test_update_one():
    data = storage_lib.update_one({'key1': 'value1'})
    assert data

def test_update_one_with_filter():
    data = storage_lib.update_one({'key': 'value_t'}, {'key1': 'value2'})
    assert data


def test_delete():
    data = storage_lib.delete({'key': 'value1'})
    assert data

def test_delete_with_filter():
    data = storage_lib.delete({'key': 'value1'})
    assert data

def test_delete_one():
    data = storage_lib.delete_one({'key1': 'value1'})
    assert data

def test_delete_one_with_filter():
    data = storage_lib.delete_one({'key': 'value_t'})
    assert data