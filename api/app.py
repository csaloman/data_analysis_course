from flask_api import FlaskAPI
import markdown

app = FlaskAPI(__name__)


@app.route("/specialties/", methods=['GET'])
def get_specialties():
    return ['a', 'b', 'c']


@app.route("/kol/<string:specialty>", methods=['GET'])
def get_kol(specialty):
    return [specialty, 'a', 'c', 'd']


if __name__ == "__main__":
    app.run()
