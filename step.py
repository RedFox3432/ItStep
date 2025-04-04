class LibraryItem:
    def __init__(self, title, author, item_id):
        self.__title = title
        self.__author = author
        self.__item_id = item_id
        self._is_borrowed = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_item_id(self):
        return self.__item_id

    def is_same_item(self, other_item):
        return self.__item_id == other_item.get_item_id()

    def borrow_item(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            print(f"{self.get_title()} взято.")
        else:
            print(f"{self.get_title()} уже взято.")

    def return_item(self):
        if self._is_borrowed:
            self._is_borrowed = False
            print(f"{self.get_title()} ыернули.")
        else:
            print(f"{self.get_title()} не было взято.")

    def display_info(self):
        raise NotImplementedError("Цей метод повинен бути реалізований у дочірньому класі")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.__pages = pages

    def display_info(self):
        print(f"Книга: {self.get_title()}, Автор: {self.get_author()}, Странички: {self.__pages}")

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.__issue_number = issue_number

    def display_info(self):
        print(f"Журнал: {self.get_title()}, Автор: {self.get_author()}, Номер выпуску: {self.__issue_number}")


class Audiobook(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.__duration = duration

    def display_info(self):
        print(f"Аудиокнига: {self.get_title()}, Автор: {self.get_author()}, длителельность: {self.__duration} хвилин")

library_items = [
    Book("1984", "Джордж Орвелл", 1, 328),
    Magazine("National Geographic", "Колектив", 2, 124),
    Audiobook("Гарри Поттер", "Джоан Роулинг", 3, 480)
]

for item in library_items:
    item.display_info()
    item.borrow_item()
    item.return_item()
    print("-" * 50)
