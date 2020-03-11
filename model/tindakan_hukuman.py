#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class tindakan_hukuman(models.Model):

    _name = "cdn.tindakan_hukuman"
    name = fields.Char( required=True, string="Name",  help="")
    poin = fields.Integer( string="Poin",  help="")
    level_pelanggaran = fields.Selection(selection=[('Ringan','Ringan'),('Sedang','Sedang'),('Berat','Berat'),('Dikeluarkan','Dikeluarkan')],  string="Level pelanggaran",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


