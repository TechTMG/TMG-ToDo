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


def get_task(task_id):
    conn = get_connecter()
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM todo WHERE id = %s'
            cursor.execute(sql, (task_id))
            result = cursor.fetchone()
    except Exception as e:
        print(e)
        result = "ERROR"
    finally:
        conn.close()
    return result


def post_task(task_json):
    posted = json.loads(task_json)
    title = str(posted['title'])
    context = str(posted['context'])
    limit_date = str(posted['limit_date'])

    conn = get_connecter()
    try:
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


def update_task(task_json):
    posted = json.loads(task_json)
    task_id = int(posted['id'])
    title = str(posted['title'])
    context = str(posted['context'])
    done = int(posted['done'])
    limit_date = str(posted['limit_date'])

    conn = get_connecter()
    try:
        with conn.cursor() as cursor:
            sql = '''UPDATE todo
            SET
                title = %s,
                context = %s,
                done = %s,
                limit_date = %s,
                updated_at = NOW()
            WHERE id = %s'''
            cursor.execute(sql, (title, context, done, limit_date, task_id))
            conn.commit()
            result = "COMPLETE UPDATE"
    except Exception as e:
        print(e)
        result = "ERROR"
    finally:
        conn.close()
    return result


def achieve_task(task_id):
    conn = get_connecter()
    try:
        with conn.cursor() as cursor:
            sql = '''UPDATE todo
            SET
                done = 1,
                updated_at = NOW()
            WHERE id = %s'''
            cursor.execute(sql, (task_id))
            conn.commit()
            result = "COMPLETE ACHIEVE"
    except Exception as e:
        print(e)
        result = "ERROR"
    finally:
        conn.close()
    return result


def cancel_task(task_id):
    conn = get_connecter()
    try:
        with conn.cursor() as cursor:
            sql = '''UPDATE todo
            SET
                done = 2,
                updated_at = NOW()
            WHERE id = %s'''
            cursor.execute(sql, (task_id))
            conn.commit()
            result = "COMPLETE CANCEL"
    except Exception as e:
        print(e)
        result = "ERROR"
    finally:
        conn.close()
    return result
