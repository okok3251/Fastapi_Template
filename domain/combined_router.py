from fastapi import APIRouter
from domain.test.test_router import test_router


combined_router = APIRouter() # FastAPI의 라우터 클래스를 사용하여 여러 엔드포인트를 그룹화 할 수 있다.

combined_router.include_router(test_router) # combined_router에 다른 라우터들을 포함시키는 구문

'''

domain 폴더 안에 있는 여러가지 도메인들의 router를 여기서 한번에 모아서 main.py로 보내줄 수 있다.
도메인이 하나 추가되면 별도의 router를 만들어 이쪽으로 보내주면 된다.
만약 question 이라는 도메인이 추가되었다면, 
from domain.question.question_router import question_router

combined_router.include_router(question_router)
이 구문을 추가해줘야 한다.
'''