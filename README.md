# flask_orator

대부분의 플라스크 DB 모듈은 sqlalchemy를 이용하지만 
이번 만큼은 남들이 가지 않는 길을 가보고 싶었다. 
orator 모듈은 루비온더레일즈와 라라벨의 엘롭퀀트?ORM을 연상시키는 문법을 가지고 있어서 
document를 읽는데도 부담이 없었다. 
단지 .... 만든 이가 더 이상 유지/보수를 안하는 것이 매우 안타깝다.

이 repository의 목표는 flutter backend api 구성이다. 
실제로 [pythonanywhere](https://www.pythonanywhere.com/)에 소스를 올리고, 구글 마켓까지만이라도 빌드하는 것이 목표다. 
그렇지만 뭘 만들지는 아직 미정.... ㅠㅠ 



### 가상화 (Mac)
1. 작업 공간으로 이동: `cd ~/workspace/flask_orator`
2. 가상화 생성: `python -m venv .venv`
3. 가상화 실행: `. .venv/bin/activate`
4. 가상화 종료: `deactivate`

### 가상화 (Windows)
1. 작업 공간으로 이동:
    1. 드라이브 이동: `d:`
    2. 작업 공간 이동: `cd workspace\flask_orator`
2. 가상화 생성: `python -m venv venv`
3. 가상화 실행: `venv\Scripts\activate`
4. 가상화 종료: `deactivate`

### package 설치
* pip 업그레이드: `python -m pip install --upgrade pip`
* 패키지 설치: `pip install -r requirements.txt`


### Mac에서 mysql, mysqlclient 설치
* mysql 설치: `brew install mysql`
* mysql client 설치 (Mac에서 원래 그냥 pip 설치하면 되었는데 버그로 인하여 openssl을 이용해야한다고 함)
* `brew install openssl`
* `cd ~/workspace/flask_orator`
* `LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient`

### Windows 에서 mysqlclient 설치
* [링크 이동](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient) 에서 자신의 파이썬버전과 cpu 에 맞게 파일 다운로드
* 다운받은 파일로 설치 Ex. `pip install D:\workspace\flask_orator\mysqlclient-1.4.6-cp37-cp37m-win32.whl`


### database configs
```python
app.config['ORATOR_DATABASES'] = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'flask_orator',
        'user': 'sjahn',
        'password': '1234',
        'prefix': '',
        'log_queries': True
    }
}
```

### database migration
* create migration: `python db.py make:migration create_users_table --table users --create`
* run migration: `python db.py migrate`


### run
`FLASK_DEBUG=1 flask run`


### url
- web: http://127.0.0.0.1:5000
- swagger: http://127.0.0.1:5000/apidocs