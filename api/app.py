from flask import Response
from flask_api import FlaskAPI
from flask import request
import markdown

from api import OpenPaymentsBL

app = FlaskAPI(__name__)


@app.route("/specialties/", methods=['GET'])
def get_specialties():
    specialties = OpenPaymentsBL.OpenPaymentsBL.get_specialties()
    if specialties is None:
        return Response(status=500, response='Error in get specialties')
    return specialties


@app.route("/kol/<string:specialty>", methods=['GET'])
def get_kol(specialty):
    if 'limit' in request.args:
        limit = int(request.args['limit'])
        results = OpenPaymentsBL.OpenPaymentsBL.get_kol_by_specialty(specialty, limit)
    else:
        results = OpenPaymentsBL.OpenPaymentsBL.get_kol_by_specialty(specialty)
    if results is None:
        return Response(status=500, response='Error in get KOL for {}'.format(specialty))
    return results


if __name__ == "__main__":
    app.run()
