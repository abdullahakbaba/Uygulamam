import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime, time

st.set_page_config(page_title="Akbaba Asistan", page_icon="📖")
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🚀 Akbaba Günlük Takip")

# Giriş Alanları
uyanis = st.time_input("☀️ Uyanış", time(5, 0))
enerji = st.select_slider("⚡ Enerji", options=["Düşük", "Orta", "Yüksek", "Fişek"])

c1, c2, c3, c4 = st.columns(4)
with c1: kuran = st.number_input("Kuran", 0, 100, 5)
with c2: tevbe = st.checkbox("Tevbe")
with c3: hadis = st.number_input("Hadis", 0, 100, 2)
with c4: tefsir = st.number_input("Tefsir", 0, 100, 5)

st.divider()
ik = st.checkbox("İng Kelime")
io = st.checkbox("İng Okuma")
id_ = st.checkbox("İng Dinleme")
iy = st.checkbox("İng Yazma")
ak = st.checkbox("Ara Kelime")
ao = st.checkbox("Ara Okuma")
ad = st.checkbox("Ara Dinleme")
ay = st.checkbox("Ara Yazma")
sh = st.checkbox("Hikaye")
sp = st.checkbox("Post")
sr = st.checkbox("Reels")
fikir = st.text_area("Notlar")

if st.button("💾 KAYDET"):
    # Yeni veri
    data = {
        "Tarih": [datetime.now().strftime('%Y-%m-%d')],
        "Uyanis": [uyanis.strftime('%H:%M')],
        "Enerji": [enerji],
        "Kuran": [kuran],
        "Tevbe": ["Evet" if tevbe else "Hayır"],
        "Hadis": [hadis],
        "Tefsir": [tefsir],
        "Ing_Kelime": ["Evet" if ik else "Hayır"],
        "Ing_Okuma": ["Evet" if io else "Hayır"],
        "Ing_Dinleme": ["Evet" if id_ else "Hayır"],
        "Ing_Yazma": ["Evet" if iy else "Hayır"],
        "Ara_Kelime": ["Evet" if ak else "Hayır"],
        "Ara_Okuma": ["Evet" if ao else "Hayır"],
        "Ara_Dinleme": ["Evet" if ad else "Hayır"],
        "Ara_Yazma": ["Evet" if ay else "Hayır"],
        "SM_Hikaye": ["Evet" if sh else "Hayır"],
        "SM_Post": ["Evet" if sp else "Hayır"],
        "SM_Reels": ["Evet" if sr else "Hayır"],
        "Fikir": [fikir]
    }
    yeni_df = pd.DataFrame(data)

    try:
        # Mevcut dosyayı oku
        # ttl=0 kullanarak önbelleği (cache) devre dışı bırakıyoruz
        df = conn.read(worksheet="Sheet1", ttl=0)
        
        # Eğer dosya okunabiliyorsa alt alta ekle
        if df is not None:
            df = pd.concat([df, yeni_df], ignore_index=True)
        else:
            df = yeni_df

        # Güncelle
        conn.update(worksheet="Sheet1", data=df)
        st.balloons()
        st.success("Sonunda Oldu!")
    except Exception as e:
        st.error(f"Hata devam ediyor: {e}")
        st.info("İpucu: Eğer 'Bad Request' diyorsa Google Sheets linkini Secrets kısmından silip tekrar yapıştırıp kaydet.")
