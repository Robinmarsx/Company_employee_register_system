import pymysql
db = pymysql.connect("localhost", "root", "root", "mmse", charset='utf8')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS userTable")
cursor.execute("DROP TABLE IF EXISTS eventTable")
cursor.execute("DROP TABLE IF EXISTS recruitmentTable")
cursor.execute("DROP TABLE IF EXISTS financialTable")
cursor.execute("DROP TABLE IF EXISTS taskTable")

sql1 = '''CREATE TABLE `eventTable` (
  `name` CHAR(20),
  `info` CHAR(100),
  `scsA_R` CHAR(20),
  `fmInfo` CHAR(20),
  `amA_R` CHAR(20)
);
'''


sql2 = '''CREATE TABLE `recruitmentTable` (
  `name` CHAR(20),
  `info` CHAR(100),
  `hrA_R` CHAR(20)
);
'''

sql3 = '''CREATE TABLE `financialTable` (
  `name` CHAR(20),
  `info` CHAR(100),
  `fmA_R` CHAR(20)
);
'''

sql4 = '''CREATE TABLE `taskTable` (
  `name` CHAR(20),
  `subteam` CHAR(20),
  `info` CHAR(100),
  `subinfo` CHAR(100)
);
'''

sql5 = '''CREATE TABLE `userTable` (
  `type` int,
  `user` CHAR(20),
  `passwd` CHAR(20)
);
'''

sql6 ='''INSERT INTO userTable ( type, user, passwd )
                       VALUES
                       ( 1, 't1', 't1' ),
                       ( 2, 't2', 't2' ),
                       ( 3, 't3', 't3' ),
                       ( 4, 't4', 't4' ),
                       ( 5, 't5', 't5' ),
                       ( 6, 't6', 't6' ),
                       ( 7, 't7', 't7' ),
                       ( 8, 't8', 't8' );
                       
'''
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.execute(sql6)
db.commit()
# 关闭数据库连接
db.close()