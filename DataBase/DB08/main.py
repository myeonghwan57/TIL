from datetime import datetime
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

### 4. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `name` 이 봉준호인 데이터를 아래와 같이 출력하는 코드를 작성하세요.

# > 출력 예시
# > 

# ```
# id : 1
# name : 봉준호
# debut : 1993-01-01 00:00:00
# country : KOR
# ```

d1 = Director.objects.get(id = 1)
print('id :',d1.id)
print('name :',d1.name)
print('debut :',d1.debut)
print('country :',d1.country)


### 5. Queryset 메소드 `get` 을 활용해서 `Genre` 테이블에서 `title` 이 드라마인 데이터를 아래와 같이 출력하는 코드를 작성하세요.
t1 = Genre.objects.get(title = '드라마')
print('id : ',t1.id)
print('title : ',t1.title)

### 6. 위 문제에서 찾은 `director` 와 `genre` 와 아래 `힌트 코드`를 활용해서 `Movie` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.
import datetime
director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')

movie = Movie()

movie.director = director_
movie.genre = genre_

movie.title = '기생충'
movie.opening_date = datetime.date(2019,5,30)
movie.running_time = 132
movie.screening = False

movie.save()

movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for i in movies:
    movie = Movie()
    movie.director = Director.objects.get(name = i[0])
    movie.genre = Genre.objects.get(title = i[1])
    movie.title = i[2]
    movie.opening_date = i[3]
    movie.running_time = i[4]
    movie.screening = i[5]
    
    movie.save()

Movie.objects.values()

for i in range(1,10):
    movie = Movie.objects.get(id=i)
    d = Director.objects.get(movie.director)
    print(d.name,movie.genre,
    movie.title,movie.opening_date,
    movie.running_time,movie.screening)


for i in range(1,10):
    movie = Movie.objects.get(id=i)
    d = Director.objects.get(id = movie.director_id ) 
    print(d.name,movie.genre,
    movie.title,movie.opening_date,
    movie.running_time,movie.screening)

movie=Movie.objects.all().order_by('-opening_date')
for i in movie:
    
    d = Director.objects.get(id = i.director_id )
    t = Genre.objects.get(id = i.genre_id) 
    print(d.name,t.title,
    i.title,i.opening_date,
    i.running_time,i.screening)

movie=Movie.objects.all().order_by('opening_date')[0]
d = Director.objects.get(id = movie.director_id )
t = Genre.objects.get(id = movie.genre_id) 
print(d.name,t.title,
movie.title,movie.opening_date,
movie.running_time,movie.screening)

d = Director.objects.get(name = '봉준호')
movie=Movie.objects.filter( director_id = d.id).order_by('opening_date')
for i in movie:
    t = Genre.objects.get(id = i.genre_id) 
    print(d.name,t.title,
    i.title,i.opening_date,
    i.running_time,i.screening)

movie = Movie.objects.filter(running_time__gt=119).order_by('running_time')
for i in movie:
    d = Director.objects.get(id = i.director_id )
    t = Genre.objects.get(id = i.genre_id) 
    print(d.name,t.title,
    i.title,i.opening_date,
    i.running_time,i.screening)