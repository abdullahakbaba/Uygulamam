import streamlit as st
import pandas as pd
from datetime import datetime, time

# Uygulama Ayarları
st.set_page_config(page_title="Akbaba'nın Paneli", page_icon="👔", layout="centered")

st.title("🚀 Akbaba Kişisel Asistan")

# --- YENİ BAŞLIK: SABAH RUTİNİ & MANEVİYAT ---
st.markdown("## 🕌 Güne Başlarken (Sabah Rutini)")
with st.container():
    col_t1, col_t2 = st.columns([1, 1])
    with col_t1:
        uyanis_saati = st.time_input("☀️ Uyandığın Saat", time(7, 0))
    with col_t2:
        mod = st.select_slider("⚡ Enerji Seviyen", options=["Düşük", "Orta", "Yüksek", "Fişek"])

    # Maneviyat Görevleri tek bir blok içinde
    st.markdown("#### 📖 Manevi Ödevler")
    m1, m2, m3 = st.columns(3)
    with m1:
        k_okundu = st.checkbox("Kur'an-ı Kerim", key="kuran_check")
        if k_okundu:
            k_sayfa = st.number_input("Sayfa Sayısı", min_value=0, value=10, key="k_sayfa")
    with m2:
        h_okundu = st.checkbox("Hadis-i Şerif", key="hadis_check")
        if h_okundu:
            h_sayfa = st.number_input("Sayfa Sayısı", min_value=0, value=2, key="h_sayfa")
    with m3:
        st.checkbox("Tefsir Okuması", key="tefsir_check")

st.divider()

# --- BÖLÜM 2: DÜNYEVİ İŞLER & GELİŞİM ---
st.subheader("💻 Yazılım & Kariyer")
# ... (kodun geri kalanı aynı kalabilir)
