import program

# CARA MENJALANKAN PROGRAM (main.py)
# python3 main.py

# Program dibuat oleh Dzaki Muhammad 13519049 dan Rezda Abdullah F 13519194
# Untuk memenuhi Tugas Kecil 3 Strategi Algoritma IF2211 2020/2021

# set tipe visualisasi graf
# in case graf gabisa digambar karena tipenya g sesuai, dicoba aja salah satu dari yang lain (default = 0 = planar)
# -1 = use x y position
# 0 = planar (default)
# 1 = circular
# 2 = spectral
# 3 = spring
# 4 = shell
tipe = 0

program.setgraphtype(tipe)
program.start()
program.process()