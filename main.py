import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime, time

# 1. Uygulama Ayarları
st.set_page_config(page_title="Akbaba'nın Paneli", page_icon="👔", layout="centered")

# 2. Google Sheets Bağlantısı
# NOT: Bu kısmın çalışması için 'requirements.txt' içinde 'st-gsheets-connection' yazmalı.
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception as e:
    st.error("Bağlantı ayarı yapılamadı. Lütfen requirements.txt dosyasını kontrol et.")

st.title("🚀 Kişisel Yönetim Paneli")

# --- BÖLÜM 1: SABAH RUTİNİ ---
st.subheader("☀️ Sabah Disiplini")
uyanis_saati = st.time_input("Bugün saat kaçta uyandın?", time(7, 0))

st.divider()

# --- BÖLÜM 2: GÜNLÜK GÖREVLER ---
st.subheader("✅ Bugünün Görevleri")
tarih = datetime.now().strftime("%d/%m/%Y")
st.info(f"Bugünün Tarihi: {tarih}")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📖 Kur'an")
    kuran_check = st.checkbox("Okundu", key="chk_kuran")
    kuran_sayfa = st.number_input("Sayfa:", min_value=0, value=10, step=1, key="num_kuran")

with col2:
    st.markdown("### 📖 Hadis")
    hadis_check = st.checkbox("Okundu", key="chk_hadis")
    hadis_sayfa = st.number_input("Sayfa:", min_value=0, value=2, step=1, key="num_hadis")
    tefsir_check = st.checkbox("Tefsir", key="chk_tefsir")

with col3:
    st.markdown("### 💻 Gelişim")
    python_check = st.checkbox("Python/Pandas", key="chk_python")
    export_check = st.checkbox("İhracat Takip", key="chk_export")

# --- BÖLÜM 3: FİKİR DEFTERİ ---
st.divider()
st.subheader("💡 Parq Aura & Fikirler")
kategori = st.selectbox("Kategori Seç", ["Parq Aura (Moda)", "Ekonomi & Master", "Genel"])
fikir = st.text_area("Aklına gelen notu buraya yaz...", placeholder="Yeni model fikri, pazar araştırması vb.")

# --- BÖLÜM 4: VERİLERİ KAYDET ---
st.divider()
if st.button("💾 Bugünü Veritabanına Kaydet"):
    yeni_satir = {
        "Tarih": datetime.now().strftime("%Y-%m-%d"),
        "Uyanis_Saati": uyanis_saati.strftime("%H:%M"),
        "Kuran": kuran_sayfa if kuran_check else 0,
        "Hadis": hadis_sayfa if hadis_check else 0,
        "Tefsir": tefsir_check,
        "Python": python_check,
        "Ihracat": export_check,
        "Fikir": fikir
    }
    
    try:
        # Google Sheets'ten mevcut veriyi oku
        # 'Sheet1' kısmını Google Sheets'teki sayfa adınla aynı yap (genelde 'Sayfa1' veya 'Sheet1'dir)
        existing_data = conn.read(worksheet="Sheet1", ttl=0) 
        updated_df = pd.concat([existing_data, pd.DataFrame([yeni_satir])], ignore_index=True)
        
        # Güncellenmiş listeyi geri yaz
        conn.update(worksheet="Sheet1", data=updated_df)
        
        st.balloons()
        st.success("Harika! Veriler başarıyla Google Sheets'e işlendi.")
    except Exception as e:
        st.warning("Görüntü hazır ama Google Sheets bağlantısı henüz kurulmadı.")
        st.info("Streamlit Cloud Ayarları > Secrets kısmına bağlantı kodunu eklemelisin.")

# Alt Bilgi
st.markdown("---")
st.caption("Akbaba Personal Assistant v2.0 | 2026")
