
from flask import render_template
from . import web

@web.route('/', methods=['GET'])
def root():
    return web.send_static_file('html/setadvertise.html')
    #return render_template('setadvertise.html')

