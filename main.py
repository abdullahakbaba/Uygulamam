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
    st.error("Bağlantı ayarı yapılamadı. Lütfen Secrets kısmını kontrol et.")

# --- ANA BAŞLIK ---
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
    kuran_sayfa = st.number_input("Sayfa", min_value=0, value=5, step=1, key="kuran_ana")
    st.caption("🎯 Hedef: 5 Sayfa") 

with m2:
    st.markdown("**Tevbe Duası**")
    chk_tevbe = st.checkbox("Yapıldı", key="chk_tevbe")
    st.caption("🎯 Günlük")

with m3:
    st.markdown("**Hadis-i Şerif**")
    hadis_sayfa = st.number_input("Miktar", min_value=0, value=2, step=1, key="hadis_ana")
    st.caption("🎯 Hedef: 2 Hadis")

with m4:
    st.markdown("**Tefsir**")
    tefsir_sayfa = st.number_input("Sayfa", min_value=0, value=5, step=1, key="tefsir_ana")
    st.caption("🎯 Hedef: 5 Sayfa")
    
st.divider()

# --- BÖLÜM 2: İŞ & DİL GELİŞİM ---
st.header("💻 İş & Dil Gelişim")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🌎 İngilizce")
    ing_kelime = st.checkbox("Kelime Ezberleme")
    ing_okuma = st.checkbox("Okuma")
    ing_dinleme = st.checkbox("Dinleme")
    ing_yazma = st.checkbox("Yazma")

with c2:
    st.markdown("### 🌎 Arapça")
    ara_kelime = st.checkbox("Arapça Kelime Ezberleme")
    ara_okuma = st.checkbox("Arapça Okuma")
    ara_dinleme = st.checkbox("Arapça Dinleme")
    ara_yazma = st.checkbox("Arapça Yazma")

with c3:
    st.markdown("### 📱 Sosyal Medya")
    sm_hikaye = st.checkbox("Hikaye")
    sm_post = st.checkbox("Post")
    sm_reels = st.checkbox("Reels")

st.divider()

# --- BÖLÜM 3: YENİ FİKİRLER ---
st.header("✨ Yeni Fikirler")
fikir_kategori = st.selectbox("Fikir Türü", ["İş", "Dini", "Genel", "Kişisel"])
fikir_notu = st.text_area("Aklına gelen detayı buraya bırak...")

# --- BÖLÜM 4: KAYDETME ---
if st.button("💾 BUGÜNÜ KAYDET"):
    tarih_str = datetime.now().strftime('%Y-%m-%d')
    
    # Yeni veri satırı (Sheets başlıklarına dikkat)
    yeni_satir = pd.DataFrame([{
        "Tarih": tarih_str,
        "Uyanis": uyanis_saati.strftime('%H:%M'),
        "Enerji": enerji,
        "Kuran": kuran_sayfa,
        "Tevbe": "Evet" if chk_tevbe else "Hayır",
        "Hadis": hadis_sayfa,
        "Tefsir": tefsir_sayfa,
        "Ing_Kelime": ing_kelime,
        "Ara_Kelime": ara_kelime,
        "Sosyal_Medya": f"{sm_hikaye}/{sm_post}/{sm_reels}",
        "Fikir": fikir_notu
    }])

    try:
        # Google Sheets'e Kayıt
        # Not: Sayfa adının Google Sheets'te 'Sayfa1' olduğundan emin ol
        mevcut_veri = conn.read(worksheet="Sayfa1", ttl=0)
        guncel_df = pd.concat([mevcut_veri, yeni_satir], ignore_index=True)
        conn.update(worksheet="Sayfa1", data=guncel_df)
        
        st.balloons()
        st.success(f"Başarıyla kaydedildi aga! Kur'an: {kuran_sayfa}, Hadis: {hadis_sayfa}")
    except Exception as e:
        st.error("Kayıt sırasında hata: Google Sheets bağlantını kontrol et.")
        st.info("Hata detayı: " + str(e))

# Alt Bilgi
st.markdown("---")
st.caption(f"Tarih: {datetime.now().strftime('%d/%m/%Y')} | Allah'ın İzni ile Başaracağız!")
