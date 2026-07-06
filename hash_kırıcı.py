import hashlib
import time

def hash_kirici(hedef_hash, kelime_listesi):
    print(f"\n[*] Hedef Hash: {hedef_hash}")
    print("[*] Kaba kuvvet (Brute-force) saldırısı başlatılıyor...\n")
    
    baslangic_zamani = time.time()
    deneme_sayisi = 0
    bulundu = False

    # Listemizdeki her bir kelimeyi sırayla deniyoruz
    for kelime in kelime_listesi:
        deneme_sayisi += 1
        
        # Kelimeyi MD5 algoritması ile şifreliyoruz (Hash'liyoruz)
        sifrelenmis_kelime = hashlib.md5(kelime.encode('utf-8')).hexdigest()
        
        # Ekranda denenen kelimeleri çok hızlı akarken görmek için (Opsiyonel)
        print(f"[{deneme_sayisi}] Deneniyor: {kelime} -> {sifrelenmis_kelime}")
        
        # Bulduğumuz hash ile hedeflenen hash eşleşiyorsa şifre kırılmıştır!
        if sifrelenmis_kelime == hedef_hash:
            gecen_sure = time.time() - baslangic_zamani
            print("\n" + "="*40)
            print("[+] BAŞARILI! ŞİFRE KIRILDI!")
            print(f"[+] Orijinal Parola: {kelime}")
            print(f"[+] Toplam Deneme: {deneme_sayisi}")
            print(f"[+] Geçen Süre: {gecen_sure:.4f} saniye")
            print("="*40 + "\n")
            bulundu = True
            break
            
    if not bulundu:
        print("\n[-] BAŞARISIZ: Parola bu kelime listesinde bulunamadı.")

# --- Programın Ana Kısmı ---
print("=== Python MD5 Hash Kırıcı ===")

# Test için 'admin123' kelimesinin MD5 hashlenmiş hali:
ornek_hedef_hash = "0192023a7bbd73250516f069df18b500" 

# Hata almamanız için şimdilik kelimeleri dosya yerine bir liste olarak veriyoruz.
# Gerçek senaryolarda bu liste 'rockyou.txt' gibi milyonlarca kelimelik dosyalardan okunur.
siber_sozluk = [
    "123456", "password", "qwerty", "iloveyou", 
    "futbol", "matrix", "admin", "admin1", 
    "admin123", "root", "toor", "test1234"
]

hash_kirici(ornek_hedef_hash, siber_sozluk)
