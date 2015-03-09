import paste.deploy.converters

import ckan.lib.helpers as h

import ckan.lib.base as base

from ckan.common import _
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email import Utils

import pylons.config as config

from time import time

render = base.render

import logging

logger = logging.getLogger(__name__)
logger.setLevel (logging.DEBUG)

class ContactException(Exception):
    pass

#redefine mailer.py
def send_mail(self, data, contactmail):

    recipient_name = config['ckan_contacto.recipient_name']
    recipient_email = config['ckan_contacto.recipient_email']
    subject = config['ckan_contacto.subject']

    error_flag = False
    mail_from = contactmail
    body = data
    headers={}
    msg = MIMEText(body.encode('utf-8'), 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = ("%s ") % (mail_from)
    recipient = u"%s <%s>" % (recipient_name, recipient_email)
    msg['To'] = Header(recipient, 'utf-8')
    msg['Date'] = Utils.formatdate(time())

    # Send the email using Python's smtplib.
    smtp_connection = smtplib.SMTP()
    if 'smtp.test_server' in config:
        # If 'smtp.test_server' is configured we assume we're running tests,
        # and don't use the smtp.server, starttls, user, password etc. options.
        smtp_server = config['smtp.test_server']
        smtp_starttls = False
        smtp_user = None
        smtp_password = None
    else:
        smtp_server = config.get('smtp.server', 'localhost')
        smtp_starttls = paste.deploy.converters.asbool(
                config.get('smtp.starttls'))
        smtp_user = config.get('smtp.user')
        smtp_password = config.get('smtp.password')
    smtp_connection.connect(smtp_server)
    try:

        # Identify ourselves and prompt the server for supported features.
        smtp_connection.ehlo()

        # If 'smtp.starttls' is on in CKAN config, try to put the SMTP
        # connection into TLS mode.
        if smtp_starttls:
            if smtp_connection.has_extn('STARTTLS'):
                smtp_connection.starttls()
                # Re-identify ourselves over TLS connection.
                smtp_connection.ehlo()
            else:		
	        error_flag = True
		logger.error('Error: SMTP server does not support STARTTLS' )
		abort(400, _('An error occurred while sending the mail, please contact us ') + recipient_email )
                raise ContactException("SMTP server does not support STARTTLS")

        # If 'smtp.user' is in CKAN config, try to login to SMTP server.
        if smtp_user:
            assert smtp_password, ("If smtp.user is configured then "
                    "smtp.password must be configured as well.")
            smtp_connection.login(smtp_user, smtp_password)

        smtp_connection.sendmail(mail_from, [recipient_email], msg.as_string())

    except smtplib.SMTPException, e:
        error_flag = True
	logger.error('Error: smtplib.SMTPException' + e)
	abort(400, _('An error occurred while sending the mail, please contact us ') + recipient_email )
        msg_error = '%r' % e
        raise ContactException(msg_error)
    finally:
        smtp_connection.quit()
	if not error_flag:
		logger.info('Mail sent. Mail: ' + contactmail + 'Body:'+data)
		h.flash_success(_('Your email has been sent...Thanks'))
	# if ckan_contacto.form_result exist, it opens ckan_contacto.form_result html, if not, it opens default html
	if 'ckan_contacto.form_result' in config:
		return render(config['ckan_contacto.form_result'])
	else:
		return render('contacto/form_result.html')




