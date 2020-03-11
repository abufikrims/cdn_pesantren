#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ustadz_pengajar(models.Model):
    """inherit res.partner"""

    _name = "res.partner"

    _inherit = "res.partner"
    is_tahfidz = fields.Boolean( string="Is tahfidz",  help="")


