import re
import jsonpath
import pytest
import requests

from common.apiAssert_util import ApiAssert
from common.extract_util import write_yaml, read_yaml, read_testcase
from common.request_util import RequestUtil
class TestWebLogin:
    @pytest.mark.parametrize("caseinfo",read_testcase("./testcases/test_webLogin.yaml"))
    @pytest.mark.run(order=1)
    def test_webLogin(self, ex_output, caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        json = caseinfo["request"]["json"]
        headers = caseinfo["request"]["headers"]
        # res = TestApi.sess.request(method=method,url=url,json=datas,headers=headers)
        res = RequestUtil().send_all_request(method=method,url=url,json=json,headers=headers)
        #断言
        hold_res = res.json()
        ApiAssert.api_assert(str(hold_res["retcode"]),'==',str(caseinfo["validate"]["retcode"]))
        print("响应数据:",res.text)
        result = res.text
        login_mobile = re.search('"mobile":"(.*?)"',result)[1]
        write_yaml({"login_mobile":login_mobile})
        login_uid = re.search('"userId":"(.*?)"',result)[1]
        write_yaml({"login_uid":login_uid})

    @pytest.mark.parametrize("caseinfo", read_testcase("./testcases/test_getValidOrgIds.yaml"))
    def test_getValidOrgIds(self, caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        json = caseinfo["request"]["json"]
        json["uid"] = read_yaml("login_uid")
        res = RequestUtil().send_all_request(method=method, url=url, json=json)
        result = res.json()
        print("响应数据:",result)
        orgIds = jsonpath.jsonpath(result, '$.data.validOrgIds')
        for orgIdlst in orgIds:
            orgid_lst = []
            for orgId in orgIdlst:
                orgid_lst.append(orgId)
        write_yaml({"orgid_lst": orgid_lst})
        write_yaml({"login_orgid": orgid_lst[-1]})

    @pytest.mark.parametrize("caseinfo", read_testcase("./testcases/test_getUsersSegment.yaml"))
    def test_getUsersSegment(self,caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        json = caseinfo["request"]["json"]
        json["mobile"] = read_yaml("login_mobile")
        json["orgId"] = read_yaml("login_orgid")
        res = RequestUtil().send_all_request(method=method,url=url,json=json)
        print("响应数据:",res.json())
        result = res.json()
        users = jsonpath.jsonpath(result,"$.data.users")
        mobile_lst = []
        for user in users:
            for item in user:
                mobile = item["mobile"]
                mobile_lst.append(mobile)
        print(mobile_lst)
        write_yaml({"mobile_lst":mobile_lst})

    @pytest.mark.parametrize("caseinfo", read_testcase("./testcases/test_getDepts.yaml"))
    def test_getDepts(self,caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        json = caseinfo["request"]["json"]
        json["updateFlag"] = read_yaml("login_orgid")
        json["mobile"] = read_yaml("login_mobile")
        json["orgId"] = read_yaml("login_orgid")
        res = RequestUtil().send_all_request(method=method,url=url,json=json)
        result = res.json()
        print("响应数据:",result)
        depts = jsonpath.jsonpath(result,"$.data.depts")
        print(depts)
        for dept in depts:
            deptid_lst = []
            for item in dept:
                deptid = item["id"]
                deptid_lst.append(deptid)
            write_yaml({"deptid_lst":deptid_lst})

    @pytest.mark.parametrize("caseinfo", read_testcase("./testcases/test_webUpload.yaml"))
    @pytest.mark.run(order=2)
    def test_webUpload(self, caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        fileType = caseinfo["request"]["fileType"]
        url = url + str(fileType)
        #获取文件路径
        files = caseinfo["request"]["files"]
        #以二进制方式打开文件
        files["media"] = open(files["media"],"rb")
        #上传文件
        res = RequestUtil().send_all_request(method=method, url=url, files=files)
        result = res.json()
        print("响应数据:", result)
        fileUrl = jsonpath.jsonpath(result, "$.fileUrl")
        write_yaml({"fileUrl": fileUrl})
        intranet = jsonpath.jsonpath(result, "$.intranet")
        write_yaml({"intranet": intranet})
