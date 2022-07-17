# Helper module:
# Containing the common helper functions to be called when 
# some operation is needed to be performed.

def update_data(data, update_exp):
    """
    Updates the value of the key in data which are passed 
    in the update_exp and returns the updated data.

    :param data:    Data which is needed to be altered.
    :param update_exp:    key value pair which are needed to be updated in the data
    """
    for key, value in update_exp.items():
            data[key] = value
    return data


def filtered_data(data, filter_exp = None):
    """
    Runs the filter logic according to the dict.
    Returns the filtered data.

    :param data:    Data which is needed to be filtered.
    :param filter_exp:    key value pair which is being used to filter the data.
    """
    if filter_exp:
        if list(filter_exp.keys())[0] in data and data[list(filter_exp.keys())[0]] == list(filter_exp.values())[0]:
            return True
        else:
            return False
    return True