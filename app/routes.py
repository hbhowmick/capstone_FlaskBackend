from app import app, db
from flask import render_template, url_for, redirect, request, jsonify
from app.forms import AddressForm


@app.route('/')
@app.route('/index')
@app.route('/index', methods=['GET','POST'])
def index():
    form_Address = AddressForm()
    if form_Address.validate_on_submit():
        street = form_Address.street.data
        city = form_Address.city.data
        state = form_Address.state.data
        zip = form_Address.zip.data
    return render_template('index.html', title='Home', form_Address=form_Address, street=street, city=city, state=state, zip=zip)

@app.route('/')
def upload():
    return render_template('upload.html', title='Upload')

@app.route('/scene')
def scene():
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('scene.html', title='3D Scene')

@app.route('/tilt')
def tilt():
    metadata = {'keywords': 'viewport', 'description':'initial-scale=1, maximum-scale=1, user-scalable=no'}
    return render_template('tilt.html', title='Tilted Scene')
