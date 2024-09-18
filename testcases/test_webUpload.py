import re
import jsonpath
import pytest
import requests
from common.extract_util import write_yaml, read_yaml, read_testcase
from common.request_util import RequestUtil
# 前置函数
class TestWebUpload:
    pass
    # @pytest.mark.parametrize("caseinfo", read_testcase("./testcases/test_webUpload.yaml"))
    # def test_webUpload(self, caseinfo):
    #     method = caseinfo["request"]["method"]
    #     url = caseinfo["request"]["url"]
    #     fileType = caseinfo["request"]["fileType"]
    #     url = url + str(fileType)
    #     files = caseinfo["request"]["files"]
    #     files["media"] = open(files["media"], "rb")
    #     res = RequestUtil().send_all_request(method=method, url=url, files=files)
    #     result = res.json()
    #     print("响应数据:", result)
    #     fileUrl = jsonpath.jsonpath(result, "$.fileUrl")
    #     write_yaml({"fileUrl": fileUrl})
    #     intranet = jsonpath.jsonpath(result, "$.intranet")
    #     write_yaml({"intranet": intranet})
