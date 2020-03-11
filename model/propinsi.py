#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class propinsi(models.Model):

    _name = "cdn.propinsi"
    name = fields.Char( required=True, string="Name",  help="")
    keterangan = fields.Text( string="Keterangan",  help="")


