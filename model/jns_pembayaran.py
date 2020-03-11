#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class jns_pembayaran(models.Model):

    _name = "cdn.jns_pembayaran"
    name = fields.Char( required=True, string="Name",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")
    nominal = fields.Integer( string="Nominal",  help="")
    is_angsuran = fields.Boolean( string="Is angsuran",  help="")
    jml_angsuran = fields.Integer( string="Jml angsuran",  help="")
    nominal_angsuran = fields.Integer( string="Nominal angsuran",  help="")
    tgl_bayar_bulanan = fields.Integer( string="Tgl bayar bulanan",  help="")
    tgl_jth_tempo = fields.Date( string="Tgl jth tempo",  help="")


