import sqlite3
import os

dirname = os.path.dirname(__file__)
database_path = os.path.join(dirname, '../model/registeredUser.db')
table_name = 'user'
password_column = 'password'


def login_request(user_name, password):
    conn = sqlite3.connect(database_path)
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT "
                           "CASE WHEN " + password_column + " = ? "
                                                            "THEN 'Yes' ELSE 'No' END AS PasswordPresent "
                                                            "FROM " + table_name + " WHERE username= ?;",
                           (password, user_name))
            result = cursor.fetchone()
            if result is not None and result[0] == 'Yes':
                return True
        finally:
            if cursor is not None:
                cursor.close()
    conn.close()


def register_request(username, password, student_class, gender):
    conn = sqlite3.connect(database_path)
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute("Insert Into " + table_name + " Values(?,?,?,?)",
                           (username, password, student_class, gender))
        except sqlite3.IntegrityError as e:
            return False, str(e)
        finally:
            if cursor is not None:
                cursor.close()
    conn.close()
    return True, None
