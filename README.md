# \# Legends Vote

# 

# Legends Online için günlük oy hatırlatıcı. Belirlenen saatte giriş yapar ve

# 4 oy sitesini sekme olarak açar.

# 

# \*\*Bot doğrulaması aşılmaz.\*\* Cloudflare, ALTCHA, reCAPTCHA çıkarsa sen elle

# geçersin.

# 

# \## İndir \& Çalıştır

# 

# 1\. \[Releases](../../releases) sayfasından \*\*LegendsVote-v1.0.0.zip\*\* indir.

# 2\. Zip'i bir klasöre çıkar (örn. `C:\\\\LegendsVote`).

# 3\. `.env.example` dosyasını `.env` olarak kopyala.

4\. `.env` içine Legends Online kullanıcı adı ve şifreni yaz:

LEGENDS\_USER=kullanici\_adin
===

LEGENDS\_PASS=sifren

5. `LegendsVote.exe` çift tıkla — Chrome açılır, 4 sekme gelir.
===

# 

# PC her açıldığında arka planda otomatik çalışır. Her gün saat 20:00'de

# bildirim gelir, sekmeler açılır.

# 

# \## Kaldırma

# 

# \- \*\*Startup'tan çıkar:\*\* `shell:startup` klasörünü aç (Win+R), `LegendsVote.lnk`

# kısayolunu sil.

# \- \*\*Klasörü sil:\*\* `C:\\LegendsVote` klasörünü sil.

# 

# \## Sık Sorulan

# 

# \*\*Saat kaçta çalışıyor?\*\* 20:00. Değiştirmek istersen kaynak koddan derle

# (`vote\_app.py` → `DAILY\_HOUR`).

# 

# \*\*Aynı gün ikinci kez çalışır mı?\*\* Hayır. Bir kez çalışınca o gün tekrar

# tetiklenmez.

# 

# \*\*Chrome açılıyor ama sekmeler gelmiyor?\*\* `.env` dosyasında kullanıcı adı

# ve şifre doğru mu kontrol et. `logs\\` klasöründeki bugünün log dosyasına bak.

# 

# \*\*Cloudflare çıkıyor?\*\* Kutucuğu elle işaretle. Araç doğrulamayı aşmaz.

# 

# \## Uyarı

# 

# Bu araç yalnızca kişisel kullanım içindir. Oy sitelerinin ve Legends Online'ın

# kullanım şartlarına uymak \*\*senin sorumluluğundadır\*\*. `.env` dosyanı kimseyle

# paylaşma.

# 

# \## Lisans

# 

# MIT

