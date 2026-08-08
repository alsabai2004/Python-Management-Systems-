# ==============================
# كلاس المنتج
# ==============================
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.price} x {self.quantity}"


# ==============================
# كلاس المتجر (يشمل المخزون والمبيعات)
# ==============================
class Store:
    def __init__(self, store_id, name):
        self.store_id = store_id
        self.name = name
        self.products = []  # List of Product
        self.sales = []     # List of dictionaries

    def add_product(self, product):
        # التحقق من عدم وجود منتج بنفس المعرف
        for existing_product in self.products:
            if existing_product.product_id == product.product_id:
                print(f"خطأ: يوجد منتج بنفس المعرف {product.product_id} بالفعل")
                return False
        self.products.append(product)
        print(f"تم إضافة المنتج: {product}")
        return True

    def remove_product(self, product_id):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                removed = self.products.pop(i)
                print(f"تم حذف المنتج: {removed}")
                return True
        print(f"لم يتم العثور على منتج بالمعرف {product_id}")
        return False

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def show_inventory(self):
        if not self.products:
            print(f"\nالمخزون فارغ في متجر: {self.name}")
            return
        print(f"\n=== مخزون متجر: {self.name} ===")
        print(f"{'ID':<6} {'المنتج':<20} {'السعر':<10} {'الكمية':<10}")
        print("-" * 50)
        for product in self.products:
            print(f"{product.product_id:<6} {product.name:<20} ${product.price:<9} {product.quantity:<10}")
        print("-" * 50)

    def make_sale(self, product_id, quantity, payment_method, customer_id=None):
        product = self.find_product(product_id)
        if not product:
            print("فشل البيع: المنتج غير موجود.")
            return 0
        
        if product.quantity < quantity:
            print(f"فشل البيع: الكمية غير متوفرة. المتوفر: {product.quantity}")
            return 0
        
        if payment_method not in ["Cash", "Credit Card", "Debit Card", "Mobile Payment"]:
            print("فشل البيع: طريقة الدفع غير مقبولة.")
            return 0

        total = product.price * quantity
        product.quantity -= quantity
        
        sale = {
            "product_id": product_id,
            "product": product.name,
            "quantity": quantity,
            "total": total,
            "payment_method": payment_method,
            "customer_id": customer_id
        }
        self.sales.append(sale)
        print(f"بيع ناجح: {quantity} x {product.name} = ${total:.2f}")
        return total

    def total_sales(self):
        return sum(sale['total'] for sale in self.sales)

    def get_sales_count(self):
        return len(self.sales)

    def show_sales_history(self):
        if not self.sales:
            print(f"\nلا توجد مبيعات في متجر: {self.name}")
            return
        print(f"\n=== سجل مبيعات متجر: {self.name} ===")
        for i, sale in enumerate(self.sales, 1):
            print(f"{i}. {sale['product']} x {sale['quantity']} = ${sale['total']} ({sale['payment_method']})")


# ==============================
# كلاس العميل
# ==============================
class Customer:
    def __init__(self, customer_id, name, phone=None, email=None):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.purchase_history = []  # List of tuples (store_name, product_name, quantity, total)

    def add_purchase(self, store_name, product_name, quantity, total):
        if total > 0:
            self.purchase_history.append((store_name, product_name, quantity, total))
            print(f"تم إضافة الشراء لتاريخ العميل {self.name}")

    def show_history(self):
        if not self.purchase_history:
            print(f"\nلا يوجد سجل شراء للعميل: {self.name}")
            return
        print(f"\n=== سجل مشتريات {self.name} ===")
        total_spent = 0
        for i, purchase in enumerate(self.purchase_history, 1):
            print(f"{i}. متجر: {purchase[0]}, المنتج: {purchase[1]}, الكمية: {purchase[2]}, الإجمالي: ${purchase[3]:.2f}")
            total_spent += purchase[3]
        print(f"إجمالي المشتريات: ${total_spent:.2f}")

    def get_total_spent(self):
        return sum(purchase[3] for purchase in self.purchase_history)

    def __str__(self):
        return f"{self.name} (ID: {self.customer_id})"


# ==============================
# كلاس الموظف
# ==============================
class Employee:
    def __init__(self, emp_id, name, position, salary=0):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id}) - {self.position}"


# ==============================
# كلاس النظام العام لإدارة المركز
# ==============================
class MallManagementSystem:
    def __init__(self):
        self.stores = []  # List of Store
        self.customers = {}  # Dict of customer_id -> Customer
        self.employees = {}  # Dict of emp_id -> Employee
        self.payment_methods = {"Cash", "Credit Card", "Debit Card", "Mobile Payment"}  # Set
        self.financial_records = []  # List of tuples (date, total_revenue)

    def add_store(self, store):
        # التحقق من عدم وجود متجر بنفس المعرف
        for existing_store in self.stores:
            if existing_store.store_id == store.store_id:
                print(f"خطأ: يوجد متجر بنفس المعرف {store.store_id} بالفعل")
                return False
        self.stores.append(store)
        print(f"تم إضافة المتجر: {store.name}")
        return True

    def find_store(self, store_id):
        for store in self.stores:
            if store.store_id == store_id:
                return store
        return None

    def add_customer(self, customer):
        if customer.customer_id in self.customers:
            print(f"خطأ: يوجد عميل بنفس المعرف {customer.customer_id} بالفعل")
            return False
        self.customers[customer.customer_id] = customer
        print(f"تم إضافة العميل: {customer.name}")
        return True

    def add_employee(self, employee):
        if employee.emp_id in self.employees:
            print(f"خطأ: يوجد موظف بنفس المعرف {employee.emp_id} بالفعل")
            return False
        self.employees[employee.emp_id] = employee
        print(f"تم إضافة الموظف: {employee.name}")
        return True

    def record_finance(self, date, revenue):
        if revenue > 0:
            self.financial_records.append((date, revenue))
            print(f"تم تسجيل الإيرادات: ${revenue} في تاريخ {date}")
        else:
            print("لم يتم تسجيل الإيرادات (القيمة صفر أو سالبة)")

    def show_all_stores(self):
        if not self.stores:
            print("\nلا توجد متاجر في المركز")
            return
        print("\n=== المتاجر في المركز ===")
        for store in self.stores:
            print(f"ID: {store.store_id} - {store.name} (عدد المنتجات: {len(store.products)})")

    def show_all_employees(self):
        if not self.employees:
            print("\nلا يوجد موظفين")
            return
        print("\n=== الموظفين ===")
        for emp in self.employees.values():
            print(emp)

    def show_all_customers(self):
        if not self.customers:
            print("\nلا يوجد عملاء")
            return
        print("\n=== العملاء ===")
        for customer in self.customers.values():
            print(f"ID: {customer.customer_id} - {customer.name} (إجمالي المشتريات: ${customer.get_total_spent():.2f})")

    def show_payment_methods(self):
        print("\n=== طرق الدفع المقبولة ===")
        for method in sorted(self.payment_methods):
            print(f"- {method}")

    def calculate_total_revenue(self):
        total = sum(store.total_sales() for store in self.stores)
        print(f"\nالإيرادات الإجمالية من جميع المتاجر: ${total:.2f}")
        return total

    def show_financial_records(self):
        if not self.financial_records:
            print("\nلا توجد سجلات مالية")
            return
        print("\n=== السجلات المالية ===")
        for record in self.financial_records:
            print(f"التاريخ: {record[0]}, الإيرادات: ${record[1]:.2f}")

    def get_customer_by_id(self, customer_id):
        return self.customers.get(customer_id)

    def get_employee_by_id(self, emp_id):
        return self.employees.get(emp_id)

    def show_store_details(self, store_id):
        store = self.find_store(store_id)
        if store:
            store.show_inventory()
            store.show_sales_history()
        else:
            print(f"لم يتم العثور على متجر بالمعرف {store_id}")


# ==============================
# القائمة التفاعلية
# ==============================
def get_valid_number(prompt, number_type=float):
    """الحصول على رقم صحيح من المستخدم"""
    while True:
        try:
            if number_type == int:
                return int(input(prompt))
            else:
                return float(input(prompt))
        except ValueError:
            print("خطأ: يجب إدخال رقم صحيح")

def main_menu(mall):
    while True:
        print("\n=== نظام إدارة المركز التجاري ===")
        print("1. عرض المتاجر")
        print("2. إضافة متجر")
        print("3. إضافة منتج لمتجر")
        print("4. عرض المخزون لمتجر")
        print("5. إجراء عملية بيع")
        print("6. إضافة عميل")
        print("7. إضافة موظف")
        print("8. عرض العملاء")
        print("9. عرض الموظفين")
        print("10. عرض الإيرادات")
        print("11. عرض السجلات المالية")
        print("12. عرض تفاصيل متجر")
        print("13. عرض طرق الدفع")
        print("0. خروج")

        choice = input("اختر خياراً: ")

        if choice == "1":
            mall.show_all_stores()

        elif choice == "2":
            try:
                store_id = int(input("أدخل معرف المتجر: "))
                name = input("أدخل اسم المتجر: ")
                mall.add_store(Store(store_id, name))
            except ValueError:
                print("خطأ: يجب إدخال رقم صحيح للمعرف")

        elif choice == "3":
            try:
                store_id = int(input("أدخل معرف المتجر: "))
                store = mall.find_store(store_id)
                if store:
                    pid = int(input("معرف المنتج: "))
                    pname = input("اسم المنتج: ")
                    price = get_valid_number("السعر: ", float)
                    qty = int(input("الكمية: "))
                    store.add_product(Product(pid, pname, price, qty))
                else:
                    print("لم يتم العثور على المتجر")
            except ValueError:
                print("خطأ: يجب إدخال رقم صحيح")

        elif choice == "4":
            try:
                store_id = int(input("أدخل معرف المتجر: "))
                store = mall.find_store(store_id)
                if store:
                    store.show_inventory()
                else:
                    print("لم يتم العثور على المتجر")
            except ValueError:
                print("خطأ: يجب إدخال رقم صحيح")

        elif choice == "5":
            try:
                store_id = int(input("أدخل معرف المتجر: "))
                store = mall.find_store(store_id)
                if not store:
                    print("لم يتم العثور على المتجر")
                    continue
                
                product_id = int(input("أدخل معرف المنتج: "))
                qty = int(input("الكمية: "))
                print("طرق الدفع المتاحة: Cash, Credit Card, Debit Card, Mobile Payment")
                method = input("طريقة الدفع: ")
                
                customer_id = input("معرف العميل (أو اضغط Enter للتخطي): ")
                if customer_id:
                    customer_id = int(customer_id)
                    if customer_id not in mall.customers:
                        print("تحذير: العميل غير موجود في النظام")
                else:
                    customer_id = None
                
                total = store.make_sale(product_id, qty, method, customer_id)
                
                if total > 0 and customer_id and customer_id in mall.customers:
                    product = store.find_product(product_id)
                    if product:
                        mall.customers[customer_id].add_purchase(store.name, product.name, qty, total)
                        
            except ValueError:
                print("خطأ: يجب إدخال رقم صحيح")

        elif choice == "6":
            try:
                cid = int(input("معرف العميل: "))
                name = input("اسم العميل: ")
                phone = input("رقم الهاتف (اختياري): ")
                email = input("البريد الإلكتروني (اختياري): ")
                mall.add_customer(Customer(cid, name, phone or None, email or None))
            except ValueError:
                print("خطأ: يجب إدخال رقم صحيح للمعرف")

        elif choice == "7":
            try:
                eid = int(input("معرف الموظف: "))
                name = input("اسم الموظف: ")
                job = input("المسمى الوظيفي: ")
                salary = input("الراتب (اختياري): ")
                mall.add_employee(Employee(eid, name, job, float(salary) if salary else 0))
            except ValueError:
                print("خطأ: يجب إدخال رقم صحيح")

        elif choice == "8":
            mall.show_all_customers()

        elif choice == "9":
            mall.show_all_employees()

        elif choice == "10":
            rev = mall.calculate_total_revenue()
            date = input("أدخل التاريخ (YYYY-MM-DD): ")
            mall.record_finance(date, rev)

        elif choice == "11":
            mall.show_financial_records()

        elif choice == "12":
            try:
                store_id = int(input("أدخل معرف المتجر: "))
                mall.show_store_details(store_id)
            except ValueError:
                print("خطأ: يجب إدخال رقم صحيح")

        elif choice == "13":
            mall.show_payment_methods()

        elif choice == "0":
            print("تم إنهاء البرنامج. شكراً لاستخدامك النظام!")
            break

        else:
            print("خيار غير صالح. حاول مرة أخرى.")


# ==============================
# تشغيل البرنامج
# ==============================
if __name__ == "__main__":
    mall = MallManagementSystem()
    
    # إضافة بيانات افتراضية للتجربة
    store1 = Store(1, "متجر الإلكترونيات")
    store1.add_product(Product(101, "لابتوب", 999.99, 10))
    store1.add_product(Product(102, "هاتف ذكي", 599.99, 20))
    
    store2 = Store(2, "متجر الملابس")
    store2.add_product(Product(201, "تي شيرت", 29.99, 50))
    store2.add_product(Product(202, "جينز", 49.99, 30))
    
    mall.add_store(store1)
    mall.add_store(store2)
    
    main_menu(mall)
