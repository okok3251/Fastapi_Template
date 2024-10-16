from fastapi import FastAPI
# fastapi의 가장 큰 특징은 데이터타입을 엔드포인트로 명시하지 않아도 알아서 알맞게 바꿔주는 큰 장점이 있다.
import uvicorn # fastapi 애플리케이션을 실행하기 위해 사용하는 ASGI 서버이다.
'''
ASGI는 비동기 웹 서버를 의미하며, 자세한 것은 여기서 다루기 길어져 검색을 해보길 바란다.

'''
from fastapi.middleware.cors import CORSMiddleware
import database.models
from domain.combined_router import combined_router

def include_router(app):
    app.include_router(combined_router)

'''
domain에 있는 모든 라우터를 모아서 반환해주는 combined_router가 있는데, 여기서 마지막으로 추가해줌으로써
모든 api 엔드포인트가 활성화되며, 그 엔드포인트들에 요청을 보낼 수 있다.
'''

def start_application(): # fastapi 애플리케이션을 설정하고 초기화 하는 역할.
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ) # 통신하기 위한 미들웨어
    '''
    app = FastAPI() 부분을 통해 애플리케이션을 실행 할 수 있고,
    add_middleware를 통해서 FastAPI 애플리케이션에 미들웨어를 추가할 수 있다 이를 통해
    요청과 응답 사이에 추가적인 처리를 수행할 수 있게 되는 것이다.
    CORSMiddleware는 CORS를 처리하기 위한 미들웨어로 다른 포트에서 실행되는 API에
    접근할 수 있도록 해주는 기특한 녀석이다.

    allow_origins : CORS를 통해 허용할 출처들의 리스트라고 볼 수 있다. 만약 3001번도 허용하고 싶다면
    http://localhost:3001을 리스트에 추가해주면 된다.

    allow_credentials = True 이부분을 통해 클라이언트가 자격 증명 (쿠키 등)을 사용할 수 있게된다.

    allow_methods 부분을 통해서 허용할 HTTP 메서드를 설정할 수 있고, GET, POST, PUT, DELETE 등이 있는데
    *로 함으로써 모든 메서드를 허용하겠다는 의미이다.

    allow_headers 부분은 허용할 HTTP 헤더를 설정하는 구문이고, 이또한 Content-type, Authorization 등
    다양한 헤더를 사용할 수 있고, *로 설정함으로써 모든 헤더를 허용한다.
    '''

    # database.modles.Base.metadata.drop_all(bind=setting.database.engine) # 테이블 삭제
    database.models.Base.metadata.create_all(bind=database.database.engine) # 테이블 생성
    '''
    database.models에 정의된 Base 모델을 기반으로 실제로 데이터 베이스에 매핑 시켜주는 부분이고 
    create_all 메서드를 통해 테이블을 생성할 수 있고 이미 정의된 테이블은 변경되지 않는다.
    drop_all 메서드를 통해 테이블을 모두 삭제할 수 있다. 테이블이 삭제된 다는것은 그 안의 데이터도 모두
    삭제된다는 의미이기 때문에, 유의해서 사용하자
    '''
    include_router(app) # 여기서 include_router를 통해서 모든 라우터를 통합한다.
    return app 
'''
위의 start_application 함수를 호출을 통해서 CORS 미들웨어를 추가하고, 데이터베이스의 테이블을 생성하여
모든 라우터를 포함시켜 최종적으로 설정이 완료된 FastAPI의 인스턴스를 반환하여, 서버가 실행될 준비를 갖추게 된다.
'''

app = start_application() # start_application 함수를 실행시켜 서버가 실행된다.


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True) # python main.py로 실행 가능

'''
간단하게 이 조건문은 현재 스크립트가 직접 실행될 때만 아래 코드를 실행하고, 다른 모듈에서 import 될 경우
실행되지 않는다. 나머지는 uvicorn 서버를 실행하는 부분이다. main.py에 있는 app을 실행하며,
port는 8000번으로, 코드 변경 시 서버가 다시 자동으로 시작되게 하는 reload를 True로 설정하는 부분이다.
'''