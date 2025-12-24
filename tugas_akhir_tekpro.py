import streamlit as st
import pandas as pd
import csv
import os
import matplotlib.pyplot as plt

FILE_NAME = "pengeluaran.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Kategori", "Deskripsi", "Jumlah (Rp)"])   

def load_data():
    df = pd.read_csv(FILE_NAME)
    df.columns = df.columns.str.strip()  # Bersihkan spasi kolom
    df["Jumlah (Rp)"] = pd.to_numeric(df["Jumlah (Rp)"], errors="coerce").fillna(0)
    return df   

st.title("💸 Aplikasi Tracking Pengeluaran")
menu = st.sidebar.radio("Menu", ["Tambah Pengeluaran", "Daftar & Statistik"])
if menu == "Tambah Pengeluaran":
    st.subheader(" Tambah Pengeluaran Baru")
    kategori = st.selectbox("Kategori", ["Makanan", "Transportasi", "Hiburan", "Belanja", "Lainnya"])
    deskripsi = st.text_input("Deskripsi Pengeluaran")
    jumlah = st.number_input("Jumlah (Rp)", min_value=0.0, format="%.2f")
    if st.button("Simpan Pengeluaran"):
        with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([kategori, deskripsi, jumlah])
        st.success("Pengeluaran berhasil disimpan!")
        st.balloons()

