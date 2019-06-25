#!/usr/bin/env python

__author__ = 'SLZ'

'''
digwebs framework controller.
'''

from digwebs.web import current_app

@current_app.view('home.html')
@current_app.get('/')
def hello_world():
    return dict()

@current_app.view('blogs.html')
@current_app.get('/views/blogs')
def list_blogs():
	blogs = []
	blogs.append({
	'title':'What is digwebs',
	'description':'A tiny web framework called digwebs which is developed by Python.',
	'detail_link':'######'})
	blogs.append({
	'title':'Why you should use digwebs',
	'description':'Digwebs is a Python web framework, which you can use to accelerate the development process of building a web service.',
	'detail_link':'######'})
	blogs.append({'title':'How to use digolds web framework','description':'You can use digwebs in a few steps. First pull the source code. Second install jinja2. Finally run python .\digwebs\project_generator.py to generate the project file structure.','detail_link':'######'})
	return dict(template_blogs=blogs)