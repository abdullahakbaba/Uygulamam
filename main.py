import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime, time

# 1. Uygulama Ayarları
st.set_page_config(page_title="Akbaba Asistan", page_icon="📖")
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🚀 Akbaba Günlük Takip")

# --- FORM ALANLARI ---
uyanis_v = st.time_input("☀️ Uyanış", time(5, 0))
enerji_v = st.select_slider("⚡ Enerji", options=["Düşük", "Orta", "Yüksek", "Fişek"])

col1, col2, col3, col4 = st.columns(4)
with col1: kuran_v = st.number_input("Kuran", 0, 100, 5)
with col2: tevbe_v = st.checkbox("Tevbe")
with col3: hadis_v = st.number_input("Hadis", 0, 100, 2)
with col4: tefsir_v = st.number_input("Tefsir", 0, 100, 5)

st.divider()
st.markdown("### 🌎 Dil & Sosyal Medya")
c1, c2, c3 = st.columns(3)
with c1:
    ik = st.checkbox("İng Kelime")
    io = st.checkbox("İng Okuma")
    id_ = st.checkbox("İng Dinleme")
    iy = st.checkbox("İng Yazma")
with c2:
    ak = st.checkbox("Ara Kelime")
    ao = st.checkbox("Ara Okuma")
    ad = st.checkbox("Ara Dinleme")
    ay = st.checkbox("Ara Yazma")
with c3:
    sh = st.checkbox("Hikaye")
    sp = st.checkbox("Post")
    sr = st.checkbox("Reels")

fikir_v = st.text_area("✨ Yeni Fikirler")

# --- KAYIT BUTONU ---
if st.button("💾 VERİLERİ KAYDET"):
    # Bu sözlükteki isimler Excel başlıklarıyla %100 aynı!
    yeni_satir = {
        "Tarih": datetime.now().strftime('%Y-%m-%d'),
        "Uyanis": uyanis_v.strftime('%H:%M'),
        "Enerji": enerji_v,
        "Kuran": kuran_v,
        "Tevbe": "Evet" if tevbe_v else "Hayır",
        "Hadis": hadis_v,
        "Tefsir": tefsir_v,
        "Ing_Kelime": "Evet" if ik else "Hayır",
        "Ing_Okuma": "Evet" if io else "Hayır",
        "Ing_Dinleme": "Evet" if id_ else "Hayır",
        "Ing_Yazma": "Evet" if iy else "Hayır",
        "Ara_Kelime": "Evet" if ak else "Hayır",
        "Ara_Okuma": "Evet" if ao else "Hayır",
        "Ara_Dinleme": "Evet" if ad else "Hayır",
        "Ara_Yazma": "Evet" if ay else "Hayır",
        "SM_Hikaye": "Evet" if sh else "Hayır",
        "SM_Post": "Evet" if sp else "Hayır",
        "SM_Reels": "Evet" if sr else "Hayır",
        "Fikir": fikir_v
    }

    try:
        # Önce tabloyu oku
        df = conn.read(worksheet="Sheet1", ttl=0)
        # Yeni veriyi ekle
        df_guncel = pd.concat([df, pd.DataFrame([yeni_satir])], ignore_index=True)
        # Geri yaz
        conn.update(worksheet="Sheet1", data=df_guncel)
        st.balloons()
        st.success("Sonunda başardık aga!")
    except Exception as e:
        st.error(f"Hata: {e}")
