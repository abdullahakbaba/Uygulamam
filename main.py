import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime, time

# 1. Uygulama Ayarları
st.set_page_config(page_title="Akbaba Asistan", page_icon="📖", layout="centered")

# 2. Google Sheets Bağlantısı
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception as e:
    st.error("Bağlantı hatası! Secrets ayarlarını kontrol et.")

st.title("🚀 Akbaba Günlük Takip Paneli")

# --- BÖLÜM 1: GÜNE BAŞLARKEN ---
st.header("🕌 Güne Başlarken")
col_u1, col_u2 = st.columns(2)
with col_u1:
    uyanis_saati = st.time_input("☀️ Uyandığın Saat", time(5, 0))
with col_u2:
    enerji = st.select_slider("⚡ Enerji Seviyen", options=["Düşük", "Orta", "Yüksek", "Fişek"])

st.markdown("#### 📝 Günlük Okuma Miktarların")
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown("**Kur'an-ı Kerim**")
    kuran_sayfa = st.number_input("Sayfa", 0, 500, 5, key="kuran_n")
with m2:
    st.markdown("**Tevbe Duası**")
    chk_tevbe = st.checkbox("Yapıldı", key="t_c")
with m3:
    st.markdown("**Hadis-i Şerif**")
    hadis_sayfa = st.number_input("Miktar", 0, 100, 2, key="h_n")
with m4:
    st.markdown("**Tefsir**")
    tefsir_sayfa = st.number_input("Sayfa", 0, 500, 5, key="tf_n")

st.divider()

# --- BÖLÜM 2: İŞ & DİL GELİŞİM ---
st.header("💻 İş & Dil Gelişim")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🌎 İngilizce")
    i_kel = st.checkbox("Kelime Ezber", key="i_k")
    i_oku = st.checkbox("Okuma", key="i_o")
    i_din = st.checkbox("Dinleme", key="i_d")
    i_yaz = st.checkbox("Yazma", key="i_y")

with c2:
    st.markdown("### 🌎 Arapça")
    a_kel = st.checkbox("Kelime Ezber", key="a_k")
    a_oku = st.checkbox("Arapça Okuma", key="a_o")
    a_din = st.checkbox("Arapça Dinleme", key="a_d")
    a_yaz = st.checkbox("Arapça Yazma", key="a_y")

with c3:
    st.markdown("### 📱 Sosyal Medya")
    s_hik = st.checkbox("Hikaye", key="s_h")
    s_pos = st.checkbox("Post", key="s_p")
    s_ree = st.checkbox("Reels", key="s_r")

st.divider()

# --- BÖLÜM 3: YENİ FİKİRLER ---
st.header("✨ Yeni Fikirler")
fikir_kat = st.selectbox("Fikir Türü", ["İş", "Dini", "Genel", "Kişisel"])
fikir_not = st.text_area("Notunu buraya bırak...", key="f_n")

# --- BÖLÜM 4: KAYDETME ---
if st.button("💾 VERİLERİ GOOGLE SHEETS'E KAYDET"):
    tarih_str = datetime.now().strftime('%Y-%m-%d')
    
    yeni_satir = pd.DataFrame([{
        "Tarih": tarih_str,
        "Uyanis": uyanis_saati.strftime('%H:%M'),
        "Enerji": enerji,
        "Kuran": kuran_sayfa,
        "Tevbe": "Evet" if chk_tevbe else "Hayır",
        "Hadis": hadis_sayfa,
        "Tefsir": tefsir_sayfa,
        "Ing_Kelime": "Evet" if i_kel else "Hayır",
        "Ing_Okuma": "Evet" if i_oku else "Hayır",
        "Ing_Dinleme": "Evet" if i_din else "Hayır",
        "Ing_Yazma": "Evet" if i_yaz else "Hayır",
        "Ara_Kelime": "Evet" if a_kel else "Hayır",
        "Ara_Okuma": "Evet" if a_oku else "Hayır",
        "Ara_Dinleme": "Evet" if a_din else "Hayır",
        "Ara_Yazma": "Evet" if a_yaz else "Hayır",
        "SM_Hikaye": "Evet" if s_hik else "Hayır",
        "SM_Post": "Evet" if s_pos else "Hayır",
        "SM_Reels": "Evet" if s_ree else "Hayır",
        "Fikir": fikir_not
    }])

    try:
        # worksheet ismini "Sheet1" olarak kullanıyoruz
        mevcut_veri = conn.read(worksheet="Sheet1", ttl=0)
        
        if mevcut_veri is not None and not mevcut_veri.empty:
            guncel_df = pd.concat([mevcut_veri, yeni_satir], ignore_index=True)
        else:
            guncel_df = yeni_satir

        conn.update(worksheet="Sheet1", data=guncel_df)
        
        st.balloons()
        st.success("Tüm detaylar Excel'e işlendi aga! Helal olsun.")
    except Exception as e:
        st.error(f"Hata: {e}")
