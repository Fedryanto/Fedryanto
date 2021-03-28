#Fungsi Menghitung Bilangan Kuadrat
print("Fungsi Hitung Kuadrat")
def hitungKuadrat(bil):
	return bil*bil
daftar_bil = [0, 2, 3, 4, 5]
hasil = map(hitungKuadrat, daftar_bil)
print(hasil)
print(list(hasil))