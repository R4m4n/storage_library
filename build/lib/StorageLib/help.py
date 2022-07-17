def update_data(file_data, update_exp):
    for key, value in update_exp.items():
            file_data[key] = value


def filtered_data(data, filter_exp = None):
    if filter_exp:
        if list(filter_exp.keys())[0] in data and data[list(filter_exp.keys())[0]] == list(filter_exp.values())[0]:
            return True
        else:
            return False
    return True