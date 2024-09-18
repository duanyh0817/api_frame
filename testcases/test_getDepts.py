import jsonpath
import pytest

from common.extract_util import read_yaml, write_yaml, read_testcase
from common.request_util import RequestUtil


class TestGetDepts():
    pass
    # @pytest.mark.parametrize("caseinfo", read_testcase("./testcases/test_getDepts.yaml"))
    # def test_getDepts(self, caseinfo):
    #     method = caseinfo["request"]["method"]
    #     url = caseinfo["request"]["url"]
    #     json = caseinfo["request"]["json"]
    #     json["updateFlag"] = read_yaml("login_orgid")
    #     json["mobile"] = read_yaml("login_mobile")
    #     json["orgId"] = read_yaml("login_orgid")
    #     res = RequestUtil().send_all_request(method=method, url=url, json=json)
    #     result = res.json()
    #     print("响应数据:", result)
    #     depts = jsonpath.jsonpath(result, "$.data.depts")
    #     print(depts)
    #     for dept in depts:
    #         deptid_lst = []
    #         for item in dept:
    #             deptid = item["id"]
    #             deptid_lst.append(deptid)
    #         write_yaml({"deptid_lst": deptid_lst})