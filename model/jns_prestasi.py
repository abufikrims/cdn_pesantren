#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class jns_prestasi(models.Model):
    """ref jenis prestasi"""

    _name = "cdn.jns_prestasi"
    name = fields.Char( required=True, string="Name",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


