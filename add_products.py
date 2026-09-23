import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electronics_catalog.settings')
django.setup()

from products.models import Brand, Category, Product

# Create Brands if not exist
for b in ["Dell", "HP", "Apple", "Samsung", "Lenovo", "Asus", "OnePlus", "Xiaomi"]:
    Brand.objects.get_or_create(name=b)

# Create Categories
cat_laptop, _ = Category.objects.get_or_create(name="Laptops", defaults={"slug":"laptops"})
cat_mobile, _ = Category.objects.get_or_create(name="Mobiles", defaults={"slug":"mobiles"})
cat_tablet, _ = Category.objects.get_or_create(name="Tablets", defaults={"slug":"tablets"})

products_data = [
    # LAPTOPS - 8
    ["Dell XPS 13", "Laptops", "Dell", "XPS13-9340", "Premium ultrabook", "Intel i7-1360P", "16GB", "512GB SSD", "13.4 OLED", "55Wh", "1080p", "Windows 11", 125000],
    ["Dell Inspiron 15", "Laptops", "Dell", "INSP-3520", "Budget daily use", "Intel i5-1235U", "8GB", "512GB SSD", "15.6 FHD", "41Wh", "720p", "Windows 11", 55000],
    ["HP Victus 16", "Laptops", "HP", "VICTUS-16-E1000", "Gaming laptop", "Ryzen 7 7840HS", "16GB", "1TB SSD", "16.1 FHD 144Hz", "83Wh", "1080p", "Windows 11", 85000],
    ["HP Pavilion 14", "Laptops", "HP", "PAV-14-EC2000", "Thin and light", "Intel i5-1335U", "16GB", "512GB SSD", "14 FHD", "51Wh", "1080p", "Windows 11", 68000],
    ["Apple MacBook Air M2", "Laptops", "Apple", "MBA-M2-2023", "Super light Apple Silicon", "Apple M2", "8GB", "256GB SSD", "13.6 Liquid Retina", "52Wh 18Hrs", "1080p", "macOS Sonoma", 105000],
    ["Apple MacBook Pro 14", "Laptops", "Apple", "MBP-14-M3", "Pro performance", "Apple M3 Pro", "18GB", "512GB SSD", "14.2 XDR", "70Wh", "1080p", "macOS Sonoma", 185000],
    ["Lenovo IdeaPad Gaming 3", "Laptops", "Lenovo", "IDEAPAD-G3-15", "Budget gaming", "Ryzen 5 5600H", "8GB", "512GB SSD", "15.6 FHD 120Hz", "45Wh", "720p", "Windows 11", 62000],
    ["Asus ROG Strix G15", "Laptops", "Asus", "ROG-G15-5530", "High performance gaming", "Ryzen 9 7940HS", "16GB", "1TB SSD", "15.6 QHD 165Hz", "90Wh", "1080p", "Windows 11", 135000],

    # MOBILES - 8
    ["iPhone 15 Pro", "Mobiles", "Apple", "IPHONE-15-PRO", "Titanium flagship", "A17 Pro", "8GB", "256GB", "6.1 Super Retina XDR", "3200mAh", "48MP+12MP+12MP", "iOS 17", 134900],
    ["Samsung Galaxy S23 Ultra", "Mobiles", "Samsung", "S23-ULTRA", "S Pen flagship", "Snapdragon 8 Gen 2", "12GB", "256GB", "6.8 Dynamic AMOLED", "5000mAh", "200MP Quad", "Android 14", 124999],
    ["OnePlus 11R", "Mobiles", "OnePlus", "11R-5G", "Flagship killer", "Snapdragon 8+ Gen 1", "16GB", "256GB", "6.74 AMOLED 120Hz", "5000mAh", "50MP Triple", "OxygenOS 14", 44999],
    ["Xiaomi Redmi Note 13 Pro", "Mobiles", "Xiaomi", "RN13-PRO-5G", "Best camera midrange", "Snapdragon 7s Gen 2", "12GB", "256GB", "6.67 OLED 120Hz", "5100mAh", "200MP Triple", "MIUI 15", 26999],
    ["Samsung Galaxy A54", "Mobiles", "Samsung", "A54-5G", "Midrange balanced", "Exynos 1380", "8GB", "128GB", "6.4 Super AMOLED", "5000mAh", "50MP Triple", "Android 14", 35999],
    ["OnePlus Nord 3", "Mobiles", "OnePlus", "NORD-3-5G", "Fast and smooth", "Dimensity 9000", "12GB", "256GB", "6.74 AMOLED 120Hz", "5000mAh", "50MP Triple", "OxygenOS 14", 33999],
    ["iPhone 14", "Mobiles", "Apple", "IPHONE-14", "Popular Apple", "A15 Bionic", "6GB", "128GB", "6.1 Super Retina", "3279mAh", "12MP Dual", "iOS 17", 69900],
    ["Xiaomi 14", "Mobiles", "Xiaomi", "MI-14-5G", "Leica camera flagship", "Snapdragon 8 Gen 3", "12GB", "512GB", "6.36 OLED 120Hz", "4610mAh", "50MP Leica Triple", "HyperOS", 59999],

    # TABLETS - 4
    ["iPad Air M1", "Tablets", "Apple", "IPAD-AIR-M1", "Thin powerful tablet", "Apple M1", "8GB", "256GB", "10.9 Liquid Retina", "28Wh 10Hrs", "12MP", "iPadOS 17", 65900],
    ["Samsung Galaxy Tab S9", "Tablets", "Samsung", "TAB-S9", "Flagship Android tablet", "Snapdragon 8 Gen 2", "12GB", "256GB", "11 Dynamic AMOLED", "8400mAh", "13MP", "Android 14", 72999],
    ["Lenovo Tab P12", "Tablets", "Lenovo", "TAB-P12", "Entertainment tablet", "Dimensity 7050", "8GB", "128GB", "12.7 3K", "10200mAh", "8MP", "Android 13", 29999],
    ["Xiaomi Pad 6", "Tablets", "Xiaomi", "PAD-6", "Gaming tablet", "Snapdragon 870", "8GB", "256GB", "11 WQHD+ 144Hz", "8840mAh", "13MP", "MIUI Pad 14", 26999],
]

for p in products_data:
    name, cat_name, brand_name, model_no, desc, proc, ram, storage, display, battery, camera, os_name, price = p
    brand = Brand.objects.get(name=brand_name)
    cat = Category.objects.get(name=cat_name)
    obj, created = Product.objects.get_or_create(
        name=name,
        defaults={
            "category": cat,
            "brand": brand,
            "model_number": model_no,
            "description": desc,
            "processor": proc,
            "ram": ram,
            "storage": storage,
            "display": display,
            "battery": battery,
            "camera": camera,
            "os": os_name,
            "current_price": price
        }
    )
    print(f"{'Created' if created else 'Exists'}: {name}")

print("\nDONE! 20 Products Added!")