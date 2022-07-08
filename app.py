from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

## import config


app=Flask(__name__)
## app.config.from_object(config)



'''配置数据库'''
app.config['SECRET_KEY'] = 'hard to guess'  # 一个字符串，密码。也可以是其他如加密过的

# 在此登录的是root用户，要填上密码如123456，MySQL默认端口是3306。并填上创建的数据库名如youcaihua
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@47.101.69.44:3306/testsql'

# 设置下方这行code后，在每次请求结束后会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    return 'hh'


db = SQLAlchemy(app)    # 实例化数据库对象，它提供访问Flask-SQLAlchemy的所有功能


'''定义模型，建立关系'''
class Role(db.Model):   # 所有模型的基类叫 db.Model，它存储在创建的SQLAlchemy实例上。
    # 定义表名
    __tablename__ = 'roles'

    # 定义对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role')

    # __repr__()方法显示一个可读字符串，虽然不是完全必要，不过用于调试、测试是很不错的。
    def __repr__(self):
        return '<Role {}>'.format(self.name)



'''进行数据库操作'''
if __name__ == '__main__':
    #删除旧表
    db.drop_all()
    db.create_all()#创建新表



    app.run(debug=True)