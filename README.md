# Eksperimen SML - Diabetes Dataset

Repository ini dibuat untuk memenuhi **Kriteria 1** pada submission kelas **Membangun Sistem Machine Learning**. Repository ini berisi proses eksperimen awal terhadap dataset Diabetes, mulai dari pengenalan dataset, data loading, exploratory data analysis, preprocessing manual melalui notebook, hingga otomatisasi preprocessing menggunakan script Python.

## Deskripsi Dataset

Dataset yang digunakan adalah **Diabetes Dataset** yang diperoleh dari Kaggle.

Sumber dataset: [Diabetes Dataset - Kaggle](https://www.kaggle.com/datasets/johndasilva/diabetes)

Dataset ini merupakan data tabular yang berisi informasi medis pasien dan digunakan untuk memprediksi kemungkinan seseorang terkena diabetes. Dataset terdiri dari **2000 baris data** dan **9 kolom**. Seluruh kolom memiliki nilai non-null, sehingga tidak ditemukan missing value secara eksplisit.

Permasalahan yang diselesaikan pada dataset ini adalah **klasifikasi biner**. Kolom target yang digunakan adalah `Outcome`, dengan nilai:

- `0`: pasien tidak terindikasi diabetes
- `1`: pasien terindikasi diabetes

## Fitur Dataset

| Kolom                      | Deskripsi                                     | Tipe Data |
| -------------------------- | --------------------------------------------- | --------- |
| `Pregnancies`              | Jumlah kehamilan                              | int64     |
| `Glucose`                  | Kadar glukosa                                 | int64     |
| `BloodPressure`            | Tekanan darah                                 | int64     |
| `SkinThickness`            | Ketebalan kulit                               | int64     |
| `Insulin`                  | Kadar insulin                                 | int64     |
| `BMI`                      | Indeks massa tubuh                            | float64   |
| `DiabetesPedigreeFunction` | Faktor riwayat diabetes berdasarkan keturunan | float64   |
| `Age`                      | Usia pasien                                   | int64     |
| `Outcome`                  | Label target diabetes                         | int64     |

## Struktur Repository

    Eksperimen_SML_Fathiyya-Nafisah
    ├── diabetes_raw
    │   └── diabetes.csv
    ├── preprocessing
    │   ├── Eksperimen_Fathiyya-Nafisah.ipynb
    │   ├── automate_Fathiyya-Nafisah.py
    │   └── diabetes_preprocessing
    │       ├── train.csv
    │       ├── test.csv
    │       └── diabetes_preprocessed.csv
    └── README.md

## Tahapan Eksperimen

Tahapan eksperimen yang dilakukan pada notebook `Eksperimen_Fathiyya-Nafisah.ipynb` adalah sebagai berikut:

1. Perkenalan dataset.
2. Import library.
3. Memuat dataset.
4. Exploratory Data Analysis.
5. Data preprocessing.
6. Menyimpan dataset hasil preprocessing.

## Exploratory Data Analysis

Pada tahap Exploratory Data Analysis, dilakukan beberapa pengecekan untuk memahami karakteristik dataset, yaitu:

1. Melihat ukuran dataset.
2. Melihat informasi tipe data.
3. Melihat statistik deskriptif.
4. Mengecek missing value.
5. Mengecek data duplikat.
6. Melihat distribusi target.
7. Mengecek nilai 0 pada beberapa fitur medis.
8. Melihat korelasi antar fitur.

Berdasarkan hasil EDA, dataset memiliki:

- Jumlah data: 2000 baris
- Jumlah kolom: 9 kolom
- Missing value eksplisit: tidak ditemukan
- Data duplikat: 1256 data
- Target klasifikasi: `Outcome`

Distribusi target pada dataset adalah sebagai berikut:

| Label | Keterangan                 | Jumlah Data |
| ----- | -------------------------- | ----------: |
| 0     | Tidak terindikasi diabetes |        1316 |
| 1     | Terindikasi diabetes       |         684 |

Selain itu, ditemukan nilai 0 pada beberapa fitur medis, yaitu:

| Kolom           | Jumlah Nilai 0 |
| --------------- | -------------: |
| `Glucose`       |             13 |
| `BloodPressure` |             90 |
| `SkinThickness` |            573 |
| `Insulin`       |            956 |
| `BMI`           |             28 |

Nilai 0 pada kolom `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, dan `BMI` dianggap kurang realistis secara medis. Oleh karena itu, nilai tersebut ditangani pada tahap preprocessing.

## Data Preprocessing

Tahapan preprocessing yang dilakukan adalah:

1. Membuat salinan dataset agar data mentah tetap aman.
2. Menghapus data duplikat.
3. Mengganti nilai 0 pada kolom medis tertentu menjadi NaN.
4. Mengisi nilai NaN menggunakan nilai median dari masing-masing kolom.
5. Memisahkan fitur dan target.
6. Membagi dataset menjadi data latih dan data uji.
7. Melakukan standarisasi fitur numerik menggunakan `StandardScaler`.
8. Menyimpan dataset hasil preprocessing ke dalam file CSV.

Kolom yang ditangani karena memiliki nilai 0 tidak realistis adalah:

    Glucose
    BloodPressure
    SkinThickness
    Insulin
    BMI

Setelah data duplikat dihapus, ukuran dataset berkurang dari 2000 data menjadi 744 data. Dataset kemudian dibagi menjadi data latih dan data uji dengan rasio 80:20.

Hasil pembagian data:

| Dataset    | Jumlah Data |
| ---------- | ----------: |
| Data latih |         595 |
| Data uji   |         149 |

## Hasil Preprocessing

Dataset hasil preprocessing disimpan pada folder:

    preprocessing/diabetes_preprocessing

File yang dihasilkan adalah:

| File                        | Keterangan                                           |
| --------------------------- | ---------------------------------------------------- |
| `train.csv`                 | Data latih hasil preprocessing                       |
| `test.csv`                  | Data uji hasil preprocessing                         |
| `diabetes_preprocessed.csv` | Gabungan data latih dan data uji hasil preprocessing |

Dataset hasil preprocessing ini akan digunakan pada tahap berikutnya, yaitu pelatihan model machine learning menggunakan MLflow.

## Otomatisasi Preprocessing

Selain preprocessing manual pada notebook, repository ini juga menyediakan file otomatisasi preprocessing:

    preprocessing/automate_Fathiyya-Nafisah.py

File ini berisi fungsi-fungsi untuk menjalankan proses preprocessing secara otomatis, mulai dari memuat dataset mentah hingga menghasilkan dataset siap latih.

Tahapan yang dilakukan pada file otomatisasi:

1. Memuat dataset dari folder `diabetes_raw`.
2. Menghapus data duplikat.
3. Menangani nilai 0 pada fitur medis tertentu.
4. Mengisi nilai kosong menggunakan median.
5. Memisahkan fitur dan target.
6. Membagi data menjadi train dan test.
7. Melakukan standarisasi fitur.
8. Menyimpan hasil preprocessing ke folder `diabetes_preprocessing`.

## Cara Menjalankan Otomatisasi Preprocessing

Pastikan posisi terminal berada pada folder repository:

    cd Eksperimen_SML_Fathiyya-Nafisah

Kemudian masuk ke folder preprocessing:

    cd preprocessing

Jalankan file otomatisasi preprocessing:

    python automate_Fathiyya-Nafisah.py

Jika berhasil, file hasil preprocessing akan tersimpan pada folder:

    preprocessing/diabetes_preprocessing

Output yang dihasilkan:

    train.csv
    test.csv
    diabetes_preprocessed.csv

## Library yang Digunakan

Library utama yang digunakan dalam eksperimen ini adalah:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Cara Menjalankan Notebook

Buka file notebook berikut:

    preprocessing/Eksperimen_Fathiyya-Nafisah.ipynb

Kemudian jalankan seluruh cell secara berurutan dari awal hingga akhir.

Notebook berisi proses:

1. Import library.
2. Memuat dataset.
3. Exploratory Data Analysis.
4. Data preprocessing.
5. Menyimpan hasil preprocessing.

Pastikan file dataset mentah tersedia pada path berikut:

    diabetes_raw/diabetes.csv

## Tujuan Repository

Tujuan dari repository ini adalah menghasilkan dataset yang telah melalui proses eksplorasi dan preprocessing sehingga siap digunakan untuk tahap pelatihan model machine learning. Repository ini juga menjadi bagian awal dari alur MLOps pada submission kelas Membangun Sistem Machine Learning.

## Author

Fathiyya Nafisah
