import streamlit as st
import pandas as pd
import sqlite3
import os
from datetime import datetime, time

# Uygulama Ayarları
st.set_page_config(page_title="Akbaba Asistan", page_icon="📖", layout="centered")

# --- VERİTABANI AYARLARI ---
DB_NAME = "akbaba_asistan.db"

def veritabani_hazirla():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Senin tüm o özel sütunlarını buraya tanımlıyoruz
    c.execute('''CREATE TABLE IF NOT EXISTS takip (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Tarih TEXT, Uyanis TEXT, Enerji TEXT,
                    Kuran INTEGER, Tevbe TEXT, Hadis INTEGER, Tefsir INTEGER,
                    Ing_Kelime TEXT, Ing_Okuma TEXT, Ing_Dinleme TEXT, Ing_Yazma TEXT,
                    Ara_Kelime TEXT, Ara_Okuma TEXT, Ara_Dinleme TEXT, Ara_Yazma TEXT,
                    SM_Hikaye TEXT, SM_Post TEXT, SM_Reels TEXT, Fikir TEXT)''')
    conn.commit()
    conn.close()

veritabani_hazirla()

st.title("🚀 Akbaba Günlük Takip Paneli")

# --- BÖLÜM 1: GÜNE BAŞLARKEN ---
st.header("🕌 Güne Başlarken")
col_u1, col_u2 = st.columns(2)
with col_u1:
    uyanıs_saati = st.time_input("☀️ Uyandığın Saat", time(5, 0))
with col_u2:
    enerji = st.select_slider("⚡ Enerji Seviyen", options=["Düşük", "Orta", "Yüksek", "Fişek"])

st.markdown("#### 📝 Günlük Okuma Miktarların")
m1, m2, m3, m4 = st.columns(4)
with m1:
    kuran_sayfa = st.number_input("Kur'an (Sayfa)", 0, 500, 5)
with m2:
    chk_tevbe = st.checkbox("Tevbe Duası")
with m3:
    hadis_sayfa = st.number_input("Hadis (Miktar)", 0, 100, 2)
with m4:
    tefsir_sayfa = st.number_input("Tefsir (Sayfa)", 0, 500, 5)

st.divider()

# --- BÖLÜM 2: İŞ & DİL GELİŞİM ---
st.header("💻 İş & Dil Gelişim")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🌎 İngilizce")
    i_kel = st.checkbox("Kelime Ezber", key="ik")
    i_oku = st.checkbox("Okuma", key="io")
    i_din = st.checkbox("Dinleme", key="id")
    i_yaz = st.checkbox("Yazma", key="iy")

with c2:
    st.markdown("### 🌎 Arapça")
    a_kel = st.checkbox("Arapça Kelime", key="ak")
    a_oku = st.checkbox("Arapça Okuma", key="ao")
    a_din = st.checkbox("Arapça Dinleme", key="ad")
    a_yaz = st.checkbox("Arapça Yazma", key="ay")

with c3:
    st.markdown("### 📱 Sosyal Medya")
    s_hik = st.checkbox("Hikaye", key="sh")
    s_pos = st.checkbox("Post", key="sp")
    s_ree = st.checkbox("Reels", key="sr")

st.divider()

# --- BÖLÜM 3: YENİ FİKİRLER ---
st.header("✨ Yeni Fikirler")
fikir_not = st.text_area("Notunu buraya bırak...", placeholder="Yeni iş fikri, dini notlar veya kişisel gelişim...")

# --- BÖLÜM 4: KAYDETME ---
if st.button("💾 VERİLERİ SİSTEME KAYDET"):
    tarih_str = datetime.now().strftime('%Y-%m-%d')
    
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        query = '''INSERT INTO takip (
                    Tarih, Uyanis, Enerji, Kuran, Tevbe, Hadis, Tefsir,
                    Ing_Kelime, Ing_Okuma, Ing_Dinleme, Ing_Yazma,
                    Ara_Kelime, Ara_Okuma, Ara_Dinleme, Ara_Yazma,
                    SM_Hikaye, SM_Post, SM_Reels, Fikir
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        
        values = (
            tarih_str, uyanıs_saati.strftime('%H:%M'), enerji, kuran_sayfa,
            "Evet" if chk_tevbe else "Hayır", hadis_sayfa, tefsir_sayfa,
            "Evet" if i_kel else "Hayır", "Evet" if i_oku else "Hayır", 
            "Evet" if i_din else "Hayır", "Evet" if i_yaz else "Hayır",
            "Evet" if a_kel else "Hayır", "Evet" if a_oku else "Hayır", 
            "Evet" if a_din else "Hayır", "Evet" if a_yaz else "Hayır",
            "Evet" if s_hik else "Hayır", "Evet" if s_pos else "Hayır", 
            "Evet" if s_ree else "Hayır", fikir_not
        )
        
        c.execute(query, values)
        conn.commit()
        conn.close()
        
        st.balloons()
        st.success("Aga tüm detaylar sisteme işlendi! Helal olsun.")
    except Exception as e:
        st.error(f"Kayıt Hatası: {e}")

st.divider()

# --- BÖLÜM 5: VERİLERİ GÖR VE İNDİR ---
st.header("📊 Geçmiş Kayıtların")
if os.path.exists(DB_NAME):
    conn = sqlite3.connect(DB_NAME)
    df_goster = pd.read_sql_query("SELECT * FROM takip ORDER BY Tarih DESC", conn)
    conn.close()
    
    if not df_goster.empty:
        st.dataframe(df_goster)
        
        # Excel formatında indirme butonu
        csv = df_goster.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="📥 Tüm Verileri Excel (CSV) Olarak İndir",
            data=csv,
            file_name=f"akbaba_asistan_yedek_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
        )
    else:
        st.info("Henüz kayıtlı veri yok aga.")
