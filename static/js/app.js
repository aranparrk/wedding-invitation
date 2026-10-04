console.log("app.js 연결 성공");

// ======================================================
// 결혼식 날짜 설정
// ======================================================

const weddingDate = new Date('2026-10-16T13:00:00+09:00');


// ======================================================
// 결혼식 날짜 카운트다운
// ======================================================

const countdownElement = document.getElementById('countdown');
const messageElement = document.getElementById('countdown-message');

const daysElement = document.getElementById('days');
const hoursElement = document.getElementById('hours');
const minutesElement = document.getElementById('minutes');
const secondsElement = document.getElementById('seconds');


function updateCountdown() {
    const now = new Date();

    const diff = weddingDate - now;

    // 결혼식 날짜가 지난 경우
    if (diff <= 0) {
        countdownElement.style.display = 'none';

        messageElement.textContent =
            '함께해 주시고 축하해 주셔서 감사합니다.';

        return;
    }

    const days = Math.floor(
        diff / (1000 * 60 * 60 * 24)
    );

    const hours = Math.floor(
        (diff / (1000 * 60 * 60)) % 24
    );

    const minutes = Math.floor(
        (diff / (1000 * 60)) % 60
    );

    const seconds = Math.floor(
        (diff / 1000) % 60
    );

    daysElement.textContent = days;
    hoursElement.textContent = hours;
    minutesElement.textContent = minutes;
    secondsElement.textContent = seconds;
}


// 페이지가 열리자마자 한 번 실행
updateCountdown();

// 이후 1초마다 실행
setInterval(updateCountdown, 1000);


// ======================================================
// 결혼식 달력
// ======================================================

const calendarTitle = document.getElementById('calendar-title');
const calendarDates = document.getElementById('calendar-dates');

const weddingYear = weddingDate.getFullYear();
const weddingMonth = weddingDate.getMonth();
const weddingDay = weddingDate.getDate();


// 월 이름
const monthNames = [
    'JANUARY',
    'FEBRUARY',
    'MARCH',
    'APRIL',
    'MAY',
    'JUNE',
    'JULY',
    'AUGUST',
    'SEPTEMBER',
    'OCTOBER',
    'NOVEMBER',
    'DECEMBER'
];


// 달력 제목
calendarTitle.textContent =
    `${monthNames[weddingMonth]} ${weddingYear}`;


// 결혼식 달의 1일이 무슨 요일인지 구하기
const firstDayOfWeek = new Date(
    weddingYear,
    weddingMonth,
    1
).getDay();


// 결혼식 달의 마지막 날짜 구하기
const lastDate = new Date(
    weddingYear,
    weddingMonth + 1,
    0
).getDate();


// 현재 날짜
const today = new Date();


// 오늘이 결혼식과 같은 연도 / 월인지 확인
const isSameMonth =
    today.getFullYear() === weddingYear &&
    today.getMonth() === weddingMonth;


// 달력 앞쪽 빈칸 생성
for (let i = 0; i < firstDayOfWeek; i++) {
    const emptyElement = document.createElement('div');

    emptyElement.classList.add('calendar-date', 'empty');

    calendarDates.appendChild(emptyElement);
}


// 1일부터 마지막 날짜까지 생성
for (let day = 1; day <= lastDate; day++) {
    const dateElement = document.createElement('div');

    dateElement.classList.add('calendar-date');


    // 날짜 숫자
    const numberElement = document.createElement('span');

    numberElement.textContent = day;

    dateElement.appendChild(numberElement);


    // 결혼식 날짜
    if (day === weddingDay) {
        dateElement.classList.add('wedding-day');

        const weddingLabel = document.createElement('small');

        weddingLabel.textContent = 'WEDDING';

        dateElement.appendChild(weddingLabel);
    }


    // 현재 날짜
    // 오늘이 결혼식과 같은 연도 / 월일 때만 표시
    if (isSameMonth && day === today.getDate()) {
        dateElement.classList.add('today');

        const todayLabel = document.createElement('small');

        todayLabel.textContent = 'TODAY';

        dateElement.appendChild(todayLabel);
    }


    calendarDates.appendChild(dateElement);
}