from abc import ABC, abstractmethod
import os

# ===== الكلاسات الأساسية =====
class Service(ABC):
    def __init__(self, customer, amount, price):
        # المتغيرات الخاصة Private
        self.__customer = customer
        self.__amount = amount
        self.__price = price

    # Getter و Setter للعميل
    def get_customer(self):
        return self.__customer

    def set_customer(self, customer):
        self.__customer = customer

    # Getter و Setter للمبلغ
    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    # Getter و Setter للرسوم
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    # دالة مجردة ليتم اعادة تنفيذها من قبل الابناء وتحدد نوع العملية
    @abstractmethod
    def get_category(self):
        pass

    # عرض بيانات العملية
    def display(self):
        print(f"العميل: {self.get_customer()} | المبلغ: {self.get_amount()} | الرسوم: {self.get_price()}")

    # تحويل البيانات لسطر واحد للحفظ في الملف
    def to_line(self):
        return f"{self.get_category()},{self.get_customer()},{self.get_amount()},{self.get_price()}\n"

    # دالة ثابتة لا تحتاج اوبجكت وتفهم نوع العملية وتقرا سطر من الملف وتعيد انشاء كائن جديد
    @staticmethod
    def from_line(line):
        try:
            cat, customer, amount, price = line.strip().split(",")
            amount = float(amount)
            price = float(price)

            if cat == "صرف عملة":
                return CurrencyExchange(customer, amount, price)
            elif cat == "حوالة دولية":
                return InternationalTransfer(customer, amount, price)
            elif cat == "حوالة محلية":
                return LocalTransfer(customer, amount, price)
            else:
                return None
        except (ValueError, IndexError):
            print(f"خطأ في قراءة السطر: {line}")
            return None

# ===== فروع الوراثة =====
class CurrencyExchange(Service):
    def get_category(self):
        return "صرف عملة"

class InternationalTransfer(Service):
    def get_category(self):
        return "حوالة دولية"

class LocalTransfer(Service):
    def get_category(self):
        return "حوالة محلية"

# ===== كلاس الصرافة الرئيسي =====
class ExchangeOffice:
    def __init__(self, filename="exchange.txt"):
        self.services = []
        self.filename = filename
        self.load_from_file()

    # إضافة عملية
    def add_service(self, service):
        self.services.append(service)
        print("تم إضافة العملية")
        self.save_to_file()

    # عرض العمليات
    def show_services(self):
        if not self.services:
            print("لا يوجد عمليات")
            return
        print("\n========= العمليات =========")
        for i, s in enumerate(self.services, 1):
            print(f"{i}. {s.get_category()} - ", end="")
            s.display()
        print("=============================")
    
    # حذف عملية
    def delete_service(self, index):
        if 0 <= index < len(self.services):
            deleted = self.services.pop(index)
            print(f"تم حذف العملية: {deleted.get_category()}")
            self.save_to_file()
        else:
            print("رقم غير صحيح")
    
    # تعديل عملية
    def edit_service(self, index):
        if 0 <= index < len(self.services):
            s = self.services[index]
            print("تعديل العملية:")
            s.display()

            new_name = input("اسم العميل الجديد (Enter لتخطي): ")
            new_amount = input("المبلغ الجديد (Enter لتخطي): ")
            new_price = input("الرسوم الجديدة (Enter لتخطي): ")

            if new_name:
                s.set_customer(new_name)
            if new_amount:
                try:
                    s.set_amount(float(new_amount))
                except ValueError:
                    print("خطأ: المبلغ يجب أن يكون رقماً")
            if new_price:
                try:
                    s.set_price(float(new_price))
                except ValueError:
                    print("خطأ: الرسوم يجب أن تكون رقماً")

            print("تم التعديل")
            self.save_to_file()
        else:
            print("رقم غير صحيح")
    
    # حفظ العمليات في الملف
    def save_to_file(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                for s in self.services:
                    f.write(s.to_line())
            print("تم حفظ البيانات بنجاح")
        except Exception as e:
            print(f"خطأ في حفظ البيانات: {e}")
    
    # تحميل العمليات من الملف
    def load_from_file(self):
        if not os.path.exists(self.filename):
            print("لا يوجد ملف سابق، سيتم البدء بقائمة فارغة")
            return
        
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():  # تخطي الأسطر الفارغة
                        s = Service.from_line(line)
                        if s:
                            self.services.append(s)
            print(f"تم تحميل {len(self.services)} عملية من الملف")
        except Exception as e:
            print(f"خطأ في تحميل البيانات: {e}")
            self.services = []

    # الحصول على عدد العمليات
    def get_services_count(self):
        return len(self.services)

    # البحث عن عملية حسب اسم العميل
    def search_by_customer(self, customer_name):
        results = []
        for s in self.services:
            if customer_name.lower() in s.get_customer().lower():
                results.append(s)
        return results

    # عرض العمليات حسب النوع
    def show_services_by_type(self, category):
        results = []
        for s in self.services:
            if s.get_category() == category:
                results.append(s)
        
        if results:
            print(f"\n=== عمليات {category} ===")
            for i, s in enumerate(results, 1):
                print(f"{i}. ", end="")
                s.display()
        else:
            print(f"لا توجد عمليات من نوع {category}")
        
        return results

# ===== البرنامج الرئيسي =====
def display_menu():
    print("\n=============================")
    print("   نظام الصرافة")
    print("=============================")
    print("1. إضافة عملية")
    print("2. عرض العمليات")
    print("3. حذف عملية")
    print("4. تعديل عملية")
    print("5. البحث عن عملية")
    print("6. عرض العمليات حسب النوع")
    print("7. عدد العمليات")
    print("0. خروج")
    print("=============================")

def get_valid_number(prompt):
    """الحصول على رقم صحيح من المستخدم"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("خطأ: يجب إدخال رقم صحيح")

def main():
    office = ExchangeOffice()
    
    # إضافة عمليات افتراضية إذا كانت القائمة فارغة
    if not office.services:
        print("لا توجد عمليات، سيتم إضافة عمليات افتراضية")
        office.add_service(CurrencyExchange("أحمد علي", 500, 15))
        office.add_service(InternationalTransfer("سارة محمد", 1200, 25))
        office.add_service(LocalTransfer("خالد عبدالله", 800, 10))

    while True:
        display_menu()
        choice = input("اختر رقم العملية: ")

        if choice == "1":
            print("\nاختر نوع الخدمة:")
            print("1. صرف عملة")
            print("2. حوالة دولية")
            print("3. حوالة محلية")
            
            try:
                sec = input("رقم الخدمة: ")
                name = input("اسم العميل: ")
                amount = get_valid_number("المبلغ: ")
                price = get_valid_number("قيمة الرسوم: ")

                if sec == "1":
                    service = CurrencyExchange(name, amount, price)
                elif sec == "2":
                    service = InternationalTransfer(name, amount, price)
                elif sec == "3":
                    service = LocalTransfer(name, amount, price)
                else:
                    print("خدمة غير صحيحة")
                    continue

                office.add_service(service)
            except Exception as e:
                print(f"حدث خطأ: {e}")

        elif choice == "2":
            office.show_services()

        elif choice == "3":
            office.show_services()
            try:
                index = int(input("رقم العملية للحذف: ")) - 1
                office.delete_service(index)
            except ValueError:
                print("خطأ: يجب إدخال رقم صحيح")

        elif choice == "4":
            office.show_services()
            try:
                index = int(input("رقم العملية للتعديل: ")) - 1
                office.edit_service(index)
            except ValueError:
                print("خطأ: يجب إدخال رقم صحيح")

        elif choice == "5":
            name = input("أدخل اسم العميل للبحث: ")
            results = office.search_by_customer(name)
            if results:
                print(f"\n=== نتائج البحث عن: {name} ===")
                for i, s in enumerate(results, 1):
                    print(f"{i}. ", end="")
                    s.display()
            else:
                print("لا توجد نتائج مطابقة")

        elif choice == "6":
            print("\nاختر نوع العملية:")
            print("1. صرف عملة")
            print("2. حوالة دولية")
            print("3. حوالة محلية")
            
            type_choice = input("اختر النوع: ")
            if type_choice == "1":
                office.show_services_by_type("صرف عملة")
            elif type_choice == "2":
                office.show_services_by_type("حوالة دولية")
            elif type_choice == "3":
                office.show_services_by_type("حوالة محلية")
            else:
                print("خيار غير صحيح")

        elif choice == "7":
            count = office.get_services_count()
            print(f"عدد العمليات في النظام: {count}")

        elif choice == "0":
            print("وداعاً")
            break

        else:
            print("خيار غير صحيح")

if __name__ == "__main__":
    main()
