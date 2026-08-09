# 🏦 نظام إدارة البنك (Bank Management System)

نظام إدارة بنكي متكامل مكتوب بلغة Python باستخدام البرمجة الكائنية (OOP) وتخزين البيانات في ملفات JSON. يدير النظام ثلاث أنواع من المستخدمين (مدير، فرع، عميل) مع صلاحيات مختلفة لكل نوع.

---

## 📋 نظرة عامة

نظام إدارة البنك هو تطبيق Python يعمل في بيئة سطر الأوامر (Console) ويوفر واجهة شاملة للتعامل مع العمليات المصرفية الأساسية:

- 🔐 نظام مصادقة بثلاث مستويات (مدير، فرع، عميل).
- 💰 عمليات الإيداع والسحب.
- 👥 إدارة الحسابات (إنشاء، تعديل، حذف، عرض).
- 📊 إحصائيات وأرباح الخدمات.
- 💾 تخزين البيانات في ملفات JSON.

---

## ✨ الميزات الرئيسية

### 👑 المدير (Manager)
- تغيير كلمة المرور الخاصة به.
- عرض إجمالي أرباح الخدمات (الإيداع والسحب).
- عرض إحصائيات عدد الحسابات.
- عرض جميع الحسابات المسجلة.
- إنشاء حساب فرع جديد (Branch).
- إنشاء حساب عميل عادي (Normal).
- تعديل حسابات الفروع والعملاء.
- حذف حسابات الفروع والعملاء.

### 🏢 الفرع (Branch)
- تغيير كلمة المرور الخاصة به.
- إيداع مبلغ في حسابه.
- سحب مبلغ من حسابه.

### 👤 العميل العادي (Normal)
- تغيير كلمة المرور الخاصة به.
- إيداع مبلغ في حسابه.
- سحب مبلغ من حسابه.

---

## 🛠️ التقنيات المستخدمة

| التقنية | الاستخدام |
|---------|-----------|
| **Python 3** | لغة البرمجة الأساسية |
| **OOP (Object-Oriented Programming)** | البرمجة الكائنية (كلاس Account) |
| **JSON** | تخزين البيانات في ملفات |
| **os module** | للتحكم في نظام التشغيل (مسح الشاشة) |
| **File I/O** | قراءة وكتابة الملفات |

---

## 📁 هيكل المشروع

```

/
├── Bank-Management-System.py       # الملف الرئيسي للتطبيق
├── accounts.txt         # ملف تخزين بيانات الحسابات (JSON)
└── README.md           # هذا الملف

```

---

## 🏗️ هيكل الكلاسات

### كلاس Account

```python
class Account:
    def __init__(self, name, id, password, phone, balance, type):
        self.name = name
        self.id = id
        self.password = password
        self.phone = phone
        self.balance = balance
        self.type = type  # manager, branch, normal
```

---

📖 دليل الاستخدام

1️⃣ تسجيل الدخول

عند تشغيل البرنامج لأول مرة، سيتم إنشاء حساب مدير افتراضي:

```
الاسم: Admin
ID: admin
كلمة المرور: 1234
نوع الحساب: manager
الرصيد: 1000
```

لتسجيل الدخول:

1. أدخل ID الخاص بك.
2. أدخل كلمة المرور الخاصة بك.
3. اختر نوع الحساب:
   · 1 للمدير (Manager)
   · 2 للفرع (Branch)
   · 3 للعميل العادي (Normal)

مثال:

```
=== log in ===
enter the ID: admin
enter the password: 1234

choice account type:
1. Manager
2. Branch
3. Normal
choice account type (1/2/3): 1
Admin, Hello, you are logged in as a manager !
```

---

2️⃣ واجهة المدير (Manager)

```
=== Bank manager ===
1. change password
2. read Profits
3. Statistics
4. view accounts
5. create a branch account
6. create a normal account
7. edit branch or normal account
8. delete branch or normal account
9. log out
0. back to login
```

الخيارات بالتفصيل:

1. تغيير كلمة المرور (change password)

· إدخال كلمة المرور القديمة.
· إدخال كلمة المرور الجديدة.
· تأكيد كلمة المرور الجديدة.

2. عرض الأرباح (read Profits)

· عرض إجمالي أرباح الخدمات (100 ريال لكل عملية إيداع أو سحب).

3. الإحصائيات (Statistics)

· عرض عدد الحسابات المسجلة في النظام.

4. عرض الحسابات (view accounts)

· عرض جميع الحسابات مع تفاصيلها (الاسم، ID، النوع، الرصيد).

5. إنشاء حساب فرع (create a branch account)

· إدخال اسم الفرع.
· إدخال ID (يتم التحقق من عدم التكرار).
· إدخال كلمة المرور.
· إدخال رقم الهاتف.
· إدخال الرصيد الابتدائي.

6. إنشاء حساب عميل (create a normal account)

· إدخال اسم العميل.
· إدخال ID (يتم التحقق من عدم التكرار).
· إدخال كلمة المرور.
· إدخال رقم الهاتف.
· إدخال الرصيد الابتدائي.

7. تعديل حساب (edit branch or normal account)

· إدخال ID الحساب المراد تعديله.
· تعديل الاسم، كلمة المرور، رقم الهاتف، الرصيد.

8. حذف حساب (delete branch or normal account)

· إدخال ID الحساب المراد حذفه.

9. تسجيل الخروج (log out)

0. العودة إلى شاشة تسجيل الدخول (back to login)

---

3️⃣ واجهة الفرع (Branch)

```
=== Branch ===
1. change password
2. Deposit
3. Withdraw
4. log out
0. back to login
```

الخيارات:

· 1: تغيير كلمة المرور الخاصة بالفرع.
· 2: إيداع مبلغ في حساب الفرع.
· 3: سحب مبلغ من حساب الفرع (يجب أن يكون الرصيد كافياً).
· 4 أو 0: تسجيل الخروج والعودة إلى شاشة تسجيل الدخول.

---

4️⃣ واجهة العميل العادي (Normal)

```
=== Normal ===
1. change password
2. Deposit
3. Withdraw
4. log out
0. back to login
```

الخيارات:

· 1: تغيير كلمة المرور الخاصة بالعميل.
· 2: إيداع مبلغ في حساب العميل.
· 3: سحب مبلغ من حساب العميل (يجب أن يكون الرصيد كافياً).
· 4 أو 0: تسجيل الخروج والعودة إلى شاشة تسجيل الدخول.

---

📝 أمثلة على الاستخدام

إنشاء حساب فرع جديد

```
=== Bank manager ===
1. change password
2. read Profits
3. Statistics
4. view accounts
5. create a branch account
6. create a normal account
7. edit branch or normal account
8. delete branch or normal account
9. log out
0. back to login

choose a choice number: 5
Branch name: فرع الرياض
account number (ID): 1001
password: 1234
phone number: 0555123456
Initial branch balance: 5000
The account has been created. فرع الرياض is new branch.
```

إيداع مبلغ

```
Enter the amount to deposit: 1000
Successfully deposited. Your current balance: 6000
```

سحب مبلغ

```
Enter the amount to withdraw: 500
Successfully withdrawn. Your current balance: 5500
```

عرض جميع الحسابات

```
=== All accounts ===
Admin (ID: admin, account type: manager, the balance: 1000)
فرع الرياض (ID: 1001, account type: branch, the balance: 5500)
أحمد محمد (ID: 1002, account type: normal, the balance: 2000)
```

---

🗂️ هيكل ملف التخزين (accounts.txt)

```json
[
  {
    "name": "Admin",
    "id": "admin",
    "password": "1234",
    "phone": "0000",
    "balance": 1000,
    "type": "manager"
  },
  {
    "name": "فرع الرياض",
    "id": "1001",
    "password": "1234",
    "phone": "0555123456",
    "balance": 5500,
    "type": "branch"
  },
  {
    "name": "أحمد محمد",
    "id": "1002",
    "password": "1234",
    "phone": "0555987654",
    "balance": 2000,
    "type": "normal"
  }
]
```

---

🔄 تدفق البرنامج

```
1. بدء البرنامج
   ↓
2. تحميل البيانات من accounts.txt
   ↓
3. إنشاء حساب مدير افتراضي إذا لم يكن موجوداً
   ↓
4. عرض شاشة تسجيل الدخول
   ↓
5. إدخال ID، كلمة المرور، ونوع الحساب
   ↓
6. التحقق من البيانات
   ↓
7. عرض الواجهة المناسبة حسب نوع الحساب
   ↓
8. تنفيذ العمليات المطلوبة
   ↓
9. تسجيل الخروج والعودة إلى شاشة تسجيل الدخول
```

---

🚀 كيفية التشغيل

المتطلبات

· Python 3.6 أو أحدث.
· نظام تشغيل Windows، Linux، أو macOS.

الخطوات

1. نسخ الكود:
   قم بنسخ الكود إلى ملف جديد باسم Bank-Management-System.py.
2. تشغيل البرنامج:
   ```bash
   python Bank-Management-System.py
   ```
3. تسجيل الدخول:
   استخدم بيانات الدخول الافتراضية:
   ```
   ID: admin
   Password: 1234
   Account Type: 1 (Manager)
   ```

---

🔧 التخصيص والتطوير

تغيير بيانات تسجيل الدخول الافتراضية

يمكنك تغيير بيانات المدير الافتراضي في نهاية الكود:

```python
if not any(acc.type == "manager" for acc in accounts_data):
    accounts_data.append(Account("Admin", "admin", "1234", "0000", 1000, "manager"))
    save_accounts_to_file()
```

تغيير قيمة الأرباح

يمكنك تغيير قيمة الأرباح المضافة لكل عملية في دالتي deposit() و withdraw():

```python
service_earn += 100  # قم بتغيير 100 إلى القيمة المطلوبة
```

إضافة صلاحيات جديدة

1. أضف نوع الحساب الجديد في دالة login().
2. أنشئ دالة جديدة للواجهة الخاصة بالنوع الجديد.
3. أضف الخيار في قائمة أنواع الحسابات.

---

🐛 معالجة الأخطاء

الخطأ المعالجة
ID غير موجود رسالة "ID or password or account type is wrong"
كلمة مرور خاطئة رسالة "ID or password or account type is wrong"
ID مكرر رسالة "The ID already exists"
رصيد غير كافٍ رسالة "balance is insufficient or amount is invalid"
مبلغ غير صحيح رسالة "amount is Invalid"

---

📊 العلاقات بين الكلاسات

```
┌─────────────────────────────────────────────────────────────┐
│                 Bank Management System                     │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              accounts_data[]                        │   │
│  │  ┌─────────────────────────────────────────────┐  │   │
│  │  │              Account                        │  │   │
│  │  │  - name                                     │  │   │
│  │  │  - id                                       │  │   │
│  │  │  - password                                 │  │   │
│  │  │  - phone                                    │  │   │
│  │  │  - balance                                  │  │   │
│  │  │  - type (manager/branch/normal)             │  │   │
│  │  └─────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           service_earn (أرباح الخدمات)             │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

📄 الترخيص

هذا المشروع مفتوح المصدر ويمكن استخدامه وتعديله بحرية لأي غرض تعليمي أو شخصي.

---

👨‍💻 المطور

Eng\ Mohammed Najeeb Alsabai

---

🤝 المساهمة

يمكنك المساهمة في تطوير المشروع من خلال:

1. إضافة نظام تقارير وإحصائيات متقدمة.
2. إضافة واجهة مستخدم رسومية (GUI).
3. إضافة عمليات مصرفية إضافية (تحويلات، قروض).
4. إضافة نظام إشعارات للعمليات.
5. تحسين أمان النظام (تشفير كلمات المرور).

---

Bank Management System © 2026 - نظام إدارة بنكي متكامل وسهل الاستخدام.

```
