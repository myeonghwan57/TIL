import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 
Director.objects.create(name = '봉준호',debut=datetime.date(1993,1,1),country='KOR')
import datetime

#3
Director.objects.bulk_create([
    Director(name = '봉준호',debut = datetime.date(1993,1,1),country='KOR'),
    Director(name = '김한민', debut = datetime.date(1999,1,1),country='KOR'),
    Director(name = '최동훈', debut = datetime.date(2004,1,1),country='KOR'),
    Director(name = '이정재', debut = datetime.date(2022,1,1),country='KOR'),
    Director(name = '이경규', debut = datetime.date(1992,1,1),country='KOR'),
    Director(name = '한재림', debut = datetime.date(2005,1,1),country='KOR'),
    Director(name = 'Joseph Kosinski', debut = datetime.date(1999,1,1),country='KOR'),
    Director(name = '김철수', debut = datetime.date(2022,1,1),country='KOR'),
])

#4
list_= ['액션','드라마', '사극', '범죄', '스릴러', 'SF','무협','첩보','재난']
for i in list_:
    genre = Genre()
    genre.title = i
    genre.save() 

#5
for i in range(8):
    print(Director.objects.all()[i].name,
    Director.objects.all()[i].debut,
    Director.objects.all()[i].country)
#6
director = Director.objects.get(id = 1)
print(director.name,director.debut,director.country)

#7
director = Director.objects.get(country = 'USA')
print(director.name,director.debut,director.country)

### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서 
#  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고,
#  출력하는 코드를 작성하세요.
director = Director.objects.get(name = 'Joseph Kosinski')
director.country = 'USA'
director.save()

###10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 
#`country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

for i in range(1,8):
    director = Director.objects.get(id = i)
    if director.country == 'KOR':
        print(director.name,director.debut,director.country)