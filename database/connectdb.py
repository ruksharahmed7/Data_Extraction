import sqlite3
import traceback


sql = '''
                    CREATE TABLE IF NOT EXISTS project_info (
                        ProjectId TEXT PRIMARY KEY NOT NULL,
                        ProjectName TEXT NOT NULL,
                        Status INTEGER NOT NULL,
                        DPPstatus INTEGER,
                        MMstatus INTEGER,
                        SUMMARYstatus INTEGER
                    )
                '''
def connect():
    conn = sqlite3.connect(r"projectInfo.db")
    connection = conn.cursor()
    print("connected")
    return conn,connection

def create():
    try:
        conn,connection=connect()
        connection.execute(sql)
    except:
        pass

def insert(project_id,project_name):
    conn,connection=connect()
    print(project_id,project_name)
    try:
        connection.execute("INSERT INTO project_info VALUES(?,?,0,0,0,0)",(str(project_id),project_name))
        conn.commit()
        print('successfully inserted')
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        print('faild to insert')

def update_dpp_status(project_id):
    print("updated")


def update_mm_status(project_id):
    print("updated")

def update_summary_status(project_id):
    print("updated")

def fatch(project_id):
    conn,connection=connect()
    try:
        print('fatching')
        connection.execute("Select ProjectName from project_info WHERE ProjectId="+str(project_id))
        project_name=connection.fetchall()
        print(project_name)
        return project_name[0][0]
    except:
        return None



