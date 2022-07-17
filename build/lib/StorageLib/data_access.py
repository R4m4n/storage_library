import json


class DataAccess:

    @classmethod
    def read(cls):
        try:
            with open('data/storage_lib_data', 'r') as file:
                data = json.load(file)
                file.close()
        except:
            print ('Exception')
            data = []
        return data

    @classmethod
    def write(cls, data):
        with open('data/storage_lib_data', 'w') as file:
            json.dump(data, file)
            file.close()
        return True