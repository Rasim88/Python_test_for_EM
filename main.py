from phonebook import Phonebook

def main():
    phonebook = Phonebook("phonebook.txt")

    while True:
        print("1. Вывести записи")
        print("2. Добавить новую запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выход")

        choice = input("Выберите опцию (1-5): ")

        if choice == "1":
            phonebook.display_entries()
        elif choice == "2":
            entry = input("Введите информацию для новой записи: ")
            phonebook.add_entry(entry)
        elif choice == "3":
            index = int(input("Введите номер записи для редактирования: "))
            phonebook.edit_entry(index)
        elif choice == "4":
            attributes = {}
            attributes['фамилия'] = input("Введите фамилию: ")
            attributes['имя'] = input("Введите имя: ")
            attributes['отчество'] = input("Введите отчество: ")
            attributes['название организации'] = input("Введите название организации: ")
            attributes['телефон рабочий'] = input("Введите рабочий телефон: ")
            attributes['телефон личный'] = input("Введите личный телефон: ")
            phonebook.search_entries(**attributes)
        elif choice == "5":
            break
        else:
            print("Некорректный выбор")

if __name__ == "__main__":
    main()
