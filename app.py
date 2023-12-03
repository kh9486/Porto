from flask import Flask, render_template, request, redirect
import boto3
from boto3.dynamodb.conditions import Key


app = Flask(__name__)

id_pass = {"admin": "admin"}

aws_access_key_id = 'AKIAWYYZB6Q2Z27JIOKV'
aws_secret_access_key = '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'
region_name = 'us-west-2'
dynamodb_table_name = 'porto_submit'

dynamodb = boto3.resource('dynamodb', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
table = dynamodb.Table('porto_submit')


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
        return redirect('/resume')
    return render_template('resume.html')


@app.route('/submit', methods=['GET','POST'])
def submit():
        username = request.form['username']
        address = request.form['address']
        phone = request.form['phone']
        email = request.form['email']
        Github_url = request.form['Github_url']
        other_url = request.form['other_url']
        SKILL1 = request.form['SKILL1']
        skill_1 = request.form['skill_1']
        SKILL2 = request.form['SKILL2']
        skill_2 = request.form['skill_2']
        SKILL3 = request.form['SKILL3']
        skill_3 = request.form['skill_3']
        SKILL4 = request.form['SKILL4']
        skill_4 = request.form['skill_4']
        Experience_main_1 = request.form['Experience_main_1']
        Experience_details_1 = request.form['Experience_details_1']
        Experience_main_2 = request.form['Experience_main_2']
        Experience_details_2 = request.form['Experience_details_2']
        Experience_main_3 = request.form['Experience_main_3']
        Experience_details_3 = request.form['Experience_details_3']


        table.put_item(
            Item={
            'username': username,
            'address': address,
            'phone': phone,
            'email': email,
            'Github_url': Github_url,
            'other_url': other_url,
            'SKILL1': SKILL1,
            'skill_1': skill_1,
            'SKILL2': SKILL2,
            'skill_2': skill_2,
            'SKILL3': SKILL3,
            'skill_3': skill_3,
            'SKILL4': SKILL4,
            'skill_4': skill_4,
            'Experience_main_1': Experience_main_1,
            'Experience_details_1': Experience_details_1,
            'Experience_main_2': Experience_main_2,
            'Experience_details_2': Experience_details_2,
            'Experience_main_3': Experience_main_3,
            'Experience_details_3': Experience_details_3
                    }
                        )


        return render_template('submit.html',
        username=username,
        address=address,
        phone = phone,
        email = email,
        Github_url = Github_url,
        other_url = other_url,
        SKILL1 = SKILL1,
        skill_1 = skill_1,
        SKILL2 = SKILL2,
        skill_2 = skill_2,
        SKILL3 = SKILL3,
        skill_3 = skill_3,
        SKILL4 = SKILL4,
        skill_4 = skill_4,
        Experience_main_1 = Experience_main_1,
        Experience_details_1 = Experience_details_1,
        Experience_main_2 = Experience_main_2,
        Experience_details_2 = Experience_details_2,
        Experience_main_3 = Experience_main_3,
        Experience_details_3 = Experience_details_3
        )






if __name__ == '__main__':
    app.run(debug="True")


