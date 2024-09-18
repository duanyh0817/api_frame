import yaml

#写入中间值
def write_yaml(data):
    with open("./extract.yaml", mode="a+", encoding='utf-8') as f:
        yaml.safe_dump(data, stream=f, allow_unicode=True)
#读取中间值
def read_yaml(key):
    with open("./extract.yaml",mode="r", encoding="utf-8") as f:
        all_value = yaml.safe_load(f)
        return all_value[key]
#清空中间值
def clear_yaml():
    with open('./extract.yaml',mode="w", encoding='utf-8') as f:
        pass

#读取测试用例
def read_testcase(path):
    with open(path,mode="r", encoding="utf-8") as f:
        all_value = yaml.safe_load(f)
        return all_value