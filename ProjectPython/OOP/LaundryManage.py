class Pelanggan:
    def __init__(self, nama, nomor, id):
        self.nama = nama
        self.nomor = nomor
        self.id = id
    
    def getNama(self):
        return self.nama
    
    def setNama(self, nama):
        self.nama = nama
    
    def tampilPelanggan(self):
        print("=== DATA PELANGGAN ===")
        print(f"Nama  : {self.nama}")
        print(f"Nomor : {self.nomor}")
        print(f"ID    : {self.id}")
        print()


class Pesanan:

    def __init__(self, jenis, berat):
        self.jenis = jenis
        self.berat = berat

    
    def tampilPesanan(self, napel):
        print("=== PESANAN ===")
        print(f"Pelanggan : {napel}")
        print(f"Jenis     : {self.jenis}")
        print(f"Berat     : {self.berat}")
        print()

    


pel = Pelanggan("Budi", 856, 232)
pel1 = Pelanggan("Aryo", 832, 233)

pes = Pesanan("Cuci + Setrika", 5)
pes1 = Pesanan("Setrika", 2)


pel.tampilPelanggan()
pes.tampilPesanan(pel.nama)

pel1.tampilPelanggan()
pes1.tampilPesanan(pel1.nama)




    