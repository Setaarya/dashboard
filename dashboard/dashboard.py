import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned datasets
day_df = pd.read_csv("D:\submission\dashboard\main_data.csv")

# Menambahkan logo di sidebar
logo_path = "D:\submission\dashboard\\tensorflow.svg"  # Ganti dengan jalur logo Anda
st.sidebar.image(logo_path, use_column_width=True)

st.title("Dashboard Analisis Penyewaan Sepeda")

# Sidebar for navigation
st.sidebar.title("Navigasi")
option = st.sidebar.selectbox("Pilih Analisis", 
                                ("Perbandingan Sewa Sepeda Setiap Hari", 
                                 "Pengaruh Cuaca", 
                                 "Sewa Berdasarkan Jenis Hari", 
                                 "Sewa Berdasarkan Musim", 
                                 "Sewa Tiap Bulan", 
                                 "Tren Penyewaan Tiap Bulan"))

# Menampilkan sumber data di sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("**Sumber Data:** [Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)")

if option == "Perbandingan Sewa Sepeda Setiap Hari":
    st.subheader("Perbandingan Penyewa Sepeda Setiap Hari")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weekday', y='cnt', data=day_df, order=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],errorbar=None)
    plt.title('Perbandingan Penyewa Sepeda Setiap Hari')
    plt.xlabel('Hari')
    plt.ylabel('Jumlah Penyewa Sepeda')
    st.pyplot(plt)

elif option == "Pengaruh Cuaca":
    st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=day_df, errorbar=None)
    plt.title('Jumlah Penyewa Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Penyewa Sepeda')
    st.pyplot(plt)

elif option == "Sewa Berdasarkan Jenis Hari":
    st.subheader("Sewa Sepeda Berdasarkan Jenis Hari")
    plt.figure(figsize=(10, 6))
    sns.pointplot(data=day_df, x='mnth', y='cnt', hue='workingday', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], errorbar=None)
    plt.title('Jumlah Penyewa Sepeda berdasarkan Jenis Hari')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewa Sepeda')
    st.pyplot(plt)

elif option == "Sewa Berdasarkan Musim":
    st.subheader("Sewa Sepeda Berdasarkan Musim")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', data=day_df, errorbar=None)
    plt.title('Jumlah Penyewa Sepeda berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Penyewa Sepeda')
    st.pyplot(plt)

elif option == "Sewa Tiap Bulan":
    st.subheader("Jumlah Penyewa Sepeda Tiap Bulan")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=day_df, x='mnth', y='cnt', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], errorbar=None)
    plt.title('Penyewa Sepeda Setiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewa Sepeda')
    st.pyplot(plt)

elif option == "Tren Penyewaan Tiap Bulan":
    st.subheader("Tren Penyewaan Sepeda Tiap Bulan")
    plt.figure(figsize=(10, 6))
    sns.pointplot(data=day_df, x='mnth', y='cnt', hue='yr', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], errorbar=None)
    plt.title('Tren Penyewa Sepeda')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewa Sepeda')
    st.pyplot(plt)