#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class kelas_paralel(models.Model):

    _name = "cdn.kelas_paralel"
    name = fields.Char( required=True, string="Name",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


    siswa_ids = fields.One2many(comodel_name="cdn.siswa",  inverse_name="kelas_paralel_id",  string="Siswas",  help="")
    kelas_id = fields.Many2one(comodel_name="cdn.kelas",  string="Kelas",  help="")
    ustadz_id = fields.Many2one(comodel_name="res.partner",  string="Ustadz",  help="")
