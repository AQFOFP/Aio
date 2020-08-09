from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, TIMESTAMP, Date
from sqlalchemy.ext.declarative import declarative_base


MYSQL_CONFIG = 'mysql+pymysql://root:root@127.0.0.1:3306/userdb'

Base = declarative_base()
engine = create_engine(MYSQL_CONFIG, encoding='utf-8', echo=True, pool_size=50, max_overflow=50, pool_recycle=14000)

# 创建会话实例对象
Session = sessionmaker(bind=engine)
session = Session()


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String(200), nullable=False)
    pub_date = Column(String(200), nullable=False)


def init_db():
    """创建所有定义的表到数据库中"""
    Base.metadata.create_all(engine)


def drop_db():
    """从数据库中删除所有定义的表"""
    Base.metadata.drop_all(engine)


def init_data():
    session.add_all([
        Question(question_text='我是谁？', pub_date='2020-07-08'),
        Question(question_text='我在哪？', pub_date='2020-07-08'),
        Question(question_text='我为啥在这？', pub_date='2020-07-08'),
        Question(question_text='你是谁？', pub_date='2020-07-08')
    ])

    session.commit()


if __name__ == '__main__':
    # # 执行创建表
    init_db()
    #
    # # 初始化数据
    # init_data()

    # ques_obj = session.query(Question).filter_by().scalar()
    # print(ques_obj.group.name)
