from sqlalchemy import create_engine

DB_URI = 'mysql+mysqldb://{}:{}@{}/{}.format(root, 123456, "47.101.69.44", 3306, testsql)'
# 创建数据库引擎
engine = create_engine(DB_URI)

engine.connect()