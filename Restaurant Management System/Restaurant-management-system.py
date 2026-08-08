import os

# ==== قوائم البيانات ====
meals = []
drinks = []
desserts = []
orders = []
customers = []

# ============================================
# ===== دوال التحميل من الملفات =====
# ============================================

def load_meals():
    global meals
    meals = []
    try:
        with open("meals.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    name, price = line.strip().split(",")
                    meals.append({"name": name, "price": float(price)})
    except FileNotFoundError:
        meals = []

def load_drinks():
    global drinks
    drinks = []
    try:
        with open("drinks.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    name, price = line.strip().split(",")
                    drinks.append({"name": name, "price": float(price)})
    except FileNotFoundError:
        drinks = []

def load_desserts():
    global desserts
    desserts = []
    try:
        with open("desserts.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    name, price = line.strip().split(",")
                    desserts.append({"name": name, "price": float(price)})
    except FileNotFoundError:
        desserts = []

def load_orders():
    global orders
    orders = []
    try:
        with open("orders.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    customer, items = line.strip().split("|")
                    orders.append({"customer": customer, "items": items.split(",")})
    except FileNotFoundError:
        orders = []

def load_all_data():
    load_meals()
    load_drinks()
    load_desserts()
    load_orders()

# ============================================
# ===== دوال الحفظ في الملفات =====
# ============================================

def save_meals():
    with open("meals.txt", "w", encoding="utf-8") as f:
        for meal in meals:
            f.write(f"{meal['name']},{meal['price']}\n")

def save_drinks():
    with open("drinks.txt", "w", encoding="utf-8") as f:
        for drink in drinks:
            f.write(f"{drink['name']},{drink['price']}\n")

def save_desserts():
    with open("desserts.txt", "w", encoding="utf-8") as f:
        for dessert in desserts:
            f.write(f"{dessert['name']},{dessert['price']}\n")

def save_orders():
    with open("orders.txt", "w", encoding="utf-8") as f:
        for order in orders:
            items_str = ",".join(order['items'])
            f.write(f"{order['customer']}|{items_str}\n")

def save_all_data():
    save_meals()
    save_drinks()
    save_desserts()
    save_orders()

# ============================================
# ===== دوال إدارة الوجبات =====
# ============================================

def add_meal():
    name = input("ادخل اسم الوجبة: ")
    try:
        price = float(input("ادخل سعر الوجبة: "))
        meals.append({"name": name, "price": price})
        print("تمت اضافة الوجبة بنجاح.")
    except ValueError:
        print("خطا: يجب ادخال رقم صحيح للسعر.")

def print_meals():
    if not meals:
        print("لا توجد وجبات حاليا.")
        return
    print("\n=== قائمة الوجبات ===")
    for i, meal in enumerate(meals, 1):
        print(f"{i}. {meal['name']} - {meal['price']} ريال")

def edit_meal():
    if not meals:
        print("لا توجد وجبات للتعديل.")
        return
    print_meals()
    try:
        index = int(input("ادخل رقم الوجبة التي تريد تعديلها: ")) - 1
        if 0 <= index < len(meals):
            new_name = input("ادخل الاسم الجديد: ")
            new_price = float(input("ادخل السعر الجديد: "))
            meals[index] = {"name": new_name, "price": new_price}
            print("تم تعديل الوجبة بنجاح.")
        else:
            print("رقم غير صحيح.")
    except ValueError:
        print("خطا: يجب ادخال رقم.")

def delete_meal():
    if not meals:
        print("لا توجد وجبات للحذف.")
        return
    print_meals()
    try:
        index = int(input("ادخل رقم الوجبة التي تريد حذفها: ")) - 1
        if 0 <= index < len(meals):
            deleted = meals.pop(index)
            print(f"تم حذف الوجبة '{deleted['name']}' بنجاح.")
        else:
            print("رقم غير صحيح.")
    except ValueError:
        print("خطا: يجب ادخال رقم.")

def search_meal():
    if not meals:
        print("لا توجد وجبات للبحث.")
        return
    keyword = input("ادخل كلمة البحث: ").lower()
    found = [m for m in meals if keyword in m['name'].lower()]
    if found:
        print("\n=== نتائج البحث ===")
        for meal in found:
            print(f"- {meal['name']} - {meal['price']} ريال")
    else:
        print("لم يتم العثور على وجبات تطابق البحث.")

# ============================================
# ===== دوال إدارة المشروبات =====
# ============================================

def add_drink():
    name = input("ادخل اسم المشروب: ")
    try:
        price = float(input("ادخل سعر المشروب: "))
        drinks.append({"name": name, "price": price})
        print("تمت اضافة المشروب بنجاح.")
    except ValueError:
        print("خطا: يجب ادخال رقم صحيح للسعر.")

def print_drinks():
    if not drinks:
        print("لا توجد مشروبات حاليا.")
        return
    print("\n=== قائمة المشروبات ===")
    for i, drink in enumerate(drinks, 1):
        print(f"{i}. {drink['name']} - {drink['price']} ريال")

def edit_drink():
    if not drinks:
        print("لا توجد مشروبات للتعديل.")
        return
    print_drinks()
    try:
        index = int(input("ادخل رقم المشروب الذي تريد تعديله: ")) - 1
        if 0 <= index < len(drinks):
            new_name = input("ادخل الاسم الجديد: ")
            new_price = float(input("ادخل السعر الجديد: "))
            drinks[index] = {"name": new_name, "price": new_price}
            print("تم تعديل المشروب بنجاح.")
        else:
            print("رقم غير صحيح.")
    except ValueError:
        print("خطا: يجب ادخال رقم.")

def delete_drink():
    if not drinks:
        print("لا توجد مشروبات للحذف.")
        return
    print_drinks()
    try:
        index = int(input("ادخل رقم المشروب الذي تريد حذفه: ")) - 1
        if 0 <= index < len(drinks):
            deleted = drinks.pop(index)
            print(f"تم حذف المشروب '{deleted['name']}' بنجاح.")
        else:
            print("رقم غير صحيح.")
    except ValueError:
        print("خطا: يجب ادخال رقم.")

def search_drink():
    if not drinks:
        print("لا توجد مشروبات للبحث.")
        return
    keyword = input("ادخل كلمة البحث: ").lower()
    found = [d for d in drinks if keyword in d['name'].lower()]
    if found:
        print("\n=== نتائج البحث ===")
        for drink in found:
            print(f"- {drink['name']} - {drink['price']} ريال")
    else:
        print("لم يتم العثور على مشروبات تطابق البحث.")

# ============================================
# ===== دوال إدارة الحلويات =====
# ============================================

def add_dessert():
    name = input("ادخل اسم الحلوى: ")
    try:
        price = float(input("ادخل سعر الحلوى: "))
        desserts.append({"name": name, "price": price})
        print("تمت اضافة الحلوى بنجاح.")
    except ValueError:
        print("خطا: يجب ادخال رقم صحيح للسعر.")

def print_desserts():
    if not desserts:
        print("لا توجد حلويات حاليا.")
        return
    print("\n=== قائمة الحلويات ===")
    for i, dessert in enumerate(desserts, 1):
        print(f"{i}. {dessert['name']} - {dessert['price']} ريال")

def edit_dessert():
    if not desserts:
        print("لا توجد حلويات للتعديل.")
        return
    print_desserts()
    try:
        index = int(input("ادخل رقم الحلوى التي تريد تعديلها: ")) - 1
        if 0 <= index < len(desserts):
            new_name = input("ادخل الاسم الجديد: ")
            new_price = float(input("ادخل السعر الجديد: "))
            desserts[index] = {"name": new_name, "price": new_price}
            print("تم تعديل الحلوى بنجاح.")
        else:
            print("رقم غير صحيح.")
    except ValueError:
        print("خطا: يجب ادخال رقم.")

def delete_dessert():
    if not desserts:
        print("لا توجد حلويات للحذف.")
        return
    print_desserts()
    try:
        index = int(input("ادخل رقم الحلوى التي تريد حذفها: ")) - 1
        if 0 <= index < len(desserts):
            deleted = desserts.pop(index)
            print(f"تم حذف الحلوى '{deleted['name']}' بنجاح.")
        else:
            print("رقم غير صحيح.")
    except ValueError:
        print("خطا: يجب ادخال رقم.")

def search_dessert():
    if not desserts:
        print("لا توجد حلويات للبحث.")
        return
    keyword = input("ادخل كلمة البحث: ").lower()
    found = [d for d in desserts if keyword in d['name'].lower()]
    if found:
        print("\n=== نتائج البحث ===")
        for dessert in found:
            print(f"- {dessert['name']} - {dessert['price']} ريال")
    else:
        print("لم يتم العثور على حلويات تطابق البحث.")

# ============================================
# ===== دوال إدارة الطلبات =====
# ============================================

def add_order():
    customer = input("ادخل اسم العميل: ")
    print("\n=== اختر الاصناف ===")
    print("1. وجبات")
    print("2. مشروبات")
    print("3. حلويات")
    print("4. انهاء الطلب")
    
    items = []
    while True:
        choice = input("اختر نوع الصنف (او 4 للانهاء): ")
        if choice == "4":
            break
        elif choice == "1":
            if not meals:
                print("لا توجد وجبات متاحة.")
                continue
            print_meals()
            try:
                idx = int(input("اختر رقم الوجبة: ")) - 1
                if 0 <= idx < len(meals):
                    items.append(meals[idx]['name'])
                    print(f"تم اضافة {meals[idx]['name']}")
                else:
                    print("رقم غير صحيح.")
            except ValueError:
                print("خطا: يجب ادخال رقم.")
        elif choice == "2":
            if not drinks:
                print("لا توجد مشروبات متاحة.")
                continue
            print_drinks()
            try:
                idx = int(input("اختر رقم المشروب: ")) - 1
                if 0 <= idx < len(drinks):
                    items.append(drinks[idx]['name'])
                    print(f"تم اضافة {drinks[idx]['name']}")
                else:
                    print("رقم غير صحيح.")
            except ValueError:
                print("خطا: يجب ادخال رقم.")
        elif choice == "3":
            if not desserts:
                print("لا توجد حلويات متاحة.")
                continue
            print_desserts()
            try:
                idx = int(input("اختر رقم الحلوى: ")) - 1
                if 0 <= idx < len(desserts):
                    items.append(desserts[idx]['name'])
                    print(f"تم اضافة {desserts[idx]['name']}")
                else:
                    print("رقم غير صحيح.")
            except ValueError:
                print("خطا: يجب ادخال رقم.")
        else:
            print("خيار غير صحيح.")
    
    if items:
        orders.append({"customer": customer, "items": items})
        print(f"تم انشاء طلب للعميل {customer} بنجاح.")
    else:
        print("لم يتم اضافة اي اصناف، لم يتم انشاء الطلب.")

def print_orders():
    if not orders:
        print("لا توجد طلبات حاليا.")
        return
    print("\n=== قائمة الطلبات ===")
    for i, order in enumerate(orders, 1):
        print(f"{i}. العميل: {order['customer']}")
        print(f"   الاصناف: {', '.join(order['items'])}")

def edit_order():
    if not orders:
        print("لا توجد طلبات للتعديل.")
        return
    print_orders()
    try:
        index = int(input("ادخل رقم الطلب الذي تريد تعديله: ")) - 1
        if 0 <= index < len(orders):
            new_customer = input("ادخل اسم العميل الجديد: ")
            orders[index]['customer'] = new_customer
            print("تم تعديل الطلب بنجاح.")
        else:
            print("رقم غير صحيح.")
    except ValueError:
        print("خطا: يجب ادخال رقم.")

def delete_order():
    if not orders:
        print("لا توجد طلبات للحذف.")
        return
    print_orders()
    try:
        index = int(input("ادخل رقم الطلب الذي تريد حذفه: ")) - 1
        if 0 <= index < len(orders):
            deleted = orders.pop(index)
            print(f"تم حذف طلب العميل {deleted['customer']} بنجاح.")
        else:
            print("رقم غير صحيح.")
    except ValueError:
        print("خطا: يجب ادخال رقم.")

def search_order():
    if not orders:
        print("لا توجد طلبات للبحث.")
        return
    keyword = input("ادخل اسم العميل للبحث: ").lower()
    found = [o for o in orders if keyword in o['customer'].lower()]
    if found:
        print("\n=== نتائج البحث ===")
        for order in found:
            print(f"- العميل: {order['customer']}")
            print(f"  الاصناف: {', '.join(order['items'])}")
    else:
        print("لم يتم العثور على طلبات لهذا العميل.")

# ============================================
# ===== القوائم الرئيسية =====
# ============================================

def meal_menu():
    while True:
        print("\n--- ادارة الوجبات ---")
        print("1. اضافة وجبة")
        print("2. عرض الوجبات")
        print("3. تعديل وجبة")
        print("4. حذف وجبة")
        print("5. بحث عن وجبة")
        print("6. رجوع")
        
        choice = input("اختر: ")
        if choice == "1":
            add_meal()
        elif choice == "2":
            print_meals()
        elif choice == "3":
            edit_meal()
        elif choice == "4":
            delete_meal()
        elif choice == "5":
            search_meal()
        elif choice == "6":
            break
        else:
            print("خيار غير صحيح.")

def drink_menu():
    while True:
        print("\n--- ادارة المشروبات ---")
        print("1. اضافة مشروب")
        print("2. عرض المشروبات")
        print("3. تعديل مشروب")
        print("4. حذف مشروب")
        print("5. بحث عن مشروب")
        print("6. رجوع")
        
        choice = input("اختر: ")
        if choice == "1":
            add_drink()
        elif choice == "2":
            print_drinks()
        elif choice == "3":
            edit_drink()
        elif choice == "4":
            delete_drink()
        elif choice == "5":
            search_drink()
        elif choice == "6":
            break
        else:
            print("خيار غير صحيح.")

def dessert_menu():
    while True:
        print("\n--- ادارة الحلويات ---")
        print("1. اضافة حلوى")
        print("2. عرض الحلويات")
        print("3. تعديل حلوى")
        print("4. حذف حلوى")
        print("5. بحث عن حلوى")
        print("6. رجوع")
        
        choice = input("اختر: ")
        if choice == "1":
            add_dessert()
        elif choice == "2":
            print_desserts()
        elif choice == "3":
            edit_dessert()
        elif choice == "4":
            delete_dessert()
        elif choice == "5":
            search_dessert()
        elif choice == "6":
            break
        else:
            print("خيار غير صحيح.")

def order_menu():
    while True:
        print("\n--- ادارة الطلبات ---")
        print("1. اضافة طلب")
        print("2. عرض الطلبات")
        print("3. تعديل طلب")
        print("4. حذف طلب")
        print("5. بحث عن طلب")
        print("6. رجوع")
        
        choice = input("اختر: ")
        if choice == "1":
            add_order()
        elif choice == "2":
            print_orders()
        elif choice == "3":
            edit_order()
        elif choice == "4":
            delete_order()
        elif choice == "5":
            search_order()
        elif choice == "6":
            break
        else:
            print("خيار غير صحيح.")

def main_menu():
    while True:
        print("\n===== القائمة الرئيسية =====")
        print("1. ادارة الوجبات")
        print("2. ادارة المشروبات")
        print("3. ادارة الحلويات")
        print("4. ادارة الطلبات")
        print("5. حفظ البيانات")
        print("6. خروج")
        
        choice = input("اختر خيارا: ")
        if choice == "1":
            meal_menu()
        elif choice == "2":
            drink_menu()
        elif choice == "3":
            dessert_menu()
        elif choice == "4":
            order_menu()
        elif choice == "5":
            save_all_data()
            print("تم حفظ جميع البيانات بنجاح.")
        elif choice == "6":
            save_all_data()
            print("تم حفظ البيانات. وداعا!")
            break
        else:
            print("خيار غير صالح.")

# ============================================
# ===== تشغيل البرنامج =====
# ============================================

if __name__ == "__main__":
    load_all_data()
    main_menu()
