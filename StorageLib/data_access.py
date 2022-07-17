import json
import xmltodict
from dicttoxml import dicttoxml


class DataAccess:

    @classmethod
    def read(cls):
        try:
            with open('data/storage_lib_json_data', 'r') as file:
                data = json.load(file)
                file.close()
        except:
            data = []
        return data

    @classmethod
    def write(cls, data):
        with open('data/storage_lib_json_data', 'w') as file:
            json.dump(data, file)
            file.close()
        return True


    @classmethod
    def read_xml(cls):
        # try:
        with open('data/storage_lib_xml_data', 'r') as file:
            data = xmltodict.parse(file.read())
            file.close()
        # except:
        #     data = []
        return data

    @classmethod
    def write_xml(cls, data):
        with open('data/storage_lib_xml_data', 'w') as file:
            file.write(dicttoxml(data).decode("utf-8"))
            file.close()
        return True