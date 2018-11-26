import psycopg2

class DatabaseConnection():
    def __init__(self,database,usr,pwd):
        self.database=database
        self.usr=usr
        self.pwd=pwd

    def __con__(self):
        con = psycopg2.connect(
            host='localhost',
            database=self.database,
            user=self.usr,
            password=self.pwd
        )
        con.commit()
        return con

    def get_data(self,sql_text):
        con=self.__con__()
        cursor=con.cursor()
        if sql_text.split(' ')[0].lower()=='select':
            cursor.execute(sql_text)
            return cursor.fetchall()
        else:
            print('Only "Select" is accepted.')
