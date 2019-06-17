'''连接mysql，查询表数据，用于接口/UI测试校验'''
import pymysql
from sshtunnel import SSHTunnelForwarder
from lib.read_config import read_basic_config




class ExecuteSQL(object):
    def __init__(self, sql):
        # self.dbname = dbname
        self.sql = sql
        self.ssh_host = read_basic_config.cfg['database']['ssh_host']
        self.ssh_password = read_basic_config.cfg['database']['ssh_password']
        self.db_host = read_basic_config.cfg['database']['db_host']
        self.db_password = read_basic_config.cfg['database']['db_password']

    def execute_sql(self):
        results = ''
        with SSHTunnelForwarder(
                (self.ssh_host, 22),  # 跳板机（堡垒机）B配置
                ssh_password=self.ssh_password,
                ssh_username='root',
                remote_bind_address=(self.db_host, 3306)) as server:  # 数据库存放服务器C配置
            # 打开数据库连接
            db_connect = pymysql.connect(host='127.0.0.1',
                                         port=server.local_bind_port,
                                         user='root',
                                         passwd=self.db_password,
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
    connect = ExecuteSQL(sql)
    res = connect.execute_sql()
    return res
if __name__ == '__main__':

    sql="SELECT * FROM fxydym.fx_agent  LIMIT 1"
    print(execute_sql(sql))
