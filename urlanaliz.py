import urllib.parse
import re

def analiz_et(url):
    puan = 0
    uyarilar = []

    # 1. Protokol Kontrolü (Eksikse biz ekliyoruz ki analiz çalışsın)
    if not url.startswith("http"):
        url = "http://" + url

    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc

    # 2. HTTPS Kontrolü
    if parsed_url.scheme == "http":
        puan += 30
        uyarilar.append("Güvensiz bağlantı (HTTP kullanılıyor, veri şifrelenmiyor).")

    # 3. IP Adresi Kontrolü (Hackerlar alan adı almak yerine direkt IP gizler)
    ip_arayici = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if ip_arayici.match(domain):
        puan += 40
        uyarilar.append("Alan adı yerine doğrudan IP adresi kullanılmış (Kritik Şüpheli).")

    # 4. Şüpheli Kelime Kontrolü (Oltalama sitelerinin sık kullandığı tuzak kelimeler)
    supheli_kelimeler = ["login", "free", "update", "admin", "secure", "bank", "account", "verify", "password"]
    for kelime in supheli_kelimeler:
        if kelime in url.lower():
            puan += 15
            uyarilar.append(f"Tuzak kelime tespit edildi: '{kelime}'")

    # 5. URL Uzunluğu (Kullanıcının gözünü yormak için genelde çok uzun linkler kullanılır)
    if len(url) > 75:
        puan += 10
        uyarilar.append("URL çok uzun (Oltalama siteleri karmaşık görünmek için uzun linkler kullanır).")

    # 6. Alt Alan Adı (Subdomain) Sayısı
    subdomains = domain.split('.')
    if len(subdomains) > 3:
        puan += 15
        uyarilar.append("Çok fazla alt alan adı (subdomain) var (örnek: login.secure.bank.com).")

    # --- Sonuç Raporu Ekranı ---
    print("\n" + "-"*30)
    print(f"Taranan URL: {url}")
    print(f"Risk Puanı: {puan} / 100")
    print("-" * 30)
    
    if puan == 0:
        print("[+] GÜVENLİ: Temel oltalama (phishing) belirtisi yok.")
    elif puan < 40:
        print("[!] DİKKAT: Bazı şüpheli işaretler var, emin olmadan tıklamayın.")
    else:
        print("[-] TEHLİKELİ: Yüksek risk tespit edildi! Bu linkten uzak durun.")

    if uyarilar:
        print("\nTespit Edilen Risk Sebepleri:")
        for uyari in uyarilar:
            print(f"  * {uyari}")

# Programın Ana Döngüsü
print("=== Defansif Güvenlik: Sezgisel URL Analiz Aracı ===")
print("Çıkmak için 'q' tuşuna basın.\n")

while True:
    hedef_url = input("Analiz edilecek URL'yi girin: ")
    if hedef_url.lower() == 'q':
        print("Programdan çıkılıyor...")
        break
    
    if hedef_url.strip() == "":
        print("Lütfen geçerli bir URL girin.")
        continue
        
    analiz_et(hedef_url)
    print("\n" + "="*50 + "\n")
