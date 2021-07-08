### Ejemplo básico odoo 14

Creación de un módulo basico en Odoo 14.
En la carpeta instalacionodoo se  encuentra un script para instalarlo en Linux.

Nos posicionamos en /opt/osoo/odoo y ejecutamos

~~~~
sudo ./odoo-bin scaffold ejemplo ./addons/
~~~~

Siendo ejemplo el nombre del módulo. 

 En models/models.py añadimos la defininón del nuevo modelo:
~~~~

from odoo import models, fields, api

class persona(models.Model):
	_name = 'ejemplo.persona'
	_description = 'model persona'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	telefono = fields.Char(string='Teléfono',required=True)
~~~~

name es el nombre del campo que se utilizará como índice, siempre se debe llamar así.


