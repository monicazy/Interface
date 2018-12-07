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
    df = pd.read_excel(project_path.test_case_path, sheet_name="init")
    username = df.iloc[0, 0]
    password = df.iloc[1, 0]
    assert_id = df.iloc[2, 0]
    assert_name = df.iloc[3, 0]
    type_id = df.iloc[4, 0]
    start_time = df.iloc[5, 0]
    end_time = df.iloc[6, 0]
    color = df.iloc[7, 0]
    label_name = df.iloc[8, 0]
    label_id = df.iloc[9, 0]
    label_editname = df.iloc[10, 0]
    address = df.iloc[11, 0]
    avatar_url = df.iloc[12, 0]
    poi_name = df.iloc[13, 0]

if __name__ == '__main__':
    print(GetData().username)
