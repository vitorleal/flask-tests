from flask  import Flask, jsonify, abort, make_response

app = Flask(__name__)

#Init the app
if __name__ == '__main__':
    app.run(debug=True)
