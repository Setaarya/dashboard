import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk memuat dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

# Fungsi untuk memfilter data berdasarkan rentang tanggal
def filter_data_by_date(df, start_date, end_date):
    return df[(df['dteday'] >= pd.to_datetime(start_date)) & (df['dteday'] <= pd.to_datetime(end_date))]

# Fungsi untuk visualisasi Perbandingan Sewa Sepeda Setiap Hari
def plot_daily_rent_comparison(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weekday', y='cnt', data=df, 
                order=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], 
                errorbar=None)
    plt.title('Perbandingan Penyewa Sepeda Setiap Hari')
    plt.xlabel('Hari')
    plt.ylabel('Jumlah Penyewa Sepeda')
    plt.tight_layout()
    return plt

# Fungsi untuk visualisasi Pengaruh Cuaca terhadap Penyewaan Sepeda
def plot_weather_impact(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=df, errorbar=None)
    plt.title('Jumlah Penyewa Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Penyewa Sepeda')
    plt.tight_layout()
    return plt

# Fungsi untuk visualisasi Sewa Sepeda Berdasarkan Jenis Hari
def plot_working_day_rent(df):
    plt.figure(figsize=(10, 6))
    sns.pointplot(data=df, x='mnth', y='cnt', hue='workingday', 
                  order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 
                         'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], errorbar=None)
    plt.title('Jumlah Penyewa Sepeda berdasarkan Jenis Hari')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewa Sepeda')
    plt.tight_layout()
    return plt

# Fungsi untuk visualisasi Sewa Sepeda Berdasarkan Musim
def plot_season_rent(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', data=df, errorbar=None)
    plt.title('Jumlah Penyewa Sepeda berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Penyewa Sepeda')
    plt.tight_layout()
    return plt

# Fungsi untuk visualisasi Jumlah Penyewa Sepeda Tiap Bulan
def plot_monthly_rent(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='mnth', y='cnt', 
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 
                       'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], errorbar=None)
    plt.title('Penyewa Sepeda Setiap Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewa Sepeda')
    plt.tight_layout()
    return plt

# Fungsi untuk visualisasi Tren Penyewaan Sepeda Tiap Bulan
def plot_monthly_trend(df):
    plt.figure(figsize=(10, 6))
    sns.pointplot(data=df, x='mnth', y='cnt', hue='yr', 
                  order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 
                         'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], errorbar=None)
    plt.title('Tren Penyewa Sepeda')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewa Sepeda')
    plt.tight_layout()
    return plt
