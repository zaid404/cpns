import pandas as pd
import numpy as np

# Membaca data dari file CSV
data = pd.read_csv('allkumhamsma2018.csv')  # Gantilah dengan nama file yang sesuai
rules = pd.read_csv('data_asli.csv')

# Mengambil variabel yang diperlukan dari rules
results = []

# Mengambil data dari setiap baris dalam rules
for index, row in rules.iterrows():
    jumlah_pelamar = row['Jumlah_Pelamar']  # Ambil jumlah pelamar untuk setiap kota
    peserta_ikut_skb = row['Lulus_SKB']  # Data peserta yang lulus SKB
    max_asli = row['nilai max asli']  # Nilai maksimum asli
    min_asli = row['nilai min asli']  # Nilai minimum asli

    # Konfigurasi bootstrapping
    n_iterations = 1000  # Jumlah iterasi bootstrap
    sample_size = jumlah_pelamar  # Ukuran sampel setiap pengulangan bootstrap
    hasil = pd.DataFrame(columns=['Iteration', 'Rata-Rata Total', 'Rentang Nilai Keseluruhan', 'Min Nilai SKB', 'Max Nilai SKB'])
    log_file = 'loghasil.csv'

    # Inisialisasi log file
    with open(log_file, 'w') as f:
        f.write("Jumlah Peserta,Formasi SKB,Formasi yang Dibutuhkan,Min Nilai SKB,Max Nilai SKB\n")

    # Mengubah 'Total' menjadi tipe numerik
    data['Total'] = pd.to_numeric(data['Total'], errors='coerce')

    # Loop untuk setiap iterasi bootstrap
    for j in range(n_iterations):
        # Sampling tanpa pengulangan
        sample = data.sample(n=sample_size, replace=False, random_state=j)

        # Tentukan jumlah formasi
        jumlah_peserta = len(sample)
        formasi_skb = jumlah_peserta // 58
        formasi_yang_dibutuhkan = formasi_skb // 3

        # Hitung rata-rata dan rentang nilai keseluruhan
        rata_rata_total = sample['Total'].mean()
        rentang_nilai_keseluruhan = f"{sample['Total'].min()}-{sample['Total'].max()}"
        
        # Menghitung rentang nilai SKB untuk peserta teratas
        if formasi_skb > 0:
            top_participants = sample.nlargest(formasi_skb, 'Total')
            min_nilai_skb = top_participants['Total'].min()
            max_nilai_skb = top_participants['Total'].max()
        else:
            min_nilai_skb = np.nan
            max_nilai_skb = np.nan
        
        # Simpan hasil ke DataFrame
        hasil = pd.concat([hasil, pd.DataFrame({
            'Iteration': [j + 1],
            'Rata-Rata Total': [rata_rata_total],
            'Rentang Nilai Keseluruhan': [rentang_nilai_keseluruhan],
            'Min Nilai SKB': [min_nilai_skb],
            'Max Nilai SKB': [max_nilai_skb]
        })], ignore_index=True)

    # Hitung rata-rata Min dan Max Nilai SKB
    avg_min_skb = hasil['Min Nilai SKB'].mean()
    avg_max_skb = hasil['Max Nilai SKB'].mean()

    # Tambahkan data ke dalam hasil
    results.append({
        'Kota': row['Kota'],
        'Jumlah_Pelamar': jumlah_pelamar,
        'Peserta_Ikut_SKB': peserta_ikut_skb,
        'Max_Asli': max_asli,
        'Min_Asli': min_asli,
        'Avg_Min_SKB': avg_min_skb,
        'Avg_Max_SKB': avg_max_skb
    })

# Buat DataFrame dari hasil
pengujian_df = pd.DataFrame(results)

# Simpan DataFrame ke file CSV
pengujian_df.to_csv('pengujian.csv', index=False)

print("Data pengujian telah disimpan di 'pengujian.csv'")

# Mengonversi ke DataFrame untuk evaluasi
evaluasi_df = pengujian_df.copy()

# Menghitung MAE
mae_min = np.mean(np.abs(evaluasi_df['Min_Asli'] - evaluasi_df['Avg_Min_SKB']))
mae_max = np.mean(np.abs(evaluasi_df['Max_Asli'] - evaluasi_df['Avg_Max_SKB']))

# Menghitung MAPE
mape_min = np.mean(np.abs((evaluasi_df['Min_Asli'] - evaluasi_df['Avg_Min_SKB']) / evaluasi_df['Min_Asli'])) * 100
mape_max = np.mean(np.abs((evaluasi_df['Max_Asli'] - evaluasi_df['Avg_Max_SKB']) / evaluasi_df['Max_Asli'])) * 100

# Menghitung RMSE
rmse_min = np.sqrt(np.mean((evaluasi_df['Min_Asli'] - evaluasi_df['Avg_Min_SKB']) ** 2))
rmse_max = np.sqrt(np.mean((evaluasi_df['Max_Asli'] - evaluasi_df['Avg_Max_SKB']) ** 2))

# Tampilkan hasil evaluasi
print("Hasil Evaluasi untuk Semua Kota:")
print(f"MAE (Min): {mae_min:.2f}")
print(f"MAE (Max): {mae_max:.2f}")
print(f"MAPE (Min): {mape_min:.2f}%")
print(f"MAPE (Max): {mape_max:.2f}%")
print(f"RMSE (Min): {rmse_min:.2f}")
print(f"RMSE (Max): {rmse_max:.2f}")

# Buat matriks hasil evaluasi
evaluasi_matrix = pd.DataFrame({
    'Metric': ['MAE (Min)', 'MAE (Max)', 'MAPE (Min)', 'MAPE (Max)', 'RMSE (Min)', 'RMSE (Max)'],
    'Value': [mae_min, mae_max, mape_min, mape_max, rmse_min, rmse_max]
})

# Simpan matriks hasil evaluasi ke file CSV
evaluasi_matrix.to_csv('evaluasi_matrix.csv', index=False)

print("Matriks hasil evaluasi telah disimpan di 'evaluasi_matrix.csv'")
