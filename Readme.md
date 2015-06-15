![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)

ckanext-contacto
================
Esta extensión proporciona un formulario de contacto, con él podemos diseñar un formulario que, una vez relleno, se envía por correo electrónico.
Esta extensión ha sido desarrollada para [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) como formulario de contacto en la que los usuarios que crean aplicaciones usando datosabiertos.malaga.eu, nos informan de las características, ubicación y enlaces disponibles de las aplicaciones.

<b>IMPORTANTE:</b>

Esta extensión funciona para CKAN 2.2 o anteriores, para versiones superiores esta versión <b>NO ES COMPATIBLE</b>.
Para usar la extensión ckanext-contacto en CKAN 2.3 o superiores, deberá usar la rama pertinente de este repositorio.

Esta extensión funciona para CKAN 2.3 y superiores, para versiones anteriores esta versión <b>NO ES COMPATIBLE</b>.
Para usar la extensión ckanext-contacto en CKAN 2.2 o anteriores, deberá usar la rama pertinente de este repositorio.

v2.0-CKAN2.3-respon
###ckanext-contacto (en)
This CKAN extension provides a contact form. You can design a form that and it will be sent by email.
This CKAN extension has been developed for [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu). This extension is used for developers and IT that use our opendata files to inform us a new applications characteristics.

<b>NOTE:</b>

This extension works for CKAN 2.2 and less versions.
If you want to use this extension for CKAN 2.2 and above, you have to use [this](https://github.com/damalaga/ckanext-contacto/) branch.

This extension works for CKAN 2.3 and + versions.
If you want to use this extension for CKAN 2.2 or less, you have to use [this branch](https://github.com/damalaga/ckanext-contacto/tree/v1.0-for-CKAN-2.2-y-ant).
v2.0-CKAN2.3-respon

##Cómo funciona ?
Una vez el formulario es rellenado por un usuario que no tiene que estar logado, al pulsar el botón "enviar" se genera el cuerpo del correo mediante una función Javascript (en nuestro caso, la función concatena todos los campos del formulario) y es enviado a una dirección de correo electrónica que está configurada en el fichero .ini.
Esta extensión tiene un método muy parecido a mailer.py, pero está adaptado a las necesidades de la extensión.
###How does it works ?
Form is filled by an user (not login needed), them user presses "Send" buttom and a Javascript creates a body email concatening fields (this Javascript can be change). Body is sent by email to a sender that is configure into ini file. 
This CKAN extension has implemented a method that it is similar to mailer.py. But several modifications where required, so this extension does not use mailer.py original.

##Posibles modificaciones
* form.html tiene una función Javascript que compone el cuerpo del correo electrónico, esta función puede ser modificada para que generar otro cuerpo del correo, pero el id tiene que existir, ya que, será el cuerpo del correo que se envía y, además, llamarse mailbody que es el parámetro que espera el generador de correo.
* Existe un parámetro de configuración que podemos añadir al fichero .ini que es el html al que se dirigirá el formulario tras el envío de correo, si no se especifica, irá a /form_result.html.
* El fichero form_result.html puede ser modificado libremente.
* Estos mensajes están parametrizados y pueden ser traducidos en el fichero ckan.po del lenguaje en cuestión.
<pre>
<code>"Your email has been sent...Thanks"</code>
<code>"An error occurred while sending the mail, please contact us "</code>
<code>"Contact us"</code>
<code>"Text about contact us"</code>
</pre>

### Available changes
* form.html: this file shows form field. All fields can be removed except mailbody and contactmail, because these fields are used to send mail and method expected this id fields.
* form_contact.html shows "what happened" after sent mail, but you can configure and change this file, and ckan can open another file. If you want to change this, you must add ckan_contacto.form_result into ini config and write new html file, form_contact.html is showed by default.
* These messages are parameterised and can be translate in ckan.po file:
<pre>
<code>"Your email has been sent...Thanks"</code>
<code>"An error occurred while sending the mail, please contact us "</code>
<code>"Contact us"</code>
<code>"Text about contact us"</code>
</pre>

##Importante
Los siguientes campos, son usados por contact.py, por lo que deben estar rellenos y tener ese id.
* 'mailbody': contenido del cuerpo del correo electrónico (en nuestro caso se rellena con la función Javascript).
* 'contactmail': email de quien envía el correo.

###Notice
There are two required input text: mailbody and contactmail. These two field are expected to be filled.

##Instalación de la extensión
* descargar el fichero en /ckan/lib/default/src/
* ir al directorio cd /ckan/lib/default/src/ckanext-contacto
* activar el entorno . /....activate
* instalar: python setup.py develop

### How can I install de extension ?
* Download this extension in  /ckan/lib/default/src/
* Go to cd /ckan/lib/default/src/ckanext-contacto
* Active enviroment  . /....activate
* Execute: python setup.py develop

##Configuración
- Añadir los siguientes parámetros en el fichero ini:
<pre>
<code>ckan_contacto.recipient_name = #Nombre del destinatario.</code>
<code>ckan_contacto.recipient_email = #Correo electrónico del destinatario (en nuestro caso el personal encargado de dar de alta las aplicaciones).</code>
<code>ckan_contacto.subject = #Asunto del correo.</code>
<code>ckan_contacto.form_result = #Fichero html que debe abrirse tras el envío de correo.</code>
</pre>
- Hay que añadir la extensión "contacto" a los plugins de ckan <pre><code>ckan.plugins = ....contacto</code></pre>
- Llamar al formulario con /contacto/form.html

###Configuration
- You have to add this parameter into .ini config file
<pre>
<code>ckan_contacto.recipient_name = #Recipient name </code>
<code>ckan_contacto.recipient_email = # Recipient email (that is: who is going to recieve this mail...your CKAN admin, I suppose :)</code>
<code>ckan_contacto.subject = # Mail subject</code>
<code>ckan_contacto.form_result = #html file will be opened after CKAN has sent a mail.</code>
- add contact extension as plugin:<pre><code>ckan.plugins = ... contacto</code></pre>
- Finally you have to call contact form /contacto/form.html

## Licencia
El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo en el cabecero o pie de página a modo de reconocimiento a Datos abiertos Málaga. Gracias!
### License
This code can be use and modified. But if you use our code or part of it, please, we ask for you include our logo on header or footer as a thank. Thanks!

![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)


