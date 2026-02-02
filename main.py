import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime, time

# 1. Uygulama Ayarları
st.set_page_config(page_title="Akbaba Asistan", page_icon="📖", layout="centered")

# 2. Google Sheets Bağlantısı
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🚀 Akbaba Günlük Takip Paneli")

# --- BÖLÜM 1: GÜNE BAŞLARKEN ---
st.header("🕌 Güne Başlarken")
col_u1, col_u2 = st.columns(2)
with col_u1:
    uyanis_v = st.time_input("☀️ Uyandığın Saat", time(5, 0))
with col_u2:
    enerji_v = st.select_slider("⚡ Enerji Seviyen", options=["Düşük", "Orta", "Yüksek", "Fişek"])

st.markdown("#### 📝 Günlük Okuma")
m1, m2, m3, m4 = st.columns(4)
with m1:
    kuran_v = st.number_input("Kur'an Sayfa", 0, 500, 5)
with m2:
    tevbe_v = st.checkbox("Tevbe Duası Yapıldı", key="t_v")
with m3:
    hadis_v = st.number_input("Hadis Miktarı", 0, 100, 2)
with m4:
    tefsir_v = st.number_input("Tefsir Sayfa", 0, 500, 5)

st.divider()

# --- BÖLÜM 2: İŞ & DİL ---
st.header("💻 İş & Dil")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### 🌎 İngilizce")
    ik = st.checkbox("İngilizce Kelime")
    io = st.checkbox("İngilizce Okuma")
    idin = st.checkbox("İngilizce Dinleme")
    iy = st.checkbox("İngilizce Yazma")
with c2:
    st.markdown("### 🌎 Arapça")
    ak = st.checkbox("Arapça Kelime")
    ao = st.checkbox("Arapça Okuma")
    adin = st.checkbox("Arapça Dinleme")
    ay = st.checkbox("Arapça Yazma")
with c3:
    st.markdown("### 📱 Sosyal Medya")
    sh = st.checkbox("Hikaye")
    sp = st.checkbox("Post")
    sr = st.checkbox("Reels")

st.divider()
fikir_v = st.text_area("✨ Yeni Fikirler")

if st.button("💾 VERİLERİ GOOGLE SHEETS'E KAYDET"):
    tarih_str = datetime.now().strftime('%Y-%m-%d')
    
    # Senin koddaki değişkenleri (ik, io vb.) tek tek buraya eşitledim
    yeni_satir = {
        "Tarih": tarih_str,
        "Uyanis": uyanis_v.strftime('%H:%M'),
        "Enerji": enerji_v,
        "Kuran": kuran_v,
        "Tevbe": "Evet" if tevbe_v else "Hayır",
        "Hadis": hadis_v,
        "Tefsir": tefsir_v,
        "Ing_Kelime": "Evet" if ik else "Hayır",
        "Ing_Okuma": "Evet" if io else "Hayır",
        "Ing_Dinleme": "Evet" if idin else "Hayır",
        "Ing_Yazma": "Evet" if iy else "Hayır",
        "Ara_Kelime": "Evet" if ak else "Hayır",
        "Ara_Okuma": "Evet" if ao else "Hayır",
        "Ara_Dinleme": "Evet" if adin else "Hayır",
        "Ara_Yazma": "Evet" if ay else "Hayır",
        "SM_Hikaye": "Evet" if sh else "Hayır",
        "SM_Post": "Evet" if sp else "Hayır",
        "SM_Reels": "Evet" if sr else "Hayır",
        "Fikir": fikir_v
    }

    try:
        # Sheet1 ismini kontrol etmeyi unutma aga!
        df = conn.read(worksheet="Sheet1", ttl=0)
        
        # Eğer tablo tamamen boşsa başlıkları kendisi oluştursun
        if df is None or df.empty:
            df_guncel = pd.DataFrame([yeni_satir])
        else:
            # Sütunları hizalayarak ekle (Eksik/Fazla sütun hatasını önler)
            yeni_df = pd.DataFrame([yeni_satir])
            df_guncel = pd.concat([df, yeni_df], ignore_index=True, sort=False)

        conn.update(worksheet="Sheet1", data=df_guncel)
        st.balloons()
        st.success("SONUNDA OLDU AGA!")
    except Exception as e:
        st.error(f"Hata detayı (Bunu bana at): {e}")
