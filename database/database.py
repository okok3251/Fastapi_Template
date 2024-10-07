from sqlalchemy import create_engine # 데이터 베이스와 연결할 수 있는 엔진을 생성
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .setting import settings # 아까 정의한 setting 객체를 가져온다.
'''
sqlalchemy는 python에서 관계형 데이터베이스와의 연결 및 ORM 등을 활용할 수 있도록 만든 라이브러리이며
MySQL 같은 특정한 데이터베이스에 연결하기 위해 추가 드라이버가 필요한데, 그것이 바로 pymysql이다.

'''

engine = create_engine(
    settings.DATABASE
)
'''
create_engine 함수에 전달된 문자열은 데이터베이스 연결 정보를 포함하고, 아까 setting.py에서 
가져왔던 설정정보를 넣음으로써, 우리의 테이블에 연결된 것이다. inital_setting.env 파일을 보면
DB의 주소값이 적혀있는데 마지막 스키마 명은  ** 중요 ** -> 실제로 있는 스키마 명이 되야한다.
'''

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
'''
sessionmaker를 호출하여 SessionLocal 이라는 세션 팩토리를 생성하는데, 이 세션은 데이터베이스와의
상호작용을 관리하는 작업 단위이다. 이 말은 세션을 통해 데이터베이스에 CRUD 작업을 수행할 수 있음을 의미한다.
또한 이 세션은 하나의 트랜잭션 단위로, 여러 작업을 묶어서 처리할 수 있는데, 이 세션이 종료되기 전까지
수행된 작업들은 커밋될 때까지 데이터베이스에 반영되지 않는다.
'''

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
'''
이 get_db 함수는 데이터베이스 세션을 생성하고 관리하는 제너레이터 함수이다.
db = SessionLocal() 구문으로 아까 생성하였던 세션 팩토리를 호출하고,
yield db 구문을 통해 세션을 호출하는 곳에 전달하며, 함수의 실행을 중단하고 이후에 다시 호출할 수 있도록
만들어준다. finally 구문을 통해서 세션이 사용된 후에 항상 db.close()가 호출되며, 세션을 닫아 리소스가 해제됨
'''

Base = declarative_base()
'''
declarative_base 함수를 호출하여 Base라는 기본 클래스를 생성하는데, 이 클래스를 상속받아서
데이터베이스 테이블과 매핑되는 모델 클래스를 정의할 수 있다. 결국 Base 클래스를 통해 SQLAlchemy 모델과
데이터베이스 간의 매핑을 자동으로 처리할 수 있는 것이다. models.py 파일에 정의되어 있다.
'''