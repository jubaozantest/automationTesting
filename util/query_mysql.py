'''连接mysql，查询表数据，用于接口/UI测试校验'''
import pymysql
from sshtunnel import SSHTunnelForwarder

class ExecuteSQL(object):
    def __init__(self, sql):
        #self.dbname = dbname
        self.sql = sql

    def execute_sql(self):
        results = ''
        with SSHTunnelForwarder(
                ('119.23.12.157', 22),  # 跳板机（堡垒机）B配置
                ssh_password='j70ubz##$y*movsr4W(1fntqlEJBZ70#',
                ssh_username='root',
                remote_bind_address=('10.0.103.69', 3306)) as server:  # 数据库存放服务器C配置
            # 打开数据库连接
            db_connect = pymysql.connect(host='127.0.0.1',
                                         port=server.local_bind_port,
                                         user='root',
                                         passwd='ilszRSaCXojd',
                                         )  # 需要连接的数据库的名称
            # 使用cursor()方法获取操作游标
            cursor = db_connect.cursor()
            try:
                # 执行SQL语句
                cursor.execute(self.sql)
                # 获取所有记录列表
                results = cursor.fetchall()
            except Exception as data:
                print('Error: 执行查询失败，%s' % data)
            db_connect.close()
            return results
def execute_sql(sql):
    #print('sql',sql)
    connect = ExecuteSQL(sql)
    res = connect.execute_sql()
    return res[0][0]
if __name__ == '__main__':
    #sql = "select mobile from fx_agent where agentid='14494534'"
    #sql = "select money from fxydym.fx_angent_extend where agentid=14507854"
    sql="SELECT mobile FROM fxydym.fx_agent WHERE sjid=1122 AND mobile>1 GROUP BY mobile DESC LIMIT 1"
    print(execute_sql(sql))



