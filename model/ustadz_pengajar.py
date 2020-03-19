#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ustadz_pengajar(models.Model):
    """inherit hr.employee"""

    _name = "hr.employee"

    _inherit = "hr.employee"
    is_tahfidz = fields.Boolean( string="Ustadz Tahfidz ?",  help="")
    is_ustadz  = fields.Boolean( string="Ustadz Akademik ?",  help="")


