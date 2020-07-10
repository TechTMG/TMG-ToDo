import pymysql.cursors

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    db = 'test-schema',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
    )

def get_SELECT():
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM todo' 
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        conn.close()
    
    return result
