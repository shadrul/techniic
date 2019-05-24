import webapp2
import jinja2
import os
import json
from sets import  Set
import session_handler 
import urllib
import jinja2
import json
from google.appengine.api import urlfetch

import ast




jinja_environment = jinja2.Environment(autoescape=True,
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'template')))

url="/"

class Main(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('index.html')
		self.response.write(home.render())

class Blank(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('hello_world.html')
		self.response.write(home.render())

class Contact(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('contact.html')
		self.response.write(home.render())

class Blank1(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('humbleweb.html')
		self.response.write(home.render())


# class Contact(webapp2.RequestHandler):
#     def get(self):
#     	if self.request.get('id'):
#             values={'email':str(self.request.get('id'))}
#         else:
#             values={'email':''}
            
#     	home = jinja_environment.get_template('contactus.html')
#         self.response.write(home.render(values))

# class leads_details(webapp2.RequestHandler):
#     def post(self):
        
#         email = self.request.get('email')
#         name = self.request.get('name')
#         phone = self.request.get('phone')
#         content = self.request.get('content')
#         # print name,phone,content
#         mailHandler.sendMail().sendLeadsDetails('tech.innobins@gmail.com', email,name,phone,content)
#         self.redirect('/contactus')
#         self.response.out.write("success")

# class Error(session_handler.BaseSessionHandler):
# 	def get(self):
# 		home = jinja_environment.get_template('404.html')
# 		self.response.write(home.render())


# class Services(session_handler.BaseSessionHandler):
# 	def get(self):
# 		home = jinja_environment.get_template('services.html')
# 		self.response.write(home.render())


		

# class ContactUs(session_handler.BaseSessionHandler):
# 	def get(self):
# 		home = jinja_environment.get_template('contact.html')
# 		self.response.write(home.render())

# class Blog(session_handler.BaseSessionHandler):
# 	def get(self):
# 		home = jinja_environment.get_template('blog.html')
# 		self.response.write(home.render())

# class Innotrack(session_handler.BaseSessionHandler):
# 	def get(self):
# 		home = jinja_environment.get_template('innotrack.html')
# 		self.response.write(home.render())



# class Mtrack(session_handler.BaseSessionHandler):
# 	def get(self):
# 		home = jinja_environment.get_template('mtrack.html')
# 		self.response.write(home.render())

# class Innoprolife(session_handler.BaseSessionHandler):
# 	def get(self):
# 		home = jinja_environment.get_template('innoprolife.html')
# 		self.response.write(home.render())

# class Team(session_handler.BaseSessionHandler):
# 	def get(self):
# 		home = jinja_environment.get_template('team.html')
# 		self.response.write(home.render())

# class Appstore(session_handler.BaseSessionHandler):
# 	def get(self):
# 		home = jinja_environment.get_template('app.html')
# 		self.response.write(home.render())



class SSLEncrypt(session_handler.BaseSessionHandler):
	def get(self):
		self.response.write('0wCPmJXu9F-YwKEPp4Zi_XJnNFj6zDAdHzK4LuenMNc.iETOPsLx79qW-4SSuNL6DdBRj2-p3Ty-hL7cYOT54wg')

class SSLEncryptRoot(session_handler.BaseSessionHandler):
	def get(self):
		self.response.write('QXQRXiB8wSV3P71Ai7DfSyFM0VZkpX69KOJR8uuYNDw.iETOPsLx79qW-4SSuNL6DdBRj2-p3Ty-hL7cYOT54wg')

class SerVer(session_handler.BaseSessionHandler):
    def get(self):
        home = jinja_environment.get_template('404.html')
        self.response.write(home.render())




app = webapp2.WSGIApplication([
	('/',Main),
	# ('/leads_details',leads_details),
	('/hello_world',Blank),
	('/contact',Contact),
	('/humbleweb',Blank1),
	# ('/services',Services),
	# ('/blog',Blog),
	# ('/mtrack',Mtrack),
	# ('/innoprolife',Innoprolife),
	# ('/team',Team),
	# ('/contact',ContactUs),
	# ('/app',Appstore),
	('/.well-known/acme-challenge/0wCPmJXu9F-YwKEPp4Zi_XJnNFj6zDAdHzK4LuenMNc',SSLEncrypt),
	('/.well-known/acme-challenge/QXQRXiB8wSV3P71Ai7DfSyFM0VZkpX69KOJR8uuYNDw',SSLEncryptRoot),
	('/.*',SerVer)
	

	
	
	
	


], debug=True,
config = session_handler.myconfig_dict)
