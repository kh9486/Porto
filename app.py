from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

id_pass = {"admin": "admin"}

# 정아야 내가 정말정말 사랑해❤

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('/result')
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['userName']
        password = request.form['userPassword']
        if id in id_pass:
            if id_pass[id] == password:
                return redirect("/")
            else:
                return """
                    <script>
                    alert("로그인 실패, 비밀번호가 틀렸습니다.")
                    history.back()
                    </script>
                    """
        else:
            return """
                <script>
                alert("로그인 실패, 다시 입력하세요.")
                history.back()
                </script>
                """
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form['userName']
        password = request.form['userPassword']
        if id in id_pass:
            return """
                <script>
                alert("이미 존재하는 아이디입니다.")
                history.back()
                </script>
                """
        else:
            id_pass[id] = password
            return redirect('/login')
    return render_template('register.html')


@app.route('/resume', methods=['GET', 'POST'])
def resume():
    if request.method == 'POST':
        return redirect('/result')
    return render_template('resume.html')


if __name__ == '__main__':
    app.run()

