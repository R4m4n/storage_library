# Here all the transaction to the storage medium is handled.
# This file is a middleware between the storage source and the 
# storage library.

import json
import xmltodict
import boto3
from dicttoxml import dicttoxml


class DataAccess:
    s3 = boto3.resource('s3')

    @classmethod
    def read(cls):
        """
        Reads the data from the file storage and converts it to json.

        Read data is returned in json format.
        """
        try:
            with open('data/storage_lib_json_data', 'r') as file:
                data = json.load(file)
                file.close()
        except:
            data = []
        return data

    @classmethod
    def write(cls, data):
        """
        Writes data to the file storage after converting it to json.

        :param data:    data is the data which is needed to be stored in the file
        """
        with open('data/storage_lib_json_data', 'w') as file:
            json.dump(data, file)
            file.close()
        return True


    @classmethod
    def read_xml(cls):
        """
        Reads the data from the file storage in xml format.

        Read data is returned in json format.
        """
        try:
            with open('data/storage_lib_xml_data', 'r') as file:
                data = xmltodict.parse(file.read())
                file.close()
        except:
            data = []
        return data

    @classmethod
    def write_xml(cls, data):
        """
        Writes data to the file storage after converting it to xml.

        :param data:    data is the data which is needed to be stored in the file
        """
        with open('data/storage_lib_xml_data', 'w') as file:
            file.write(dicttoxml(data).decode("utf-8"))
            file.close()
        return True


    @classmethod
    def read_s3(cls):
        """
        Reads the data from the S3 storage and converts it to json.

        Read data is returned in json format.
        """
        try:
            s3_data_object = cls.s3.Object('storage_lib_s3_data', 'storage_lib_json_data')
            file_content = s3_data_object.get()['Body'].read().decode('utf-8')
            data = json.loads(file_content)
        except:
            data = []
        return data

    @classmethod
    def write_s3(cls, data):
        """
        Writes data to the S3 storage after converting it to json.

        :param data:    data is the data which is needed to be stored in the S3
        """
        s3_data_object = cls.s3.Object('storage_lib_s3_data', 'storage_lib_json_data')
        s3_data_object.put(
            Body=(bytes(json.dumps(data).encode('UTF-8')))
        )
        return True