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

# import dataframe
daily_df = pd.read_csv('days.csv')
hourly_df = pd.read_csv('hours.csv')

daily_df['dteday'] = pd.to_datetime(daily_df['dteday'])
hourly_df['dteday'] = pd.to_datetime(hourly_df['dteday'])


# Filter data
min_date = hourly_df["dteday"].min()
max_date = hourly_df["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image('https://github.com/santuyyy/sandy/blob/main/bikesharing.jpg', width=100)
    st.header('Bike Sharing')
    st.markdown("\n")
    
    st.markdown("""
    <div style="text-align: justify">
        Pilih tanggal untuk melihat data pada rentang tanggal tersebut.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("\n")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
main_df = hourly_df[(hourly_df["dteday"] >= str(start_date)) & 
                (hourly_df["dteday"] <= str(end_date))]


# Menyiapkan dataframe yang dikelompokkan
byhour_df = byhour(main_df)
bymonth_df = bymonth(hourly_df)

st.header('Bike Sharing Dashboard')
st.markdown("""
<div style="text-align: justify">
  Dashboard ini berfungsi untuk memvisualisasikan data yang menggambarkan penggunaan sepeda berdasarkan bulan dari tahun 2011 sampai 2012. Selain itu, menyajikan perbandingan dari penggunaan bike sharing pada saat weekday dan holiday
</div>
""", unsafe_allow_html=True)

st.markdown("\n")

st.subheader('Jumlah Bike Sharing Pada Tahun 2011')
# Plotting Jumlah Bike Sharing Pada Tahun 2011
fig, ax = plt.subplots(figsize=(16, 8))
ax.bar(bymonth_df.index, bymonth_df.values, color='#00E8FF')
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

# Mengubah warna label dan ticks jika diperlukan
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# Menambahkan label x, label y, dan judul
ax.set_xlabel('Month', color='black', fontsize=18)
ax.set_ylabel('Jumlah Bike Sharing', color='black', fontsize=18)

# Tampilkan plot menggunakan st.pyplot()
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
fig, ax = plt.subplots(figsize=(16, 8))
ax.bar(bymonth_df.index, bymonth_df.values, color='#00E8FF')
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

# Mengubah warna label dan ticks jika diperlukan
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# Menambahkan label x, label y, dan judul
ax.set_xlabel('Month', color='black', fontsize=18)
ax.set_ylabel('Jumlah Bike Sharing', color='black', fontsize=18)

# Tampilkan plot menggunakan st.pyplot()
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

labels1 = ['Weekday', 'Holiday']
sizes1 = [15, 3]
colors1 = ['gold', 'yellowgreen']

ax.pie(sizes1, labels=labels1, colors=colors1, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Memastikan lingkaran berbentuk lingkaran
ax.set_title('Perbandingan Penggunaan Bike Sharing pada saat Weekday dan Holiday')
plt.show()

with st.expander("See explanation"):
    st.write(
        """Bike sharing sering digunakan pada saat weekday dibandingkan pada saat holiday pada tahun 2011 dan 2012
        """
    )

st.caption('Copyright © Sandy Aryo Mustiko')

    