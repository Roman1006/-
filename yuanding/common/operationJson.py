#主要是对json数据文件进行读写操作，这里默认对data.json这个文件进行操作，
# 如果要指定操作某个json文件只需要在调用该方法的时候传入json文件路径即可
import json
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
jsonPath = os.path.join(proDir, "../testDataFile/data.json")


class OperationJson:
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = jsonPath

    def open_json(self):
        """打开json文件
        :return:返回json文件数据
        """
        with open(self.file_name, 'r',encoding='utf-8') as fp:
            data = json.load(fp)
            return data
            fp.close()

    def key_get_data(self, key):
        """通过key值获取数据
        :param key: 需要获取的值对应的key
        :return:
        """
        data = self.open_json()[key]
        return data

    def write_data(self, w_data, key1, key2=None):
        """修改json数据
        :param w_data: 修改后的数据
        :param key1: 要修改的键值1
        :param key2: 要修改的键值2
        :return:
        """
        data_dict = self.open_json()
        if key2 == None:
            data_dict[key1] = w_data
        else:
            data_dict[key1][key2] = w_data
        with open(self.file_name, 'w') as fp:
            fp.write(json.dumps(data_dict, ensure_ascii=False, sort_keys=False, indent=2))  # 对写入的json数据进行格式化
            fp.close()

