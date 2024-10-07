from pydantic_settings import BaseSettings
from typing import Optional
import os


'''
Basesettings는 pydantic의 설정 관리 기능을 확장해 환경 변수와 설정파일을 손쉽게 로드하여
검증할 수 있도록 돕는 클래스이고, pydantic은 간단히 말해서 데이터 검증 및 설정 관리를 위한 라이브러리
라고 보면 된다. pydantic의 기본 기능중 하나는 데이터 검증 기능인데, 정의된 타입에 맞지 않는 값이
설정되면 에러가 발생하여, 잘못된 값이 입력되는 것을 미리 방지할 수 있음.
'''

class Settings(BaseSettings):
    DATABASE : Optional[str] = None # python 3.10 버전 이후부터는 str | None = None으로 가능하다 (똑같은 말임)
    '''
    여기서 db_address : str 처럼 타입을 지정해줄 수 있는데, default 값을 설정하고 싶다면
    db_address : str = root 와 같이 표현할 수 있다. 또한 typing의 Optional을 이용하여
    ad_address : Optional[str] = None 과 같이 표현할 수 있는데, 이를 통해 null 값도 허용할 수 있다.
    Optional -> 변수에 값이 없을 수도 있음을 명시하는 방법.
    '''
    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '../initial_setting.env')

    '''
    ## config 클래스는 pydantic 모델의 동작을 조정하는 다양한 설정 옵션을 정의하는 내부 클래스!

    config 클래스 내부에는 다음과 같은 속성들이 있는데

    # env_file  : 옵션 설정을 통해 설정파일 값을 로드할 수 있다.
        -> env 파일은 설정을 한곳에서 관리할 수 있고, 간단하게 중요한 정보를 숨기기 위해 사용한다
        -> env 파일은 github 등에 push할때, 빼고 올려야 한다.

    # case_sensitive : 환경 변수 이름의 대소문자를 구분할지를 설정하며 True || False로 설정 가능
    # allow_population_by_field_name : 필드 이름을 사용하여 모델을 초기화 할 수 있는지의 여부 True || False
      --settings = Settings(user_name="myuser", password="mypassword") -> 이렇게 사용할 수 있다는 뜻
    # orm_mode : ORM 과의 호환성 설정
    등등등이 있지만, 이 단계에서는 굳이 세세하게 설정해줄 필요는 없다.

    '''

settings = Settings()
'''
settings = Settings()를 통해 설정 인스턴스를 생성하면, 정의된 환경 변수들이 
settings 객체의 속성으로 할당되며, 다른 곳에서 활용할 수 있게 된다.
'''
