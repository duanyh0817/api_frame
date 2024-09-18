import jsonpath
import pytest

from common.extract_util import read_yaml, write_yaml, read_testcase
from common.request_util import RequestUtil


class TestGetUsersSegment():
    pass
    # @pytest.mark.parametrize("caseinfo", read_testcase("./testcases/test_getUsersSegment.yaml"))
    # def test_getUsersSegment(self, caseinfo):
    #     method = caseinfo["request"]["method"]
    #     url = caseinfo["request"]["url"]
    #     json = caseinfo["request"]["json"]
    #     json["mobile"] = read_yaml("login_mobile")
    #     json["orgId"] = read_yaml("login_orgid")
    #     res = RequestUtil().send_all_request(method=method, url=url, json=json)
    #     print("响应数据:", res.json())
    #     result = res.json()
    #     users = jsonpath.jsonpath(result, "$.data.users")
    #     mobile_lst = []
    #     for user in users:
    #         for item in user:
    #             mobile = item["mobile"]
    #             mobile_lst.append(mobile)
    #     print(mobile_lst)
    #     write_yaml({"mobile_lst": mobile_lst})