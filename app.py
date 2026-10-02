from flask import Flask
from dotenv import load_dotenv
import os
import pymysql

# .env 파일의 환경 변수 불러오기
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


# DB 연결 객체 생성
def get_connection():
    if DB_PASSWORD is None:
        raise ValueError('DB_PASSWORD가 세팅 되지 않았습니다.')

    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset='utf8mb4'
    )

app = Flask(__name__)

@app.route('/api/test-db')
def test_db():
    conn = get_connection()
    conn.close()

    return 'DB 연결 성공'

@app.route('/')
def index():
    return "Wedding Invitation Service"

if __name__ == '__main__':
    app.run(debug=True)