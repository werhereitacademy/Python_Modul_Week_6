from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Özel anahtar kelimeler sözlüğü
SPECIAL_KEYWORDS = {
    "bugün": datetime.today().date(),
    "yarın": (datetime.today() + timedelta(days=1)).date(),
    "gelecek hafta": (datetime.today() + timedelta(weeks=1)).date()
}

# Soyut Görev Sınıfı
class Gorev(ABC):
    def _init_(self, ad, son_tarih, durum="Beklemede"):
        self.ad = ad
        self.son_tarih = self.son_tarihi_hesapla(son_tarih)
        self.durum = durum
    
    def son_tarihi_hesapla(self, tarih):
        if tarih.lower() in SPECIAL_KEYWORDS:
            return SPECIAL_KEYWORDS[tarih.lower()]
        try:
            return datetime.strptime(tarih, "%Y-%m-%d").date()
        except ValueError:
            print(f"Hatalı tarih formatı: {tarih}. YYYY-MM-DD formatında giriniz.")
            return None

    @abstractmethod
    def detaylari_goster(self):
        pass

# Kişisel Görev Sınıfı
class KisiselGorev(Gorev):
    def detaylari_goster(self):
        return f"[Kişisel] {self.ad} - Son Tarih: {self.son_tarih} - Durum: {self.durum}"

# İş Görevi Sınıfı
class IsGorevi(Gorev):
    def detaylari_goster(self):
        return f"[İş] {self.ad} - Son Tarih: {self.son_tarih} - Durum: {self.durum}"

# Görev Yönetimi Sınıfı
class GorevYoneticisi:
    def _init_(self):
        self.gorev_listesi = []
    
    def gorev_ekle(self, gorev):
        if gorev.son_tarih is not None:
            self.gorev_listesi.append(gorev)
            print(f"Görev eklendi: {gorev.ad}")
    
    def gorevleri_listele(self):
        for gorev in self.gorev_listesi:
            print(gorev.detaylari_goster())

# Görev Planlama Sınıfı
class GorevPlanlama:
    @staticmethod
    def yeni_gorev_olustur(gorev_tipi, ad, son_tarih):
        if gorev_tipi == "kişisel":
            return KisiselGorev(ad, son_tarih)
        elif gorev_tipi == "iş":
            return IsGorevi(ad, son_tarih)
        else:
            print("Geçersiz görev tipi")
            return None

# Görev Düzenleme Sınıfı
class GorevDuzenleme:
    @staticmethod
    def gorev_durum_guncelle(gorev, yeni_durum):
        gorev.durum = yeni_durum
        print(f"{gorev.ad} durumu güncellendi: {yeni_durum}")

    @staticmethod
    def gorev_sil(gorev_yoneticisi, gorev_adi):
        gorev_yoneticisi.gorev_listesi = [g for g in gorev_yoneticisi.gorev_listesi if g.ad != gorev_adi]
        print(f"Görev silindi: {gorev_adi}")

# Görev Takip Sınıfı
class GorevTakip:
    @staticmethod
    def gorev_durumunu_goster(gorev):
        print(f"{gorev.ad} - Durum: {gorev.durum}")
    
    @staticmethod
    def gorevi_tamamla(gorev):
        gorev.durum = "Tamamlandı"
        print(f"{gorev.ad} tamamlandı!")

# Ana Program
if _name_ == "_main_":
    yonetici = GorevYoneticisi()
    
    # Yeni görevler oluştur
    gorev1 = GorevPlanlama.yeni_gorev_olustur("kişisel", "Kitap oku", "yarın")
    gorev2 = GorevPlanlama.yeni_gorev_olustur("iş", "Toplantı", "2025-02-05")
    
    # Görevleri ekle
    if gorev1:
        yonetici.gorev_ekle(gorev1)
    if gorev2:
        yonetici.gorev_ekle(gorev2)
    
    # Görevleri listele
    print("\nGörev Listesi:")
    yonetici.gorevleri_listele()
    
    # Görev durumunu güncelle
    if gorev1:
        GorevDuzenleme.gorev_durum_guncelle(gorev1, "Devam Ediyor")
    
    # Görevi tamamla
    if gorev2:
        GorevTakip.gorevi_tamamla(gorev2)
    
    # Güncellenmiş görevleri listele
    print("\nGüncellenmiş Görev Listesi:")
    yonetici.gorevleri_listele()
    
    # Görev sil
    GorevDuzenleme.gorev_sil(yonetici, "Kitap oku")
    
    # Son listeyi göster
    print("\nSon Görev Listesi:")
    yonetici.gorevleri_listele()
