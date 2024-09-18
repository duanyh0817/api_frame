import re
import jsonpath
import pytest
import requests
from common.extract_util import write_yaml, read_yaml, read_testcase
from common.request_util import RequestUtil
# 前置函数
class TestgetValidOrgIds:
    pass
    # @pytest.mark.parametrize("caseinfo", read_testcase("./testcases/test_getValidOrgIds.yaml"))
    # def test_getValidOrgIds(self, caseinfo):
    #     method = caseinfo["request"]["method"]
    #     url = caseinfo["request"]["url"]
    #     json = caseinfo["request"]["json"]
    #     json["uid"] = read_yaml("login_uid")
    #     res = RequestUtil().send_all_request(method=method, url=url, json=json)
    #     result = res.json()
    #     print("响应数据:", result)
    #     orgIds = jsonpath.jsonpath(result, '$.data.validOrgIds')
    #     for orgIdlst in orgIds:
    #         orgid_lst = []
    #         for orgId in orgIdlst:
    #             orgid_lst.append(orgId)
    #     write_yaml({"orgid_lst": orgid_lst})
    #     write_yaml({"login_orgid": orgid_lst[-1]})