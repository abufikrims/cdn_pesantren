#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class tahsin_siswa(models.Model):

    _name = "cdn.tahsin_siswa"
    name = fields.Char( required=True, string="Name",  help="")
    tgl_tahsin = fields.Date( string="Tgl tahsin",  help="")
    tahsin_halaman = fields.Integer( string="Tahsin halaman",  help="")
    tahsin_jilid = fields.Integer( string="Tahsin jilid",  help="")
    nilai = fields.Integer( string="Nilai",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  string="Siswa",  help="")
