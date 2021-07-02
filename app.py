from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/hello', methods=['GET'])
def helloWorld():
    content = {
        'message': 'Hello World'
    }
    return jsonify(content)

if __name__ == '__main__':
    app.run()