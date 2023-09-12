from flask import Flask, jsonify, request

app = Flask(__name__)

hello = "Message: Hello, Cognum!"

@app.route("/hello",methods=["GET"])
def obter_mensagem():
    return jsonify(hello)

app.run(port=3000,host="localhost",debug=True)