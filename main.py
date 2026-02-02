import streamlit as st
import pandas as pd
from datetime import datetime

# Uygulama Ayarları
st.set_page_config(page_title="Akbaba'nın Paneli", page_icon="👔", layout="centered")

st.title("🚀 Kişisel Yönetim Paneli")

# --- BÖLÜM 1: GÜNLÜK RUTİNLER ---
st.subheader("✅ Bugünün Görevleri")
tarih = datetime.now().strftime("%d/%m/%Y")
st.write(f"Tarih: {tarih}")

# Sütunları 3'e çıkarıyoruz ki col3 hata vermesin
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📖 Kur'an")
    kuran_check = st.checkbox("Okundu", key="chk_kuran")
    kuran_sayfa = st.number_input("Sayfa:", min_value=0, value=10, step=1, key="num_kuran")

with col2:
    st.markdown("### 📖 Hadis")
    hadis_check = st.checkbox("Okundu", key="chk_hadis")
    hadis_sayfa = st.number_input("Sayfa:", min_value=0, value=2, step=1, key="num_hadis")

with col3:
    st.markdown("### 📖 Tefsir")
    tefsir_check = st.checkbox("Okundu", key="chk_tefsir")


# --- BÖLÜM 2: FİKİR DEFTERİ ---
st.divider()
st.subheader("💡 Parq Aura & Fikirler")
kategori = st.selectbox("Kategori Seç", ["Parq Aura (Moda)", "Ekonomi & Master", "Genel"])
fikir = st.text_area("Aklına gelen harika fikri buraya yaz...", key="idea_text")

if st.button("Kaydet"):
    st.balloons()
    st.success("Fikir başarıyla hafızaya alındı!")

# --- BÖLÜM 3: ÖZEL NOTLAR ---
st.divider()
with st.expander("📅 Önemli Hatırlatıcılar"):
    st.write("- Ocak 2026 Mezuniyet Süreci")
    st.write("- Katar Üniversitesi Başvuru Tarihleri")
    st.write("- Ocean Export Gemi Takvimi")

# Stil düzenlemesi
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stCheckbox { font-size: 18px !important; }
    </style>
    """, unsafe_allow_html=True)
