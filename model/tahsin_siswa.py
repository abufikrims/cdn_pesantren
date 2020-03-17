#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class tahsin_siswa(models.Model):

    _name = "cdn.tahsin_siswa"
    name = fields.Char(string="No. Referensi",  help="", readonly=True, default='Auto')
    tgl_tahsin = fields.Date( string="Tanggal Aktivitas", default=fields.Date.context_today, required=True, help="")
    tahsin_halaman = fields.Integer( string="Tahsin halaman",  help="")
    tahsin_jilid = fields.Integer( string="Tahsin jilid",  help="")
    nilai = fields.Integer( string="Nilai",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


    siswa_id = fields.Many2one(comodel_name="cdn.siswa", required=True, string="Siswa",  help="")
    ustadz_id = fields.Many2one(comodel_name="res.partner",  string="Ustadz",  help="")

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('cdn.tahsin_siswa')
        return super(tahsin_siswa, self).create(vals)
