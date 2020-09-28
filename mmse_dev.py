#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
import os
import pymysql
db = pymysql.connect("localhost", "root", "root", "mmse", charset='utf8')
cursor = db.cursor()

#系统的用户登录
#os.system('clear')


def login():
    global userType
    userType = 0
    # while True:  # this is login
    name = input("\033[1mplease input your login account:").strip()  # strip()意为去除空格
    passwd = input("\033[1mplease input your login password:").strip()
    sql = '''SELECT * FROM userTable'''
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        if name == row[1] and passwd == row[2]:
            userType = row[0]
            # print(userType)
            # print("\033[32mYour account and password right!")
            return userType
    if userType == 0:
        print("\033[31mYour account or password error!")
    return userType


print('\n')


def display1():
    global select_input
    print("\033[34m\t######### \033[1;32mWelcome! customer service!\033[0;34m #########")
    print("\033[32m\033[1m\t\t\t1\033[33m\033[1m.Create Event\n")
    print("\033[32m\033[1m\t\t\t2\033[33m\033[1m.Event Feedback\n")
    print("\033[32m\033[1m\t\t\t3\033[33m\033[1m.Delete Event\n")
    print("\033[32m\033[1m\t\t\t0\033[33m\033[1m.Exit\n")
    # dict()
    while True:
        select_input = input("\033[37m\033[1mplease input you want to select items:").strip()
        if int(select_input) == 1:
            add_name = input("please input eventName:").strip()
            add_info = input("please input eventInfo:").strip()
            print('succeed')
            sql_add = """
            insert into eventTable(name,info) value(%s,%s)
            """
            name = add_name
            info = add_info
            cursor.execute(sql_add, (name, info))
            db.commit()
            print('\n')
        elif int(select_input) == 2:
            sql = '''SELECT * FROM eventTable '''
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
            db.commit()
            print('\n')
        elif int(select_input) == 3:
            del_name = input('please input the event name you want to delete:').strip()
            print('finished')
            sql_del = '''DELETE FROM eventTable WHERE name = %s'''
            cursor.execute(sql_del, del_name)
            print('\n')
        elif int(select_input) == 0 or 999:
            print('\n')
            break


def display2():
    global select_input
    print("\033[34m\t######### \033[1;32mWelcome! senior customer service!\033[0;34m #########")
    print("\033[32m\033[1m\t\t\t1\033[33m\033[1m.Event Decision\n")
    print("\033[32m\033[1m\t\t\t2\033[33m\033[1m.Event Feedback\n")
    print("\033[32m\033[1m\t\t\t0\033[33m\033[1m.Exit\n")
    while True:
        select_input = input("\033[37m\033[1mplease input you want to select items:").strip()
        if int(select_input) == 1:
            sql = '''SELECT name,info FROM eventTable '''
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
            decide_name = input("please input the event_name you want to make a decision:").strip()
            decision = input("please input approve/reject:").strip()
            dec = decision
            dec_name = decide_name
            sql_new = """UPDATE eventTable SET scsA_R = %s WHERE name = %s"""
            update = [dec, dec_name]
            cursor.execute(sql_new, update)
            db.commit()
            print('\n')
        elif int(select_input) == 2:
            sql = '''SELECT * FROM eventTable '''
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
            db.commit()
            print('\n')
        elif int(select_input) == 0 or 999:
            print('\n')
            break


def display3():
    global select_input
    print("\033[34m\t######### \033[1;32mWelcome! financial manager!\033[0;34m #########")
    print("\033[32m\033[1m\t\t\t1\033[33m\033[1m.Event View\n")
    print("\033[32m\033[1m\t\t\t2\033[33m\033[1m.financialRequest view\n")
    print("\033[32m\033[1m\t\t\t0\033[33m\033[1m.Exit\n")
    while True:
        select_input = input("\033[37m\033[1mplease input you want to select items:").strip()
        if int(select_input) == 1:
            sql = '''SELECT name,info,scsA_R FROM eventTable WHERE scsA_R = "approve"or scsA_R ="SCSdecision" '''
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
            feedback_name = input("please input the event_name you want to give a feedback:").strip()
            feedback = input("please input the feedback:").strip()
            feed = feedback
            feed_name = feedback_name
            sql_new = """UPDATE eventTable SET fmInfo = %s WHERE name = %s"""
            update = [feed, feed_name]
            cursor.execute(sql_new, update)
            db.commit()
            print('\n')
        elif int(select_input) == 2:
            sql = '''SELECT * FROM financialTable'''
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
            decide_name = input("please input the financialRequest_name you want to make a decision:").strip()
            decision = input("please input approve/reject:").strip()
            dec = decision
            dec_name = decide_name
            sql_new = """UPDATE financialTable SET fmA_R = %s WHERE name = %s"""
            update = [dec, dec_name]
            cursor.execute(sql_new, update)
            db.commit()
            print('\n')
        elif int(select_input) == 0 or 999:
            print('\n')
            break


def display4():
    global select_input
    print("\033[34m\t######### \033[1;32mWelcome! administration manager!\033[0;34m #########")
    print("\033[32m\033[1m\t\t\t1\033[33m\033[1m.Event View\n")
    print("\033[32m\033[1m\t\t\t0\033[33m\033[1m.Exit\n")
    while True:
        select_input = input("\033[37m\033[1mplease input you want to select items:").strip()
        if int(select_input) == 1:
            sql = '''SELECT name,info,scsA_R,fmInfo FROM eventTable WHERE scsA_R = "approve"or scsA_R ="SCSdecision"'''
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
            decide_name = input("please input the event_name you want to make a decision:").strip()
            decision = input("please input approve/reject:").strip()
            dec = decision
            dec_name = decide_name
            sql_new = """UPDATE eventTable SET amA_R = %s WHERE name = %s"""
            update = [dec, dec_name]
            cursor.execute(sql_new, update)
            db.commit()
            print('\n')
        elif int(select_input) == 0 or 999:
            print('\n')
            break


def display5():
    global select_input
    print("\033[34m\t######### \033[1;32mWelcome! service manager!\033[0;34m #########")
    print("\033[32m\033[1m\t\t\t1\033[33m\033[1m.Create Tasks Distribution\n")
    print("\033[32m\033[1m\t\t\t2\033[33m\033[1m.Create Financial Requests\n")
    print("\033[32m\033[1m\t\t\t3\033[33m\033[1m.Create Recruitment Requests\n")
    print("\033[32m\033[1m\t\t\t4\033[33m\033[1m.View Task Feedback\n")
    print("\033[32m\033[1m\t\t\t5\033[33m\033[1m.View Financial Feedback\n")
    print("\033[32m\033[1m\t\t\t6\033[33m\033[1m.View Recruitment Feedback\n")
    print("\033[32m\033[1m\t\t\t7\033[33m\033[1m.Delete Task\n")
    print("\033[32m\033[1m\t\t\t8\033[33m\033[1m.Delete Financial\n")
    print("\033[32m\033[1m\t\t\t9\033[33m\033[1m.Delete Recruitment\n")
    print("\033[32m\033[1m\t\t\t0\033[33m\033[1m.Exit\n")
    while True:
        select_input = input("\033[37m\033[1mplease input you want to select items:").strip()
        if int(select_input) == 1:
            createtask()
            print('\n')
        elif int(select_input) == 2:
            createfinancial()
            print('\n')
        elif int(select_input) == 3:
            createrecruitment()
            print('\n')
        elif int(select_input) == 4:
            viewtask()
            print('\n')
        elif int(select_input) == 5:
            viewfinancial()
            print('\n')
        elif int(select_input) == 6:
            viewrecruitment()
            print('\n')
        elif int(select_input) == 7:
            deltask()
            print('\n')
        elif int(select_input) == 8:
            delfinancial()
            print('\n')
        elif int(select_input) == 9:
            delrecruitment()
            print('\n')
        elif int(select_input) == 0 or 999:
            print('\n')
            break


def display6():
    global select_input
    print("\033[34m\t######### \033[1;32mWelcome! production manager!\033[0;34m #########")
    print("\033[32m\033[1m\t\t\t1\033[33m\033[1m.Create Tasks Distribution\n")
    print("\033[32m\033[1m\t\t\t2\033[33m\033[1m.Create Financial Requests\n")
    print("\033[32m\033[1m\t\t\t3\033[33m\033[1m.Create Recruitment Requests\n")
    print("\033[32m\033[1m\t\t\t4\033[33m\033[1m.View Task Feedback\n")
    print("\033[32m\033[1m\t\t\t5\033[33m\033[1m.View Financial Feedback\n")
    print("\033[32m\033[1m\t\t\t6\033[33m\033[1m.View Recruitment Feedback\n")
    print("\033[32m\033[1m\t\t\t7\033[33m\033[1m.Delete Task\n")
    print("\033[32m\033[1m\t\t\t8\033[33m\033[1m.Delete Financial\n")
    print("\033[32m\033[1m\t\t\t9\033[33m\033[1m.Delete Recruitment\n")
    print("\033[32m\033[1m\t\t\t0\033[33m\033[1m.Exit\n")
    while True:
        select_input = input("\033[37m\033[1mplease input you want to select items:").strip()
        if int(select_input) == 1:
            createtask()
            print('\n')
        elif int(select_input) == 2:
            createfinancial()
            print('\n')
        elif int(select_input) == 3:
            createrecruitment()
            print('\n')
        elif int(select_input) == 4:
            viewtask()
            print('\n')
        elif int(select_input) == 5:
            viewfinancial()
            print('\n')
        elif int(select_input) == 6:
            viewrecruitment()
            print('\n')
        elif int(select_input) == 7:
            deltask()
            print('\n')
        elif int(select_input) == 8:
            delfinancial()
            print('\n')
        elif int(select_input) == 9:
            delrecruitment()
            print('\n')
        elif int(select_input) == 0 or 999:
            print('\n')
            break


def display7():
    global select_input
    print("\033[34m\t######### \033[1;32mWelcome! sub-team!\033[0;34m #########")
    print("\033[32m\033[1m\t\t\t1\033[33m\033[1m.Task View\n")
    print("\033[32m\033[1m\t\t\t0\033[33m\033[1m.Exit\n")
    while True:
        select_input = input("\033[37m\033[1mplease input you want to select items:").strip()
        if int(select_input) == 1:
            sql = '''SELECT name,subteam,info FROM taskTable'''
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
            task_name = input("please input the task_name you want to edit:").strip()
            comment = input("please input the comment:").strip()
            com = comment
            ta_name = task_name
            sql_new = """UPDATE taskTable SET subInfo = %s WHERE name = %s"""
            update = [com, ta_name]
            cursor.execute(sql_new, update)
            db.commit()
            print('\n')
        elif int(select_input) == 0 or 999:
            print('\n')
            break


def display8():
    global select_input
    print("\033[34m\t######### \033[1;32mWelcome! HR!\033[0;34m #########")
    print("\033[32m\033[1m\t\t\t1\033[33m\033[1m.Recruitment View\n")
    print("\033[32m\033[1m\t\t\t0\033[33m\033[1m.Exit\n")
    while True:
        select_input = input("\033[37m\033[1mplease input you want to select items:").strip()
        if int(select_input) == 1:
            sql = '''SELECT * FROM recruitmentTable'''
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
            recruit_name = input("please input the recruitRequest_name you want to make a decision:").strip()
            decision = input("please input approve/reject:").strip()
            dec = decision
            rec_name = recruit_name
            sql_new = """UPDATE recruitmentTable SET hrA_R = %s WHERE name = %s"""
            update = [dec, rec_name]
            cursor.execute(sql_new, update)
            db.commit()
            print('\n')
        elif int(select_input) == 0 or 999:
            print('\n')
            break


def createtask():
    add_name = input("please input taskName:").strip()
    add_sub = input("please input subteam:").strip()
    add_info = input("please input taskInfo:").strip()
    print('finish')
    sql_add = """
        insert into taskTable(name, subteam, info) value(%s,%s,%s)
        """
    name = add_name
    subteam = add_sub
    info = add_info
    cursor.execute(sql_add, (name, subteam, info))
    db.commit()


def createfinancial():
    add_name = input("please input FinancialRequestName:").strip()
    add_info = input("please input requestInfo:").strip()
    print('finish')
    sql_add = """
            insert into financialTable(name,info) value(%s,%s)
            """
    name = add_name
    info = add_info
    cursor.execute(sql_add, (name, info))
    db.commit()


def createrecruitment():
    add_name = input("please input RecruitmentName:").strip()
    add_info = input("please input RecruitmentInfo:").strip()
    print('finish')
    sql_add = """
            insert into recruitmentTable(name,info) value(%s,%s)
            """
    name = add_name
    info = add_info
    cursor.execute(sql_add, (name, info))
    db.commit()


def viewtask():
    sql = '''SELECT * FROM taskTable'''
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.commit()


def viewfinancial():
    sql = '''SELECT * FROM financialTable'''
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.commit()


def viewrecruitment():
    sql = '''SELECT * FROM recruitmentTable'''
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.commit()


def deltask():
    del_name = input('please input the task you want to delete:').strip()
    print('finished')
    sql_del = '''DELETE FROM taskTable WHERE name = %s'''
    cursor.execute(sql_del, del_name)


def delfinancial():
    del_name = input('please input the financial request you want to delete:').strip()
    print('finished')
    sql_del = '''DELETE FROM financialTable WHERE name = %s'''
    cursor.execute(sql_del, del_name)


def delrecruitment():
    del_name = input('please input the recruitment you want to delete:').strip()
    print('finished')
    sql_del = '''DELETE FROM recruitmentTable WHERE name = %s'''
    cursor.execute(sql_del, del_name)


def main():
    while True:
        loginuser = login()
        if loginuser == 1:
            display1();
        elif loginuser == 2:
            display2();
        elif loginuser == 3:
            display3();
        elif loginuser == 4:
            display4();
        elif loginuser == 5:
            display5();
        elif loginuser == 6:
            display6();
        elif loginuser == 7:
            display7();
        elif loginuser == 8:
            display8()
        if int(select_input) == 999:
            print("Exit")
            break


if __name__ == '__main__':
    main()


# def display(): #进行登陆后界面的函数定义，方便在下面的选用层级后，返回上一层时，依然可以看到选择大屏。
#     print("\033[34m########################################################################")
#     print("\033[34m\t######### \033[1;32mWelcome to this system!\033[0;34m #########")
#     print("\033[34m\t\t#################################################")
#     print("\n")
#     print("\033[32m\033[1m\t\t\t1\033[33m\033[1m.Customer Service\n")
#     print("\033[32m\033[1m\t\t\t2\033[33m\033[1m.Senior Customer Service\n")
#     print("\033[32m\033[1m\t\t\t3\033[33m\033[1m.Financial Manager\n")
#     print("\033[32m\033[1m\t\t\t4\033[33m\033[1m.Administration Manager\n")
#     print("\033[32m\033[1m\t\t\t4\033[33m\033[1m.Service Manager\n")
#     print("\033[32m\033[1m\t\t\t5\033[33m\033[1m.Production Manager\n")
#     print("\033[32m\033[1m\t\t\t6\033[33m\033[1m.Sub-Team\n")
#     print("\033[32m\033[1m\t\t\t7\033[33m\033[1m.HR\n")
#     print("\n")
#     dict ()
#
# path='C:/Users/hhoba/Desktop/employee_list.txt'
# #定义while层级标记break_tag1 = 0 以及登陆初始提示
# break_tag1 = 0
# while break_tag1 == 0:
#     display()
