from flask import Flask, render_template, request, redirect, session

# application  就是这个app
app = Flask(__name__)
app.secret_key = 'xcv'
app.debug = True
User_dict = {
    '1': {'name': '大军'},
    '2': {'name': '小花'},
    '3': {'name': '小王'},
    '4': {'name': 'a'}
}


# 默认只有 get请求  其他的都在这个里面加   比如post 之类的
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pad = request.form.get('pwd')
    if user == 'a' and pad == '1':
        session['user_info'] = user
        return redirect('/index')
    else:
        return render_template('login.html', msg='error')


@app.route('/index', methods=['GET', 'POST'])
def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    return render_template('/index.html', user_dict=User_dict)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    del session['user_info']
    return redirect('/login')


@app.route('/detail', methods=['GET', 'POST'])
def detail():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    uid = request.args.get('uid')
    info=User_dict.get(uid)
    return render_template('/detail.html', info=info)


if __name__ == '__main__':
    # print('111')
    app.run()
