#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class kesehatan(models.Model):

    _name = "cdn.kesehatan"
    name = fields.Char( required=True, string="Name",  help="")
    tgl_periksa = fields.Date( string="Tgl periksa",  help="")
    keluhan = fields.Text( string="Keluhan",  help="")
    obat = fields.Text( string="Obat",  help="")
    diperiksa_oleh = fields.Char( string="Diperiksa oleh",  help="")
    kondisi = fields.Selection(selection=[('Periksa','Periksa'),('Pengobatan','Pengobatan'),('Rawat','Rawat'),('Sembuh','Sembuh')],  string="Kondisi",  help="")
    tgl_selesai = fields.Date( string="Tgl selesai",  help="")
    catatan = fields.Text( string="Catatan",  help="")


    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  string="Siswa",  help="")
