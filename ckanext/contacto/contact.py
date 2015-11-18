import ckan.lib.helpers as h
import ckan.lib.base as base
import pylons.config as config


from ckan.common import _

import ckan.lib.mailer as mailer

import logging


class ContactException(Exception):
    pass

#redefine mailer.py

def send_mail(self, data, contactmail):

    import ckan.lib.mailer

    self.log = logging.getLogger(__name__)

    self.log.info('++correo enviado++ '+data)
    recipient_name = config['ckan_contacto.recipient_name']
    recipient_email = config['ckan_contacto.recipient_email']
    subject = config['ckan_contacto.subject']

    try:
	mailer.mail_recipient(recipient_name,recipient_email , subject, data, headers={})

    except mailer.MailerException, e:
       abort(400, _('An error occurred while sending the mail, please contact us ') + recipient_email )
       h.flash_error(_('It has been an error. Please contact us datosabiertos@malaga.eu'))
       msg_error = '%r' % e
       self.log.error('Error '+ msg_error)
       raise ContactException(msg_error)	
    else:
	render = base.render
	h.flash_success(_('Your email has been sent...Thanks'))
        self.log.info('email send')
	if 'ckan_contacto.form_result' in config:
		return render(config['ckan_contacto.form_result'])
	else:
		return render('contacto/form_result.html/')

