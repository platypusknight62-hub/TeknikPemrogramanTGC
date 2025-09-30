class sensor:
    def __init__(self, id_sensor,lokasi,jenis):
        self.id_sensor = id_sensor
        self.lokasi = lokasi    
        self.jenis = jenis
    def info(self):
        return f"Sensor ID: {self.id_sensor}, Location: {self.lokasi}, Type: {self.jenis}"

class SensorSeismik(sensor):
    def __init__(self, id_sensor, lokasi, jenis, frekuansi_sampling ):
        super().__init__(id_sensor, lokasi, jenis)
        self.frekuensi_sampling = frekuansi_sampling
        self.durasi = 0
    def info(self):
        return f"{super().info()}, frekuensi sampling : {self.frekuensi_sampling}"
    def jumalah_sample(self, durasi):
        self.durasi = durasi
        return self.frekuensi_sampling * durasi
    
seismik1 = SensorSeismik("S001", "Jakarta", "Seismik", 100)
print(seismik1.info())
print("Jumlah sampel dalam 10 detik:", seismik1.jumalah_sample(10))