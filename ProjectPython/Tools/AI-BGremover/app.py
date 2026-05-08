import streamlit as st
from rembg import remove
from PIL import Image
import io

# Konfigurasi Halaman
st.set_page_config(page_title="AI Background Remover", layout="wide")

# Bagian Header
st.title("✂️ AI Background Remover Pro")
st.markdown("Selamat datang di aplikasi penghapus latar belakang. Cukup tarik gambar kamu ke kotak di bawah!")

# Sidebar untuk pengaturan tambahan
with st.sidebar:
    st.header("Pengaturan")
    st.info("Aplikasi ini menggunakan model AI U2-Net untuk memisahkan subjek dari latar belakang.")
    st.write("Dibuat oleh: [Nama Kamu]")

# Fitur Import / Drag-n-Drop
uploaded_file = st.file_uploader("Upload gambar (JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Mengonversi file yang diupload ke objek Gambar PIL
    image = Image.open(uploaded_file)
    
    # Membuat dua kolom untuk perbandingan
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Gambar Asli")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Hasil (Tanpa Background)")
        
        # Proses penghapusan latar belakang
        with st.spinner('Sedang memproses AI... Harap tunggu...'):
            try:
                # Proses Utama
                result = remove(image)
                
                # Tampilkan hasil
                st.image(result, use_container_width=True)

                # Fitur Export (Download)
                # Kita konversi hasil ke Bytes agar bisa didownload
                buf = io.BytesIO()
                result.save(buf, format="PNG")
                byte_im = buf.getvalue()

                st.download_button(
                    label="📥 Download Hasil (.png)",
                    data=byte_im,
                    file_name=f"fixed_{uploaded_file.name.split('.')[0]}.png",
                    mime="image/png",
                )
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

else:
    # Tampilan saat belum ada gambar yang diupload
    st.warning("Silakan masukkan gambar terlebih dahulu untuk memulai.")