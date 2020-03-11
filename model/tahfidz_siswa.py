#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class tahfidz_siswa(models.Model):
    """aktivitas tahfidz"""

    _name = "cdn.tahfidz_siswa"
    name = fields.Char( required=True, string="Name",  help="")
    tgl_tahfidz = fields.Date( string="Tgl tahfidz",  help="")
    tambah_halaman = fields.Integer( string="Tambah halaman",  help="")
    murojaah_halaman = fields.Integer( string="Murojaah halaman",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


    status_hafalan_id = fields.Many2one(comodel_name="cdn.status_hafalan",  string="Status hafalan",  help="")
    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  string="Siswa",  help="")
    ustadz_id = fields.Many2one(comodel_name="res.partner",  string="Ustadz",  help="")
