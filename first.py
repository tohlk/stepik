import urllib.request
import ssl
import json

# Отключаем проверку SSL сертификата
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def get_location_fixed():
    print("Определяем местоположение...\n")
    
    try:
        # Используем контекст без проверки SSL
        with urllib.request.urlopen('https://ipinfo.io/json', context=ssl_context) as response:
            data = json.loads(response.read().decode())
            
            print("✅ Ваше местоположение:")
            print(f"🏙️  Город: {data.get('city', 'Не определен')}")
            print(f"🏛️  Регион: {data.get('region', 'Не определен')}")
            print(f"🇷🇺 Страна: {data.get('country', 'Не определена')}")
            print(f"🌐 IP-адрес: {data.get('ip', 'Не определен')}")
            
            if 'loc' in data:
                print(f"📍 Координаты: {data['loc']}")
                
    except Exception as e:
        print(f"❌ Ошибка: {e}")

get_location_fixed()