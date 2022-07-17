# Storage Library
### Latest version: 0.1.0

This library provides features to perform CRUD operations on local storage, or other kind of storages.

## Features

 - Insert single row data.
 - Insert multiple row data.
 - Query all data at once.
 - Query data with filters.
 - Update all records.
 - Update multiple records with filters.
 - Update first records with filters.
 - Delete multiple records with filters.
 - Delete single records with filters.

## Usage:

```
from StorageLib import storage_lib

# Insert data
storage_lib.insert({'key': 'value'})

# Insert multiple data
storage_lib.insert_many([{'key1': 'value1'},{'key2': 'value2'}])

# Query data
storage_lib.get()

# Query data with filter
storage_lib.get({'key': 'value'})
```

## Installation
For local usage
```
pip install -r requirements
```
## Run test
`python setup.py pytest`
