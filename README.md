# Python Deprem API

Bu proje, Türkiye'deki deprem verilerini almak için kullanılan bir API sunmaktadır. API, Koç Üniversitesi Kandilli Rasathanesi'nin veritabanından canlı deprem verilerini çekerek kullanıcılara sunmaktadır.

## Kullanım

API, `/earthquakes` endpoint'ini sağlar ve GET istekleriyle çağrılabilir. Aşağıdaki parametreleri kullanarak deprem verilerini filtreleyebilirsiniz:

- `length`: İsteğe bağlıdır. Deprem verilerinin maksimum sayısını belirler.


Örnek yanıt:

```json
{
  "status": true,
  "result": [
    {
      "tarih": "2023-05-17",
      "saat": "13:23:14",
      "enlem": "39.5",
      "boylam": "32.5",
      "depth": "10",
      "buyukluk_md": "4.5",
      "mag": "4.8",
      "buyukluk_mw": "4.7",
      "lokasyon": "Adana",
      "şehir": "ADANA",
      "timestamp": 1671987794
    },
    // Diğer deprem verileri...
  ]
}
```

## Kurulum
Deprem verilerini çekebilmek için Python 3 gereklidir. Python 3'ü yüklemek için Python web sitesini ziyaret edebilirsiniz.

Gerekli Python modüllerini yüklemek için aşağıdaki komutu çalıştırın:
```
pip install -r requirements.txt
```

API'yi başlatmak için aşağıdaki komutu çalıştırın:
```
python app.py
```

API, http://localhost:8000 adresinde çalışacaktır.
<hr>
## Katkıda Bulunma
Her türlü katkıya açığız. Projeyle ilgili hataları düzeltebilir, yeni özellikler ekleyebilir veya belgeleri geliştirebilirsiniz. Lütfen önerilerinizi ve değişikliklerinizi GitHub üzerinden yapın ve pull talepleri oluşturun.

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için lütfen lisans dosyasını inceleyin.
