import math
jumlahUang = 400
jumlahAwal = 200
bungaTahunan = 1/10
waktu = math.log(jumlahUang / jumlahAwal)/ math.log(1 + bungaTahunan) 
print ("Waktu yang dibutuhkan:", round (waktu, 3), "tahun")
