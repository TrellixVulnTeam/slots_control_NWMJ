import psycopg2

class slots_db():
    def __init__(self, database, usr, pwd):
        self.database = database
        self.usr = usr
        self.pwd = pwd

        self.con = psycopg2.connect(
            host='localhost',
            database=self.database,
            user=self.usr,
            password=self.pwd
        )
        self.con.commit()
        self.cur = self.con.cursor()
        # return cur

    def get_svcs_list(self, today):
        sql_text = f'''select distinct svc,trade from services
                        where
                            trade_lane in ('IAN','IAP','IAK','IAA')
                        and 
                            expire_date >= '{today}'
                        order by 
                            svc; '''

        svcs = self.get_data( sql_text )
        svcs_list = [x[0] for x in svcs]
        return svcs_list

    def get_data(self, sql_text):
        if sql_text.split( ' ' )[0].lower() == 'select':
            try:
                self.cur.execute( sql_text )
                return self.cur.fetchall()
            except psycopg2.ProgrammingError as E:
                print( E )
        else:
            print( 'Only "Select" is accepted.' )