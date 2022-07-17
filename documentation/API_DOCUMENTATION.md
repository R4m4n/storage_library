# Storage Library Documentation

Everything you need to know about StorageLib.

## Behold, the power of StorageLib
```
>>> from StorageLib import storage_lib
>>> storage_lib.insert({'key': 'value'})
True
>>> storage_lib.insert_many([{'key1': 'value1'},{'key2': 'value2'}])
True
>>> storage_lib.get()
[{'key': 'value'}, {'key1': 'value1'}, {'key2': 'value2'}]
>>> storage_lib.get(limit = 2)
[{'key': 'value'}, {'key1': 'value1'}]
>>> storage_lib.get({'key': 'value'})
[{'key': 'value'}]
```

## Beloved Features:
 - Insert single row data.
 - Insert multiple row data.
 - Query all data at once.
 - Query data with filters.
 - Update all records.
 - Update multiple records with filters.
 - Update first records with filters.
 - Delete multiple records with filters.
 - Delete single records with filters.
 - Can use offset and limit in get().

StorageLib supports python3.7+

## User guide

### Installation of StorageLib
StorageLib works on local installation for now and can be done using pip:

`git clone https://github.com/R4m4n/storage_library.git`

Once the source code is cloned and copied then

```
python3 -m venv venv
pip instal -r requirements.txt
```

Now let's get started with some simple examples.

Begin by importing the storage_lib module:

```
>>> from StorageLib import storage_lib
```

Now let's try to import some record.

### Insert single record

**insert(*data_json*)**

Inserts passed record to the function in the storage source. THe argument is supposed to be a dict.
```
>>> storage_lib.insert({'key': 'value'})
True
```

### Insert multiple records
**insert_many(*data_json*)**

Inserts all the records passed to the function in the storage source. The passed argument is required to be a list of dicts.
```
>>> storage_lib.insert_many([{'key1': 'value1'},{'key2': 'value2'}])
True
```

### Query records
**get(*filter_exp = None, offset = 0, limit = None*)**

Fetch and returns all the records from the storage source. The filter_exp argument is required to be dicts.
```
>>> storage_lib.get()
[{'key': 'value'}, {'key1': 'value1'}, {'key2': 'value2'}]
```
*filter_exp* can be used to get the filtered records.
To get the particular number of records and use get with pagination *offset* and *limit* can be used. *offset* will start the records from that index and *limit* will only send the records to that length after the index passed in *offset*.
```
>>> storage_lib.get(limit = 2)
[{'key': 'value'}, {'key1': 'value1'}]
>>> storage_lib.get({'key': 'value'})
[{'key': 'value'}]
```

### Query and get first record
**get_one(*filter_exp = None*)**

Fetch and returns first the record from the storage source. The filter_exp argument is required to be dicts.
```
>>> storage_lib.get_one()
{'key': 'value'}
```
Can also be used to filter out the record.
```
>>> storage_lib.get_one({'key1': 'value1'})
{'key1': 'value1'}
```

### Update records
**update(*update_exp = {}, filter_exp = None*)**

Updates the records from the storage source matching filter passed to filter_exp. The filter_exp and update_exp arguments is required to be dicts.

*update_exp* is the key value pair which is needed to be changed in the record.
```
>>> storage_lib.update({'key': 'value1'})
True
>>> storage_lib.update({'key': 'value1'}, {'key': 'value2'})
True
```
*update_one* can be used to update first record found in the storage source.
```
>>> storage_lib.update_one({'key1': 'value1'})
True
>>> storage_lib.update_one({'key': 'value_t'}, {'key1': 'value2'})
True
```


### Delete records
**delete(*update_exp = {}, filter_exp = None*)**

Deletes the records from the storage source matching filter passed to filter_exp. The filter_exp and update_exp arguments is required to be dicts.

*update_exp* is the key value pair which is needed to be deleted from the record.
```
>>> storage_lib.delete()
True
>>> storage_lib.delete({'key': 'value1'})
True
```
*update_one* can be used to update first record found in the storage source.
```
>>> storage_lib.delete_one({'key1': 'value1'})
True
>>> storage_lib.delete_one({'key': 'value_t'})
True
```
