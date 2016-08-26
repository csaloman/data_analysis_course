from flask_api import FlaskAPI
from flask import request
import markdown

from api import OpenPaymentsBL

app = FlaskAPI(__name__)


@app.route("/specialties/", methods=['GET'])
def get_specialties():
    return OpenPaymentsBL.OpenPaymentsBL.get_specialties()


@app.route("/kol/<string:specialty>", methods=['GET'])
def get_kol(specialty):
    return OpenPaymentsBL.OpenPaymentsBL.get_kol_by_specialty(specialty)


if __name__ == "__main__":
    app.run()
