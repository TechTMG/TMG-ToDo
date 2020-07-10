import pymysql.cursors

def connecter():
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        db = 'test-schema',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
        )
    return conn

def get_SELECT():
    conn = connecter()
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM todo' 
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        conn.close()
    return result

def get_task(n):
    conn = connecter()
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM todo WHERE id = %s'
            cursor.execute(sql, (n))
            result = cursor.fetchone()
    finally:
        conn.close()
    return result
