from collections import UserDict

class Field:
	def __init__ (self, value):
		self.value = value
	
	def __str__ (self):
		return str(self.value)

class Name (Field):
	def __init__(self, value):
		super().__init__(value)
		if not value:
			raise ValueError("Name cannot be empty!")

class Phone(Field):
	def __init__(self, value):
		super().__init__(value)
		if not value.isdigit() or len(value) != 10:
			raise ValueError("Phone number must be 10 digits.")

class Record:
	def __init__(self, name):
		self.name = Name(name)
		self.phones = []
	
	def __str__(self):
		phones_str = '; '.join(str(phone) for phone in self.phones)
		return f"Contact name: {self.name.value}, phones: {phones_str}"
	
	def add_phone(self, phone):
		self.phones.append(Phone(phone))
	
	def remove_phone(self, phone):
		self.phones = [phon for phon in self.phones if phon.value != phone]
	
	def edit_phone(self, old_phone, new_phone):
		for i, phone in enumerate(self.phones):
			if phone.value == old_phone:
				self.phones[i] = Phone(new_phone)
				return
		raise ValueError(f"Phone number {old_phone} not found!")
	
	def find_phone(self, phone):
		for p in self.phones:
			if p.value == phone:
				return p
		return None

class AddressBook(UserDict):
	def __init__(self):
		super().__init__()
	
	def __str__(self):
		return '\n'.join(str(record) for record in self.data.values())
	
	def add_record(self, record):
		self.data[record.name.value] = record
	
	def find(self, name):
		return self.data.get(name, None)
	
	def delete(self, name):
		if name in self.data:
			del self.data[name]
	
	def find_by_phone(self, phone):
		for record in self.data.values():
			for p in record.phones:
				if p.value == phone:
					return record
		return None

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("123456790", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
