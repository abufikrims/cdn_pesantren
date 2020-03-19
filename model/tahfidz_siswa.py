#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class tahfidz_siswa(models.Model):
    """aktivitas tahfidz"""

    _name = "cdn.tahfidz_siswa"
    name = fields.Char(string="No. Referensi",  help="", readonly=True, default='Auto')
    tgl_tahfidz = fields.Date( string="Tanggal Aktivitas", default=fields.Date.context_today, required=True, help="")
    tambah_halaman = fields.Integer( string="Hafalan halaman",  help="")
    murojaah_halaman = fields.Integer( string="Murojaah halaman",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


    status_hafalan_id = fields.Many2one(comodel_name="cdn.status_hafalan",  string="Status hafalan",  help="")
    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  required=True, string="Siswa",  help="")
    ustadz_id = fields.Many2one(comodel_name="hr.employee",  string="Ustadz",  help="")

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('cdn.tahfidz_siswa')
        return super(tahfidz_siswa, self).create(vals)

