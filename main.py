import streamlit as st
import pandas as pd
from datetime import datetime

# Uygulama Başlığı
st.set_page_config(page_title="Akbaba'nın Paneli", page_icon="👔", layout="centered")

st.title("🚀 Kişisel Yönetim Paneli")

# --- BÖLÜM 1: GÜNLÜK RUTİNLER ---
st.subheader("✅ Bugünün Görevleri")
tarih = datetime.now().strftime("%d/%m/%Y")
st.write(f"Tarih: {tarih}")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📖 Risale-i Nur")
    risale_okundu = st.checkbox("Bugün Okundu", key="rn_check")
    # Sayı giriş alanı: Varsayılan 10, ama sen 0-500 arası istediğini yazabilirsin
    risale_sayfa = st.number_input("Kaç sayfa okudun?", min_value=0, value=10, step=1, key="rn_page")
with col2:
    st.markdown("### 💻 İş & Yazılım")
    r3 = st.checkbox("Python/Pandas Çalışıldı")
    r4 = st.checkbox("İhracat Evrak Takibi")

# --- BÖLÜM 2: FİKİR DEFTERİ ---
st.divider()
st.subheader("💡 Parq Aura & Fikirler")
kategori = st.selectbox("Kategori Seç", ["Parq Aura (Moda)", "Ekonomi & Master", "Genel"])
fikir = st.text_area("Aklına gelen harika fikri buraya yaz...")

if st.button("Kaydet"):
    st.balloons()
    st.success("Fikir başarıyla hafızaya alındı!")

# --- BÖLÜM 3: ÖZEL NOTLAR ---
st.divider()
with st.expander("📅 Önemli Hatırlatıcılar"):
    st.write("- Ocak 2026 Mezuniyet Süreci")
    st.write("- Katar Üniversitesi Başvuru Tarihleri")
    st.write("- Ocean Export Gemi Takvimi")

# Stil düzenlemesi (Telefon için daha şık dursun)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stCheckbox { font-size: 20px !important; }
    </style>
    """, unsafe_allow_html=True)
