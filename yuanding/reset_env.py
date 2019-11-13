#!/usr/bin/python3
# coding=utf-8
import requests
import json
from common.myLog import MyLog
from common.operationJson import OperationJson
from config.readConfig import ReadConfig

log = MyLog()
config = ReadConfig()


class ResetEnv:
    def __init__(self):
        self.op_json = OperationJson()
        self.omp = DeleteOmpName()
        self.headers = self.op_json.key_get_data("orc_token_header")

    def get_db_list(self):
        url = config.get_base_url() + "/tenant"
        res_json = requests.get(url=url, headers=self.headers).json()
        return json.dumps(res_json, ensure_ascii=False, sort_keys=False, indent=2)

    # def delete_db(self):
    #     """清理所有DB"""
    #     all_db_dict = json.loads(self.get_db_list())
    #     if all_db_dict["status"]:
    #         all_db_list = []
    #         db_number = len(all_db_dict["results"])
    #         for i in range(db_number):
    #             db_id = all_db_dict["results"][i]["tenant_name"]
    #             all_db_list.append(db_id)
    #             url = config.get_base_url() + "/clearDB/" + all_db_list[i]
    #             res_json = requests.delete(url=url, headers=self.headers).json()
    #             if res_json["status"]:
    #                 log.info(message="已经清理所有Tenant DB!")
    #                 self.omp.delete_profile_name()
    #                 return True
    #             else:
    #                 return False
    #     else:
    #         log.info(message="环境干净无需清理...")
    #         self.omp.delete_profile_name()
    #         return True

    def delete_db(self):
        """只是清理Test DB"""
        # db_name = "auto_tenant_name"
        # url = config.get_base_url() + "/clearDB/" + db_name
        # res_json = requests.delete(url=url, headers=self.headers).json()
        # if res_json["status"]:
        #     log.info(message="已经清理Test Tenant DB!")
        #     return True
        # else:
        #     return True


class DeleteOmpName:
    def __init__(self):
        self.profile_list = []

    def get_omp_profile_name(self):
        url = config.get_omp_url() + "/omp/listProfileName"
        res = requests.get(url=url).json()
        if len(res) != 0:
            for i in range(len(res)):
                profile_name = res[i]['profileName']
                self.profile_list.append(profile_name)
            else:
                log.info(message="ompProfilesName列表：%s" % str(self.profile_list))
                return True
        else:
            return False

    def delete_profile_name(self):
        base_url = config.get_omp_url() + "/omp/ompProfile?name="
        is_name = self.get_omp_profile_name()
        if is_name:
            for i in self.profile_list:
                url = base_url + i
                res = requests.delete(url=url).text
                if res == 'OK':
                    log.info(message="ProfileName：%s删除成功" % i + " >>> " + res)
                else:
                    log.error(message="ProfileName：%s删除失败" % i + " >>> " + res)
        else:
            log.info(message="没有可以删除的ProfileName！")


if __name__ == "__main__":
    r = ResetEnv()
    # r.get_db_list()
    print(r.get_db_list())
