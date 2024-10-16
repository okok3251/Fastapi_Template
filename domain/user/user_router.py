from fastapi import APIRouter, Depends, HTTPException
from database.database import get_db
from sqlalchemy.orm import Session
from typing import List
from .user_schema import *
from .user_crud import * # user_curd 파일에서 정의한 모든 함수를 사용할 수 있다.
'''
FastAPI 애플리케이션의 라우터를 정의하는 부분으로 API 엔드포인트를 설정하고, CRUD를 연결하는 부분이다.
엔드포인트는 @user_router.get() , @user_router.post()와 같은 데코레이터를 사용하여 정의한다.
예시로 @user_router.get('/') 이런 형태로 사용할 수 있다.

'''
user_router = APIRouter()





# HTTP GET 요청을 처리하는 엔드포인트를 정의하는 구문이다.
# response_model 을 통해 우리가 최종적으로 이 엔드포인트에서 반환하는 형태를 지정해줄 수 있다.
# 이외에도 response_model_exclude_unset , response_model_include, response_model_exclude 등이 있다.
# 이에 대해서는 schema에서 자세히 다루겠다.
@user_router.get('/get_all_user_data' ,response_model=List[UserInfo]) 
def get_all_user_data(db:Session=Depends(get_db)):
    try:
        '''
        사용자 정의 반환인 Response를 사용하여 반환할 수 있지만, JSONResponse 등을 사용하면, 데이터는
        검증되지 않으며, 직렬화 되지않고, 문서화도 되지 않는다. FastAPI는 이 모든것을 자동으로 해주고 있음
        return 문으로 그냥 반환해주면 된다!!
        ''' 
        
        return get_all_user(db) # crud.py에서 정의한 함수
    except HTTPException as e:
        print(f'error = {e}')
'''
get_all_user_data는 실제 요청을 처리하는 함수로 보통 엔드포인트의 url과 동일하게 사용한다.
이 함수는 SQLAlchemy의 Session 객체라는 타입을 통해 데이터베이스에 접근할 수 있다. db:Session -> db는 Session 타입이다.
Session은 간단하게 말해서 DB 연결을 유지하고 트랜잭션 관리, ORM 을 통한 레코드 간의 변환 등 여러가지를 처리한다.
FastAPI의 Depends를 사용하여 database.py에서 정의하였던 get_db 함수를 통해 데이터 베이스 세션을 주입받고,
데이터베이스 연결을 생성하고, 연결을 종료하는 역할을 하게됨으로써 데이터베이스에 접근할 수 있는 것이다.
Depends는 FastAPI에서 의존성을 주입하기 위한 도구로 매개변수로 전달 받은 함수를 실행시킨 결과를 리턴한다.
결국 db 객체에는 get_db 제너레이터에 의해 생성된 세션 객체가 주입되게 되고, db에 접근할 수 있게 되는 것이다.
'''


##########굳이굳이 불편하게 하는 방법들( 얼마나 편한지 체감해보자) 주석 풀어서 확인 ###############


# # 굳이굳이 불편하게 하는데 임포트까지 해야하는 것들 리스트
# from fastapi.encoders import jsonable_encoder
# from fastapi import Response
# import json

# @user_router.get('/test_Response' ,response_model=List[UserInfo]) 
# def get_all_user_data(db:Session=Depends(get_db)):
#     try:
#         data =  get_all_user(db) # crud.py에서 정의한 함수
#         json_compatible_data = jsonable_encoder(data)
#         return Response(content= json.dumps(json_compatible_data), media_type='application/json')
#     except HTTPException as e:
#         print(f'error = {e}')



# # 굳이굳이 불편하게 임포트 해야하는 것들 리스트
# from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder


# @user_router.get('/test_JSONResponse', response_model=List[UserInfo])
# def get_all_user_data(db: Session = Depends(get_db)):
#     try:
#         data = get_all_user(db)  # 사용자 데이터 가져오기
#         json_compatible_data = jsonable_encoder(data)
#         return JSONResponse(content=json_compatible_data, media_type='application/json')  # JSONResponse로 반환
#     except Exception as e:
#         # 예외 처리
#         raise HTTPException(status_code=500, detail=str(e))
    

# ''' 
# 실행 시켜보면 우리가 별도로 설정했던 response_model= List[UserInfo]가 적용이 안되는걸 확인할 수 있는데,
# FastAPI가 자동으로 다~ 해주는 부분이기 때문에 그냥 return 문으로 반환하도록 하자!
# 그래도 굳이굳이 이렇게 써야겠고, 반환값의 타입도 지정해주고 싶다면, data를 UserInfo(user_name) 이런식으로 반환하면 된다.
# 자세한 내용은 찾아보시길...
# '''