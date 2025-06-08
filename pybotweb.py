from bottle import route, run, template, request
from pybot import pybot
import os


@route('/hello')
def hello():
    return template('pybot_template', input_text='', output_text='')


@route('/hello', method='POST')
def do_hello():
    input_text = request.forms['input_text']
    input_image = request.files.input_image
    output_text = pybot(input_text, input_image)
    return template('pybot_template', input_text=input_text, output_text=output_text)


port = int(os.environ.get('PORT',5000))
run(host='0.0.0.0',port=port)

