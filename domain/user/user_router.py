from fastapi import APIRouter

'''
FastAPI 애플리케이션의 라우터를 정의하는 부분으로 API 엔드포인트를 설정하고, CRUD를 연결하는 부분이다.
엔드포인트는 @user_router.get() , @user_router.post()와 같은 데코레이터를 사용하여 정의한다.
예시로 @user_router.get('/') 이런 형태로 사용할 수 있다.

'''


user_router = APIRouter()