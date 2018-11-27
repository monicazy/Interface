# -*- coding: utf-8 -*-
# @Time  : 2018/11/8 22:58
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : get_data.py
import pandas as pd
from tools import project_path


class GetData:
    Cookie = None
    # 从excel中读取变量数据
    df=pd.read_excel(project_path.test_case_path, sheet_name="init")
    tel = df.iloc[0,0] # 获取未注册的手机号
    normal_tel = df.iloc[1,0]
    admin_tel = df.iloc[2,0]
    loan_member_id = df.iloc[3,0]
    memberID = df.iloc[4,0]
    loanId =eval(df.iloc[5,0]) #初始值为None的变量eval一下还原本身

if __name__ == '__main__':
    print(GetData().loanId)