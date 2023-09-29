import os
import shutil 

# Mevcut çalışma dizinini alacağı kısım
current_directory = os.getcwd()

# dosyaların kaynak ve hedef dizinleri belirteceğimiz kısım
# karışık dosyaların konumlarını hedef belirttiğiniz dizi
source_directory = os.path.join(current_directory, 'dosya_duzenle')
# düzenlenmiş dosyaların kaydedileceği kısım
destination_directory = os.path.join(current_directory, 'duzenlenmis_dosyalar')

# Dosya türleri ve hedef klasörleri eşleştiren bir sözlük oluşturun (sayı artırılabilir)
dosya_turleri = {
    'pdf': 'PDFs',
    'png': 'resimler',
    'jpg': 'resimler',
    'gif': 'resimler',
    'docx': 'dokumanlar',
    'txt': 'dokumanlar',
    'mp3': 'Muzik',
    'rar': 'arsiv',
    'zip': 'arsiv',
    'exe': 'dosya',
    'wmv': 'videolar',
    'mp4': 'videolar',
}

# Hedef klasörlerini oluştur
for target_folder in dosya_turleri.values():
    os.makedirs(os.path.join(destination_directory, target_folder), exist_ok=True)

# Kaynak dizinini kontrol et
if os.path.exists(source_directory):
    # Kaynak dizindeki dosyaları al
    files = os.listdir(source_directory)

    for file_name in files:
        # Dosya uzantısını al
        file_extension = file_name.split('.')[-1].lower()

        # Dosyanın hedef dizinine taşınacağı yol
        source_path = os.path.join(source_directory, file_name)
        if file_extension in dosya_turleri:
            target_folder = dosya_turleri[file_extension]
            destination_path = os.path.join(destination_directory, target_folder, file_name)

            # Dosyayı hedef dizine taşı veya kopyala
            shutil.move(source_path, destination_path)
else:
    print("Kaynak dizin bulunamadı!")

print("Dosyalar başarıyla düzenlendi.")
