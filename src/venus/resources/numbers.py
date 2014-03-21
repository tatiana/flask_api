from flask import Blueprint, jsonify, Response


api_numbers = Blueprint('numbers_blueprint', __name__)


NUMBER_TRANSLATOR = {
    1: "one",
    2: "two",
    3: "three",
    10: "ten"
}


def translate_number(number):
    """
    Provided a integer number, return its name in English.
    """
    return NUMBER_TRANSLATOR.get(number, "undefined")


@api_numbers.route("/numbers/<int:number>")
def route_number(number):
    """
    Provided a integer number, return its name in English.
    """
    response = translate_number(number)

    if response:
        return response
    else:
        msg = u"unknown number, sorry"
        response = jsonify({u"error": msg})
        response.status_code = 500
        return response
