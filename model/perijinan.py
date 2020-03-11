#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class perijinan(models.Model):

    _name = "cdn.perijinan"
    name = fields.Char( required=True, string="Name",  help="")
    tgl_ijin = fields.Date( string="Tgl ijin",  help="")
    lama_ijin = fields.Integer( string="Lama ijin",  help="")
    state = fields.Selection(selection=[('Draft','Pengajuan'),('Approve','Disetujui'),('Reject','Ditolak'),('Permission','Ijin Keluar'),('Return','Kembali')],  string="State",  help="")
    penjemput = fields.Char( string="Penjemput",  help="")
    keperluan = fields.Text( string="Keperluan",  help="")
    tgl_kembali = fields.Datetime( string="Tgl kembali",  help="")
    catatan = fields.Text( string="Catatan",  help="")


    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  string="Siswa",  help="")
