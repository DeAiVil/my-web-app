from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Настройки базы данных
DB_HOST = 'localhost'
DB_NAME = 'your_db_name'
DB_USER = 'your_db_user'
DB_PASS = 'your_db_password'

# Подключение к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

# Получение доступных слотов для выбранной даты
@app.route('/api/slots', methods=['GET'])
def get_slots():
    date = request.args.get('date')
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM time_slots WHERE date = %s;', (date,))
    slots = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(slots)

# Бронирование слота
@app.route('/api/slots/book', methods=['POST'])
def book_slot():
    data = request.get_json()
    slot_id = data['slotId']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE time_slots SET is_available = FALSE WHERE id = %s RETURNING *;', (slot_id,))
    slot = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Slot booked successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
