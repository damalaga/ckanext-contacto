import contact as c
from ckan.lib.base import BaseController, request
import ckan.lib.captcha as captcha
import ckan.lib.base as base

import pylons.config as config

render = base.render

class ContactController(BaseController):
	def send_contact(self):
		if 'ckan.recaptcha.publickey' in config:
			try:
				captcha.check_recaptcha(request)
			except captcha.CaptchaError:
				error_msg = _(u'Bad Captcha. Please try again.')
				h.flash_error(error_msg)
				return render('contacto/form.html')
		return c.send_mail(self, request.params.get('mailbody'), request.params.get('contactmail'))
