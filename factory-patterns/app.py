from flask import Flask, jsonify

app = Flask(__name__)


# Health Route
@app.route('/health')
def get_serviceB_data():
    data = {
        "msg": "I'm alive"
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
