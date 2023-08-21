class Phonebook:
    def __init__(self, filename):
        self.filename = filename

    def display_entries(self, page_size=10):
        entries = self._load_entries()
        num_entries = len(entries)

        if num_entries == 0:
            print("Справочник пуст")
            return

        num_pages = (num_entries - 1) // page_size + 1

        try:
            page_num = int(input(f"Введите номер страницы (1-{num_pages}): "))
        except ValueError:
            print("Введен некорректный номер страницы")
            return

        if page_num < 1 or page_num > num_pages:
            print("Введен некорректный номер страницы")
            return

        start_index = (page_num - 1) * page_size
        end_index = start_index + page_size
        page_entries = entries[start_index:end_index]

        for entry in page_entries:
            print(entry)

    def add_entry(self, entry):
        entries = self._load_entries()
        entries.append(entry)
        self._save_entries(entries)

    def edit_entry(self, index):
        entries = self._load_entries()

        if index < 1 or index > len(entries):
            print("Введен некорректный номер записи")
            return

        entry = entries[index - 1]
        new_entry = input("Введите новую информацию для записи: ")
        entries[index - 1] = new_entry
        self._save_entries(entries)

    def search_entries(self, **attributes):
        entries = self._load_entries()

        matched_entries = []
        for entry in entries:
            if all(entry.get(attr) == value for attr, value in attributes.items()):
                matched_entries.append(entry)

        if len(matched_entries) == 0:
            print("Записи не найдены")
            return

        for entry in matched_entries:
            print(entry)

    def _load_entries(self):
        try:
            with open(self.filename, "r") as file:
                entries = eval(file.read())
        except FileNotFoundError:
            entries = []
        return entries

    def _save_entries(self, entries):
        with open(self.filename, "w") as file:
            file.write(repr(entries))
