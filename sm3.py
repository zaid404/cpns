import pandas as pd

# Membaca data dari CSV
datax = pd.read_csv('xdata.csv')

#data = datax.sample(frac=1, random_state=42).reset_index(drop=True)
#data = datax.sample(n=100, random_state=25)
data = datax.sample(n=6908).reset_index(drop=True)

# Pastikan kolom 'Total' bertipe numerik
data['Total'] = pd.to_numeric(data['Total'], errors='coerce')

# Menentukan jumlah formasi yang dibutuhkan
formasi_yang_dibutuhkan = 62
formasi_skb = formasi_yang_dibutuhkan * 3  # Formasi SKB = 3

# Hasil DataFrame
hasil = pd.DataFrame(columns=['Nama', 'Total', 'Peluang Masuk (%)', 'Rentang Nilai Keseluruhan', 'Rentang Nilai SKB'])

# Simulasi dengan memasukkan peserta satu per satu
for i in range(len(data)):
    peserta = data.iloc[i:i+1]  # Ambil satu peserta
    total = peserta['Total'].values[0]

    # Tambahkan peserta ke hasil
    hasil = pd.concat([hasil, peserta[['Nama', 'Total']].reset_index(drop=True)], ignore_index=True)

    # Pastikan 'Total' tetap dalam format numerik
    hasil['Total'] = pd.to_numeric(hasil['Total'], errors='coerce')  # Convert to numeric

    # Hitung peluang masuk
    peluang_masuk = 1 / (i + 1)  # 100% untuk peserta pertama, 50% untuk kedua, dll.
    
    # Hitung rentang nilai keseluruhan
    rentang_nilai_keseluruhan = f"{min(hasil['Total'])}-{max(hasil['Total'])}"
    
    # Menghitung rentang nilai SKB
    if len(hasil) < formasi_skb:
        rentang_nilai_skb = f"{min(hasil['Total'])}-{max(hasil['Total'])}"  # Untuk kurang dari 3 peserta
    else:
        top_participants = hasil.nlargest(formasi_skb, 'Total')  # Ambil 3 teratas
        rentang_nilai_skb = f"{top_participants['Total'].min()}-{top_participants['Total'].max()}"

    # Update hasil DataFrame
    hasil.loc[hasil.index[-1], 'Peluang Masuk (%)'] = f"{peluang_masuk:.2%}"
    hasil.loc[hasil.index[-1], 'Rentang Nilai Keseluruhan'] = rentang_nilai_keseluruhan
    hasil.loc[hasil.index[-1], 'Rentang Nilai SKB'] = rentang_nilai_skb

    # Tampilkan hasil sementara
#    print(hasil)

# Menyimpan hasil ke dalam file CSV
hasil.to_csv('hasil.csv', mode='w', index=False)  # Ganti mode='a' dengan 'w' untuk overwrite
