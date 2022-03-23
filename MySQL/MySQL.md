# SQL 문법 

## CREATE

### 데이터베이스 생성

> **CREATE DATABASE** 데이터베이스이름;

### 데이터베이스 선택

> **USE** 데이터베이스이름;

### 테이블 생성

> **CREATE TABLE** 테이블 이름
>
> (
>
> ​	필드이름1 필드타입1 제약조건1,
>
> ​	필드이름2 필트타입2 제약조건2,
>
> );

## ALTER

### 데이터베이스 수정

데이터베이스의 전체적인 특성을 수정. `db.opt` 파일에 저장되어 있음.

> **ALTER** **DATABASE** 데이터베이스이름 **CHARACTER SET**=문자집합이름;

CHARACTER SET 인코딩 관련 문자셋인듯 하다..? utf8, euckr

> **ALTER DATAVASE** 데이터베이스이름 **COLLATE**=콜레이션이름;

콜레이션: 데이터베이스에서 검색이나 정렬과 같은 작업을 할 떄 사용하는 비교는 위한 규칙의 집합..?

### 테이블 수정

#### 새로운 필드 추가

> **ALTER TABLE** 테이블이름 **ADD** 필드이름 필드타입;

#### 기존 필드의 삭제

> **ALTER TABLE** 테이블이름 **DROP** 필드이름;

#### 필드 타입 변경

> **ALTER TABLE** 테이블이름 **MODIFY COLUMN** 필드이름 필드타입;

## DROP

### 데이터베이스 삭제

> **DROP DATABASE** 데이터베이스이름;

### 테이블 삭제

> **DROP TABLE** 테이블이름;

### 테이블 데이터 삭제

> **TRUNCATE TABLE** 테이블이름;

데이터만 삭제되고 테이블은 여전히 남아있게 됨.

## INSERT

### 테이블에 레코드 추가

> **INSERT INTO** 테이블이름(필드이름1, 필드이름2, 필드이름3, ...) **VALUES** (데이터 값1, 데이터값2, 데이터값3);

`NULL`, `DEFAULT`, `AUTO_INCREMENT` 가 설정되어있는 필드는 생략할 수 있다.

## UPDATE

### 레코드 수정

> **UPDATE** 테이블이름 **SET** 필드이름1=데이터값1, 필드이름2=데이터값2, ... **WHERE** 필드이름=데이터값;

## DELETE

### 레코드 삭제

> **DELETE FROM** 테이블이름 **WHERE** 필드이름=데이터값;

WHERE 문을 삭제하면 테이블의 모든 데이터가 삭제된다. -> TRUNCATE TABLE 테이블이름 과 같은 명령이 됨.

## SELECT

### 특정 조건의 레코드 선택

> **SELECT** 필드이름 **FROM** 테이블이름 **WHERE** 필드이름=데이터값;

필드이름 대신 `*`를 넣어주면 모든 필드를 선택할 수 있다.

WHERE 절에 찾고 싶은 레코드의 조건을 작성해준다.

### 중복되는 값 제거

> **SELECT DISTINCT** 필드이름 **FROM** 테이블이름;

레코드에 중복되는 값이 있다면 해당 레코드를 제외시키고 하나만 선택한다.

### 선택한 레코드 정렬

> **SELECT** 필드이름 **FROM** 테이블이름 **ORDER BY** 필드이름;

ORDER BY 를 이용하여 해당 레코드를 오름차순(`DESC`) 또는 내림차순(`ASC`) 으로 정렬하여 보여준다.

내림차순로 정렬하고 싶은 경우, `ASC`를 반드시 넣어야 한다. (default가 오름차순)

### 별칭(alias) 사용

> **SELECT** 필드이름 **AS** 별칭 **FROM** 테이블이름;

필드이름을 다른 이름으로 지정하고 싶을 때 `AS` 문을 사용한다.

# 다중 테이블 연산

## JOIN

### INNER JOIN

> **SELECT * FROM** 첫번째 테이블이름 **INNER JOIN** 두번째테이블이름 **ON** 첫번째테이블.필드이름 = 두번째테이블.필드이름

### LEFT JOIN

> **SELECT** * **FROM** 첫번째테이블이름 **LEFT JOIN** 두번째테이블이름 **ON** 첫번째테이블.필드이름 = 두번째테이블.필드이름

### RIGHT JOIN

> **SELECT * FROM** 첫번째 테이블이름 **RIGHT JOIN** 두번째테이블이름 **ON** 첫번째테이블.필드이름 = 두번째테이블.필드이름

## UNION

### UNION

> **SELECT** 필드이름 **FROM** 첫번째테이블이름 **UNION** **SELECT** 필드이름 **FROM** 두번째테이블이름;

각 필드에서 중복되는 값을 보여준다.

### UNION ALL

> **SELECT** 필드이름 **FROM** 첫번째테이블이름 **UNION ALL** **SELECT** 필드이름 **FROM** 두번째테이블이름;

중복된 레코드를 포함한 모든 레코드를 보여준다.

## 서브쿼리

다른 쿼리 내부에 포함되어 있는 SELECT 문을 의미한다. 반드시 `()`로 감싸져 있어야 한다.

> **SELECT** 필드이름 **FROM** 첫번째테이블이름 **WHERE** 필드이름 **IN** (
>
> ​	**SELECT** 필드이름 **FROM** 두번째테이블이름 **WHERE** 조건
>
> )

WHERE 문에 새로운 쿼리를 작성하여 해당 조건을 만족할 수 있는 레코드를 불러온다.



```mysql
# 데이터베이스 생성 및 선택
CREATE DATABASE School;
USE School;

# 테이블 생성
CREATE TABLE Teacher(
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Name Varchar(30), 
  Age INT, 
  Address VARCHAR(20)
);

CREATE TABLE Student(
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Name Varchar(30), 
  StudentID INT
);

CREATE TABLE CLASS(
	ID INT PRIMARY KEY AUTO_INCREMENT,
  Subject Varchar(20),
  StartDate DATE
);

INSERT INTO Teacher(ID, Name, Age, Address) VALUES (1, 'heewon', 25, 'Jeju');

INSERT INTO Student(ID, Name StudentID) VALUES (1, 'lea', '1234567');
```

