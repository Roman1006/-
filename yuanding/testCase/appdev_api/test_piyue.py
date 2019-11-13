import json
import os
import unittest
from common.httpSet import HttpMethod
from common.myLog import MyLog
from common.operationJson import OperationJson
from common.readTestData import ReadTestData
from config.readConfig import ReadConfig
from common.getRunLine import get_run_line
from common.piyuedata import write_excel
from common.excelData import ExcelData
import random
import openpyxl
import xlrd
import urllib3
import requests

urllib3.disable_warnings()

proDir = os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.join(proDir, "../../testDataFile/piyue.json")
data_path = "D:\自动化项目\接口自动化\yuanding\\testCase\\appdev_api\data.xls"
data_path1 = os.path.join(proDir,"..\\data.xls")


class LoginTest(unittest.TestCase):
    def setUp(self):
        # print('执行开始')
        self.data = ReadTestData(file_name)
        self.hea_data = ReadTestData()
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.json = OperationJson()
        self.sheet = 'app_test_piyue'
        self.sheet_id = 'app_test_data'
        self.row = list(range(2, 20))
        self.log.info(message="----------测试开始----------", name="test_piyue.py")

    def tearDown(self):
        # print("我要走了")
        self.log.info(message="----------测试结束----------", name="test01_OrcLogin.py")

    def test_piyue01(self):
        """试卷结构获取/examManage/getPcQuestionAll?examId=6272&studentId= """
        self.log.info(message="test03-2", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        # print("kaishi")
        method = self.data.get_method(self.sheet, self.row[0])
        # print(method)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        # print(url)
        headers = self.hea_data.get_header(self.sheet, self.row[0])
        # print(headers)
        data = self.data.get_request_data(self.sheet, self.row[0])
        # print(data)
        expect = self.data.get_expect_result(self.sheet, self.row[0])
        # print(expect)
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)
        # res = requests.request(method,url,data = data,headers = headers)
        # print(res.text)

        # 发送请求
        status_code, header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"], '10000', msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"],expect["msg"],msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_piyue02(self):
        """获取已批阅列表/ErrorQuestion/getAnalyAndReportExamList"""
        self.log.info(message="test03-1", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        # print("kaishi")
        method = self.data.get_method(self.sheet, self.row[1])
        # print(method)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        # print(url)
        headers = self.hea_data.get_header(self.sheet, self.row[1])
        # print(headers)
        data = self.data.get_request_data(self.sheet, self.row[1])
        # print(data)
        expect = self.data.get_expect_result(self.sheet, self.row[1])
        # print(expect)
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)
        # res = requests.request(method,url,data = data,headers = headers)
        # print(res.text)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],'10000', msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_piyue03(self):
        """获取某题整体情况/examQuestion/getUncheckedTopic/6272/27170/0"""
        self.log.info(message="test03-3", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        # print("kaishi")
        method = self.data.get_method(self.sheet, self.row[2])
        # print(method)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2])
        # print(url)
        headers = self.hea_data.get_header(self.sheet, self.row[2])
        # print(headers)
        # data = self.data.get_request_data(self.sheet, self.row[5])
        # print(data)
        expect = self.data.get_expect_result(self.sheet, self.row[2])
        # print(expect)
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        # self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)
        # res = requests.request(method,url,data = data,headers = headers)
        # print(res.text)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=None, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],'10000', msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_piyue04(self):
        """获取某提批改列表/examQuestion/getStudentNamePicAll/6272/27170"""
        self.log.info(message="test03-4", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        # print("kaishi")
        # t_id = self.data.get_t_id(self.sheet_id,self.row[0])
        # studentId = self.data.get_studentId(self.sheet_id,self.row[0])
        method = self.data.get_method(self.sheet, self.row[3])
        # print(method)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[3])
        # print(url)
        headers = self.hea_data.get_header(self.sheet, self.row[3])
        # print(headers)
        # data = self.data.get_request_data(self.sheet, self.row[3])
        # print(data)
        expect = self.data.get_expect_result(self.sheet, self.row[3])
        # print(expect)
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        # self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)
        # res = requests.request(method,url,data = data,headers = headers)
        # print(res.text)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=None, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        # print(dict_json["code"])
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        id_data = dict_json["data"]
        id_list = []
        # studentId_list = []
        score_list = []
        examID_list = []
        questionId_list = []
        for k in range(len(id_data)):
            id_list.append(id_data[k]["id"])
            # studentId_list.append(id_data[k]["studentId"])
            examID_list.append(6272)
            # print(examID_list)
            questionId_list.append(27170)
            score_data = random.randint(0,3)
            score_list.append(score_data)
        #把需要批改的题块的id和studentid取出来放到excel表格中，方便下一步进行批改
        write_excel.write_excel_data(examID_list,id_list,questionId_list,score_list)
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],'10000', msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_piyue05(self):
        """批改学生试卷/examQuestion/updateStudentUnionExam"""
        self.log.info(message="test03-6", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        sheetname = "app_test_data"
        #读取excel测试数据,获取给分请求参数
        get_data = ExcelData(data_path, sheetname)
        datas = get_data.readExcel()
        method = self.data.get_method(self.sheet, self.row[5])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[5])
        headers = self.hea_data.get_header(self.sheet, self.row[5])
        expect = self.data.get_expect_result(self.sheet, self.row[5])
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求头：%s" % headers)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="期望结果：%s" % expect)
        for i in range(0,len(datas)):
            data = datas[i]
            self.log.info(message="第一步: 获取请求数据:%s" %data)
            status_code, header_token, res_json = self.http.http_method(method=method, url=url, data=json.dumps(data),
                                                                        headers=headers)
            dict_json = json.loads(res_json)  # 把json数据转换成字典对象
            self.log.info(message="第二步:发送请求，获取返回数据：")
            self.log.info(message="%s" % res_json)
            self.log.info(message="第三步：断言")
            self.assertEqual(status_code, 200, msg=">>>接口请求失败")
            # print(dict_json["code"])
            self.assertEqual(dict_json["code"], expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
            self.assertEqual(dict_json["msg"], expect["msg"],
                             msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
            self.log.info(message="断言结束")
if __name__ == "__main__":
    unittest.main()
