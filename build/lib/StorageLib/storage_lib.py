import json
from .exceptions import InvalidDictError, InvalidListError
from .help import update_data, filtered_data
from .data_access import DataAccess


# Insert
def insert(data):
    if not isinstance(data, dict):
        raise(InvalidDictError('Invalid value, dict is required.'))
    file_data = DataAccess.read()
    file_data.append(data)
    DataAccess.write(file_data)
    return True



def insert_many(data):
    if not isinstance(data, list):
        raise(InvalidListError('Invalid value, list is required.'))
    file_data = DataAccess.read()
    file_data = file_data + data
    DataAccess.write(file_data)
    return True



# Query
def get(filter_exp = None, offset = 0, limit = None):
    file_data = DataAccess.read()
    file_data = file_data[offset: limit] if limit else file_data
    return_data = file_data
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.'))
        # filter(lambda d: d['a'] == 'b', data)
        filtered_data = [data for data in file_data if list(filter_exp.keys())[0] in data and data[list(filter_exp.keys())[0]] == list(filter_exp.values())[0]]
        return_data = filtered_data
    print ('\n\n return_data get =>>> ', return_data)
    return return_data


def get_one(filter_exp = None):
    file_data = DataAccess.read()
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.'))
        try:
            filtered_data = next(filter(lambda d: list(filter_exp.keys())[0] in d and d[list(filter_exp.keys())[0]] == list(filter_exp.values())[0], file_data))
        except:
            filtered_data = {}
        return_data = filtered_data
    else:
        return_data = file_data[0]

    print ('\n\n return_data =>> ', return_data)
    return return_data



# Update
def update(update_exp = {}, filter_exp = None):
    file_data = DataAccess.read()
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.'))
    for data in file_data:
        if filtered_data(data, filter_exp):
            update_data(data, update_exp)
    DataAccess.write(file_data)
    return True

def update_one(update_exp = {}, filter_exp = None):
    file_data = DataAccess.read()
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.'))
    for data in file_data:
        if filtered_data(data, filter_exp):
            update_data(data, update_exp)
            break
    DataAccess.write(file_data)
    return True



# Delete
def delete(filter_exp = None):
    file_data = DataAccess.read()
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.'))
    for data in file_data:
        if filtered_data(data, filter_exp):
            file_data.remove(data)
    DataAccess.write(file_data)
    return True

def delete_one(update_exp = {}, filter_exp = None):
    file_data = DataAccess.read()
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.'))
    for data in file_data:
        if filtered_data(data, filter_exp):
            file_data.remove(data)
            break
    DataAccess.write(file_data)
    return True