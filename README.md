# 프로젝트 설정 및 실행 가이드

## 1. MySQL 설정
Python 코드에 MySQL 아이디 이름과 비밀번호를 알맞게 설정해주세요.

## 2. 데이터베이스 생성
MySQL에서 다음 명령어로 programming 데이터베이스를 생성하세요:
```sql
CREATE DATABASE programming;
```

## 3. 테이블 생성
MySQL 에서 다음 명령어로 crud_information 테이블을 생성해주세요
```sql
CREATE TABLE crud_information (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    time DATETIME NULL
);
```

## 4. 파이써 코드를 실행해주시면 됩니다.
