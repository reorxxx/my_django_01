"""
处理数据库及数据


"""

import mysql.connector
import time  # 引入time模块
import random  # 引入random模块
import uuid  #引入uuid模块

def getMyDb():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Superfatgao1",
        database="plan_management"
    )
    return mydb

#创建一个任务
def create_task( title , describe , content , start_time , end_time , need_message=0, need_repeat=0):
    mydb=getMyDb()
    mycursor = mydb.cursor()
    task_id="%s%d"%(time.strftime("%Y%m%d%H%M%S", time.localtime()),random.randint(10000,99999))
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    sql = "INSERT INTO tasks (id,title,t_describe,t_content,t_start_time,t_end_time,create_time,update_time,need_message,need_repeat) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (task_id, title, describe, content, start_time, end_time, now, now, need_message, need_repeat)

    mycursor.execute(sql, val)
    mydb.commit()
    print("共 [", mycursor.rowcount, "]个 create_task 记录插入成功。")
    return task_id

#更新一个任务
def update_task(id, value={}):

    mydb=getMyDb()
    mycursor = mydb.cursor()

    set=""
    for k,v in value.items():
        # print(k,v)
        if(set!=""):
            set = "%s , %s = '%s'"%(set,k,v)
        else:
            set = "%s = '%s'" % (k, v)

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    set = "%s , update_time = '%s'"%(set,now)
    print(set)

    sql = "UPDATE tasks SET %s WHERE id = '%s'"%(set,id)
    print(sql)
    try:
        mycursor.execute(sql)
        mydb.commit()
    except mysql.connector.errors.ProgrammingError:
        print("\n---!!!!   update_task erro  !!!!---\n")

    print("共 [", mycursor.rowcount, "]个 update_task 记录插入成功。")


#获取用户任务列表
def get_task_list(page_size=20,page=0):
    mydb=getMyDb()
    mycursor = mydb.cursor()

    sql="SELECT * FROM tasks LIMIT %s OFFSET %s"%(page_size,page*page_size)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

#获取一个用户任务详情
def get_task_by_id(id=""):
    if(id==""):
        print("id erro")
        return []

    mydb=getMyDb()
    mycursor = mydb.cursor()

    sql="SELECT * FROM tasks WHERE id = %s LIMIT 1"%(id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


#从头创建一个待办事项
def create_plan(title , describe , content , start_time , end_time , need_message=0, need_repeat=0):

    task_id=create_task(title , describe , content , start_time , end_time , need_message, need_repeat)
    plan_id="%s%d"%(time.strftime("%Y%m%d%H%M%S", time.localtime()),random.randint(10000,99999))
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    mydb=getMyDb()
    mycursor = mydb.cursor()

    sql = "INSERT INTO plan (id,task_id,t_start_time,t_end_time,create_time,update_time,is_done) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (plan_id, task_id, start_time , end_time , now, now, 0)

    mycursor.execute(sql, val)
    mydb.commit()
    print("共 [", mycursor.rowcount, "]个 create_plan 记录插入成功。")
    return plan_id

#通过一个任务，创建待办事项
def create_plan_by_task(task_id,start_time,end_time):

    plan_id="%s%d"%(time.strftime("%Y%m%d%H%M%S", time.localtime()),random.randint(10000,99999))
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    mydb=getMyDb()
    mycursor = mydb.cursor()

    sql = "INSERT INTO plan (id,task_id,t_start_time,t_end_time,create_time,update_time,is_done) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (plan_id, task_id, start_time , end_time , now, now, 0)

    mycursor.execute(sql, val)
    mydb.commit()
    print("共 [", mycursor.rowcount, "]个 create_plan 记录插入成功。")
    return plan_id

create_plan_by_task(2019102518293432135,"2019-11-01 00:01","2020-01-01 00:00")

#获取待办事项列表
def get_plan_list(page_size=20,page=0):
    mydb=getMyDb()
    mycursor = mydb.cursor()

    sql="SELECT * FROM plan LIMIT %s OFFSET %s"%(page_size,page*page_size)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


#完成一个待办事项
def plan_done(plan_id):
    mydb=getMyDb()
    mycursor = mydb.cursor()
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


    sql = "UPDATE plan SET is_done='1' ,done_time = '%s'WHERE id = '%s'"%(now,plan_id)

    try:
        mycursor.execute(sql)
        mydb.commit()
    except mysql.connector.errors.ProgrammingError:
        print("\n---!!!!   update_task erro  !!!!---\n")

    print("共 [", mycursor.rowcount, "]个 update_plan 记录插入成功。")


#获取一个待办事项详情
def get_plan_by_id(id=""):
    if(id==""):
        print("get_plan_by_id id erro")
        return []

    mydb=getMyDb()
    mycursor = mydb.cursor()

    sql="SELECT * FROM plan WHERE id = %s LIMIT 1"%(id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

#查找所有某task_id的待办任务
def get_plan_by_task_id(task_id="",page_size=20,page=0):
    if(task_id==""):
        print("get_plan_by_task_id task_id erro")
        return []

    mydb=getMyDb()
    mycursor = mydb.cursor()

    sql="SELECT * FROM plan WHERE task_id = %s LIMIT %s OFFSET %s"%(task_id,page_size,page_size*page)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult
