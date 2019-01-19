from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    return 'SUCCESSFUL DEPLOYMENT'

# @app.route('/csv', methods=['GET'])
# def index():
#     return 'SUCCESSFUL DEPLOYMENT'
#
# @app.route('/json', methods=['GET'])
# def index():
#     return 'SUCCESSFUL DEPLOYMENT'



if __name__ == "__main__":
    app.run(debug=True, port=33507)
