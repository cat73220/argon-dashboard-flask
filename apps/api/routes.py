# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present WatanabeHakase
"""

from apps.api import blueprint
from flask import render_template, request
from apps import db
import json
#from flask_login import login_required
#from jinja2 import TemplateNotFound

class Soracom(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  raw_data = db.Column(db.String, nullable=True)

@blueprint.route('/api')
def list():
    print('GET(Default)')
    soracoms = Soracom.query.all()
    for soracom in soracoms:
        print( '%s => %s' % (soracom.id, soracom.raw_data ))
    return render_template('home/helloworld.html', segment='helloworld', soracoms=soracoms)

@blueprint.route('/api', methods=['POST'])
def register():
    print('POST')
    print(json.dumps(request.json))
    soracom = Soracom(
      raw_data = json.dumps(request.json)
    )
    db.session.add(soracom)
    db.session.commit()
    return {'result': 'ok'}

@blueprint.route('/api/<id>', methods=['PUT'])
def modify(id):
    print('PUT')
    print(json.dumps(request.json))
    return {'result': 'ok', 'id': id}

@blueprint.route('/api/<id>', methods=['DELETE'])
def delete(id):
    print('DELETE')
    return {'result': 'ok', 'id': id}
