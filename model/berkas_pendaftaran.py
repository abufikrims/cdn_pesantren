#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class berkas_pendaftaran(models.Model):

    _name = "cdn.berkas_pendaftaran"
    name = fields.Char( required=True, string="Name",  help="")
    keterangan = fields.Text( string="Keterangan",  help="")


    siswa_ids = fields.Many2many(comodel_name="cdn.siswa",  string="Siswas",  help="")
