#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class status_hafalan(models.Model):
    """ref status hafalan"""

    _name = "cdn.status_hafalan"
    name = fields.Char( required=True, string="Name",  help="")
    nilai = fields.Integer( string="Nilai",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


