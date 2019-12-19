from flask import Flask
from flask import request
import os
from datetime import datetime

app = Flask(__name__, static_url_path='')


@app.route("/")
def root():
    return app.send_static_file('index.html')


@app.route("/<room>")
def room(room):
    return app.send_static_file('index.html')


@app.route("/api/chat/<room>", methods=['POST'])
def post_room(room):
    username = request.form['username']
    maessage = request.form['msg']
    if not os.path.exists('rooms'):
        os.makedirs('rooms')
    file_name = 'rooms/'+room+'.txt'
    file = open(file_name, 'a+', encoding='utf-8')
    # print(datetime.now())
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
    line = '['+date_time+'] '+username+': '+maessage+'\n'
    file.write(line)
    file.close()

    return line


@app.route("/api/chat/<room>")
def get_room(room):
    file_name = 'rooms/'+room+'.txt'
    try:
        file = open(file_name, 'r', encoding='utf-8')
        content = file.read()
        file.close()
        return content
    except IOError as err:
        print(err)
        return ''


# if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(host='0.0.0.0', debug=True, threaded=True, port=8080)
    # app.run(host='localhost', debug=True, threaded=True, port=8080)
