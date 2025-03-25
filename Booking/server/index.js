const express = require('express');
const app = express();
const { Pool } = require('pg');
const db = new Pool({
    user: 'your_user',
    host: 'localhost',
    database: 'vr_club',
    password: 'your_password',
    port: 5432,
});

// Получение доступных слотов для выбранной даты
app.get('/api/slots', async (req, res) => {
    const { date } = req.query;
    try {
        const result = await db.query('SELECT * FROM time_slots WHERE date = $1', [date]);
        res.json(result.rows);
    } catch (err) {
        console.error(err);
        res.status(500).send('Ошибка сервера');
    }
});

// Бронирование слота
app.post('/api/slots/book', async (req, res) => {
    const { slotId } = req.body;
    try {
        const result = await db.query(
            'UPDATE time_slots SET is_available = FALSE WHERE id = $1 RETURNING *',
            [slotId]
        );
        res.json(result.rows[0]);
    } catch (err) {
        console.error(err);
        res.status(500).send('Ошибка сервера');
    }
});

app.listen(3000, () => console.log('Сервер запущен на порту 3000'));
