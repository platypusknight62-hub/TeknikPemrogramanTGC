import pandas as pd


input_file = "data.txt"
output_file = "data_normalized.txt"

try:
)
    df = pd.read_csv(input_file)

    
    if not {'shot', 'receiver', 'twt'}.issubset(df.columns):
        raise ValueError("Kolom yang dibutuhkan tidak lengkap (harus ada: shot, receiver, twt).")

    
    twt_min = df['twt'].min()

    
    denominator = 600 - twt_min
    if denominator == 0:
        raise ZeroDivisionError("Proses normalisasi gagal: 600 - twt_min = 0 (pembagian nol).")

    df['twt_norm'] = (df['twt'] - twt_min) / denominator

    
    df.to_csv(output_file, index=False)

    print("✅ Data berhasil dinormalisasi dan disimpan ke:", output_file)
    print(df)

except FileNotFoundError:
    print("❌ File tidak ditemukan. Pastikan nama file dan lokasinya benar.")
except pd.errors.EmptyDataError:
    print("❌ File kosong atau format tidak sesuai CSV.")
except Exception as e:
    print(f"⚠️ Terjadi kesalahan: {e}")
