from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l,):
        #fungsi yang di pannggil pertama kali
        self.p = p
        self.l = l
    def info(self):
        return f'ini adalah object persegi panjang dengan panjang = {self.p} dan lebar {self.l}'

    def hitung_luas(self):
        return self.p * self.l