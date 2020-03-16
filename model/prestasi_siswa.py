#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class prestasi_siswa(models.Model):
    """mencatat prestasi siswa"""

    _name = "cdn.prestasi_siswa"
    name = fields.Char( string="No. Referensi", readonly=True, help="", default="Auto")
    tgl_prestasi = fields.Date( string="Tanggal prestasi", default=fields.Date.context_today, required=True, help="")
    tingkat_prestasi = fields.Selection(selection=[('Internal','Internal'),('Lokal','Lokal'),('Kecamatan','Kecamatan'),('Kota','Kota'),('Propinsi','Propinsi'),('Nasional','Nasional'),('Internasional','Internasional')],  string="Tingkat prestasi",  help="")
    juara_ke = fields.Char( string="Juara ke",  help="")
    jns_prestasi_id = fields.Many2one(comodel_name="cdn.jns_prestasi",  string="Jenis prestasi",  help="")
    siswa_id = fields.Many2one(comodel_name="cdn.siswa", required=True,  string="Siswa",  help="")
    keterangan =  fields.Text(string='Keterangan')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('cdn.prestasi_siswa')
        return super(prestasi_siswa, self).create(vals)
