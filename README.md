# SIMULASI PERENGKINGAN UNTUK TAHAPAN SKB METODE BOOSTSTRAPPING SIMULATION

## Overview
This repository contains an analysis of CPNS (Calon Pegawai Negeri Sipil) data using 2018 result test SKD. 

### Simulation Overview
- **Simulation Count**: SM 3
- The analysis simulates the range of participants who could qualify for SKB (Seleksi Kompetensi Bidang). The data input is random.

### Legal Considerations
I am still questioning the legality of the data I am using. Is it permissible to conduct this type of analysis?


- **Test Conducted**: PEMERIKSA KEIMIGRASIAN PEMULA
- **Institution**: Kementerian Hukum dan Hak Asasi Manusia
- **Location**: KANTOR WILAYAH KEMENKUMHAM SUMATERA UTARA
- **Results**: 2.18 - 6.02
- **Participants**: 62
- ### Analysis Results
- **SKB Score Range**: 350.0 - 404.0
## continued
jadi kali ini menggunakan metode Boostrapping untuk simulasi nya 
```plaintext
| Kota                                               | Jumlah_Pelamar | Peserta_Ikut_SKB | Max_Asli | Min_Asli | Avg_Min_SKB | Avg_Max_SKB |
|----------------------------------------------------|----------------|------------------|----------|----------|-------------|-------------|
| PENJAGA TAHANAN (PEREMPUAN)_SumateraUtara          | 6902           | 42               | 402      | 369      | 355.808     | 404.975     |
| PENJAGA TAHANAN (PEREMPUAN)_SumateraSelatan        | 4546           | 18               | 415      | 376      | 355.903     | 402.168     |
| PENJAGA TAHANAN (PEREMPUAN)_SumateraBarat          | 2270           | 24               | 400      | 366      | 355.932     | 397.4       |
| PENJAGA TAHANAN (PEREMPUAN)_SulawesiUtara          | 1025           | 54               | 358      | 320      | 356.474     | 391.109     |
| PENJAGA TAHANAN (PEREMPUAN)_SulawesiTengah         | 0              | 0                | 0        | 0        |             |             |
| PENJAGA TAHANAN (PEREMPUAN)_SulawesiSelatan        | 3380           | 30               | 386      | 353      | 355.882     | 400.34      |
| PENJAGA TAHANAN (PEREMPUAN)_Riau                   | 2296           | 27               | 397      | 364      | 356.107     | 397.523     |
| PENJAGA TAHANAN (PEREMPUAN)_Papua Barat            | 159            | 12               | 371      | 320      | 362.435     | 374.273     |
| PENJAGA TAHANAN (PEREMPUAN)_Papua                  | 122            | 6                | 361      | 325      | 359.113     | 371.213     |
| PENJAGA TAHANAN (PEREMPUAN)_Nusa Tenggara Timur    | 1383           | 30               | 384      | 344      | 356.46      | 393.64      |
| PENJAGA TAHANAN (PEREMPUAN)_Nusa Tenggara Barat    | 1063           | 18               | 390      | 355      | 356.173     | 391.44      |
| PENJAGA TAHANAN (PEREMPUAN)_Maluku Utara           | 1064           | 15               | 393      | 329      | 356.184     | 391.442     |
| PENJAGA TAHANAN (PEREMPUAN)_Maluku                 | 1030           | 36               | 374      | 325      | 356.536     | 391.147     |
| PENJAGA TAHANAN (PEREMPUAN)_KepulauanRiau          | 741            | 21               | 396      | 355      | 357.011     | 388.546     |
| PENJAGA TAHANAN (PEREMPUAN)_KalimantanTimur        | 667            | 21               | 386      | 352      | 356.71      | 387.563     |
| PENJAGA TAHANAN (PEREMPUAN)_KalimantanTengah       | 561            | 21               | 369      | 342      | 357.336     | 386.246     |
| PENJAGA TAHANAN (PEREMPUAN)_KalimantanSelatan      | 1508           | 30               | 397      | 357      | 355.946     | 394.502     |
| PENJAGA TAHANAN (PEREMPUAN)_KalimantanBarat        | 1701           | 21               | 402      | 363      | 356.135     | 395.448     |
| PENJAGA TAHANAN (PEREMPUAN)_Jawa Timur             | 3003           | 51               | 398      | 371      | 356.038     | 399.557     |
| PENJAGA TAHANAN (PEREMPUAN)_Jawa Tengah            | 3190           | 36               | 402      | 377      | 355.812     | 400.001     |
| PENJAGA TAHANAN (PEREMPUAN)_Jawa Barat             | 1738           | 9                | 390      | 367      | 356.468     | 395.568     |
| PENJAGA TAHANAN (PEREMPUAN)_DKI Jakarta            | 1376           | 21               | 392      | 365      | 356.41      | 393.608     |
| PENJAGA TAHANAN (PEREMPUAN)_DIYogyakarta           | 915            | 9                | 432      | 380      | 356.659     | 390.149     |
| PENJAGA TAHANAN (PEREMPUAN)_Banten                 | 1137           | 30               | 379      | 352      | 356.354     | 391.87      |
| PENJAGA TAHANAN (PEREMPUAN)_Bali                   | 875            | 21               | 394      | 361      | 356.067     | 389.794     |
| PENJAGA TAHANAN (PEREMPUAN)_Aceh                   | 2982           | 21               | 397      | 351      | 355.939     | 399.522     |
| PENJAGA TAHANAN (PEREMPUAN) Papua PUTRAPUTRI PAPUA DAN PAPUA BARAT  | 118 | 12 | 316      | 262      | 358.722     | 370.926     |
| PENJAGA TAHANAN (PEREMPUAN) Papua Barat PUTRAPUTRI PAPUA DAN PAPUA BARAT | 124 | 12 | 340 | 284 | 359.381 | 371.498 |
| PENJAGA TAHANAN (LAKI-LAKI)_SumateraUtara          | 14102          | 123              | 406      | 359      | 355.767     | 409.366     |
| PENJAGA TAHANAN (LAKI-LAKI)_SumateraSelatan        | 8111           | 72               | 400      | 356      | 355.873     | 405.836     |
| PENJAGA TAHANAN (LAKI-LAKI)_SumateraBarat          | 6208           | 93               | 396      | 352      | 355.809     | 404.294     |
| PENJAGA TAHANAN (LAKI-LAKI)_SulawesiUtara          | 1823           | 159              | 381      | 309      | 356.16      | 395.769     |
| PENJAGA TAHANAN (LAKI-LAKI)_SulawesiTengah         | 0              | 30               | 0        | 0        |             |             |
| PENJAGA TAHANAN (LAKI-LAKI)_SulawesiSelatan        | 8618           | 99               | 407      | 350      | 355.848     | 406.202     |
| PENJAGA TAHANAN (LAKI-LAKI)_Riau                   | 5422           | 78               | 409      | 354      | 355.885     | 403.415     |
| PENJAGA TAHANAN (LAKI-LAKI)_Papua Barat            | 244            | 24               | 350      | 297      | 357.692     | 378.443     |
| PENJAGA TAHANAN (LAKI-LAKI)_Papua                  | 301            | 27               | 400      | 309      | 357.169     | 380.624     |
| PENJAGA TAHANAN (LAKI-LAKI)_Nusa Tenggara Timur    | 4073           | 90               | 395      | 339      | 355.868     | 401.497     |
| PENJAGA TAHANAN (LAKI-LAKI)_Nusa Tenggara Barat    | 2884           | 72               | 398      | 346      | 356.023     | 399.267     |
| PENJAGA TAHANAN (LAKI-LAKI)_Maluku Utara           | 2355           | 45               | 382      | 321      | 356.076     | 397.783     |
| PENJAGA TAHANAN (LAKI-LAKI)_Maluku                 | 2296           | 114              | 376      | 306      | 356.107     | 397.523

     |
| PENJAGA TAHANAN (LAKI-LAKI)_KepulauanRiau          | 1627           | 33               | 406      | 364      | 356.455     | 395.387     |
| PENJAGA TAHANAN (LAKI-LAKI)_KalimantanTimur        | 1460           | 45               | 402      | 358      | 356.12      | 396.789     |
| PENJAGA TAHANAN (LAKI-LAKI)_KalimantanTengah       | 1231           | 45               | 375      | 341      | 356.248     | 394.967     |
| PENJAGA TAHANAN (LAKI-LAKI)_KalimantanSelatan      | 3458           | 96               | 399      | 353      | 355.982     | 401.752     |
| PENJAGA TAHANAN (LAKI-LAKI)_KalimantanBarat        | 3957           | 66               | 401      | 355      | 356.051     | 401.911     |
| PENJAGA TAHANAN (LAKI-LAKI)_Jawa Timur             | 6961           | 138              | 404      | 364      | 355.815     | 405.369     |
| PENJAGA TAHANAN (LAKI-LAKI)_Jawa Tengah            | 7612           | 99               | 409      | 367      | 355.812     | 404.218     |
| PENJAGA TAHANAN (LAKI-LAKI)_Jawa Barat             | 4146           | 39               | 392      | 357      | 355.819     | 400.25      |
| PENJAGA TAHANAN (LAKI-LAKI)_DKI Jakarta            | 3462           | 57               | 399      | 354      | 355.87      | 398.632     |
| PENJAGA TAHANAN (LAKI-LAKI)_DIYogyakarta           | 2311           | 15               | 430      | 367      | 356.077     | 394.381     |
| PENJAGA TAHANAN (LAKI-LAKI)_Banten                 | 2957           | 84               | 395      | 357      | 355.926     | 400.174     |
| PENJAGA TAHANAN (LAKI-LAKI)_Bali                   | 2290           | 57               | 397      | 357      | 356.111     | 394.771     |
| PENJAGA TAHANAN (LAKI-LAKI)_Aceh                   | 5661           | 45               | 404      | 354      | 355.94      | 403.66      |
| PENJAGA TAHANAN (LAKI-LAKI) Papua PUTRAPUTRI PAPUA DAN PAPUA BARAT | 257 | 24 | 387 | 325 | 358.388 | 373.074 |
| PENJAGA TAHANAN (LAKI-LAKI) Papua Barat PUTRAPUTRI PAPUA DAN PAPUA BARAT | 248 | 24 | 401 | 301 | 358.727 | 374.249 |
```
### Penjelasan Hasil Evaluasi

Dalam proses evaluasi, terdapat tiga metrik utama yang digunakan untuk menilai akurasi prediksi model terhadap data CPNS pada berbagai kota:

1. **Mean Absolute Error (MAE)**:
   - MAE minimum: 15.85
   - MAE maksimum: 24.21
   
   MAE mengukur rata-rata absolut dari kesalahan prediksi, yaitu selisih antara nilai aktual dan nilai yang diprediksi. Semakin rendah nilai MAE, semakin baik akurasi prediksi model. Pada hasil ini, MAE minimum yang tercapai adalah 15.85, menunjukkan performa yang relatif baik di beberapa kota, sementara MAE maksimum adalah 24.21, menunjukkan beberapa area yang memiliki ketidakakuratan yang lebih besar.

2. **Mean Absolute Percentage Error (MAPE)**:
   - MAPE minimum: 7.18%
   - MAPE maksimum: 11.38%
   
   MAPE menggambarkan rata-rata persentase kesalahan absolut, yang membantu memahami kesalahan prediksi dalam konteks persentase relatif. Dengan MAPE minimum sebesar 7.18% dan maksimum 11.38%, model menunjukkan kesalahan relatif yang terbilang rendah, menandakan bahwa prediksi cukup konsisten dibandingkan dengan nilai sebenarnya.

3. **Root Mean Square Error (RMSE)**:
   - RMSE minimum: 39.16
   - RMSE maksimum: 47.09
   
   RMSE memperhitungkan kuadrat dari kesalahan dan memberikan bobot lebih besar pada kesalahan yang lebih besar, sehingga metrik ini berguna untuk mengidentifikasi outlier. RMSE yang lebih rendah mengindikasikan prediksi yang lebih akurat. Pada hasil ini, RMSE minimum adalah 39.16 dan RMSE maksimum adalah 47.09, yang menunjukkan bahwa variasi kesalahan masih berada dalam rentang yang dapat diterima.

Secara keseluruhan, nilai-nilai evaluasi ini menunjukkan bahwa model prediksi yang digunakan memiliki tingkat akurasi yang memadai untuk sebagian besar kota, namun ada potensi perbaikan di beberapa wilayah untuk meningkatkan konsistensi prediksi. 

Contoh penulisan di file `README.md`:

---

### Evaluasi Hasil Prediksi Model

Hasil evaluasi model prediksi untuk data CPNS per kota ditunjukkan oleh tiga metrik utama:

- **Mean Absolute Error (MAE)**:
  - Rentang: **15.85 - 24.21**
  - MAE mengukur rata-rata kesalahan absolut prediksi, semakin kecil nilainya, semakin baik akurasi prediksi.

- **Mean Absolute Percentage Error (MAPE)**:
  - Rentang: **7.18% - 11.38%**
  - MAPE membantu mengukur kesalahan dalam bentuk persentase. MAPE yang rendah menandakan prediksi yang cukup konsisten.

- **Root Mean Square Error (RMSE)**:
  - Rentang: **39.16 - 47.09**
  - RMSE memberikan bobot lebih besar pada kesalahan yang lebih besar. RMSE yang rendah menunjukkan prediksi yang lebih akurat.

Secara keseluruhan, hasil evaluasi ini menunjukkan model mampu memberikan prediksi yang cukup akurat di sebagian besar kota, meskipun masih terdapat beberapa area yang membutuhkan perbaikan.
MAPE (Max): 7.18%
RMSE (Min): 47.09
RMSE (Max): 39.16



