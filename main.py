import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Akbaba Asistan", page_icon="🚀")

st.title("🚀 Akbaba Günlük Takip")

# 1. Dosya Kontrolü (Verilerin tutulacağı yer)
DATA_FILE = "günlük_takip.csv"

# 2. Form Alanları
with st.form("takip_formu"):
    tarih = st.date_input("📅 Tarih", datetime.now())
    uyanıs = st.time_input("☀️ Uyanış Saati")
    enerji = st.slider("⚡ Enerji Seviyesi (1-10)", 1, 10, 5)
    notlar = st.text_area("📝 Günlük Notun")
    
    submit = st.form_submit_button("💾 KAYDET")

# 3. Kaydetme İşlemi
if submit:
    yeni_data = {
        "Tarih": [tarih],
        "Uyanis": [uyanıs.strftime("%H:%M")],
        "Enerji": [enerji],
        "Notlar": [notlar]
    }
    df_yeni = pd.DataFrame(yeni_data)

    # Dosya varsa üstüne ekle, yoksa yeni oluştur
    if os.path.exists(DATA_FILE):
        df_eski = pd.read_csv(DATA_FILE)
        df_son = pd.concat([df_eski, df_yeni], ignore_index=True)
    else:
        df_son = df_yeni
    
    df_son.to_csv(DATA_FILE, index=False)
    st.balloons()
    st.success("Aga veri kaydedildi! (Uygulamanın içine)")

st.divider()

# 4. Verileri İndirme Butonu (Buradan Excel'e aktarabilirsin)
if os.path.exists(DATA_FILE):
    st.subheader("📊 Kayıtlı Verilerin")
    df_goster = pd.read_csv(DATA_FILE)
    st.dataframe(df_goster)
    
    csv = df_goster.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="📥 Tüm Verileri Bilgisayara İndir (Excel/CSV)",
        data=csv,
        file_name=f"akbaba_verileri_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv",
    )
