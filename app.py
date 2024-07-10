from flask import Flask

app = Flask(__name__)

message = '''
Hello! Amazing progress so far.
You're doing great! Keep up the  work!
'''
@app.route('/')
def hello_world():
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
