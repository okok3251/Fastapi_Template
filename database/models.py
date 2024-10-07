from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
'''
sqlalchemy에서 데이터베이스 모델을 정의하기 위한 도메인을 정의하기 위한 요소들을 임포트하고,
relationship을 통해 매핑 카디널리티를 설정할 수 있다.
'''
from .database import Base # database.py에서 정의한 Base 모델을 가져오는 구문


 # 간단하게 유저와 신용카드가 있다고 가정해보자

class User(Base):
    __tablename__ = 'users'

    user_number = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(100))
    password = Column(String(100))
    user_name = Column(String(45))
    cards = relationship("Card", back_populates="owner")
'''
User라는 모델을 만들어서 Base모델을 상속받아 데이터베이스에 매핑될 수 있게 만들고,
__tablename__ 이라는 속성으로 실제 스키마의 테이블 이름을 설정할 수  있다.
밑은 테이블의 속성들을 정의한 것인데, primary_key를 통해 기본키로 설정할 수 있고,
autoincrement를 통해서 새로운 튜플이 생길때마다 자연스럽게 user_number 값이 올라가게 된다.
relationship에 대한 설명은 일단 생략하도록 하자.
'''

class Card(Base):
    __tablename__ = 'card'

    card_id = Column(Integer, primary_key=True, autoincrement=True)
    card_name = Column(String(45))
    user_number = Column(Integer,ForeignKey('users.user_number'))
    owner = relationship("User", back_populates="cards")

'''
여기도 동일하게 Card라는 모델을 만들어서 Base모델을 상속받았고, card라는 이름으로 테이블이 생길것이다.
다른점은 ForeignKey가 있는데, users 테이블의 user_id 라는 값을 가리키고 있음으로 인해서, 
한 유저는 여러개의 카드를 가질 수 있는 1 대 N 형태로 만들어 질 것이다.
'''