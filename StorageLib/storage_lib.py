import json
from .exceptions import InvalidDictError, InvalidListError
from .help import update_data, filtered_data
from .data_access import DataAccess


# Insert Functions
def insert(data):
    """
    Inserts the single data in file as it is send to this function.

    :param data:    data needs to be stored.

    Argument is supposed to be dict only.
    
    :return: boolean
    """
    if not isinstance(data, dict):
        raise(InvalidDictError('Invalid value, dict is required.'))
    file_data = DataAccess.read()
    file_data.append(data) # Append data to the retreived list from the file.
    DataAccess.write(file_data) # Write back the added data to the file.
    return True



def insert_many(data):
    """
    Inserts all the data in file as it is send to this function.

    :param data:    list of data needs to be stored.

    Argument is supposed to be list of dicts only.
    
    :return: boolean
    """
    if not isinstance(data, list):
        raise(InvalidListError('Invalid value, list is required.'))
    file_data = DataAccess.read()
    file_data = file_data + data
    DataAccess.write(file_data)
    return True



# Query Functions
def get(filter_exp = None, offset = 0, limit = None):
    """
    Returns all the data in file as a list.

    :param filter_exp:  filter expression as key value pair in dict.
    :param offset:      Offset value from where the data needs to be returned.
    :param limit:       Number of data needed to be returned.

    Argument is supposed to be list of dicts only.
    
    :return: list of fetched data.
    """
    file_data = DataAccess.read()
    file_data = file_data[offset: limit] if limit else file_data
    return_data = file_data
    # if filter expression is passed then the data is filtered else all the data is returned.
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.')) # Returns error if the filter_exp is not dict.
       
        # Data is filtered from the file using list comprehension and is assined to the return_data.
        filtered_data = [data for data in file_data if list(filter_exp.keys())[0] in data and data[list(filter_exp.keys())[0]] == list(filter_exp.values())[0]]
        return_data = filtered_data
    return return_data


def get_one(filter_exp = None):
    """
    Returns all the data in file as a list.

    :param filter_exp:  filter expression as key value pair in dict.

    Argument is supposed to be list of dicts only.
    
    :return: single fetched data.
    """
    file_data = DataAccess.read()
    # if filter expression is passed then the data is filtered else the first matching data is returned.
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.')) # Returns error if the filter_exp is not dict.
        try:
            # First matching data from file_data is returned and assigned to return_data
            filtered_data = next(filter(lambda d: list(filter_exp.keys())[0] in d and d[list(filter_exp.keys())[0]] == list(filter_exp.values())[0], file_data))
        except:
            filtered_data = {}
        return_data = filtered_data
    else:
        return_data = file_data[0]
    return return_data



# Update Functions
def update(update_exp = {}, filter_exp = None):
    """
    Updates all the matching data with the filter expression.

    :param filter_exp:  filter expression as key value pair in dict.
    :param update_exp:  update expression as key value pair in dict, the data which is needed to be updated.
    
    :return: boolean.
    """
    file_data = DataAccess.read()
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.'))
    for data in file_data:
        # data is updated if the filter expression is matched.
        if filtered_data(data, filter_exp):
            update_data(data, update_exp)
    DataAccess.write(file_data) # Updated data is rewritten in the file
    return True

def update_one(update_exp = {}, filter_exp = None):
    """
    Updates the first matching data with the filter expression.

    :param filter_exp:  filter expression as key value pair in dict.
    :param update_exp:  update expression as key value pair in dict, the data which is needed to be updated.
    
    :return: boolean.
    """
    file_data = DataAccess.read()
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.'))
    for data in file_data:
        # data is updated if the filter expression is matched.
        if filtered_data(data, filter_exp):
            data = update_data(data, update_exp)
            break
    DataAccess.write(file_data) # Updated data is rewritten in the file
    return True



# Delete Functions
def delete(filter_exp = None):
    """
    Deletes all the matching data with the filter expression.

    :param filter_exp:  filter expression as key value pair in dict.
    
    :return: boolean.
    """
    file_data = DataAccess.read()
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.'))
    for data in file_data:
        # Data is removed if a match is found
        if filtered_data(data, filter_exp):
            file_data.remove(data) 
    DataAccess.write(file_data) # Updated data is rewritten in the file
    return True

def delete_one(update_exp = {}, filter_exp = None):
    """
    Deletes the first matching data with the filter expression.

    :param filter_exp:  filter expression as key value pair in dict.
    
    :return: boolean.
    """
    file_data = DataAccess.read()
    if filter_exp:
        if not isinstance(filter_exp, dict):
            raise(InvalidDictError('Invalid value, dict is required.'))
    for data in file_data:
        # Data is removed if a match is found
        if filtered_data(data, filter_exp):
            file_data.remove(data)
            break
    DataAccess.write(file_data) # Updated data is rewritten in the file
    return True