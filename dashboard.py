import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st 
import matplotlib.lines as mlines

df = pd.read_csv('air_quality_fixed.csv')

quality_air_station = df.groupby(['station','year'])[['PM2.5','PM10','SO2','NO2','CO','O3']].mean().reset_index()

df_max_mean = quality_air_station.max()

df_min_mean = quality_air_station.min()

st.header('Air Quality Dashboard')

col1,col2 = st.columns(2)

with col1 : 
    st.caption('Kualitas udara terburuk selama 2013-2017')
    st.header(df_max_mean['station'])
    st.subheader(df_max_mean['year'])

    col12,col22 = st.columns(2)
    with col12 : 
        st.metric("PM2.5",format(df_max_mean['PM2.5'],'.2f'))
        st.metric("PM10",format(df_max_mean['PM10'],'.2f'))
        st.metric("SO2",format(df_max_mean['SO2'],'.2f'))

    with col22 : 
        st.metric("NO2",format(df_max_mean['NO2'],'.2f'))
        st.metric("CO",format(df_max_mean['CO'],'.2f'))
        st.metric("O3",format(df_max_mean['O3'],'.2f'))

with col2 : 
    st.caption('Kualitas udara terbaik selama 2013-2017')
    st.header(df_min_mean['station'])
    st.subheader(df_min_mean['year'])

    col12,col22 = st.columns(2)
    with col12 : 
        st.metric("PM2.5",format(df_min_mean['PM2.5'],'.2f'))
        st.metric("PM10",format(df_min_mean['PM10'],'.2f'))
        st.metric("SO2",format(df_min_mean['SO2'],'.2f'))

    with col22 : 
        st.metric("NO2",format(df_min_mean['NO2'],'.2f'))
        st.metric("CO",format(df_min_mean['CO'],'.2f'))
        st.metric("O3",format(df_min_mean['O3'],'.2f'))

st.subheader('Kualitas Udara Setiap Stasiun Tahun 2013-2017')
st.caption('Berdasarkan indikator PM2.5, PM10,SO2,NO2,CO,O3')
#mengatur canvas untuk melakukan plot dengan 2 baris dan 3 kolom
fig,ax = plt.subplots(1,2,figsize=(35,15))

#mengatur jarak baris(height) dan kolom(width)
fig.tight_layout(w_pad=25)

colors = ["#FA6161", "#FA6161", "#FA6161", "#D3D3D3", "#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3" ,"#D3D3D3","#8BFE47","#8BFE47","#8BFE47"]

sns.barplot(x='PM2.5',y='station',data=quality_air_station.sort_values(by='PM2.5',ascending=False),ax=ax[0],palette=colors)
ax[0].tick_params(axis='y',labelsize=30)
ax[0].tick_params(axis='x',labelsize=30)
ax[0].set_title('Kadar PM2.5 Setiap Stasiun',loc='center',fontsize=50)
ax[0].set_xlabel('Kadar PM2.5',fontsize=35)

sns.barplot(x='PM10',y='station',data=quality_air_station.sort_values(by='PM10',ascending=False),ax=ax[1],palette=colors)
ax[1].tick_params(axis='y',labelsize=30)
ax[1].tick_params(axis='x',labelsize=30)
ax[1].set_title('Kadar PM10 Setiap Stasiun',loc='center',fontsize=50)
ax[1].set_xlabel('Kadar PM10',fontsize=35)

st.pyplot(fig)

fig,ax = plt.subplots(1,2,figsize=(35,15))

#mengatur jarak baris(height) dan kolom(width)
fig.tight_layout(w_pad=25)

colors = ["#FA6161", "#FA6161", "#FA6161", "#D3D3D3", "#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3" ,"#D3D3D3","#8BFE47","#8BFE47","#8BFE47"]

sns.barplot(x='SO2',y='station',data=quality_air_station.sort_values(by='SO2',ascending=False),ax=ax[0],palette=colors)
ax[0].tick_params(axis='y',labelsize=30)
ax[0].tick_params(axis='x',labelsize=30)
ax[0].set_title('Kadar SO2 Setiap Stasiun',loc='center',fontsize=50)
ax[0].set_xlabel('Kadar SO2',fontsize=35)


sns.barplot(x='NO2',y='station',data=quality_air_station.sort_values(by='NO2',ascending=False),ax=ax[1],palette=colors)
ax[1].tick_params(axis='y',labelsize=30)
ax[1].tick_params(axis='x',labelsize=30)
ax[1].set_title('Kadar NO2 Setiap Stasiun',loc='center',fontsize=50)
ax[1].set_xlabel('Kadar NO2',fontsize=35)

st.pyplot(fig)

fig,ax = plt.subplots(1,2,figsize=(35,15))

#mengatur jarak baris(height) dan kolom(width)
fig.tight_layout(w_pad=25)

colors = ["#FA6161", "#FA6161", "#FA6161", "#D3D3D3", "#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3" ,"#D3D3D3","#8BFE47","#8BFE47","#8BFE47"]

sns.barplot(x='CO',y='station',data=quality_air_station.sort_values(by='CO',ascending=False),ax=ax[0],palette=colors)
ax[0].tick_params(axis='y',labelsize=30)
ax[0].tick_params(axis='x',labelsize=30)
ax[0].set_title('Kadar CO Setiap Stasiun',loc='center',fontsize=50)
ax[0].set_xlabel('Kadar CO',fontsize=35)


sns.barplot(x='O3',y='station',data=quality_air_station.sort_values(by='O3',ascending=False),ax=ax[1],palette=colors)
ax[1].tick_params(axis='y',labelsize=30)
ax[1].tick_params(axis='x',labelsize=30)
ax[1].set_title('Kadar O3 Setiap Stasiun',loc='center',fontsize=50)
ax[1].set_xlabel('Kadar O3',fontsize=35)

st.pyplot(fig)

st.subheader('Kuliatas Udara Tahun 2013 - 2017')
st.caption('PM memiliki ukuran yaitu berukuran kurang dari 100 µm, namun berdasarkan studi epidemiologi PM2,5 lebih berbahaya dari PM10 dan TSP, karena dapat menyusup jauh dalam area alveoli paru-paru manusia.')

per_year_quality = df.groupby(['year'])[['PM2.5','PM10','SO2','NO2','CO','O3']].mean().reset_index()

fig,ax = plt.subplots(figsize=(16,8))
ax.plot(per_year_quality['year'],per_year_quality['PM2.5'],marker='o',linewidth=2,color="#f1c232",label='PM2.5')
ax.plot(per_year_quality['year'],per_year_quality['PM10'],marker='o',linewidth=2,color="#09009f",label='PM10')
plt.legend()
ax.tick_params(axis='x',labelsize=15)
ax.tick_params(axis='y',labelsize=30)
ax.set_title('PM2.5 dan PM2.5 Tahun 2013-2017',fontsize=25)

st.pyplot(fig)

st.subheader('Kualitas PM2.5 dan PM10')
st.caption('Peningkatan kedua indikator menyebabkan semakin banyak sumber polutan yang ada dan dampaknya')

fig,ax = plt.subplots()
sns.scatterplot(x= quality_air_station['PM2.5'],y = quality_air_station['PM10'])
line = mlines.Line2D([0,1],[0,1],color='red')
transform=ax.transAxes
line.set_transform(transform)
ax.add_line(line)

st.pyplot(fig)

col1,col2,col3 = st.columns(3) 

with col1:
    st.write(' ')
with col2:
    st.caption('Copyright (C) Jonathan Lexi 2023')
with col3:
    st.write(' ')





