import streamlit as st
import pandas as pd
from datetime import datetime, time

# Uygulama Ayarları
st.set_page_config(page_title="Akbaba Asistan", page_icon="📖", layout="centered")

# --- ANA BAŞLIK ---
st.title("🚀 Akbaba Günlük Takip Paneli")

# --- BÖLÜM 1: GÜNE BAŞLARKEN & MANEVİ TAKİP ---
# Bu başlık altında tüm uyanış ve okuma miktarlarını topluyoruz
st.header("🕌 Güne Başlarken")

# İlk satır: Uyanış ve Enerji
col_u1, col_u2 = st.columns(2)
with col_u1:
    uyanis_saati = st.time_input("☀️ Uyandığın Saat", time(5, 0))
with col_u2:
    enerji = st.select_slider("⚡ Enerji Seviyen", options=["Düşük", "Orta", "Yüksek", "Fişek"])

# İkinci satır: Okuma Miktarları (Burası senin için en önemli kısım)
st.markdown("#### 📝 Günlük Okuma Miktarların")
m1, m2, m3 = st.columns(3)

# Önce 4 tane boş sütun (yer) açıyoruz
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("**Kur'an-ı Kerim**")
    kuran_sayfa = st.number_input("Sayfa", min_value=0, value=5, step=1, key="kuran_ana")
    st.caption("🎯 Hedef: 5 Sayfa") 

with m2:
    st.markdown("**Tevbe Duası**")
    st.checkbox("Yapıldı", key="chk_tevbe")

with m3:
    st.markdown("**Hadis-i Şerif**")
    hadis_sayfa = st.number_input("Miktar", min_value=0, value=2, step=1, key="hadis_ana")
    st.caption("🎯 Hedef: 2 Hadis")

with m4:
    st.markdown("**Tefsir**")
    tefsir_sayfa = st.number_input("Sayfa", min_value=0, value=5, step=1, key="tefsir_ana")
    st.caption("🎯 Hedef: 5 Sayfa")
    
st.divider()

# --- BÖLÜM 2: İş & Dil Gelişim ---
st.header("💻 İş & Dil Gelişim")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🌎 Dil")
    st.checkbox("İngilizce Kelime Ezberleme")
    st.checkbox("İngilizce Okuma")
    st.checkbox("İngilizce Dinleme")
    st.checkbox("İngilizce Yazma")

with c2:
    st.markdown("### 🌎 Dil")
    st.checkbox("Arapça Kelime Ezberleme")
    st.checkbox("Arapça Okuma")
    st.checkbox("Arapça Dinleme")
    st.checkbox("Arapça Yazma")

with c3:
    st.markdown("### 🚢 Sosyal Medya")
    st.checkbox("Hikaye")
    st.checkbox("Post")
    st.checkbox("Reels")

st.divider()

# --- BÖLÜM 3: Yeni Fikirler ---
st.header("✨ Yeni Fikirler")
fikir_kategori = st.selectbox("Fikir Türü", ["İş", "Dini", "Genel", "Kişisel" ])
fikir_notu = st.text_area("Aklına gelen detayı buraya bırak...")

# --- BÖLÜM 4: KAYDETME ---
if st.button("💾 VERİLERİ GEÇİCİ OLARAK ONAYLA"):
    st.balloons()
    st.success(f"""
    Bugünkü Raporun:
    - Uyanış: {uyanis_saati.strftime('%H:%M')}
    - Kur'an: {kuran_sayfa} sayfa
    - Hadis: {hadis_sayfa} adet
    - Tefsir: {tefsir_sayfa} sayfa
    - Python: {py_saat} saat
    """)
    st.info("Aga unutma; şu an veritabanı bağlı olmadığı için bu veriler sadece onay ekranında görünür.")

# Alt Bilgi
st.markdown("---")
st.caption(f"Tarih: {datetime.now().strftime('%d/%m/%Y')} | Allahın İzni ile Başaracağız!")
