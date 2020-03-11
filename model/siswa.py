#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class siswa(models.Model):
    """model siswa"""

    _name = "cdn.siswa"
    name = fields.Char( required=True, string="Name",  help="")
    no_daftar = fields.Char( string="Nomor Pendaftaran",  help="")
    tgl_daftar = fields.Date( string="Tanggal Pendaftaran",  help="")
    program_daftar = fields.Selection(selection=[('Reguler','Reguler 10-30 juz 6 th'),('Tahfidz','Tahfidz 30 Juz 3 thn')],  string="Program daftar",  help="")
    nama_panggilan = fields.Char( string="Nama panggilan",  help="")
    jns_kel = fields.Selection(selection=[ ('Laki-laki','Laki-laki'),('Perempuan','Perempuan')],  string="Jenis Kelamin",  help="")
    tmp_lahir = fields.Char( string="Tempat lahir",  help="")
    tgl_lahir = fields.Date( string="Tanggal lahir",  help="")
    nik = fields.Char( string="NIK",  help="Nomor Induk Keluarga")
    status_dlm_kel = fields.Selection(selection=[('Anak Kandung','Anak Kandung'),('Anak Angkat','Anak Angkat'),('Anak Tiri','Anak Tiri')],  string="Status dalam Keluarga",  help="")
    cita_cita = fields.Char( string="Cita cita",  help="")
    hobi = fields.Char( string="Hobi",  help="")
    bhs_sehari = fields.Char( string="Bahasa Sehari-hari",  help="")
    gol_darah = fields.Selection(selection=[('A','A'),('B','B'),('AB','AB'),('O','O')],  string="Golongan Darah",  help="")
    tinggi_badan = fields.Integer( string="Tinggi Badan (cm)",  help="")
    berat_badan = fields.Integer( string="Berat Badan (kg)",  help="")
    agama_siswa = fields.Selection(selection=[('Islam','Islam'),('Kristen','Kristen'),('Katolik','Katolik'),('Hindu','Hindu'),('Budha','Budha')],  string="Agama Siswa",  help="", default="Islam")
    alamat_siswa = fields.Text( string="Alamat siswa",  help="")
    rt_rw = fields.Char( string="RT / RW",  help="")
    kota_asal = fields.Char( string="Kota Asal",  help="")
    no_telp_rumah = fields.Char( string="No Telepon Rumah",  help="")
    email_siswa = fields.Char( string="Email siswa",  help="")
    kodepos = fields.Integer( string="Kodepos",  help="")
    tinggal_bersama = fields.Char( string="Tinggal Bersama",  help="")
    sakit_tbc_pernah = fields.Boolean( string="Pernah TBC",  help="")
    sakit_tbc_ket = fields.Char( string="Sakit TBC",  help="")
    sakit_asma_pernah = fields.Boolean( string="Pernah ASMA",  help="")
    sakit_asma_ket = fields.Char( string="Sakit ASMA",  help="")
    sakit_hepatitisb_pernah = fields.Boolean( string="Pernah Hepatitis B",  help="")
    sakit_hepatitisb_ket = fields.Char( string="Sakit Hepatitis B",  help="")
    sakit_cacar_pernah = fields.Boolean( string="Pernah CACAR",  help="")
    sakit_cacar_ket = fields.Char( string="Sakit CACAR",  help="")
    sakit_lain_pernah = fields.Boolean( string="Pernah Sakit Berat Lainnya",  help="")
    sakit_lain_ket = fields.Char( string="Sakit Berat Lainnya",  help="")
    sekolah_asal = fields.Char( string="Sekolah asal",  help="")
    nisn = fields.Char( string="Nisn",  help="")
    alamat_sekolah_asal = fields.Text( string="Alamat sekolah asal",  help="")
    kepsek_sekolah_asal = fields.Char( string="Nama Kepala Sekolah",  help="")
    telp_sekolah_asal = fields.Char( string="Telp sekolah asal",  help="")
    status_sekolah_asal = fields.Selection(selection=[('Negeri','Negeri'),('Swasta','Swasta')],  string="Status sekolah asal",  help="")
    prestasi_di_sekolah = fields.Text( string="Prestasi di sekolah",  help="")
    raport_4sd_1 = fields.Float( string="Raport 4 SD Smt 1",  help="")
    raport_4sd_2 = fields.Float( string="Raport 4 SD Smt 2",  help="")
    raport_5sd_1 = fields.Float( string="Raport 5 SD Smt 1",  help="")
    raport_5sd_2 = fields.Float( string="Raport 5 SD Smt 2",  help="")
    raport_6sd_1 = fields.Float( string="Raport 6 SD Smt 1",  help="")
    baca_quran = fields.Selection(selection=[('Belum Bisa','Belum Bisa'),('Kurang Lancar','Kurang Lancar'),('Lancar','Lancar'),('Tartil','Tartil')],  string="Baca quran",  help="")
    ayah_nama = fields.Char( string="Nama Ayah",  help="")
    ayah_tmp_lahir = fields.Char( string="Tempat Lahir",  help="")
    ayah_tgl_lahir = fields.Date( string="Tanggal Lahir",  help="")
    ayah_warganegara = fields.Char( string="Kewarganegaraan",  help="")
    ayah_telp = fields.Char( string="No Telepon/HP",  help="")
    ayah_email = fields.Char( string="Email",  help="")
    ayah_alamat_kantor = fields.Text( string="Alamat Kantor",  help="")
    ayah_penghasilan = fields.Integer( string="Penghasilan/bln",  help="")
    ayah_pendidikan = fields.Selection(selection=[('SD','SD'),('SMP','SMP Sederajat'),('SMA','SMA Sederajat'),('Diploma','Diploma'),('S1','Sarjana S1'),('S2','Magister S2'),('S3','Doktoral S3')],  string="Pendidikan",  help="")
    ibu_nama = fields.Char( string="Nama Ibu",  help="")
    ibu_tmp_lahir = fields.Char( string="Tempat Lahir",  help="")
    ibu_tgl_lahir = fields.Date( string="Tanggal Lahir",  help="")
    ibu_warganegara = fields.Char( string="Kewarganegaraan",  help="")
    ibu_telp = fields.Char( string="No Telepon/HP",  help="")
    ibu_email = fields.Char( string="Email",  help="")
    # ibu_pekerjaan = fields.Char( string="Pekerjaan",  help="")
    ibu_alamat_kantor = fields.Text( string="Alamat Kantor",  help="")
    ibu_penghasilan = fields.Integer( string="Penghasilan/bln",  help="")
    ibu_pendidikan = fields.Selection(selection=[('SD','SD'),('SMP','SMP Sederajat'),('SMA','SMA Sederajat'),('Diploma','Diploma'),('S1','Sarjana S1'),('S2','Magister S2'),('S3','Doktoral S3')],  string="Pendidikan",  help="")
    wali_nama = fields.Char( string="Nama Lengkap",  help="")
    wali_tmp_lahir = fields.Char( string="Tempat Lahir",  help="")
    wali_tgl_lahir = fields.Date( string="Tanggal lahir",  help="")
    wali_warganegara = fields.Char( string="Kewarganegaraan",  help="")
    wali_telp = fields.Char( string="No Telepon/WA",  help="")
    wali_email = fields.Char( string="Email",  help="")
    # wali_pekerjaan = fields.Char( string="Pekerjaan",  help="")
    wali_alamat_kantor = fields.Text( string="Alamat Kantor",  help="")
    wali_penghasilan = fields.Integer( string="Penghasilan/bln",  help="")
    wali_pendidikan = fields.Selection(selection=[('SD','SD'),('SMP','SMP Sederajat'),('SMA','SMA Sederajat'),('Diploma','Diploma'),('S1','Sarjana S1'),('S2','Magister S2'),('S3','Doktoral S3')],  string="Pendidikan",  help="")
    institusi_tahfidz = fields.Char( string="Institusi Tahfidz Sebelumnya",  help="")
    hafalan_sejak_kelas = fields.Char( string="Hafalan Sejak Kelas",  help="")
    motivasi_menghafal = fields.Text( string="Motivasi Menghafal",  help="")
    pilihan_tahfidz = fields.Selection(selection=[('1 Tahun','1 Tahun'),('2 Tahun','2 Tahun')],  string="Pilihan tahfidz",  help="")
    image = fields.Binary( string="Foto",  help="")


    propinsi_id = fields.Many2one(comodel_name="cdn.propinsi",  string="Propinsi",  help="")
    ayah_pekerjaan_id = fields.Many2one(comodel_name="cdn.pekerjaan",  string="Pekerjaan",  help="")
    ibu_pekerjaan_id = fields.Many2one(comodel_name="cdn.pekerjaan",  string="Pekerjaan",  help="")
    wali_pekerjaan_id = fields.Many2one(comodel_name="cdn.pekerjaan",  string="Pekerjaan",  help="")
    kelas_paralel_id = fields.Many2one(comodel_name="cdn.kelas_paralel",  string="Kelas paralel",  help="")
    keuangan_siswa_ids = fields.One2many(comodel_name="cdn.keuangan_siswa",  inverse_name="siswa_id",  string="Keuangan Siswa",  help="")
    berkas_ids = fields.Many2many(comodel_name="cdn.berkas_pendaftaran",  string="Berkas Pendaftaran",  help="")

    @api.multi
    def open_perijinan(self):
        return {
            'name': _('Perijinan'),
            'domain': [('siswa_id','=', self.id)],
            'view_type': 'form',
            'res_model': 'cdn.perijinan',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'

        }

    def get_perijinan_count(self):
        count = self.env['cdn.perijinan'].search_count([('siswa_id','=', self.id)])
        self.perijinan_count = count

    perijinan_count = fields.Integer(string='Perijinan', compute='get_perijinan_count')