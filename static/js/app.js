console.log("app.js 연결 성공");

// ======================================================
// 결혼식 날짜 카운트다운
// ======================================================

// 결혼식 날짜 설정
const weddingDate = new Date('2027-05-15T13:00:00');

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

