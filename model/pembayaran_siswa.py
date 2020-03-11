#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class pembayaran_siswa(models.Model):

    _name = "cdn.pembayaran_siswa"
    name = fields.Char( required=True, string="Name",  help="")
    tgl_bayar = fields.Date( string="Tgl bayar",  help="")
    nominal_bayar = fields.Integer( string="Nominal bayar",  help="")
    bayar_via = fields.Char( string="Bayar via",  help="")
    state = fields.Selection(selection=[('Draft','Input'),('Verified','Sudah Verifikasi')],  string="State",  help="")


    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  string="Siswa",  help="")
    jns_pembayaran_id = fields.Many2one(comodel_name="cdn.jns_pembayaran",  string="Jns pembayaran",  help="")
