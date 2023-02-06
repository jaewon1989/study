## 실행방법 (PyCharm 기준)

1. [github 소스 다운로드](https://github.com/jaewon1989/study.git)
2. 다운로드한 소스 IDE 열기
3. IDE menu > settings > Python Interpreter 설정
4. Package 다운로드
    - Django 4.1.6
    - Markdown 3.4.1
    - asgiref 3.6.0
    - django-filter 22.1
    - djangorestframework 3.14.0
    - mysqlclient 2.1.1
    - pip 23.0
    - pytz 2022.7.1
    - setuptools 67.1.0
    - sqlparse 0.4.3
    - wheel 0.38.4
5. venv 환경 터미널 내 "cd study"로 진입 후 manage.py 파일 확인
6. test case 전체 실행
    - venv 환경 터미널 내 "python manage.py test" 입력
7. run server 실행
    - venv 환경 터미널 내 "python manage.py runserver" 입력

## 개발환경

- Pycharm
- DataGrip
- Postman
- Sourcetree

## 사용기술

- python3
- Django
- DRF
- AWS RDS Aurora(MySql)

## 기능 요구사항 및 구현 여부

| 기능 요구사항      | 개발  | 테스트 |
|--------------|-----|-----|
| 회원 가입 기능     | 완료  | 완료  |  
| 로그인 기능       | 완료  | 완료  |
| 내 정보 보기 기능   | 완료  | 완료  | 
| 비밀번호 찾기(재설정) | 완료  | 완료  |  

## 주요 함수

- [전화번호 인증 참조](study/authphone/views.py)
    - set_auth_info : 인증 정보 저장
    - update_auth_info 인증 번호 변경

- [회원 참조](study/customer/views.py)
    - signup : 회원 가입
    - signin : 로그인
    - mypage : 내 정보 보기
    - password : 비밀번호 찾기(재설정)

## 회원 가입 시나리오

1. 웹상에서 유저가 회원 가입 form 내 전화번호 인증번호 발송을 클릭한다.
2. 유저가 입력한 전화번호와 인증번호 6자리 숫자가 랜덤 발급되어 인증테이블에 저장된다.
3. 유저가 수신받은 인증번호를 입력하고 확인을 누르면 인증테이블를 업데이트 한다.
4. 유저가 from data에 전화번호 인증 완료 값을 포함해 from submit 한다.
5. 백엔드에서 from data 내 포함된 전화번호 인증 완료 값에 상관 없이 한번 더 전화번호 인증 여부를 확인한다.
6. 전화번호 인증이 완료된 상태이고 가입에 필수 항목 데이터들이 세팅되어 있으면 회원 가입 완료한다.

## 로그인 시나리오

- 비밀번호는 필수 입력
- 이메일, 닉네임, 전화번호는 중복안됨
- 이름은 중복 가능
- 로그인 가능 케이스
    - 이메일 + 비밀번호
    - 이메일 + 닉네임 + 비밀번호
    - 이메일 + 닉메임 + 이름 + 비밀번호
    - 이메일 + 닉네임 + 이름 + 전화번호 + 비밀번호
    - 닉네임 + 비밀번호
    - 닉네임 + 이름 + 비밀번호
    - 닉네임 + 이름 + 전화번호 + 비밀번호
    - 이름 + 전화번호 + 비밀번호
    - 전화번호 + 비밀번호
- 로그인 불가능 케이스
    - 이름 + 비밀번호

## 내 정보 보기 시나리오

1. 웹상에서 로그인 된 유저가 마이페이지 진입
2. 로그인 된 회원 시퀀스값으로 회원정보 조회

## 비밀번호 찾기(재설정) 시나리오

1. 웹상에서 로그인하지 않은 회원이 비밀번호 찾기 from 내 전화번호 인증번호 발송을 클릭한다.
2. 유저가 입력한 전화번호와 인증번호 6자리 숫자가 랜덤 발급되고 이전에 저장된 인증테이블 데이터가 업데이트 된다.
3. 유저가 수신받은 인증번호를 입력하고 확인을 누르면 인증테이블를 업데이트 한다.
4. 유저가 from data에 전화번호 인증 완료 값을 포함해 from submit 한다.
5. 백엔드에서 from data 내 포함된 전화번호 인증 완료 값에 상관 없이 한번 더 전화번호 인증 여부를 확인한다.
6. 전화번호 인증이 완료된 상태이고 신규 비밀번호가 세팅되어 있으면 비밀번호 변경 완료한다.

## 특별히 신경 쓴 부분

- python 개발이 난생 처음이라 실무 환경에 최대한 가깝게 세팅하고자 Django, DRF, AWS RDS Aurora(mysql) 사용하였습니다.
- 여러 개발환경을 대응하기 위해 [settings](study/study/settings)을 만들었습니다.
- SECRET_KEY 노출을 방지하기 위해 [secrets.json](study/secrets.json)을 만들었습니다.
- [전화번호 인증관련 기능](study/authphone)과 [회원관련 기능](study/customer)을 각각 app으로 만들었습니다.
- 회원과 인증테이블 모델링 시 1:1 관계로 생각을 했고 models.OneToOneFiels를 사용해봤지만 원하는 결과가 아니여서 수정하였습니다.
- serializer시 여러개의 serializer class를 만들어야 할지 하나의 serializer class에 (partial=Ture) 옵션을 주고 대응해야 하는지 고민했습니다. (이부분은 실무를 해보지
  않아 스스로 명확하게 필드 정의를 하는게 맞다고 생각하여 개발하였습니다.)
- [utils.py](study/customer/utils.py)를 생성하여 공통으로 사용할 전화번호 유효성 검증 모듈을 만들었습니다.
- [휴대전화 인증 관련 테스트](study/authphone/tests.py)는 휴대전화 인증에 관한 케이스를 작성하였습니다.
- [회원 관련 테스트](study/customer/tests.py)는 기능 요구사항에 관한 케이스를 작성하였습니다.