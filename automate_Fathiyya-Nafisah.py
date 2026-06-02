import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(input_path):
    """
    Memuat dataset dari file CSV.
    """
    df = pd.read_csv(input_path)
    return df


def clean_data(df):
    """
    Membersihkan dataset dengan menghapus data duplikat dan menangani nilai 0
    pada beberapa kolom medis yang kurang realistis.
    """
    df_clean = df.copy()

    # Menghapus data duplikat
    df_clean = df_clean.drop_duplicates()

    # Kolom medis yang kurang realistis jika bernilai 0
    zero_columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    # Mengganti nilai 0 menjadi NaN
    df_clean[zero_columns] = df_clean[zero_columns].replace(0, np.nan)

    # Mengisi nilai NaN dengan median masing-masing kolom
    for col in zero_columns:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())

    return df_clean


def split_and_scale_data(df, target_column="Outcome"):
    """
    Memisahkan fitur dan target, membagi data menjadi train-test,
    lalu melakukan standarisasi fitur numerik.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    X_train_scaled = pd.DataFrame(X_train_scaled, columns=X.columns)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=X.columns)

    y_train = y_train.reset_index(drop=True)
    y_test = y_test.reset_index(drop=True)

    train_data = pd.concat([X_train_scaled, y_train], axis=1)
    test_data = pd.concat([X_test_scaled, y_test], axis=1)

    diabetes_preprocessed = pd.concat(
        [train_data, test_data],
        axis=0
    ).reset_index(drop=True)

    return train_data, test_data, diabetes_preprocessed


def save_data(train_data, test_data, diabetes_preprocessed, output_dir):
    """
    Menyimpan hasil preprocessing ke folder output.
    """
    os.makedirs(output_dir, exist_ok=True)

    train_data.to_csv(os.path.join(output_dir, "train.csv"), index=False)
    test_data.to_csv(os.path.join(output_dir, "test.csv"), index=False)
    diabetes_preprocessed.to_csv(
        os.path.join(output_dir, "diabetes_preprocessed.csv"),
        index=False
    )


def preprocess_data(input_path, output_dir):
    """
    Menjalankan seluruh proses preprocessing dari data mentah
    sampai menghasilkan dataset siap latih.
    """
    df = load_data(input_path)

    print("Dataset berhasil dimuat.")
    print(f"Ukuran dataset awal: {df.shape}")
    print(f"Jumlah duplikat awal: {df.duplicated().sum()}")

    df_clean = clean_data(df)

    print("Data berhasil dibersihkan.")
    print(f"Ukuran dataset setelah cleaning: {df_clean.shape}")
    print(f"Jumlah duplikat setelah cleaning: {df_clean.duplicated().sum()}")

    train_data, test_data, diabetes_preprocessed = split_and_scale_data(df_clean)

    save_data(train_data, test_data, diabetes_preprocessed, output_dir)

    print("Preprocessing selesai.")
    print(f"Ukuran train data: {train_data.shape}")
    print(f"Ukuran test data: {test_data.shape}")
    print(f"Data train disimpan di: {os.path.join(output_dir, 'train.csv')}")
    print(f"Data test disimpan di: {os.path.join(output_dir, 'test.csv')}")
    print(f"Data gabungan disimpan di: {os.path.join(output_dir, 'diabetes_preprocessed.csv')}")


if __name__ == "__main__":
    input_path = "../diabetes_raw/diabetes.csv"
    output_dir = "diabetes_preprocessing"

    preprocess_data(input_path, output_dir)