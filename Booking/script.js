document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript загружен!');

    const calendarEl = document.getElementById('calendar');
    const slotsList = document.getElementById('slots-list');
    const timeSlotsSection = document.getElementById('time-slots');
    let selectedDate = null;

    if (!calendarEl) {
        console.error('Элемент #calendar не найден!');
        return;
    }

    console.log('Элемент найден, создаём календарь...');

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'ru', // Русский язык
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek'
        },
        dateClick: function(info) {
            selectedDate = info.dateStr;
            console.log('Выбрана дата:', selectedDate);
            fetchTimeSlots(selectedDate);
        },
        events: '/api/slots' // Подключение событий с сервера
    });

    calendar.render();
    console.log('Календарь загружен!');

    function fetchTimeSlots(date) {
        fetch(`/api/slots?date=${date}`)
            .then(response => response.json())
            .then(slots => {
                slotsList.innerHTML = '';
                slots.forEach(slot => {
                    const slotButton = document.createElement('button');
                    slotButton.textContent = `${slot.time} — ${slot.price} BYN`;
                    slotButton.classList.add(slot.is_available ? 'available' : 'booked');
                    slotButton.disabled = !slot.is_available;

                    slotButton.addEventListener('click', () => {
                        if (slot.is_available) {
                            bookSlot(slot.id);
                        }
                    });

                    slotsList.appendChild(slotButton);
                });
                timeSlotsSection.style.display = 'block';
            })
            .catch(error => console.error('Ошибка загрузки слотов:', error));
    }

    function bookSlot(slotId) {
        fetch('/api/slots/book', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ slotId })
        })
        .then(response => response.json())
        .then(data => {
            alert('Успешное бронирование!');
            fetchTimeSlots(selectedDate);
        })
        .catch(error => console.error('Ошибка бронирования:', error));
    }
});
