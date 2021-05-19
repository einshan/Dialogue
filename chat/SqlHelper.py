# -*- coding: UTF-8 -*-

import pymysql
import pandas as pd
import json

class QADialogue(object):
    def __init__(self,session_id,user_id,role,sku,content,intent):
        self.session_id = session_id
        self.user_id = user_id
        self.role = role
        self.sku = sku
        self.content = content
        self.intent = intent




if __name__ == '__main__':
    df = pd.read_csv('/Users/shiwa/Downloads/web-chatroom/JDDC-Dialog-Solution/E-commerce/JDDC_Dataset_LREC.txt', error_bad_lines=False)
    print(df.shape)
    df = df[df["MONTH"].isin([1])]

    conn = pymysql.connect(host="localhost", user="root", password="root", database="flight", charset="utf8")
    cursor = conn.cursor()

    for index, row in df.iterrows():
        session_id = row["session_id"]
        user_id = row['user_id']
        role = row['role']
        sku = row['sku']
        content = row['content']
        intent = row['intent']

        sql = "INSERT INTO flight_info(session_id,user_id,role,sku,content,intent) " \
              "VALUES (%s,%s,%s, %s,%s,%s);"
        try:
            # 执行SQL语句
            cursor.execute(sql, [session_id,user_id,role,sku,content,intent])
            # 提交事务
            conn.commit()
            # 提交之后，获取刚插入的数据的ID
            last_id = cursor.lastrowid
            print(last_id)
        except Exception as e:
            # 有异常，回滚事务
            conn.rollback()
            print(e)
    cursor.close()
    conn.close()
    print("ok")

