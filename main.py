#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
#
# oauth for push in cmd: appcfg.py --oath2 update ~/path-to-project/
import webapp2
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)

################################################################################
#
# Rendering Functions
#
################################################################################
class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

################################################################################
#
# Shopping List.  Links to shopping_list.html
#
################################################################################
class ShoppingList(Handler):
	def get(self):
		items = self.request.get_all("food")
		self.render("shopping_list.html", items = items)

################################################################################
#
# Fizzbuzz.  Links to fizzbuzz.html
#
################################################################################
class FizzBuzz(Handler):
	def get(self):
		n = self.request.get("n")
		if n:
			n = int(n)
		else:
			n = 0
		self.render("fizzbuzz.html", n = n)
		
############################################################
#
#Main page listing all path's within this project
#
############################################################
class MainPage(webapp2.RequestHandler):
	def write_form(self, host=""):
		mainForm="""
			<H1>You have reached the main page</H1>
			<p>The following links can be found from this project:
				<div>
					%(list)s
				</div>
			</p>
			"""
		host = str(self.request.url)
		pages = self.makeList(host, "shopping", "fizzbuzz?n=100")
		self.response.out.write(mainForm % {"list": pages})

	def get(self):
		self.write_form()

	def makeList(self, host, *args):
			#args = args or [""]
			pageList = ""
			for page in args:
				path = str(host)+str(page)
				name = str(page)
				pageList += '<li><a href="' + path + '">' + page + '</a></li>'
			return pageList
		
app = webapp2.WSGIApplication([
	('/', MainPage),
	('/shopping', ShoppingList),
	('/fizzbuzz', FizzBuzz)], 
	debug=True)