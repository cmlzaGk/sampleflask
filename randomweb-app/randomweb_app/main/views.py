import json
from flask import render_template, Response
from . import main
from ..random_creator import random_int


@main.route('/')
@main.route('/betterrandomhome')
def taskeditor():
    return render_template('betterrandom.html')


@main.route('/betterrandomservice', methods=['POST'])
def betterrandomservice():
    result = {'random_int': random_int()}
    result_json = json.dumps(result)
    return Response(result_json, mimetype= 'application/json')
