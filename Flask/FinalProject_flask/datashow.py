import pymysql
from flask import Flask, url_for, render_template, json

app = Flask(__name__, template_folder='./templates')


# Q1
def getData_Q1():
    db = pymysql.connect(
        user='root',
        password='root',
        host='192.168.75.129',
        database='sogou',
        charset='utf8',
        port=3306
    )

    # 获取游标
    cursor = db.cursor()

    # 执行SQL
    cursor.execute('select * from sogou.sogou_Q1')

    # 得到数据
    all_data = cursor.fetchall()

    return all_data


@app.route('/query1Json')
def query1Json():
    all_data = getData_Q1()

    t1 = []
    t2 = []
    for res in all_data:
        t1.append(res[0])
        t2.append(res[1])
        json_value = json.dumps({'keyword': t1, 'count': t2})
        print(json_value)
    return json_value


@app.route('/query1')
def show1():
    return render_template('datashow1.html')


# Q2
def getData_Q2():
    db = pymysql.connect(
        user='root',
        password='root',
        host='192.168.75.129',
        database='sogou',
        charset='utf8',
        port=3306
    )

    # 获取游标
    cursor = db.cursor()

    # 执行SQL
    cursor.execute('select * from sogou.sogou_Q2')

    # 得到数据
    all_data = cursor.fetchall()

    return all_data


@app.route('/query2Json')
def query2Json():
    all_data = getData_Q2()

    t1 = []
    for res in all_data:
        t1.append(res[0])
        json_value = json.dumps({'count': t1})
        print(json_value)
    return json_value


@app.route('/query2')
def show2():
    return render_template('datashow2.html')


# 连接数据库获取数据
def getData_Q3():
    db = pymysql.connect(
        user='root',
        password='root',
        host='192.168.75.129',
        database='sogou',
        charset='utf8',
        port=3306
    )

    # 获取游标
    cursor = db.cursor()

    # 执行SQL
    cursor.execute('select * from sogou.sogou_Q3')

    # 得到数据
    all_data = cursor.fetchall()

    return all_data


@app.route('/query3Json')
def query3Json():
    all_data = getData_Q3()

    t1 = []
    t2 = []
    for res in all_data:
        t1.append(res[0])
        t2.append(res[1])
        json_value = json.dumps({'keyword': t1, 'count': t2})
        print(json_value)
    return json_value


@app.route('/query3')
def show3():
    return render_template('datashow3.html')


# 连接数据库获取数据
def getData_Q4():
    db = pymysql.connect(
        user='root',
        password='root',
        host='192.168.75.129',
        database='sogou',
        charset='utf8',
        port=3306
    )

    # 获取游标
    cursor = db.cursor()

    # 执行SQL
    cursor.execute('select * from sogou.sogou_Q4')

    # 得到数据
    all_data = cursor.fetchall()

    return all_data


@app.route('/query4Json')
def query4Json():
    all_data = getData_Q4()

    t1 = []
    t2 = []
    for res in all_data:
        t1.append(res[0])
        t2.append(res[1])
        json_value = json.dumps({'keyword': t1, 'count': t2})
        print(json_value)
    return json_value


@app.route('/query4')
def show4():
    return render_template('datashow4.html')


if __name__ == '__main__':
    app.run()
