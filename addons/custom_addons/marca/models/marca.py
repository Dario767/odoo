from odoo import models, fields, api

class Marca(models.Model):
    _name = "marca.marca"
    _description = "Marca"
    _rec_name = "name"
    _order = "name asc"

    name = fields.Char("Nombre", required=True, index=True)
    code = fields.Char("Código", required=True, help="Identificador corto único.")
    active = fields.Boolean("Activo", default=True)
    description = fields.Text("Descripción")
    website = fields.Char("Sitio web")
    logo = fields.Binary("Logo")
    sequence = fields.Integer("Secuencia", default=10, help="Orden en listados.")

    _sql_constraints = [
        ("code_unique", "unique(code)", "El código de la marca debe ser único."),
    ]
