import ckan.plugins as p

import pylons.config as config

import contact as c


class ContactMailException(Exception):
    pass


class ContactClass(p.SingletonPlugin):

    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)


    p.implements(p.IRoutes, inherit=True)

    def update_config(self, config):
        # add template directory that contains our snippet
		p.toolkit.add_template_directory(config, '/usr/lib/ckan/default/src/ckanext-contacto/ckanext/contacto/theme/templates')
		p.toolkit.add_public_directory (config, '/usr/lib/ckan/default/src/ckanext-contacto/ckanext/contacto/public')



    def before_map(self, map):

	con_controller = 'ckanext.contacto.controller:ContactController'

	map.connect('/send_contact', #url to map path to
	action='send_contact', 
	controller = con_controller) #controller action (method)

	return map

    #iruiz: register helper function
    def get_helpers(self):
        return {}

