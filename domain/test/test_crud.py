from database.models import User # database폴더의 models 패키지에서 사용할 테이블을 가져온다.

'''
여기서는 데이터베이스에 대한 처리를 할 수 있고, 이 파일안에 CRUD 연산을 수행하는 함수를 정의하면 된다.
'''

# 데이터베이스의 모든 유저의 정보를 가져오는 구문이다.
def get_all_user(db):
        all_user = db.query(User).all() # models에 정의하였던 User Table을 통해, database 테이블을 비교하여, 모든 구문을 가져온다.
        return all_user