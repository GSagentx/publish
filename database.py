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
#from codecs import encode
#import re
#import cgi

#def escape_html(s):
#	return cgi.escape(s, quote=True)

############################################################
#
#Main page listing all path's within this project
#
############################################################
def write_form(host="http://localhost:9080/"):
	#host = self.request.url
	print(host)
	pages = makeList(str(host), ["login", "rot13"])
	print(pages)
	#self.response.out.write(mainForm % {"first": escape_html(host+"rot13"),
	#									"second": escape_html(host+"login")
	#									})

def makeList(host, args):
	#args = args or [""]
	pageList = ""
	for page in args:
		pageList += '<li><a href="' + host + page + '">' + page + '</a></li>'

	return pageList

write_form()