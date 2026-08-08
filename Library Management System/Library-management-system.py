class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # التحقق من عدم وجود كتاب بنفس الـ ISBN
        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                print(f"خطأ: يوجد كتاب بنفس رقم ISBN ({book.isbn}) بالفعل.")
                return
        self.books.append(book)
        print(f"تم إضافة الكتاب: {book}")

    def remove_book(self, isbn):
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                removed_book = self.books.pop(i)
                print(f"تم حذف الكتاب: {removed_book}")
                return
        print("لم يتم العثور على الكتاب بالـ ISBN المدخل.")

    def display_books(self):
        if not self.books:
            print("لا توجد كتب في المكتبة.")
            return
        print("\n=== كتب المكتبة ===")
        # عرض الكتب مرتبة حسب العنوان
        sorted_books = sorted(self.books, key=lambda x: x.title)
        for i, book in enumerate(sorted_books, 1):
            print(f"{i}. {book}")

    def search_books(self, title=None, author=None):
        results = []
        for book in self.books:
            if title and title.lower() in book.title.lower():
                results.append(book)
            elif author and author.lower() in book.author.lower():
                results.append(book)
                
        if results:
            print("\n=== نتائج البحث ===")
            for i, book in enumerate(results, 1):
                print(f"{i}. {book}")
        else:
            print("لا توجد نتائج مطابقة.")

    def get_book_count(self):
        return len(self.books)

    def get_books_by_author(self, author):
        """إرجاع قائمة بالكتب لمؤلف معين"""
        return [book for book in self.books if author.lower() in book.author.lower()]

    def update_book(self, isbn, title=None, author=None, year=None):
        """تحديث معلومات كتاب موجود"""
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                if year:
                    book.year = year
                print(f"تم تحديث الكتاب: {book}")
                return
        print("لم يتم العثور على الكتاب بالـ ISBN المدخل.")


def display_menu():
    print("\n=== قائمة المكتبة ===")
    print("1. إضافة كتاب")
    print("2. حذف كتاب")
    print("3. عرض جميع الكتب")
    print("4. البحث عن كتاب")
    print("5. تحديث معلومات كتاب")
    print("6. عرض عدد الكتب")
    print("7. الخروج")


def get_valid_year():
    """الحصول على سنة صحيحة من المستخدم"""
    while True:
        year = input("أدخل سنة النشر: ")
        try:
            year_int = int(year)
            if 1000 <= year_int <= 9999:
                return year_int
            else:
                print("خطأ: يجب أن تكون السنة بين 1000 و 9999.")
        except ValueError:
            print("خطأ: يجب إدخال رقم صحيح للسنة.")


def main():
    library = Library()
    
    while True:
        display_menu()
        choice = input("اختر خيارًا: ")

        if choice == "1":
            title = input("أدخل عنوان الكتاب: ")
            author = input("أدخل اسم المؤلف: ")
            year = get_valid_year()
            isbn = input("أدخل رقم ISBN: ")
            book = Book(title, author, year, isbn)
            library.add_book(book)

        elif choice == "2":
            isbn = input("أدخل رقم ISBN للكتاب الذي تريد حذفه: ")
            library.remove_book(isbn)

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            print("\nخيارات البحث:")
            print("1. البحث بالعنوان")
            print("2. البحث بالمؤلف")
            print("3. البحث بالعنوان والمؤلف")
            search_choice = input("اختر خيار البحث: ")
            
            if search_choice == "1":
                title = input("أدخل عنوان الكتاب للبحث: ")
                library.search_books(title=title)
            elif search_choice == "2":
                author = input("أدخل اسم المؤلف للبحث: ")
                library.search_books(author=author)
            elif search_choice == "3":
                title = input("أدخل عنوان الكتاب للبحث: ")
                author = input("أدخل اسم المؤلف للبحث: ")
                # البحث بالعنوان والمؤلف معاً
                results = []
                for book in library.books:
                    if (title.lower() in book.title.lower() and 
                        author.lower() in book.author.lower()):
                        results.append(book)
                if results:
                    print("\n=== نتائج البحث ===")
                    for i, book in enumerate(results, 1):
                        print(f"{i}. {book}")
                else:
                    print("لا توجد نتائج مطابقة.")
            else:
                print("خيار غير صحيح.")

        elif choice == "5":
            isbn = input("أدخل رقم ISBN للكتاب الذي تريد تحديثه: ")
            print("اترك الحقل فارغاً إذا كنت لا تريد تغييره.")
            title = input("العنوان الجديد (أو اضغط Enter للتخطي): ")
            author = input("المؤلف الجديد (أو اضغط Enter للتخطي): ")
            year = input("سنة النشر الجديدة (أو اضغط Enter للتخطي): ")
            
            # تحويل السنة إلى int إذا تم إدخالها
            if year:
                try:
                    year = int(year)
                except ValueError:
                    print("خطأ: السنة غير صحيحة، لن يتم تحديثها.")
                    year = None
            else:
                year = None
                
            library.update_book(isbn, title or None, author or None, year)

        elif choice == "6":
            count = library.get_book_count()
            print(f"عدد الكتب في المكتبة: {count}")

        elif choice == "7":
            print("شكرًا لاستخدامك المكتبة!")
            break

        else:
            print("خيار غير صحيح. حاول مرة أخرى.")


if __name__ == "__main__":
    main()
