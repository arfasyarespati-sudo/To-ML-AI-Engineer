import pandas as pd

df_kelas_a = pd.DataFrame({
    'NIM': ['001', '002', '003', '004', '005'],
    'Nama Mahasiswa': ['A', 'B', 'C', 'D', 'E'],
    'Gender': ['Laki-laki', 'Perempuan', 'Laki-laki', 'Perempuan', 'Laki-laki'],
    'Kelas': ['A', 'A', 'A', 'A', 'A'],
    'Nilai': [85, 92, 78, 88, 95]
})

df_kelas_b = pd.DataFrame({
    'NIM': ['006', '007', '008', '009', '010'],
    'Nama Mahasiswa': ['F', 'G', 'H', 'I', 'J'],
    'Gender': ['Perempuan', 'Perempuan', 'Laki-laki', 'Perempuan', 'Laki-laki'],
    'Kelas': ['B', 'B', 'B', 'B', 'B'],
    'Nilai': [75, 89, 82, 71, 86]
})

df_combined = pd.concat([df_kelas_a, df_kelas_b], ignore_index=True)

print("=" * 70)
print("DATA KOMBINASI KELAS A DAN KELAS B")
print("=" * 70)
print(df_combined)
print()

print("=" * 70)
print("A. MAHASISWA DENGAN NILAI LEBIH DARI 80")
print("=" * 70)
hasil_a = df_combined[df_combined['Nilai'] > 80]
print(hasil_a)
print()

print("=" * 70)
print("B. KOLOM NIM DAN NILAI")
print("=" * 70)
hasil_b = df_combined[['NIM', 'Nilai']]
print(hasil_b)
print()

print("=" * 70)
print("C. MAHASISWA PEREMPUAN DENGAN NILAI KURANG DARI 80")
print("=" * 70)
hasil_c = df_combined[(df_combined['Nilai'] < 80) & (df_combined['Gender'] == 'Perempuan')]
print(hasil_c)
print()