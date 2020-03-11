#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class matpel(models.Model):

    _name = "cdn.matpel"
    name = fields.Char( required=True, string="Name",  help="")
    nilai_kkm = fields.Float( string="Nilai kkm",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


    aspek_matpel_ids = fields.One2many(comodel_name="cdn.aspek_matpel",  inverse_name="matpel_id",  string="Aspek matpels",  help="")
