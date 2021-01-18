import pymongo
from flask import Flask, request, jsonify, render_template, make_response

from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient(
    "mongodb+srv://admin:super@cluster0.jucg0.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.web


@app.route('/login', methods=['GET', 'POST'])
def add_message():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    p = json.loads(request.get_data())
    user = db.users.find_one({'log': p["login"]})
    if user:
        if user['pas'] == p['password']:
            db.users.update_one({'log': p["login"]},
                                {'$set': {'ip': str(ip)}})
            return make_response({'is': True, 'pass': True})
        else:
            return make_response({'is': True, 'pass': False})
    else:
        return make_response({'is': False})


@app.route('/regist', methods=['GET', 'POST'])
def add_message1():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    p = json.loads(request.get_data())
    user = db.users.find_one({'log': p["login"]})
    if user:
        return make_response({'is': False})
    else:
        db.users.insert({
            'ip': str(ip),
            "log": p['login'],
            "pas": p['password'],
            'name': p['name'],
            'fam': p['fam'],
            'work': p['work'],
            '1': False,
            '2': False,
            '3': False,
            '4': False,
        })
        return make_response({'is': True})


@app.route('/check', methods=['GET', 'POST'])
def add_message2():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    user = db.users.find_one({'ip': str(ip)})
    if user:
        return make_response({'is': True, 'name': user['name'], 'fam': user['fam']})
    else:
        return make_response({'is': False})


@app.route('/out', methods=['GET', 'POST'])
def add_message3():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    db.users.update_one({'ip': str(ip)},
                        {'$set': {'ip': '123'}})
    return make_response({'is': False})


@app.route('/kurs', methods=['GET', 'POST'])
def add_message4():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    user = db.users.find_one({'ip': str(ip)})
    if user:
        return make_response({'is': True,
                              '1': user['1'],
                              '2': user['2'],
                              '3': user['3'],
                              '4': user['4']})
    else:
        return make_response({'is': False})


@app.route('/new', methods=['GET', 'POST'])
def add_message5():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    p = request.get_data().decode('utf-8')
    user = db.users.find_one({'ip': str(ip)})
    if user:
        b = not user[p[0]]
        db.users.update_one({'ip': str(ip)},
                            {'$set': {p[0]: b}})
        user = db.users.find_one({'ip': str(ip)})
        return make_response({'is': True,
                              '1': user['1'],
                              '2': user['2'],
                              '3': user['3'],
                              '4': user['4']})
    else:
        return make_response({'is': False})


if __name__ == '__main__':
    app.run()
