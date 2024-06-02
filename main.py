import os
import sys
import subprocess


def upgrade():
    # 查询需要更新的包
    outdated_info = os.popen('pip list -o -i https://pypi.tuna.tsinghua.edu.cn/simple/').readlines()
    # 抽取包的名称
    package_name = [i.split()[0] for i in outdated_info[2:]]
    print(f"可升级的库有：{package_name}")
    for i in package_name[:-1]:
        try:
            print(f'开始升级库：{i}', sep='\n')
            command = 'pip install --upgrade ' + i + ' -i https://pypi.tuna.tsinghua.edu.cn/simple/'
            print(command)
            a = os.popen(command, 'r')
            print(a.read())
        except:
            print(f'升级发生错误：{i}')


if __name__ == '__main__':
    # 更新pip版本
    # a = os.popen('python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/', 'r')
    # print(a.read())
    upgrade()
