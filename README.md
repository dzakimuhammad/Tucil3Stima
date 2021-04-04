# Tucil3Stima
Tugas Kecil 3 Strategi Algoritma : Implementasi Algoritma A* untuk Menentukan Lintasan Terpendek

## Identitas Pembuat:
1. Dzaki Muhammad (K-1) 13519049
2. Rezda Abdullah Fachrezzi (K-4) 13519194

## Struktur Direktori:
1. **doc** -> lokasi penyimpanan laporan tugas kecil.
2. **src** -> lokasi penyimpanan *source code* dari program.
3. **test** -> lokasi penyimpanan dokumen uji.

## Deskripsi Program:
Program ini dibuat untuk menentukan lintasan terpendek antara dua titik pada suatu graf yang menyatakan peta menggunakan algoritma A*.

## Instalasi Modul:
Program ini menggunakan bahasa pemrograman Python sehingga untuk menjalankannya diperlukan untuk menginstalasi Python terlebih dahulu melalui laman *https://www.python.org/downloads/*. Selain itu diperlukan juga untuk menginstalasi Jupyter Notebook untuk menjalankan file IPython Notebook. Panduan instalasi Jupyter Notebook dapat dilihat pada laman *https://jupyter.org/install*.

Selain kedua program yang sudah disebutkan di atas, diperlukan pula package manager PIP untuk library, panduan instalasi dapat dilihat pada laman *https://pip.pypa.io/en/stable/installing/*.

### Prerequisite Library
Sebelum menjalankan program, agar graf dapat ditampilkan maka perlu dilakukan beberapa instalasi library
melalui terminal dengan perintah **pip install *keyword***
1. matplotlib
2. networkx

## Contoh isi file
Baris pertama adalah jumlah simpul N

Baris kedua sampai N+1 adalah nama-nama simpul (tanpa spasi) beserta koordinatnya (dalam latitude dan longitude)

Baris sisanya merupakan matriks ketetanggaan yang sesuai urutan simpul di atasnya.
```
8
SimpangTuguAsiaAfrika -6.921210 107.607689
MuseumAsiaAfrika -6.921023 107.609848
BragaCityWalk -6.916968 107.609178
MercureCityCentre -6.923878 107.611800
SudirmanStreetMarket -6.920395 107.600530
PendopoKota -6.922503 107.607066
PasarBaru -6.917585 107.604353
BatagorKingsley -6.919173 107.615111
0 1 0 1 1 1 1 0
1 0 1 1 0 0 0 0
0 1 0 0 0 0 0 1
1 1 0 0 0 1 0 0
1 0 0 0 0 0 1 0
1 0 0 1 0 0 0 0
1 0 0 0 1 0 0 0
0 0 1 0 0 0 0 0
```

## Cara Menggunakan Program:
1. Buka terminal, arahkan ke direktori tempat program disimpan yaitu pada folder Tucil3Stima.
2. Jalankan perintah berikut untuk membuka web lokal berbasis Jupyter.
```
jupyter-lab
```
3. Buka folder Tucil3.ipynb yang terdapat pada folder src.
4. Jalankan program sesuai dengan langkah-langkah yang dijelaskan pada file tersebut.
5. Input lokasi file txt uji ketika program meminta input, beberapa data uji txt tersedia dalam folder test (input ../test/*namafile*).
6. Program akan berjalan meminta input pengguna, menampilkan peta berbentuk graf berbobot lalu menampilkan lintasan terpendek dari simpul awal ke simpul tujuan sesuai algoritma A* dan menghitung jaraknya.

### Alternatif Penggunaan Program
1. Buka terminal, arahkan ke direktori tempat program disimpan yaitu pada folder Tucil3Stima/src.
2. Jalankan perintah berikut.
```
python3 main.py
```
3. Program akan meminta nama file. Jika terbaca, akan muncul pop-up gambar graf terkait. Jika sudah selesai melihat-lihat, tutup pop-up tersebut dan program akan meminta simpul awal dan simpul tujuan.
4. Program akan menuliskan jarak mininum pada simpul tersebut dan menampilkan Graf lagi tetapi dengan jalur yang sudah diwarnai sesuai dengan hasil dari Algoritma A*.
