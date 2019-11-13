import configparser
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir,"config.ini")

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_base_url(self):
        protocol = self.cf.get("HTTP","protocol")
        host = self.cf.get("HTTP","host")
        port = self.cf.get("HTTP", "port")
        base_url = protocol+'://'+host+':'+port
        return base_url

    def get_base1_url(self):
        protocol = self.cf.get("HTTP","protocol")
        host1 = self.cf.get("HTTP","host1")
        port = self.cf.get("HTTP", "port")
        base_url = protocol+'://'+host1+':'+port
        return base_url

    def get_email(self,mail_key):
        email_value = self.cf.get("EMAIL",mail_key)
        return email_value

    def get_t_id(self,t_id):
        t_id = self.cf.get("EXCEL_ID",t_id)
        return t_id

    def get_studentId(self,studentId):
        studentId = self.cf.get("EXCEL_ID",studentId)
        return studentId

    def get_excel(self, excel_key):
        excel_vale = self.cf.get("EXCEL", excel_key)
        # if excel_vale==None:
        #     excel_vale = excel_vale
        # else:
        #     excel_vale = None
        return excel_vale