#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class keuangan_siswa(models.Model):

    _name = "cdn.keuangan_siswa"
    name = fields.Char( required=True, string="Name",  help="")
    nominal_total = fields.Integer( string="Nominal total",  help="")
    jml_angsuran = fields.Integer( string="Jml angsuran",  help="")
    nominal_angsuran = fields.Integer( string="Nominal angsuran",  help="")
    tgl_jth_tempo = fields.Date( string="Tgl jth tempo",  help="")


    jns_pembayaran_id = fields.Many2one(comodel_name="cdn.jns_pembayaran",  string="Jns pembayaran",  help="")
    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  string="Siswa",  help="")
