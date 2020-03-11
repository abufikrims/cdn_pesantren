#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class pekerjaan(models.Model):

    _name = "cdn.pekerjaan"
    name = fields.Char( required=True, string="Name",  help="")
    keterangan = fields.Text( string="Keterangan",  help="")


