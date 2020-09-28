import mmse_dev
import pymysql

db = pymysql.connect("localhost", "root", "root", "mmse", charset='utf8')
cursor = db.cursor()
table = input("please input test item:")

mmse_dev.main()
print('\n')
print('\n')
print('\n')
if table == 'event':
    sql = '''SELECT * FROM eventTable WHERE name = "concert" '''
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print(results)
    db.commit()
elif table == 'task':
    sql = '''SELECT * FROM taskTable WHERE name = "party_subtask" '''
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print(results)
    db.commit()
elif table == 'recruit':
    sql = '''SELECT * FROM recruitmentTable WHERE name = "party_stuff" '''
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print(results)
    db.commit()
elif table == 'financial':
    sql = '''SELECT * FROM financialTable WHERE name = "party_financial" '''
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print(results)
    db.commit()