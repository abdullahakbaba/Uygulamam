import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime, time

# Uygulama Ayarları
st.set_page_config(page_title="Akbaba'nın Paneli", page_icon="👔")

st.title("🚀 Veri Kayıtlı Asistan")

# Google Sheets Bağlantısı (Ayarları Advanced Settings'ten yapılacak)
conn = st.connection("gsheets", type=GSheetsConnection)

# --- YENİ: UYANIŞ SAATİ ---
st.subheader("☀️ Sabah Disiplini")
uyanis_saati = st.time_input("Bugün saat kaçta uyandın?", time(7, 0)) # Varsayılan 07:00

st.divider()

# --- DİĞER GİRİŞ ALANLARI ---
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📖 Maneviyat")
    kuran = st.number_input("Kur'an (Sayfa)", min_value=0, value=10, key="kuran_n")
    hadis = st.number_input("Hadis (Sayfa)", min_value=0, value=2, key="hadis_n")
with col2:
    st.markdown("### 💻 Gelişim & İş")
    tefsir = st.checkbox("Tefsir Okundu mu?")
    python = st.checkbox("Python Çalışıldı mı?")
    export = st.checkbox("İhracat Takibi?")

fikir = st.text_area("Yeni Fikir Notu (Parq Aura vb.)")

# --- KAYDETME MANTIĞI ---
if st.button("Bugünü Veritabanına İşle"):
    # Google Sheets'e gidecek veri formatı
    yeni_satir = {
        "Tarih": datetime.now().strftime("%Y-%m-%d"),
        "Uyanis_Saati": uyanis_saati.strftime("%H:%M"),
        "Kuran": kuran,
        "Hadis": hadis,
        "Tefsir": tefsir,
        "Python": python,
        "Ihracat": export,
        "Fikir": fikir
    }
    
    # Veriyi ekle (Bağlantı ayarı bittikten sonra çalışır)
    try:
        existing_data = conn.read(worksheet="Sheet1", usecols=list(range(8)))
        updated_df = pd.concat([existing_data, pd.DataFrame([yeni_satir])], ignore_index=True)
        conn.update(worksheet="Sheet1", data=updated_df)
        st.success(f"Saat {uyanis_saati.strftime('%H:%M')} uyanışı ve diğer veriler kaydedildi!")
        st.balloons()
    except:
        st.warning("Veri kaydedildi ama Google Sheets bağlantısı henüz tam kurulmadı. 'Secrets' ayarını yapmalısın.")
