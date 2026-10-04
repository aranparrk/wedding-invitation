CREATE DATABASE IF NOT EXISTS wedding_invitation;
USE wedding_invitation;

-- 이모지 저장을 위한 문자셋 변경
ALTER DATABASE wedding_invitation
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

-- 방명록
CREATE TABLE IF NOT EXISTS guestbook (
    id INT PRIMARY KEY AUTO_INCREMENT,                        -- 고유번호
    writer VARCHAR(50) NOT NULL,                              -- 작성자
    contents TEXT NOT NULL,                                   -- 내용
    reg_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP      -- 작성일자
);

-- 참석 여부
CREATE TABLE IF NOT EXISTS attendance (
    id INT PRIMARY KEY AUTO_INCREMENT,                        -- 고유번호
    name VARCHAR(50) NOT NULL,                                -- 이름
    attendance_status BOOLEAN NOT NULL,                       -- 참석여부
    guest_count INT NOT NULL,                                 -- 참석인원
    meal_status BOOLEAN NOT NULL,                             -- 식사여부
    reg_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP      -- 작성일자
);

-- 테이블 생성 조회
SHOW TABLES;

-- 테이블 구조 조회
DESC guestbook;
DESC attendance;

select * from guestbook;

select * from attendance;