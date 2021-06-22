# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date,datetime

class Specialisation(models.Model):
    _name= "medical.specialisation"

    name = fields.Char(string='Nom')

    




