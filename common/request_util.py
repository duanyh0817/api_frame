import requests
import pytest
class RequestUtil:
    sess = requests.session()
    def send_all_request(self,**kwargs):
        res = RequestUtil.sess.request(**kwargs)
        print(kwargs.get("method"))
        return res
