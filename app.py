from flask import Flask, request, jsonify
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


# ====================================================
# 방명록 (guestbook)
# ====================================================

# 방명록 생성
@app.route('/api/guestbook', methods=['POST'])
def create_guestbook():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            'message': '요청 데이터가 없습니다.'
        }), 400

    if 'writer' not in data:
        return jsonify({
            'message': 'writer가 존재하지 않습니다.'
        }), 400

    if 'contents' not in data:
        return jsonify({
            'message': 'contents가 존재하지 않습니다.'
        }), 400

    writer = data.get('writer')
    contents = data.get('contents')

    if not isinstance(writer, str) or not isinstance(contents, str):
        return jsonify({
            'message': 'writer와 contents는 문자열이어야 합니다.'
        }), 400

    if not writer.strip() or not contents.strip():
        return jsonify({
            'message': '작성자 또는 내용이 비었습니다.'
        }), 400

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            '''
                INSERT INTO guestbook (writer, contents)
                VALUES (%s, %s)
            ''',
            (writer, contents)
        )

        conn.commit()

        return jsonify({
            'message': '방명록이 등록되었습니다.'
        }), 201

    except pymysql.MySQLError as e:
        if conn is not None:
            conn.rollback()

        print(e)

        return jsonify({
            'message': 'create_guestbook() DB 처리 실패'
        }), 500

    finally:
        if cur is not None:
            cur.close()

        if conn is not None:
            conn.close()


# 방명록 조회
@app.route('/api/guestbook', methods=['GET'])
def get_guestbook():
    conn = get_connection()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cur.execute(
            '''
                SELECT id, writer, contents, reg_date
                FROM guestbook
            '''
        )

        guestbook = cur.fetchall()

        return jsonify({
            'guestbook': guestbook
        }), 200

    except pymysql.MySQLError as e:
        print(e)

        return jsonify({
            'message': 'get_guestbook() DB 처리 실패'
        }), 500

    finally:
        if cur is not None:
            cur.close()

        if conn is not None:
            conn.close()


# ====================================================
# 참석여부 (attendance)
# ====================================================

# 참석여부 생성
@app.route('/api/attendance', methods=['POST'])
def create_attendance():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            'message': '요청 데이터가 없습니다.'
        }), 400

    if 'name' not in data:
        return jsonify({
            'message': 'name이 존재하지 않습니다.'
        }), 400

    if 'attendance_status' not in data:
        return jsonify({
            'message': 'attendance_status가 존재하지 않습니다.'
        }), 400

    name = data.get('name')
    attendance_status = data.get('attendance_status')

    if not isinstance(name, str):
        return jsonify({
            'message': 'name은 문자열이어야 합니다.'
        }), 400

    if not name.strip():
        return jsonify({
            'message': '이름이 비었습니다.'
        }), 400

    if type(attendance_status) is not bool:
        return jsonify({
            'message': 'attendance_status는 boolean이어야 합니다.'
        }), 400

    # 참석하는 경우
    if attendance_status:
        if 'guest_count' not in data:
            return jsonify({
                'message': 'guest_count가 존재하지 않습니다.'
            }), 400

        if 'meal_status' not in data:
            return jsonify({
                'message': 'meal_status가 존재하지 않습니다.'
            }), 400

        guest_count = data.get('guest_count')
        meal_status = data.get('meal_status')

        if type(guest_count) is not int:
            return jsonify({
                'message': 'guest_count는 정수여야 합니다.'
            }), 400

        if guest_count < 1:
            return jsonify({
                'message': '참석 인원은 1명 이상이어야 합니다.'
            }), 400

        if type(meal_status) is not bool:
            return jsonify({
                'message': 'meal_status는 boolean이어야 합니다.'
            }), 400

    # 참석하지 않는 경우
    else:
        guest_count = 0
        meal_status = False

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            '''
                INSERT INTO attendance
                (name, attendance_status, guest_count, meal_status)
                VALUES (%s, %s, %s, %s)
            ''',
            (name, attendance_status, guest_count, meal_status)
        )

        conn.commit()

        return jsonify({
            'message': '참석여부가 등록되었습니다.'
        }), 201

    except pymysql.MySQLError as e:
        if conn is not None:
            conn.rollback()

        print(e)

        return jsonify({
            'message': 'create_attendance() DB 처리 실패'
        }), 500

    finally:
        if cur is not None:
            cur.close()

        if conn is not None:
            conn.close()


# 참석여부 조회
@app.route('/api/attendance', methods=['GET'])
def get_attendance():
    conn = get_connection()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cur.execute(
            '''
                SELECT id, name, attendance_status,
                       guest_count, meal_status, reg_date
                FROM attendance
            '''
        )

        attendance = cur.fetchall()

        return jsonify({
            'attendance': attendance
        }), 200

    except pymysql.MySQLError as e:
        print(e)

        return jsonify({
            'message': 'get_attendance() DB 처리 실패'
        }), 500

    finally:
        if cur is not None:
            cur.close()

        if conn is not None:
            conn.close()


@app.route('/api/test-db')
def test_db():
    conn = get_connection()
    conn.close()

    return 'DB 연결 성공'


@app.route('/')
def index():
    return 'Wedding Invitation Service'


if __name__ == '__main__':
    app.run(debug=True)