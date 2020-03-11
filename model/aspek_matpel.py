#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class aspek_matpel(models.Model):

    _name = "cdn.aspek_matpel"
    name = fields.Char( required=True, string="Name",  help="")
    nilai_kkm = fields.Float( string="Nilai kkm",  help="")
    nilai_max = fields.Float( string="Nilai max",  help="")
    nilai_min = fields.Float( string="Nilai min",  help="")


    matpel_id = fields.Many2one(comodel_name="cdn.matpel",  string="Matpel",  help="")
