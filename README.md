# Prototype Kartu Pintar Calon Kades - Alif Setiawan (Desa Tegalpingen)

Prototype web portal kampanye berbasis **Smart Business Card** interaktif untuk **Alif Setiawan** (Calon Kepala Desa Tegalpingen, Kec. Pengadegan, Kab. Purbalingga). Dapat langsung diakses melalui scan Barcode / QR Code oleh warga.

## 📱 Fitur Utama
1. **Header Smart Business Card:**
   - Foto Calon Kades, Nomor Urut Badge (`NO. 01`), Visi & Misi singkat.
   - Status terverifikasi dan lokasi desa.
2. **Primary Actions:**
   - 🟢 **Lapor Pak Kades (WhatsApp Aspirasi)** dengan *prefilled chat message* otomatis.
   - 🌐 **Buku Kontak Desa** quick jump.
   - Baris Medsos resmi (Instagram, TikTok, Facebook, YouTube).
   - Tombol **Simpan Kontak (.vcf)** langsung ke buku kontak HP warga.
3. **Direktori Kontak Cepat Desa:**
   - 🔍 **Live Search Bar**: Filter pencarian real-time berdasarkan nama, jabatan, kategori, atau nomor HP.
   - 🏷️ **Kategori Filter Chips**: `Semua`, `Darurat 🚨`, `Perangkat Desa 🏛️`, `Kepala Dusun 🌾`, `RT / RW 🏘️`.
   - Tombol 1-Klik: Salin Nomor, Telepon langsung (`tel:`), dan Chat WhatsApp otomatis (`wa.me`).
4. **Fitur Ekstra:**
   - Modal QR Code Barcode preview.
   - Sheet Share ke WhatsApp, Facebook, Telegram, dan salin link.
   - Toast notification feedback.

## 🚀 Cara Menjalankan & Deploy

### 1. Test di Browser Lokal
Cukup buka file `index.html` langsung di browser Anda (Chrome / Edge / Safari).

### 2. Deploy ke Vercel (Gratis & 1 Menit Jadi)
- **Via Vercel CLI**:
  ```bash
  npx vercel
  ```
- **Via GitHub**:
  Push folder ini ke repository GitHub, lalu import di dashboard [Vercel](https://vercel.com).
