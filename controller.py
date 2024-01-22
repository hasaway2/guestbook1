import flask as f
import model as m

# 플라스크 앱(백엔드 서버)을 생성
app = f.Flask(__name__)

# 방명록을 출력 : 127.0.0.1:5000
@app.route("/") 
def list():
  guestbook = m.findall()
  # list.html에 list란 이름으로 guestbook을 넘겨준다
  return f.render_template("list.html", list=guestbook)

@app.route("/write", methods=['post'])
def write():
  content = f.request.form.get('content', type=str)
  m.save(content=content)
  return f.redirect("/")

@app.route("/delete", methods=['post'])
def delete():
  gno = f.request.form.get('gno', type=int)
  m.delete(gno)
  return f.redirect("/")

# 서버를 개발자 모드(변경하면 자동 재실행)로 실행
app.run(debug=True)
