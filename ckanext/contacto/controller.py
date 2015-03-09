import contact as c
from ckan.lib.base import BaseController, request
import ckan.lib.base as base

import pylons.config as config

class ContactController(BaseController):
	def send_contact(self):
		return c.send_mail(self, request.params.get('mailbody'), request.params.get('contactmail'))
