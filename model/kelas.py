#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class kelas(models.Model):

    _name = "cdn.kelas"
    name = fields.Char( required=True, string="Name",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


    kelas_paralel_ids = fields.One2many(comodel_name="cdn.kelas_paralel",  inverse_name="kelas_id",  string="Kelas paralels",  help="")
