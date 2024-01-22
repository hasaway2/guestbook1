import datetime as d

# 데이터 : model
guestbook=list()
gb1 = {"gno":1, "content":"첫번째 방명록", "writeday":"2024-01-22"}

# 파이썬에서 타입은 모두 클래스
# 클래스 이름으로 객체를 생성할 수 있으며 함수처럼 사용
gb2 = dict(gno=2, content="두번째 방명록", writeday="2024-01-22")

guestbook.append(gb1)
guestbook.append(gb2)

gno =3

# 리스트 전부 출력 - 스프링은 모델 함수 이름이 정해져있다. 땡겨서 사용
def findall() :
  return guestbook

def save(content:str) :
  global gno
  writeday = d.datetime.now().date()
  gb = dict(gno=gno, content=content, writeday=writeday)
  guestbook.append(gb)
  gno+=1

def delete(gno:int):
  for gb in guestbook:
    if gb['gno']==gno:
      guestbook.remove(gb)



