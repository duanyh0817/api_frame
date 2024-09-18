import traceback
from loguru import logger
class ApiAssert:
    @classmethod  # 类方法  不需要实例化
    def api_assert(cls, result, condition, exp_result, msg='断言操作'):

        # 断言结果描述--把结果放到日志中去
        pass_msg = '验证通过，断言结果：预期是：，实际结果是：'
        fail_msg = '验证失败，断言结果：预期是：，实际结果是：'
        # 简单方案
        # if condition == ‘==’：
        # assert 1==1
        #   elif condition =='in' :
        # assert 1 in [1,2,3]
        try:
            assert_type = {
                '==': result == exp_result,
                '>': result > exp_result,
                '<': result < exp_result,
                'in': result in exp_result,
                'not in': result not in exp_result,
            }
            # 使用断言类型
            if condition in assert_type:
                assert assert_type[condition]  # 断言操作
            else:
                # 断言类型不存在--报错
                raise ValueError('请输入正确的断言情况')  # 创建异常实例--进入到excepet中去
        except Exception as error:
            logger.error(traceback.format_exc())  # 打印详细的报错
            # 在这里已经处理了异常，如果不抛出，pytest不知道，不能被统计到
            raise error  # 抛出异常

