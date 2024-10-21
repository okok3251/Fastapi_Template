from pydantic import BaseModel, field_validator
from typing import List
from pydantic_core.core_schema import FieldValidationInfo
from fastapi import HTTPException




'''
settings에서 언급했듯이 Pydantic은 데이터 검증 등을 지원하는 라이브러리이다.
이 파일에서는 Pydantic의 모델을 정의하는데, 입력된 데이터를 검증할 수 있고, 출력 데이터의 형식을 정의
해줄 수 있다. Pydantic의 BaseModel을 상속받아서 데이터 모델을 정의하면 된다.
'''

# 유저가 로그인 할때 필요한 정보를 받아오기 위해 생성한 객체 모델
class UserLogin(BaseModel): 
    user_id : str           #  user_id 속성을 str형으로 정의하고, 형에 맞게 들어오지 않으면 pydantic에 의해서 에러가 나게된다.
    password :  str

    @field_validator('user_id', 'password', mode='before')          # field_validator를 통해서 클래스 내부의 유효성 검사를 할 수 있다.
    # before는 필드의 값이 모델에 실제로 할당되기 전에 유효성 검사를 수행한다는 뜻이다.
    @classmethod # 클래스 메서드 라는 것을 명시하는 부분이다. 신경쓰지 않아도 됨
    def is_not_empty(cls,v):  # cls는 지금 UserCreate 객체를 가리키는 것이고, v는 검증할 필드의 값을 나타낸다.
        if not v or not v.strip():
            raise HTTPException(status_code=500, detail='빈 값은 허용되지 않음')
        return v



 # 유저가 회원가입할 때, 필요한 정보를 받아오기 위해 생성한 객체 모델, user_id와 password 뿐만 아니라 user_name도 필요하기 때문에 UserLogin을 상속받아서 정의
class UserCreate(UserLogin):
    password_check : str
    user_name: str
    @field_validator('user_id', 'password','user_name', 'password_check', mode='before') 
    @classmethod
    def is_not_empty(cls, v):
        return super().is_not_empty(v)              # UserLogin의 is_not_empty 함수를 상속받아서 유효성 검사를 수행하고,
        # UserCreate에서는 field_validator를 따로 설정해줌으로써, 두 클래스 모두 동일한 유효성 검사를 수행가능하다.
    
    @field_validator('password_check', mode='before')
    @classmethod
    def password_match(cls, v, info:FieldValidationInfo):                    # FieldValidationInfo : 현재 필드의 유효성 검사와 관련된 정보를 포함한다.
        if 'password' in info.data and v!= info.data['password']:              # 여기서 v는 password_check가 되고, 결국 password와 password_check가 일치하는지를 검증
            raise HTTPException(status_code=500, detail='비밀번호와 비밀번호 확인이 일치하지 않음.')
        return v                                                              # 문제가 없으면 password_check를 return 하며 마무리 된다.
'''
## 개인적으로 이러한 상속 구조를 사용하지 않고, 따로 BaseMdoel을 넣어주는 것을 선호한다.
상속 구조를 사용하기 위해 고려해야 될것이 많고, 복잡하기 때문에 일반적으론 BaseModel을 사용한다.
 필요시에 다른 속성을 추가할 수 있다. ex) age = int
 '''

# 유저의 정보를 보여주기 위해 생성한 객체 모델, 이를 통해 비밀번호같은 민감한 정보는 프론트로 보내지 않는다.
class UserInfo(BaseModel):
    user_name : str | None 





### user_router response_model 부분 참고

# 예시를 위한 스키마
class Example(BaseModel):
    example_number : int
    example_name : str
    example_list : List[str]
    example_type : str | None
'''
response_model_include={'example_number', 'exmaple_name'} 이라고 선언하면 해당 속성만 가져올 수 있다.
response_model_exclude={'example_type'} 이라고 선언하면 해당 속성을 제외하고 모든 속성을 가져온다.
'''