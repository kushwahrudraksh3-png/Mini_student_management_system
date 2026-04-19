import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root@12345",
            database="student_db"
        )
        print("🔥 Database Connected Successfully!")
        return conn

    except Exception as e:
        print("❌ Error:", e)
        return None