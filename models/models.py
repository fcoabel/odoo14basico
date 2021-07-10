# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ejemplo(models.Model):
#     _name = 'ejemplo.ejemplo'
#     _description = 'ejemplo.ejemplo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



from odoo import models, fields, api

class persona(models.Model):
	_name = 'ejemplo.persona'
	_description = 'model persona'

	name = fields.Char('DNI',required=True,unique=True)
	nombre = fields.Char(string='Nombre',required=True)
	telefono = fields.Char(string='Teléfono',required=True)
	fecha_nacimiento = fields.Date(string="Fevha de nacimiento",required=True)