from flask import Flask, render_template, make_response, render_template, redirect, url_for
from flask import jsonify
from flask import Markup
from werkzeug.utils import secure_filename
from flask import request
from sqlalchemy import Table, Column, Integer, String
import json
import config
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_bootstrap import Bootstrap

#首先引入了Flask包，并创建一个Web应用的实例”app”
app = Flask(__name__)
app.config.from_object(config)
app.config['SECERT_KEY'] = 'hard to guess'
#登录数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'you database url'
#设置每一次提交数据库的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class News(db.Model):
    """定义数据模型"""
    __tablename__ = 'NEWS'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True)
    texts = db.Column(db.Text)


def __init__(self, title, msg):
    self.title = title
    self.msg = msg


a = []
#ID = 0
for i in range(1, 10):
    #ID+=1
    n = News.query.filter_by(id=i).first()
    a.append({"title": n.title, "texts": n.texts})


b = a


@app.route('/news')
def news():
    c = b

    return render_template("gamenew.html", c=c)


__author__ = 'aim'


@app.route('/')  #定义路由规则这个函数级别的注解指明了当地址是根路径时，就调用下面的函数。可以定义多个路由规则
def index():  #处理请求
    return redirect(url_for('aim'), code=301)  #跳转（状态码通常301） => 通常用于旧网址转移到了新网址
    #一个函数上可以设施多个URL路由规则


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files["file"]
        base_path = path.abspath(path.dirname(__file__))
        upload_path = path.join(base_path, 'static/uploads/')
        file_name = upload_path + secure_filename(f.filename)
        f.save(file_name)
        return redirect(url_for('upload'))
    return render_template('upload.html')


@app.route('/user')
def aim():
    user_agent = request.headers.get('User-Agent')
    return jsonify({'msg': 'hello,wold'})


@app.route('/index')
def hellos():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {
                'nickname': 'John'
            },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {
                'nickname': 'Susan'
            },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)


@app.route('/user/<int:user_id>')  #可以在URL参数前添加转换器来转换参数类型
def user(user_id):
    return '<h1>hello %d <h1>' % user_id


#HTTP请求方法设置
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            return 'Admin login successfully!'
        else:
            return 'No such user'
    title = request.args.get('title', 'Default')
    return render_template('login.html', title=title)


@app.route('/user/')
def test():
    print(url_for('index', id=10, name='Anonymous', age=16))
    return 'Test'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
