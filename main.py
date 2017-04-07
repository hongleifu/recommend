from flask import Flask, request, render_template 
from flask import redirect, url_for

import os
import os.path

import gensim
from modules import mod_recommend


'''  BASICAL FUNCTIONS BEGIN  '''

app = Flask(__name__, static_url_path='')

@app.route('/error', methods=['GET', 'POST'])
#@interceptor(login_required=False)
def error():
	msg = request.args.get('msg')
	return render_template('error.html',msg=msg)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('error.html',msg=e)


'''  BUSSINESS FUNCTIONS BEGIN  '''


@app.route('/recommend', methods=['GET', 'POST'])
#@interceptor(login_required=True)
def search():
	result = mod_recommend.service(request)
	return result 


'''  MAIN ENTRY  '''
if __name__ == '__main__':
	app.debug = True
	app.run(host="jinrongdao.com",port=5200)
