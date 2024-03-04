import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

pwd = os.getcwd()

def byhour(df):
    hourly_rental = df.groupby(by='hr')['Total'].mean()
    return hourly_rental

def bymonth(df):
    monthly_rental = df.groupby(by='mnth')['Total'].mean()
    return monthly_rental

hari_df = pd.read_csv("all_data.csv")

# import dataframe
daily_df = pd.read_csv('days.csv')
hourly_df = pd.read_csv('hours.csv')

daily_df['dteday'] = pd.to_datetime(daily_df['dteday'])
hourly_df['dteday'] = pd.to_datetime(hourly_df['dteday'])


# Filter data
min_date = hourly_df["dteday"].min()
max_date = hourly_df["dteday"].max()

bymonth_df = bymonth(hourly_df)
bymonths_df = bymonth(daily_df)

st.header('Bike Sharing Dashboard')
st.markdown("""
<div style="text-align: justify">
  Dashboard ini berfungsi untuk memvisualisasikan data yang menggambarkan penggunaan sepeda berdasarkan bulan dari tahun 2011 sampai 2012. Selain itu, menyajikan perbandingan dari penggunaan bike sharing pada saat weekday dan holiday
</div>
""", unsafe_allow_html=True)

st.markdown("\n")

st.subheader('Jumlah Bike Sharing Pada Tahun 2011')
# Plotting Jumlah Bike Sharing Pada Tahun 2011
st.subheader('Jumlah Rental Sepeda')
# Berdasarkan Bulan
fig, ax = plt.subplots(figsize=(12, 5))

sns.barplot(x='mnth', y='cnt', data=hari_df[hari_df['yr'] == 2011], hue='yr')

plt.xlabel("Bulan")
plt.ylabel("Jumlah Rental Sepeda")
plt.title("Jumlah Rental Sepeda pada Tahun 2011")

ax.set_title("Berdasarkan Bulan", loc="center", fontsize=30)
ax.set_ylabel('Jumlah Rental Sepeda')
ax.set_xlabel('Bulan')
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """Pada tahun 2011, bike sharing paling banyak digunakan pada bulan Juni, sedangkan paling sedikit pada bulan Januari.
           Maka dari itu, perlunya peningkatan dan pengurangan bike sharing pada bulan tersebut.
           """
    )

st.markdown("\n")
st.markdown("\n")
st.subheader(f'Jumlah Bike Sharing Pada Tahun 2012')

# Plotting Jumlah Bike Sharing Pada Tahun 2012
st.subheader('Jumlah Rental Sepeda')
# Berdasarkan Bulan
fig, ax = plt.subplots(figsize=(12, 5))

sns.barplot(x='mnth', y='cnt', data=hari_df[hari_df['yr'] == 2012], hue='yr')

plt.xlabel("Bulan")
plt.ylabel("Jumlah Rental Sepeda")
plt.title("Jumlah Rental Sepeda pada Tahun 2012")

ax.set_title("Berdasarkan Bulan", loc="center", fontsize=30)
ax.set_ylabel('Jumlah Rental Sepeda')
ax.set_xlabel('Bulan')
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """Pada tahun 2011, bike sharing paling banyak digunakan pada bulan September, sedangkan paling sedikit pada bulan Januari. 
        Maka dari itu, perlunya peningkatan dan pengurangan bike sharing pada bulan tersebut.
        """
    )


st.markdown("\n")
st.markdown("\n")
st.subheader(f'Perbandingan Penggunaan Bike Sharing pada saat Weekday dan Holiday')

#Plotting pengguna bike sharing pada saat weekday dan holiday
# Membuat Visualisasi Data Jumlah Casual Users dan Registered Users
st.subheader('Perbandingan Jumlah Pengguna Rental')
col1, col2 = st.columns(2)

with col1:
    Week_day = hari_df['weekday'].sum()
    st.metric('Weekday', value= Week_day)

with col2:
    Holi_day = hari_df['holiday'].sum()
    st.metric('Holiday', value= Holi_day)

# Menampilkan plot
st.subheader('Visualisasi Perbandingan Jumlah Pengguna Rental')
fig, ax = plt.subplots(figsize=(8, 8))
jenis_pengguna = ['WeekDay', 'Holiday']
jumlah_pengguna = [Week_day, Holi_day]
colors = ['#8B4513', '#FFF8DC']
explode = (0.1, 0)

ax.pie(jumlah_pengguna, labels=jenis_pengguna, autopct='%1.1f%%', colors=colors, explode=explode)
st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """Bike sharing sering digunakan pada saat weekday dibandingkan pada saat holiday pada tahun 2011 dan 2012
        """
    )

st.caption('Copyright © Sandy Aryo Mustiko')

    