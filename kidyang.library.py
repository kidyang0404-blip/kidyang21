from abc import ABC, abstractmethod
from os import name
from typing import Any, Self

class LibraryItem(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display_info(self):
        pass

class ItemManager:
    def __init__(self):
        self.total_items = 0
        self.items = []

    def __init__(self):
        self.is_loaned = False
        self.borrower = None    

class ItemManager:
    total_items = 1
    self.total_items =("total_items")
    self.total_items += 1

class ItemManager:  
    def __init__(self):
        self.items = [] 
        self.loaned_items = 0
        self.info = {}  

class Book(LibraryItem):
    def __init__(self, title,  item_id, author, page_count):
        super().__init__(title, item_id) 
        self.item_id = item_id
        self.page_count = page_count                
    def display_info(self):
        return f"Book: {self.title}, Author: {self.author}, Pages: {self.page_count}"
               
b = Book("파이썬 입문", "B001", "박응용", 480) 
print(b.display_info())
b.loan_period = 14
print(f"Loan Period: {b.loan_period} days")
b.is_loaned = False 
print(f"Is Loaned: {b.is_loaned}")

class DVD(LibraryItem):
    def __init__(self, title, item_id, author, duration):
        super().__init__(title, item_id)
        self.item_id = item_id
        self.duration = duration

    def display_info(self):
        return f"DVD: {self.title}, Author: {self.author}, Duration: {self.duration} minutes"   
d = DVD("인터스텔라", "D001", "놀란","169분")
print(d.display_info())
d.loan_period = 7
print(f"Loan Period: {d.loan_period} days") 


class Magazine(LibraryItem):
    def __init__(self, title, item_id, author, issue_number):
        super().__init__(title, item_id)
        self.item_id = item_id
        self.issue_number = issue_number

    def display_info(self):
        return f"Magazine: {self.title}, Issue: {self.issue_number}" 
m = Magazine("과학동아", "M001","9월호")
print(m.display_info()) 
m.loan_period = 3
print(f"Loan Period: {m.loan_period} days")

class LibraryItemMaster:
    def __init__(self):
        self.items = []  
        self.loaned_items = 0  
        self.info = {}  

    def add_item(self, item):
        self.items.append(item)
        self.info[item.item_id] = item
        print(f"Item added: {item.display_info()}")

    def loan_item(self, item_id, borrower):
        if item_id in self.info:
            item = self.info[item_id]
            if not hasattr(item, 'is_loaned') or not item.is_loaned:
                item.is_loaned = True
                item.borrower = borrower
                self.loaned_items += 1
                print(f"Item loaned: {item.display_info()} to {borrower}")
            else:
                print(f"Item {item_id} is already loaned.")
        else:
            print(f"Item {item_id} not found.")

    def return_item(self, item_id):
        if item_id in self.info:
            item = self.info[item_id]
            if hasattr(item, 'is_loaned') and item.is_loaned:
                item.is_loaned =False   
                item.borrower = None
                self.loaned_items -= 1
                print(f"Item returned: {item.display_info()}")
            else:
                print(f"Item {item_id} was not loaned.")
        else:
            print(f"Item {item_id} not found.")
    b.check_loan_status = lambda
    self: f"Is Loaned: {self.is_loaned}"
    if hasattr(self, 'is_loaned')
    else "Loan status not available"
print(b.check_loan_status())    
print(f"Total items in library: {LibraryItemMaster().loaned_items}")    
print(f"Total items in library: {LibraryItemMaster().loaned_items}")    

print("김민준", "'파이썬 입문'대출 완료", "대출기간: 14일")
print("이서연", "'인터스텔라'대출 완료", "대출기간: 7일") 

return_item( "김민준", "'파이썬 입문' 을반납 했습니다")

CLASS LibraryItemMaster:
    def __init__(self): 
        self.items = []  
        self.loaned_items = 0  
        self.info = {}  

lib = Library("한빛도서관")
lib.add_Book(Book("파이썬 입문", "B001", "박응용", 480))
lib.add_dVD(DVD("인터스텔라", "D001", "놀란", 169)) 

    def add_item(self, item):
        self.items.append(item)
        self.info[item.item_id] = item
        print(f"Item added: {item.display_info()}")

    def loan_item(self, item_id, borrower):
        if item_id in self.info:
            item = self.info[item_id]
            if not hasattr(item, 'is_loaned') or not item.is_loaned:
                item.is_loaned = True
                item.borrower = borrower
                self.loaned_items += 1
                print(f"Item loaned: {item.display_info()} to {borrower}")
            else:
                print(f"Item {item_id} is already loaned.")
        else:
            print(f"Item {item_id} not found.")

    def return_item(self, item_id):

        if item_id in self.info:
            item = self.info[item_id]
            if hasattr(item, 'is_loaned') and item.is_loaned:
                item.is_loaned = False
                item.borrower = None
                self.loaned_items -= 1
                print(f"Item returned: {item.display_info()}")
            else:
                print(f"Item {item_id} was not loaned.")
        else:
            print(f"Item {item_id} not found.")

    def show_info(self):
        print(f"Library: {self.name}")
        for item in self.items:
            item.info()
            print(item.display_info())
        print(f"Total items in library: {len(self.items)}")
        print(f"Total loaned items: {self.loaned_items}")
        print("-" * 56, "=" * 56)
        print("한 빛 도 서 관",)
        print("=" * 56, "-" * 56)
       
    def show_loaned_items(self):   
f"{item.item_id:<6}{item.info():<32}{state:>14}")
        print(f"{'Item ID':<6}{'Info':<32}{'Loan Status':>14}")  
b001 = Book("파이썬 입문", "B001", "박응용", "480","대출중(김민준)")
b002 = Book("자료 구조 ", "B002", "김철수", "320","대출가능 ")
d001 = DVD("인터스텔라", "D001", "놀란","169","대출중(이서연)")
m001 = Magazine("과학동아", "M001", "9월호","대출가능")
        print("-" * 56, "=" * 56)
        print("=" * 56, "-" * 56)

   def report():
        print("-" * 56)
        print("종류별 등록 현황")
        print("-" * 56)
        print(f"book: {type_counts.get('Book', 0)}대")
        print(f"DVD: {type_counts.get('DVD', 0)}대")
        print(f"Magazine: {type_counts.get('Magazine', 0)}대")
        print("-" * 56, "=" * 56)