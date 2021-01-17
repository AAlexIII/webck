
from flask import Flask, request, jsonify,render_template,make_response

from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['GET', 'POST'])
def add_message():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        print(request.environ['REMOTE_ADDR'])
    else:
        print(request.environ['HTTP_X_FORWARDED_FOR'])
    p = json.loads(request.get_data().decode("utf-8"))
    p = json.loads(request.get_data())
    print(p['password'])
    return make_response({'log':'1','pas':'3'})


if __name__ == '__main__':
    app.run()
