import pymysql.cursors
import json


def get_connecter():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        db='test-schema',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn


def get_alltask():
    conn = get_connecter()
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM todo'
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        result = "ERROR"
    finally:
        conn.close()
    return result


def get_task(n):
    conn = get_connecter()
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM todo WHERE id = %s'
            cursor.execute(sql, (n))
            result = cursor.fetchone()
    except Exception as e:
        print(e)
        result = "ERROR"
    finally:
        conn.close()
    return result


def post_task(n):
    conn = get_connecter()
    try:
        posted = json.loads(n)
        title = str(posted['title'])
        context = str(posted['context'])
        limit_date = str(posted['limit_date'])
        with conn.cursor() as cursor:
            sql = '''INSERT INTO
             todo (title, context, done, created_at, limit_date, updated_at)
             VALUES (%s, %s, 0, NOW(), %s, NOW())'''
            cursor.execute(sql, (title, context, limit_date))
            conn.commit()
            result = "COMPLETE INSERT"
    except Exception as e:
        print(e)
        result = "ERROR"
    finally:
        conn.close()
    return result
