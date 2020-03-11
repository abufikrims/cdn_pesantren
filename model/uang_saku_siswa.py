#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class uang_saku_siswa(models.Model):
    """transaksi uang saku siswa"""

    _name = "cdn.uang_saku_siswa"
    name = fields.Char( required=True, string="Name",  help="")
    tgl_transaksi = fields.Date( string="Tgl transaksi",  help="")
    jns_transaksi = fields.Selection(selection=[('Masuk','Masuk'),('Keluar','Keluar')],  string="Jns transaksi",  help="")
    nominal_transaksi = fields.Integer( string="Nominal transaksi",  help="")
    state = fields.Selection(selection=[('Draft','Pengajuan'),('Approval','Verifikasi')],  string="State",  help="")
    tgl_verifikasi = fields.Date( string="Tgl verifikasi",  help="")
    transaksi_via = fields.Char( string="Transaksi via",  help="")


    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  string="Siswa",  help="")
