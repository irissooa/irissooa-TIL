

# DB

[DB!! 요약보기](https://github.com/wally-wally/TIL/blob/master/05_DB/%5BSSAFY%5DDB_%231.md#11-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4db)

> django database
>
> orm : 실제로 어떤 sql코드가 발생하는지?
>
> 

## Database

> 관계형 데이터베이스 관리 시스템
>
> 스키마(schema)
>
> 데이터베이스 구조와 제약 조건(자료의 구조, 표현방법, 관계)에 관련한 전반적인 명세를 기술한 것

- 체계화된 데이터의 모임
- **몇 개의 자료 파일을 조직적으로 통합**하여 **자료 항목의 중복**을 없애고 **자료를 구조화**하여 기억시켜 놓은 자료의 집합체
- RDBMS(관계형 데이터베이스 관리 시스템) : 관계형 모델을 기반으로하는 데이터베이스 관리시스템
  - 종류 : MySQL, SQLite, PostgreSQL, ORACLE, MS SQL
  - 모든 데이터를 2차원 테이블로 표현
  - 테이블은 row(record, tuple)과 column(field, item)으로 이루어진 기본 데이터 저장 단위
  - 상호 관련성을 가진 테이블의 집합
  - 만들거나 이용하기도 비교적 쉽고, 확장이 매우 용이하다.
- 데이터베이스의 이점
  - 데이터 중복 최소화
  - 데이터 무결성 : 정확한 정보를 보장
  - 데이터 일관성
  - 데이터 독립성 : 물리적 독립성과 논리적 독립성
  - 데이터 표준화
  - 데이터 보안 유지

![image-20200922212617089](0922_Django_Model_Relationship,SQL(ORM)_comment_댓글.assets/image-20200922212617089.png)

## 1. SQL

> SQL는 관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
>
> **sqlite3**
>
> - `.` : sqlite3 프로그램의 기능을 실행하는 것
> - `;` : 세미콜론 까지가 하나의 명령(Query)으로 간주
> - SQL 문법은 소문자로 작성해도 된다. (단, 대문자를 권장)
> - 하나의 DB에는 여러 개의 table이 존재한다.

#### (1) SQL 이란?

- 관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
- RDBMS에서 자료의 검색과 관리 데이터베이스 스키마 생성과 수정, 데이터베이스 객체 접근 조정 관리를 위해 고안되었다.



#### (2) SQL 종류

| 언어 | 개념                                       | 예시                                           |
| ---- | ------------------------------------------ | ---------------------------------------------- |
| DDL  | 데이터를 정의하기 위한 언어                | CREATE, DROP, ALTER                            |
| DML  | CRUD와 관련된 언어(저장, 수정, 삭제, 조회) | **INSERT(C), SELECT(R), UPDATE(U), DELETE(D)** |
| DCL  | DB 사용자의 권한 제어를 위해 사용되는 언어 | GRANT, REVOKE, COMMIT, ROLLBAK                 |

```sh
$ sqlite3 tutorial.sqlite3
SQLite version 3.33.0 2020-08-14 13:23:32
Enter ".help" for usage hints. 
sqlite> .databases
main: C:\Users\박수아\Desktop\ssafy\DB\00_sql\tutorial.sqlite3
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT * FROM examples;
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  -------------
1   길동          홍          600  충청도      010-2424-1232
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> .tables
classmates  examples
sqlite> DROP TABLE classmates;
sqlite> CREATE TABLE classmates (
   ...> name TEXT,
   ...> age INT,
   ...> adress TEXT
   ...> );
sqlite> INSERT INTO classmates VALUES ('홍길동', 30, '서울'), ('김철수', 23, '대
전'), ('박나래', 23, '광주'), ('이요셉', 33, '구미');
```

`sqlite> SELECT * FROM examples;`examples테이블의 모든 데이터를 가져오세요!

![image-20200922111945086](0922_Django_Model_Relationship,SQL(ORM)_comment_댓글.assets/image-20200922111945086.png)

관례 : 이름을 대문자로 씀!





------------------



# SQL과 django ORM

## 기본 준비 사항

```bash
# 폴더구조

TIL
	...
	0X_db
		00_sql # only SQL
			hellodb.csv
			tutorial.sqlite3
			users.csv
		01_sql_orm # SQL + ORM
			...
			users.csv # 해당 디렉토리로 다운로드
```

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
    $ python manage.py sqlmigrate users 0001
    ```

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ ls
    db.sqlite3 manage.py ...
    $ sqlite3 db.sqlite3
    ```

  * csv 파일 data 로드

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```

* 확인

  * sqlite3에서 스키마 확인

    ```sqlite
    sqlite > .schema users_user
    CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
    ```

#### Database 생성

#### sqlite3

```sql
sqlite3 tutorial.sqlite3 -- tutorial.sqlite3 DB 파일 생성 및 조회
.databases -- database 생성
.mode csv -- csv 모드로 변경
.import hellodb.csv examples -- hellodb.csv 파일을 이용한 examples 라는 테이블 생성
```

#### 테이블 전체 조회

```sql
SELECT * FROM examples; -- 테이블 전체 조회
1,"길동","홍",600,"충청도",010-2424-1232
```

#### 출력 형태 변경

```sql
.headers on
.mode column
SELECT * FROM examples;
id          first_name  last_name   age         country     phone
----------  ----------  ----------  ----------  ----------  -------------
1           길동          홍           600         충청도       010-2424-1232
```

---

### SQL 기본

```sql
-- 테이블 생성
CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT Null
);

-- 테이블 삭제
DROP TABLE classmates;

-- 테이블 명 변경
ALTER TABLE classmates RENAME TO news;

-- 컬럼 추가
ALTER TABLE classmates ADD COLUMN created_at TEXT NOT NULL DEFAULT 1;

-- 데이터 생성
INSERT INTO classmates VALUES ('홍길동', 23, '유성구');


-- 데이터 조회

-- 모든 데이터
SELECT * FROM classmates;

-- 특정 컬럼만
SELECT name, age FROM classmates;

-- 개수 제한
SELECT name, age FROM classmates LIMIT 10;

-- 특정 위치에서부터 가져오기
SELECT name, age FROM classmates LIMIT 10 OFFSET 2;

-- 조건을 통해 가져오기
SELECT rowid, name FROM classmates WHERE address='유성구';

-- 중복 없이 가져오기
SELECT DISTINCT age FROM clasmates;

-- 데이터 삭제
DELETE FROM classmates WHERE rowid=4;

-- 데이터 수정
UPDATE classmates SET name='홍길동', address='제주' WHERE rowid=4;


-- WHERE 심화
-- WHERE 조건
SELECT * FROM users WHERE age>=30;
SELECT age, last_name FROM users WHERE age>=30 and last_name='김';

-- 갯수 세기
SELECT COUNT(*) FROM users;

-- 평균 구하기
SELECT AVG(age) FROM users WHERE age>=30;

-- 최소, 최대 : MIN, MAX

-- 와일드카드 LIKE
SELECT * FROM users WHERE age LIKE '2_';
SELECT * FROM users WHERE phone LIKE '02-%';

-- 정렬
SELECT * FROM users ORDER BY age ASC LIMIT 10;
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;

-- GROUP BY
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
```







## 문제

> 아래의 문제들을 보면서 서로 대응되는 ORM문과 SQL문을 작성하시오.
>
> **vscode 터미널을 좌/우로 나누어 진행하시오. (sqlite / shell_plus)**

`.headers on` 을 켜고 작성해주세요.



### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   User.objects.all()
   ```

      ```sql
   -- sql
   SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(
      ...: first_name='길동',
      ...: last_name='홍',
      ...: age=100,
      ...: country='제주도',
      ...: phone='1234',
      ...: balance=10000,
      ...: )
   ```

   ```sql
   -- sql
   --모든칼럼 다 쓸때
   INSERT INTO users_user VALUES (102, '길동', '홍', 100, '제주도', '010-1234-4567', 100000);
   --아이디빼고 다른 컬럼을 명시해주게 되면, 그것만 적으면 됨
   INSERT INTO "users_user" ("first_name", "last_name", "age", "country", "phone", "balance")
   VALUES ('길동', '홍', 100, '제주도', '1234', 10000);
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `101` 번 id의 전체 레코드 조회

   ```python
   # orm
   User.objects.get(pk=101)
   ```

   ```sql
   -- sql
   SELECT * FROM users_user WHERE id=101;
   ```

4. 해당 user 레코드 수정

   - ORM: `101` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `101` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   user.last_name
   Out[5]: '홍'
   
   In [6]: user.last_name = '김'
   
   In [7]: user.save() #save()했을 떄 한번만 수정됨
   UPDATE "users_user"
      SET "first_name" = '길동',
          "last_name" = '김',
          "age" = 100,
          "country" = '제주도',
          "phone" = '1234',
          "balance" = 10000
    WHERE "users_user"."id" = 101
   ```

      ```sql
   -- sql
   sqlite> INSERT INTO users_user VALUES (102, 
   '길동', '홍', 100, '제주도', '010-1234-4567', 100000);
   sqlite> UPDATE users_user SET last_name=' ' 
        WHERE id=101;
   sqlite> SELECT * FROM users_user WHERE id=0 
   1;
   id,first_name,last_name,age,country,phone,balance
   101,"길동","홍",100,"제주도",1234,10000     
   sqlite>
      ```

5. 해당 user 레코드 삭제

   - ORM: `101` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 (ORM에서 삭제가 되었기 때문에 아무런 응답이 없음)

   ```python
   # orm
    user = User.objects.get(pk=101)     
   SELECT "users_user"."id",
          "users_user"."first_name",
          "users_user"."last_name",
          "users_user"."age",
          "users_user"."country",
          "users_user"."phone",
          "users_user"."balance"
     FROM "users_user"
    WHERE "users_user"."id" = 101
    LIMIT 21
   
   Execution time: 0.001000s [Database: default]
   
   In [9]: user.delete()
   DELETE
     FROM "users_user"
    WHERE "users_user"."id" IN (101)
   
   Execution time: 0.099942s [Database: default]
   Out[9]: (1, {'users.User': 1})
   ```

   ```sql
   -- sql
   DELETE FROM users_user WHERE id=101
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
    len(User.objects.all())
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user;
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   User.objects.filter(age=30).values('first_name')
   ```

      ```sql
   -- sql
    SELECT first_name FROM users_user WHERE age=30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   > | 키워드           | 설명                                  | 사용예시                                                     |
   > | ---------------- | ------------------------------------- | ------------------------------------------------------------ |
   > | `__lt` /` __gt`  | 보다 작다 / 보다 크다                 | id가 1보다 큰 자료 검색<br />`Department.objects.filter(id__gt=1)` |
   > | `__lte`/ `__gte` | 같거나 보다 작다/ 같거나 보다 크다    | x                                                            |
   > | `__in`           | 주어진 리스트 안에 존재하는 자료 검색 | id가 2,3,5,인 자료 검색<br />`Department.objects.filtr(id__in=[2,3,5])` |

   ```python
   # orm
   User.objects.filter(age__gte=30).count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age>=30;
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   User.objects.filter(age__lte=20).count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age<=20;
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   User.objects.filter(age=30, last_name='김').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age=30 AND last_name='김';
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   from django.db.models import Q
   User.objects.filter(Q(age=30)|Q(last_name='김')).count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age=30 OR last_name='김';
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   User.objects.filter(phone__startswith='02-').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   USer.pbjects.filter(country='강원도', last_name='황').values('first_name')
   ```
   
   ```sql
   -- sql
      SELECT first_name FROM users_user WHERE country='강원도' AND last_name='황';
   ```
   
   



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm #내림차순 정렬하고 싶다면 앞에 '-'붙이면 됨
   User.objects.order_by('-age')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   User.objects.order_by('balance')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY balance ASC LIMIT 10;
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

   ```python
   # orm
   User.objects.order_by('balance','-age')[:10]
   ```
   
   ```sql
    -- sql
      SELECT * FROM users_user ORDER BY balance ASC, age DESC LIMIT 10;
   ```
   
   
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   User.objects.order_by('-last_name','-first_name')[4]
   ```

   ```sql
   -- sql
      SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
   ```

   



---



### 4. 표현식

> ORM: `aggregate` 사용
>
> https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregation
>
> - '종합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용

1. 전체 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   User.objects.aggregate(AVG('age'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user;
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   User.objects.filter(last_name='김').aggregate(AVG('age'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user WHERE last_name='김';
      ```

   

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   User.objects.filter(country='강원도').aggregate(AVG('balance'))
   ```

   ```sql
   -- sql
   SELECT AVG(balance) FROM users_user WHERE country='강원도';
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   from django.db.models import Max
   User.objects.aggregate(Max('balance'))
   #aggregate말고 다르게 적는다면
   user = USER.objects.order_by('-balance').first() #or [0]
   ```

      ```sql
   -- sql
   SELECT MAX(balance) FROM users_user;
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   from django.db.models import Sum
   User.objects.aggregate(Sum('balance'))
   ```

      ```sql
   -- sql
   SELECT SUM(balance) FROM users_user;
      ```