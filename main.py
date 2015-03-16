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
class MainPage(Handler):
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
		
app = webapp2.WSGIApplication([
	('/', MainPage),
	('/fizzbuzz', FizzBuzz)], 
	debug=True)