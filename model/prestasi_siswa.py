#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class prestasi_siswa(models.Model):
    """mencatat prestasi siswa"""

    _name = "cdn.prestasi_siswa"
    name = fields.Char( required=True, string="Name",  help="")
    tgl_prestasi = fields.Date( string="Tgl prestasi",  help="")
    tingkat_prestasi = fields.Selection(selection=[('Internal','Internal'),('Lokal','Lokal'),('Kecamatan','Kecamatan'),('Kota','Kota'),('Propinsi','Propinsi'),('Nasional','Nasional'),('Internasional','Internasional')],  string="Tingkat prestasi",  help="")
    juara_ke = fields.Char( string="Juara ke",  help="")


    jns_prestasi_id = fields.Many2one(comodel_name="cdn.jns_prestasi",  string="Jns prestasi",  help="")
    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  string="Siswa",  help="")
