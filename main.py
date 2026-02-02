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
    uyanis_saati = st.time_input("☀️ Uyandığın Saat", time(7, 0))
with col_u2:
    enerji = st.select_slider("⚡ Enerji Seviyen", options=["Düşük", "Orta", "Yüksek", "Fişek"])

# İkinci satır: Okuma Miktarları (Burası senin için en önemli kısım)
st.markdown("#### 📝 Günlük Okuma Miktarların")
m1, m2, m3 = st.columns(3)

with m1:
    st.markdown("**Kur'an-ı Kerim**")
    kuran_sayfa = st.number_input("Kaç Sayfa?", min_value=0, value=5, step=1, key="kuran_ana")
    st.caption("Bugünkü hedef: 10")

with m1:
    st.markdown("**Sure Ezberi**")
    tefsir_sayfa = st.number_input("Kaç Tane Sure Ezberledin?", min_value=0, value=0, step=1, key="ezber_ana")
    
with m2:
    st.markdown("**Tevbe Duası**")
    st.checkbox("Yapıldı", key="chk_tevbe")
    st.caption("Günlük Tevbe")

with m2:
    st.markdown("**Hadis-i Şerif**")
    hadis_sayfa = st.number_input("Kaç Hadis/Sayfa?", min_value=0, value=2, step=1, key="hadis_ana")
    st.caption("Bugünkü hedef: 2")
    
with m3:
    st.markdown("**Tefsir**")
    tefsir_sayfa = st.number_input("Kaç Sayfa Tefsir?", min_value=0, value=2, step=1, key="tefsir_ana")
    st.caption("Bugünkü hedef :2")
    
st.divider()

# --- BÖLÜM 2: DÜNYEVİ GELİŞİM & İŞ ---
st.header("💻 İş, Yazılım ve Kariyer")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🐍 Yazılım")
    py_calisildi = st.checkbox("Python/Pandas")
    py_saat = st.number_input("Kaç Saat?", min_value=0.0, value=1.0, step=0.5)

with c2:
    st.markdown("### 🌎 Dil")
    st.checkbox("İngilizce Pratik")
    st.checkbox("Arapça Çalışma")

with c3:
    st.markdown("### 🚢 İhracat")
    st.checkbox("Evrak Kontrolü")
    st.checkbox("Gemi Takibi")

st.divider()

# --- BÖLÜM 3: Yeni Fikirler ---
st.header("✨ Yeni Fikirler")
fikir_kategori = st.selectbox("Fikir Türü", ["Model/Tasarım", "Kumaş", "Pazarlama", "Genel"])
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
st.caption(f"Tarih: {datetime.now().strftime('%d/%m/%Y')} | Mezuniyete Az Kaldı!")
