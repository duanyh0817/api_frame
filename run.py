import os
import time
import allure
import pytest
# @allure.epic('项目名称')
@allure.feature('所属模块')
class Test100:
    @allure.story('接口名称')
    @allure.title('用例标题')
    def test_c100(self):
        assert 1 == 2

    @allure.story('接口名称')
    @allure.title('用例标题')
    def test_c101(self):
        assert 1 == 1
if __name__ == '__main__':
    pytest.main()
    time.sleep(12)
    os.system("allure generate ./temps -o ./reports --clean")