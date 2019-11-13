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
file_name = os.path.join(proDir, "../../testDataFile/fenxi.json")
data_path = os.path.join(proDir,"..\\data.xls")
# print(hh)
# data_path = "D:\自动化项目\接口自动化\yuanding\\testCase\\appdev_api\data.xls"

class LoginTest(unittest.TestCase):
    def setUp(self):
        # print('执行开始')
        self.data = ReadTestData(file_name)
        self.hea_data = ReadTestData()
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.json = OperationJson()
        self.sheet = 'app_test_fenxi'
        self.row = list(range(2, 30))
        self.log.info(message="----------测试开始----------", name="test_piyue.py")

    def tearDown(self):
        # print("我要走了")
        self.log.info(message="----------测试结束----------", name="test01_OrcLogin.py")

    def test_fenxi01(self):
        """获取考试班级/AnalyzeDateEntering/findExamOfAnalyzeDone"""
        self.log.info(message="test04-1", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        headers = self.hea_data.get_header(self.sheet, self.row[0])
        # data = self.data.get_request_data(self.sheet, self.row[0])
        expect = self.data.get_expect_result(self.sheet, self.row[0])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        # self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)
        # 发送请求
        status_code, header_token, res_json = self.http.http_method(method=method, url=url, data=None, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"], '10000', msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"],expect["msg"],msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi02(self):
        """获取已分析考试列表/AnalyzeDateEntering/findExamOfTeacher"""
        self.log.info(message="test04-2", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        headers = self.hea_data.get_header(self.sheet, self.row[1])
        # data = self.data.get_request_data(self.sheet, self.row[1])
        expect = self.data.get_expect_result(self.sheet, self.row[1])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        # self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

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

    def test_fenxi03(self):
        """更新操作（点击某次考试）查看班级报告/ErrorQuestion/updateFirstNewStatus"""
        self.log.info(message="test04-3", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[2])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2])
        headers = self.hea_data.get_header(self.sheet, self.row[2])
        data = self.data.get_request_data(self.sheet, self.row[2])
        expect = self.data.get_expect_result(self.sheet, self.row[2])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

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

    def test_fenxi04(self):
        """班级报告整体情况/getAnalysis"""
        self.log.info(message="test04-4", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[3])
        url = self.config.get_base1_url() + self.data.get_url(self.sheet, self.row[3])
        headers = self.hea_data.get_header(self.sheet, self.row[3])
        data = self.data.get_request_data(self.sheet, self.row[3])
        expect = self.data.get_expect_result(self.sheet, self.row[3])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=json.dumps(data), headers=headers)
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

    def test_fenxi05(self):
        """第一名学生历次考试成绩柱状图/getAnalysis"""
        self.log.info(message="test04-5", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base1_url() + self.data.get_url(self.sheet, self.row[4])
        headers = self.hea_data.get_header(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[4])
        expect = self.data.get_expect_result(self.sheet, self.row[4])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=json.dumps(data), headers=headers)
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

    def test_fenxi06(self):
        """进退步趋势/getAnalysis"""
        self.log.info(message="test04-6", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[5])
        url = self.config.get_base1_url() + self.data.get_url(self.sheet, self.row[5])
        headers = self.hea_data.get_header(self.sheet, self.row[5])
        data = self.data.get_request_data(self.sheet, self.row[5])
        expect = self.data.get_expect_result(self.sheet, self.row[5])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code, header_token, res_json = self.http.http_method(method=method, url=url, data=json.dumps(data),
                                                                    headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"], '10000', msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi07(self):
        """知识点儿情况/getAnalysis"""
        self.log.info(message="test04-7", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[6])
        url = self.config.get_base1_url() + self.data.get_url(self.sheet, self.row[6])
        headers = self.hea_data.get_header(self.sheet, self.row[6])
        data = self.data.get_request_data(self.sheet, self.row[6])
        expect = self.data.get_expect_result(self.sheet, self.row[6])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code, header_token, res_json = self.http.http_method(method=method, url=url, data=json.dumps(data),
                                                                    headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"], '10000', msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi08(self):
        """更新操作（点击某次考试）查看评卷课件/ErrorQuestion/updateFirstNewStatus"""
        self.log.info(message="test04-8", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[7])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[7])
        headers = self.hea_data.get_header(self.sheet, self.row[7])
        data = self.data.get_request_data(self.sheet, self.row[7])
        expect = self.data.get_expect_result(self.sheet, self.row[7])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi09(self):
        """评卷课件情况总览/getCourseware"""
        self.log.info(message="test04-9", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[8])
        url = self.config.get_base1_url() + self.data.get_url(self.sheet, self.row[8])
        headers = self.hea_data.get_header(self.sheet, self.row[8])
        data = self.data.get_request_data(self.sheet, self.row[8])
        expect = self.data.get_expect_result(self.sheet, self.row[8])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=json.dumps(data), headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi10(self):
        """评卷课件试卷结构//analysisExamPic/getPcQuestionAll"""
        self.log.info(message="test04-10", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[9])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[9])
        headers = self.hea_data.get_header(self.sheet, self.row[9])
        data = self.data.get_request_data(self.sheet, self.row[9])
        expect = self.data.get_expect_result(self.sheet, self.row[9])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi11(self):
        """评卷课件试卷结构/讲评收藏的题目//analysisExamPic/getCollectionQuestion"""
        self.log.info(message="test04-11", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[10])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[10])
        headers = self.hea_data.get_header(self.sheet, self.row[10])
        data = self.data.get_request_data(self.sheet, self.row[10])
        expect = self.data.get_expect_result(self.sheet, self.row[10])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi12(self):
        """评卷课件试卷结构/讲评收藏的题目//analysisExamPic/getCollectionQuestion"""
        self.log.info(message="test04-12", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[11])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[11])
        headers = self.hea_data.get_header(self.sheet, self.row[11])
        data = self.data.get_request_data(self.sheet, self.row[11])
        expect = self.data.get_expect_result(self.sheet, self.row[11])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi13(self):
        """评卷课件试卷结构/讲评收藏的题目//analysisExamPic/getCollectionQuestion"""
        self.log.info(message="test04-13", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[12])
        url = self.config.get_base1_url() + self.data.get_url(self.sheet, self.row[12])
        headers = self.hea_data.get_header(self.sheet, self.row[12])
        data = self.data.get_request_data(self.sheet, self.row[12])
        expect = self.data.get_expect_result(self.sheet, self.row[12])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=json.dumps(data), headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi14(self):
        """查看成绩单/analysisExamPic/getScoreTableList"""
        self.log.info(message="test04-14", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[13])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[13])
        headers = self.hea_data.get_header(self.sheet, self.row[13])
        data = self.data.get_request_data(self.sheet, self.row[13])
        expect = self.data.get_expect_result(self.sheet, self.row[13])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi15(self):
        """查看学生简报/analysisExamPic/getScorePostList"""
        self.log.info(message="test04-15", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[14])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[14])
        headers = self.hea_data.get_header(self.sheet, self.row[14])
        data = self.data.get_request_data(self.sheet, self.row[14])
        expect = self.data.get_expect_result(self.sheet, self.row[14])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi16(self):
        """查看指定学生InStudentName/examManage/InStudentName"""
        self.log.info(message="test04-16", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[15])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[15])
        headers = self.hea_data.get_header(self.sheet, self.row[15])
        data = self.data.get_request_data(self.sheet, self.row[15])
        expect = self.data.get_expect_result(self.sheet, self.row[15])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi17(self):
        """查看指定学生getSureClass/examManage/verificationName"""
        self.log.info(message="test04-17", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[16])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[16])
        headers = self.hea_data.get_header(self.sheet, self.row[16])
        data = self.data.get_request_data(self.sheet, self.row[16])
        expect = self.data.get_expect_result(self.sheet, self.row[16])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi18(self):
        """查看指定学生verificationName/examManage/verificationName"""
        self.log.info(message="test04-18", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[17])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[17])
        headers = self.hea_data.get_header(self.sheet, self.row[17])
        data = self.data.get_request_data(self.sheet, self.row[17])
        expect = self.data.get_expect_result(self.sheet, self.row[17])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi19(self):
        """查看指定学生getScoreResult/examManage/getScoreResult"""
        self.log.info(message="test04-19", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[18])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[18])
        headers = self.hea_data.get_header(self.sheet, self.row[18])
        data = self.data.get_request_data(self.sheet, self.row[18])
        expect = self.data.get_expect_result(self.sheet, self.row[18])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi20(self):
        """查看全班同学综合报告结果/examManage/publishedResults"""
        self.log.info(message="test04-20", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[19])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[19])
        headers = self.hea_data.get_header(self.sheet, self.row[19])
        data = self.data.get_request_data(self.sheet, self.row[19])
        expect = self.data.get_expect_result(self.sheet, self.row[19])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_fenxi21(self):
        """查看全班同学综合报告分析/AnalyzeDateEntering/findExamAnalyzeId/6803"""
        self.log.info(message="test04-21", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[20])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[20])
        headers = self.hea_data.get_header(self.sheet, self.row[20])
        # data = self.data.get_request_data(self.sheet, self.row[20])
        expect = self.data.get_expect_result(self.sheet, self.row[20])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        # self.log.info(message="请求数据：%s" % data)
        self.log.info(message="期望结果：%s" % expect)

        # 发送请求
        status_code,header_token, res_json = self.http.http_method(method=method, url=url, data=None, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"],expect["code"], msg=">>>断言失败，实际返回结果：%s" % dict_json["code"])
        self.assertEqual(dict_json["msg"], expect["msg"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["msg"])
        self.log.info(message="断言结束")
#fg
if __name__ == "__main__":
    unittest.main()
