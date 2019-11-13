import json
import os
import unittest
from common.httpSet import HttpMethod
from common.myLog import MyLog
from common.operationJson import OperationJson
from common.readTestData import ReadTestData
from config.readConfig import ReadConfig
from common.getRunLine import get_run_line
import urllib3
urllib3.disable_warnings()
print("我是")
print(os.path.realpath(__file__))
proDir = os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.join(proDir, "../../testDataFile/orchestrator_account.json")

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadTestData(file_name)
        self.hea_data = ReadTestData()
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.json = OperationJson()
        self.sheet = 'app_test_case'
        self.row = list(range(2, 20))
        self.log.info(message="----------测试开始----------", name="test01_OrcLogin.py")

    def tearDown(self):
        self.log.info(message="----------测试结束----------", name="test01_OrcLogin.py")
    def test_login01(self):
        """登录成功/userManage/signIn"""
        self.log.info(message="test01-1", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        headers = self.hea_data.get_header(self.sheet, self.row[0])
        data = self.data.get_request_data(self.sheet, self.row[0])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        status_code,header_token,res_json = self.http.http_method(method=method, url=url, data=data)
        dict_json = json.loads(res_json) # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        if dict_json["data"]:
            orc_token = header_token["Token"]  # 提取orc_token
            self.log.info(message="提取token", name="test_login01")
            self.log.info(message="%s" % orc_token, name="test_login01")
            authorization =  orc_token
            # self.json.write_data(authorization, "orc_token_header", "Authorization")  # 把orc_token写入json文件
            self.json.write_data(authorization, "login_header_token", "Token")
            self.json.write_data(authorization, "login_header_piyue", "Token")
            self.json.write_data(authorization, "login_header_fenxi", "Token")
            self.json.write_data(authorization, "fenxi", "Token")
        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["data"], "登录成功",msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["msg"], "OK",
                         msg=">>>断言失败，实际返回值是：%s" % dict_json["msg"])
        self.log.info(message="断言结束")

    def test_login02(self):
        """获取用户信息/userManage/getInfo"""
        self.log.info(message="test02-1", name="test01_OrcLogin.py", line=get_run_line())
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
        status_code,header_token, res_json = self.http.http_method(method=method, url=url,headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        self.log.info(message="第三步：断言")
        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertEqual(dict_json["code"], '10000',msg=">>>断言失败，实际返回结果：%s" %dict_json["code"])
        self.assertEqual(dict_json["data"]["userName"], expect["userName"],msg=">>>断言失败，实际返回结果：%s" % dict_json["data"]["userName"])
        self.log.info(message="断言结束")

    def test_login03(self):
        """获取首页右上角信息/ErrorQuestion/getIndexBaseInfo"""
        self.log.info(message="test02-2", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[2])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2])
        headers = self.hea_data.get_header(self.sheet, self.row[2])
        # data = self.data.get_request_data(self.sheet, self.row[2])
        expect = self.data.get_expect_result(self.sheet, self.row[2])
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
        self.assertEqual(dict_json["code"],'10000', msg=">>>断言失败，实际返回结果：%s")
        self.assertEqual(dict_json["data"]["schoolName"], expect["schoolName"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["data"]["schoolName"])
        self.log.info(message="断言结束")

    def test_login04(self):
        """获取考试列表/examManage/getExamlist?type=2"""
        self.log.info(message="test02-3", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[3])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[3])
        headers = self.hea_data.get_header(self.sheet, self.row[3])
        # data = self.data.get_request_data(self.sheet, self.row[3])
        expect = self.data.get_expect_result(self.sheet, self.row[3])
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
        self.assertEqual(dict_json["code"], '10000',msg=">>>实际返回结果：%s" %dict_json["code"])
        self.assertEqual(dict_json["data"][0]["exam_name"], expect["exam_name"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["data"][0]["exam_name"])
        self.log.info(message="断言结束")

    def test_login05(self):
        """获取电教老师获取电教老师"""
        self.log.info(message="test02-4", name="test01_OrcLogin.py", line=get_run_line())
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        headers = self.hea_data.get_header(self.sheet, self.row[4])
        # data = self.data.get_request_data(self.sheet, self.row[4])
        expect = self.data.get_expect_result(self.sheet, self.row[4])
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
        self.assertEqual(dict_json["data"][6]["userName"], expect["userName"],
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["data"][5]["userName"])
        self.log.info(message="断言结束")

if __name__ == "__main__":
    unittest.main()
