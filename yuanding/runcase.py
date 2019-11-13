import os
import sys
import time
import unittest

from common.HTMLTestRunnerNew import HTMLTestRunner
from common.myLog import MyLog
from common.sendEmail import SendEmail
from config.readConfig import ReadConfig
from reset_env import ResetEnv

proDir = os.path.split(os.path.realpath(__file__))[0]
case_list_path = os.path.join(proDir, "case_list.txt")
test_case_path = os.path.join(proDir, "testCase")


class RunTest:
    def __init__(self):
        self.logger = MyLog()
        self.readconfig = ReadConfig()
        self.send_mail = SendEmail()
        # self.env = ResetEnv()
        self.is_send = self.readconfig.get_email("is_send")

        # 测试报告基本信息
        self.testers = "Roman"
        self.title = "元丁接口测试报告"
        self.description = "正式/测试环境：Develop，IP地址：%s" % self.readconfig.get_base_url()
        # print(self.description)

        # 导入TestCase目录下的全部测试用例
        self.discover = unittest.defaultTestLoader.discover(test_case_path, pattern='test*.py')

        # 导入指定测试用例列表文件
        self.case_list_file = case_list_path
        self.case_list_list = []
        # print(self.case_list_list)

        # 重置测试环境
        self.is_env = True
        # self.is_env = self.env.delete_db()

    def get_case_list(self):
        """获取需要进行运行的测试用例列表"""
        fb = open(self.case_list_file)
        for i in fb.readlines():
            data = str(i)
            if data != '' and not data.startswith('#'):
                self.case_list_list.append(data.replace('\n', ''))
        fb.close()
        # print(self.case_list_list)

    def set_test_suite(self):
        """设置添加测试套件"""
        self.get_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.case_list_list:
            case_name = case.split('/')[-1]
            print(case_name + '.py')
            discover = unittest.defaultTestLoader.discover(test_case_path, pattern=case_name + '.py')
            suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run_test(self):
        """执行测试"""
        if self.is_env:
            try:
                test_suite = self.set_test_suite()  # 获取测试套件
                now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))  # 获取当前日期时间
                public_path = os.path.dirname(os.path.abspath(sys.argv[0]))
                # filename = public_path + "/report/" + now + "_report.html"  # 保存的报告路径和名称
                filename = public_path + "/report/" + "index.html"  # 保存的报告路径和名称
                print("测试报告目录：%s" % filename)
                fp = open(filename, 'wb')
                runner = HTMLTestRunner(stream=fp,
                                        tester=self.testers,
                                        title=self.title,
                                        description=self.description
                                        )
                if test_suite is not None:
                    runner.run(test_suite)  # 执行指定添加的测试用例套件
                    # runner.run(self.discover) # 执行TestCase目录下的全部测试用例
                else:
                    self.logger.info("Have no case to test.")
            except Exception as e:
                self.logger.error(str(e))
            finally:
                self.logger.warning("---------------All Test End---------------")
                fp.close()
                # 发送电子邮件
                if self.is_send == 'yes':
                    self.send_mail.send_email()
                    self.logger.warning("测试报告已发送电子邮件！")
                elif self.is_send == 'no':
                    self.logger.warning("测试报告不发送电子邮件！")
                else:
                    self.logger.error("测试报告发送电子邮件为未知状态，请检查配置！")
        else:
            self.logger.warning("测试环境清理失败的，无法继续执行测试！！！")


if __name__ == "__main__":
    run = RunTest()
    run.run_test()
