## 🌟 Overview | نظرة عامة | Genel Bakış

🌍 **[EN]** WhatsApp Message Sender with RabbitMQ Integration

🌍 **[AR]** واتساب مرسل الرسائل مع تكامل RabbitMQ

🌍 **[TR]** RabbitMQ Entegrasyonlu WhatsApp Mesaj Gönderici


## 🇸🇦 عربي

### الوصف
يقوم هذا المشروع بدمج إمكانيات إرسال رسائل واتساب مع نظام صفوف الرسائل RabbitMQ، مما يتيح إرسال الرسائل تلقائياً من خلال تطبيق Python الذي يتواصل مع تطبيق C#.

### المميزات
- أتمتة رسائل واتساب
- تكامل مع نظام صفوف الرسائل RabbitMQ
- توافق متعدد المنصات (Python و C#)
- قوالب رسائل قابلة للتخصيص
- نظام تسجيل السجلات
- دعم Docker

### المتطلبات
- Python 3.8 أو أحدث
- خادم RabbitMQ
- Docker (اختياري)
- حزم Python المطلوبة (انظر requirements.txt)

### التثبيت
```bash
# استنساخ المستودع
git clone https://github.com/MuhammedNurAlsammour/store-platform-whatsapp-message-api-python.git

# تثبيت المكتبات المطلوبة
pip install -r requirements.txt

# إعداد متغيرات البيئة
cp .env.example .env
```

### الاستخدام
1. تشغيل خادم RabbitMQ
2. إعداد بيانات اعتماد واتساب في ملف .env
3. تشغيل تطبيق Python:
```bash
python main.py
```

---

## 🇹🇷 Türkçe

### Açıklama
Bu proje, WhatsApp mesajlaşma özelliklerini RabbitMQ mesaj kuyruğu ile entegre ederek, C# uygulaması ile iletişim kuran bir Python arka ucu aracılığıyla otomatik mesaj göndermeyi sağlar.

### Özellikler
- WhatsApp mesaj otomasyonu
- RabbitMQ mesaj kuyruğu entegrasyonu
- Çapraz platform uyumluluğu (Python ve C#)
- Özelleştirilebilir mesaj şablonları
- Günlük sistemi
- Docker desteği

### Gereksinimler
- Python 3.8+
- RabbitMQ Sunucusu
- Docker (isteğe bağlı)
- Gerekli Python paketleri (requirements.txt dosyasına bakın)

### Kurulum
```bash
# Depoyu klonlayın
git clone https://github.com/MuhammedNurAlsammour/store-platform-whatsapp-message-api-python.git

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Ortam değişkenlerini yapılandırın
cp .env.example .env
```

### Kullanım
1. RabbitMQ sunucusunu başlatın
2. WhatsApp kimlik bilgilerinizi .env dosyasında yapılandırın
3. Python uygulamasını çalıştırın:
```bash
python main.py
```

## Project Structure
```
store-platform-whatsapp-message-api-python/
├── constants/
├── contracts/
├── utils/
├── logs/
├── images/
├── .env
├── config.conf
├── docker-compose.yml
├── Dockerfile
├── main.py
└── requirements.txt
```
---

## 🇬🇧 English

### Description
This project integrates WhatsApp messaging capabilities with RabbitMQ message queue, allowing for automated message sending through a Python backend that communicates with a C# application.

### Features
- WhatsApp message automation
- RabbitMQ message queue integration
- Cross-platform compatibility (Python & C#)
- Configurable message templates
- Logging system
- Docker support

### Requirements
- Python 3.8+
- RabbitMQ Server
- Docker (optional)
- Required Python packages (see requirements.txt)

### Installation
```bash
# Clone the repository
git clone https://github.com/MuhammedNurAlsammour/store-platform-whatsapp-message-api-python.git

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
```

### Usage
1. Start the RabbitMQ server
2. Configure your WhatsApp credentials in .env
3. Run the Python application:
```bash
python main.py
```

## License
MIT License

## Contact
- GitHub: [@MuhammedNurAlsammour](https://github.com/MuhammedNurAlsammour)
