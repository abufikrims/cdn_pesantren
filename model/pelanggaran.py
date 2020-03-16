#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class pelanggaran(models.Model):

    _name = "cdn.pelanggaran"
    name = fields.Char(string="No. Referensi",  help="", readonly=True, default='Auto')
    tgl_pelanggaran = fields.Date( string="Tgl pelanggaran", default=fields.Date.context_today, help="")
    diperiksa_oleh = fields.Char( string="Diperiksa oleh",  help="")
    poin = fields.Integer( string="Poin",  help="")
    deskripsi = fields.Text( string="Deskripsi",  help="")


    tindakan_id = fields.Many2one(comodel_name="cdn.tindakan_hukuman",  string="Tindakan",  help="")
    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  string="Siswa",  help="")

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('cdn.pelanggaran')
        return super(pelanggaran, self).create(vals)
