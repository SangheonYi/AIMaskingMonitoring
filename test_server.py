from flask import Flask

app = Flask(__name__)

@app.route('/pii_demo', methods=['GET'])
def pii_demo():
    return "hello"

if __name__ == '__main__':
    app.run(debug=False)
