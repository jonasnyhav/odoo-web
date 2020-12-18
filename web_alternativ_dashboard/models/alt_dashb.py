# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AlternativeDasboard(models.Model):
    _name = 'af.dashb'
    _description = 'Model for alternative dashboard.'

    name = fields.Many2one('res.users', string="Namn", default=lambda self: self.env.user)
