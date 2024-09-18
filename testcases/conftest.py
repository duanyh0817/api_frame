import pytest
from common.extract_util import clear_yaml
@pytest.fixture(scope="function", autouse=False)
def ex_sql():
    print("执行用例之前先执行SQL语句")
    yield
    print("执行用例之后关闭数据库链接")

@pytest.fixture(scope="function", autouse=False)
def ex_output():
    print("手动输出哈哈哈")
#每次执行前清空extract.yaml
@pytest.fixture(scope="session", autouse=True)
def clear_extract_yaml():
    clear_yaml()
