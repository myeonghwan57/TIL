# DB - ORM

**Object - Relational - Mapping** 

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술 

객체로 DB를 조작한다.

객체를 담은 일종의 리스트를 보여준다.

모델 설계 

```python
class Genre(models.Model):
    name = models.CharField(max_length = 30) # 클래스 생성 후 DB에 반영
```





마이그래이션 

클래스 생성 테이블 생성 

필드 변경 수정 삭제 추가 

클래스 수정 -> 알아서 변경됨 



모델의 변경사항이 생겼을때 makemigrations -> migrate

 트랜잭션 

begin ~ commit

데이터 베이스 조작 

1. create 메서드 활용

Genre.objects.create(name= '발라드')

2. 인스턴스 생성 후 직접 생성 





Genre.objects.get(id=1) -> 반드시 출력 하나 없거나 많은면 오류 띄움  (PK)

Genre.objects.filter(id=1) -> 무조건 결과가 쿼리셋 나머지 모든값을 출력하거나 알고 싶을때 

