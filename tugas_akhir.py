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
    df.columns = df.columns.str.strip()  
    df["Jumlah (Rp)"] = pd.to_numeric(df["Jumlah (Rp)"], errors="coerce").fillna(0)
    return df

st.title("💸 Aplikasi Tracking Pengeluaran")

menu = st.sidebar.radio("Menu", ["Tambah Pengeluaran", "Daftar & Statistik"])

if menu == "Tambah Pengeluaran":
    st.subheader("➕ Tambah Pengeluaran Baru")

    kategori = st.selectbox("Kategori", ["Makanan", "Transportasi", "Hiburan", "Belanja", "Lainnya"])
    deskripsi = st.text_input("Deskripsi Pengeluaran")
    jumlah = st.number_input("Jumlah (Rp)", min_value=0.0, format="%.2f")

    if st.button("Simpan Pengeluaran"):
        with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([kategori, deskripsi, jumlah])
        st.success("Pengeluaran berhasil disimpan!")
        st.balloons()


elif menu == "Daftar & Statistik":
    st.subheader("📋 Daftar Pengeluaran")
    df = load_data()

    if df.empty:
        st.info("Belum ada data pengeluaran.")
    else:
        st.dataframe(df)

        total = df["Jumlah (Rp)"].sum()
        st.metric("💰 Total Pengeluaran", f"Rp {total:,.2f}")

        st.subheader("📊 Grafik Pengeluaran")

        grouped = df.groupby("Kategori")["Jumlah (Rp)"].sum()

        st.write("### Grafik Batang")
        fig1, ax1 = plt.subplots()
        grouped.plot(kind="bar", ax=ax1)
        ax1.set_ylabel("Jumlah (Rp)")
        ax1.set_title("Total Pengeluaran per Kategori")
        st.pyplot(fig1)

        st.write("### Diagram Pie")
        fig2, ax2 = plt.subplots()
        ax2.pie(grouped, labels=grouped.index, autopct="%1.1f%%")
        ax2.set_title("Distribusi Pengeluaran per Kategori")
        st.pyplot(fig2)