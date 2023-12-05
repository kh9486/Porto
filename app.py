from flask import Flask, render_template, request, redirect, session, url_for
import boto3
from boto3.dynamodb.conditions import Key



app = Flask(__name__)
app.secret_key = '0000'

# id_pass = {"admin": "admin"}

aws_access_key_id = 'AKIAWYYZB6Q2Z27JIOKV'
aws_secret_access_key = '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'
region_name = 'us-west-2'
dynamodb_table_name = 'porto_submit'

dynamodb = boto3.resource('dynamodb', aws_access_key_id=aws_access_key_id, 
                          aws_secret_access_key=aws_secret_access_key, 
                          region_name=region_name)

table = dynamodb.Table('porto_submit')


def check_if_username_exists(username):
    response = table.query(KeyConditionExpression=Key('username').eq(username))
    
    return response.get('Items', [])

def is_user_logged_in():
    return 'username' in session


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('/result')
    return render_template('index.html')




@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    session.pop('userPassword', None)
    return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['username']
        password = request.form['userPassword']
        user_data_list = check_if_username_exists(id)

        if user_data_list:
            user_data = user_data_list[0]
            if user_data.get('password') == password:
                session['username'] = id
                session['userPassword'] = password

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
                alert("로그인 실패, 사용자명이 존재하지 않습니다.")
                history.back()
                </script>
        
                """
        
    return render_template('login.html')
        


@app.route('/register', methods=['GET', 'POST'])

def register():
    if request.method == 'POST':
        id = request.form['username']
        password = request.form['userPassword']
        existing_users = check_if_username_exists(id)

        if existing_users:
            return """
                <script>
                alert("이미 존재하는 아이디입니다.");
                history.back();
                </script>
                """
        else:
            table.put_item(Item={'username': id, 'password': password})
            return """
                <script>
                alert("회원가입이 완료되었습니다. 다시 로그인해 주십시오.");
                window.location.href = "/login";
                </script>
                """
        
    return render_template('register.html')




@app.route('/resume', methods=['GET', 'POST'])
def resume():
    if not is_user_logged_in():
        return redirect(url_for('login'))
    
    else: 
        username = session.get('username')
        response = table.query(KeyConditionExpression=Key('username').eq(username))
        items=response["Items"][0]

        name = items['name'] if 'name' in items else ''
        address = items['address'] if 'address' in items else ''
        phone = items['phone'] if 'phone' in items else ''
        email = items['email'] if 'email' in items else ''
        Github_url = items['Github_url'] if 'Github_url' in items else ''
        other_url = items['other_url'] if 'other_url' in items else ''
        SKILL1 = items['SKILL1'] if 'SKILL1' in items else ''
        skill_1 = items['skill_1'] if 'skill_1' in items else ''
        SKILL2 = items['SKILL2'] if 'SKILL2' in items else ''
        skill_2 = items['skill_2'] if 'skill_2' in items else ''
        SKILL3 = items['SKILL3'] if 'SKILL3' in items else ''
        skill_3 = items['skill_3'] if 'skill_3' in items else ''
        SKILL4 = items['SKILL4'] if 'SKILL4' in items else ''
        skill_4 = items['skill_4'] if 'skill_4' in items else ''
        Experience_main_1 = items['Experience_main_1'] if 'Experience_main_1' in items else ''
        Experience_details_1 = items['Experience_details_1'] if 'Experience_details_1' in items else ''
        Experience_main_2 = items['Experience_main_2'] if 'Experience_main_2' in items else ''
        Experience_details_2 = items['Experience_details_2'] if 'Experience_details_2' in items else ''
        Experience_main_3 = items['Experience_main_3'] if 'Experience_main_3' in items else ''
        Experience_details_3 = items['Experience_details_3'] if 'Experience_details_3' in items else ''

        return render_template('resume.html',
        name = name,
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





@app.route('/submit', methods=['GET','POST'])
def submit():
    

    username = session.get('username')
    password = session.get('userPassword')
    name = request.form['name']
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
        'password' : password,
        'username': username,
        'name': name,
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
    name = name,
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

