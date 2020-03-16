#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class perijinan(models.Model):

    _name = "cdn.perijinan"
    name = fields.Char(string="No. Referensi",  help="", readonly=True, default='Auto')
    tgl_ijin = fields.Date( string="Tanggal Ijin", default=fields.Date.context_today, required=True, help="")
    #lama_ijin = fields.Integer( string="Lama ijin",  help="")
    tgl_hrs_kembali = fields.Datetime( string="Tgl kembali", required=True,  help="")
    lama_ijin = fields.Integer('Lama Ijin', readonly=True, compute='compute_day',  store=True)
    state = fields.Selection(selection=[('Draft','Pengajuan'),('Approved','Disetujui'),('Rejected','Ditolak'),('Permission','Ijin Keluar'),('Return','Kembali')],  string="State",  help="")
    penjemput = fields.Char( string="Penjemput",  help="")
    keperluan = fields.Text( string="Keperluan",  help="")
    tgl_kembali = fields.Datetime( string="Tgl kembali",  help="")
    catatan = fields.Text( string="Catatan",  help="")


    siswa_id = fields.Many2one(comodel_name="cdn.siswa",  string="Siswa", required=True, help="")

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('cdn.perijinan')
        return super(perijinan, self).create(vals)

    @api.multi
    def action_confirm(self):
        return self.write({'state': 'Draft'})

    def action_approved(self):
        return self.write({'state': 'Approved'})

    def action_rejected(self):
        return self.write({'state': 'Rejected'}) 

    def action_permission(self):
        return self.write({'state': 'Permission'}) 


    @api.one
    @api.depends('tgl_ijin', 'tgl_hrs_kembali')
    def compute_day(self):
        if self.tgl_ijin and self.tgl_hrs_kembali:
            tgl_ijin = fields.Datetime.from_string(self.tgl_ijin)
            tgl_hrs_kembali = fields.Datetime.from_string(self.tgl_hrs_kembali)
            self.lama_ijin = abs((tgl_hrs_kembali - tgl_ijin).days) + 1
