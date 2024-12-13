## python 코드에 mysql 아이디 이름과 비밀번호를 알맞게 설정해주세요.
## 설정 하셨다면 mysql 에서 programming 이라는 데이터 베이스를 생성하고 
## 테이블 생성하는 명렁어를 복붙하여 사용해주신 뒤에 프로그램을 실행해 주세요.

CREATE TABLE crud_information (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    time DATETIME NULL
);
