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
                                         charset='utf8')  # 需要连接的数据库的名称
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

def test(res):
    for data in res:
        pid=data[4]
        if not pid==0:
            sub_text=data[1]
            try:
                sql='SELECT * from menu.sys_resource_jiagedian where id={}'.format(pid)
                p_res=execute_sql(sql)[0]
                p_text=p_res[1]
                print('{0}的上级名称是{1}'.format(sub_text,p_text))
                # '''查询生产有几个'''
                sql_sub='SELECT * from menu.sys_resource_c3tech where text="{}"'.format(sub_text)
                sub_res=execute_sql(sql_sub)
                #print('{0}在生产的sql{1}'.format(sub_text,sub_res))
                if len(sub_res)>1:
                    print('c3tech中text为有{}条一样的数据'.format(len(sub_res)))
                else:
                    p_id_sql='SELECT * from menu.sys_resource_c3tech where text="{}"'.format(p_text)
                    p_id_value=execute_sql(p_id_sql)[0][0]
                    print('把{0}的pid改成{1}'.format(sub_text,p_id_value))
                    # update_sql='UPDATE menu.sys_resource_c3tech set pid={} where text="{}"'.format(p_id_value,sub_text)
                    # execute_sql(update_sql)
            except Exception as e:
                print(e)
if __name__ == '__main__':

    sql='SELECT * from menu.sys_resource_jiagedian '
    res=execute_sql(sql)
    test(res)



