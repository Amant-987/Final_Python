from Notes.NoteManager import NoteManager


class Menu:
    def __init__(self):
        self.note_manager = NoteManager()

    def create_note_menu(self):
        note_id = len(self.note_manager.notes) + 1
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        note = Note(note_id, title, body)
        self.note_manager.add_note(note)
        print("Заметка успешно создана!")

    def view_all_notes_menu(self):
        if len(self.note_manager.notes) == 0:
            print("Нет доступных заметок.")
        else:
            for note in self.note_manager.notes:
                print(f"ID: {note.note_id}")
                print(f"Заголовок: {note.title}")
                print(f"Текст: {note.body}")
                print(f"Создано: {note.created_at}")
                print(f"Обновлено: {note.updated_at}")
                print("-------------------")

    def view_note_by_id_menu(self):
        note_id = int(input("Введите ID заметки: "))
        note = self.note_manager.get_note_by_id(note_id)
        if note:
            print(f"ID: {note.note_id}")
            print(f"Заголовок: {note.title}")
            print(f"Текст: {note.body}")
            print(f"Создано: {note.created_at}")
            print(f"Обновлено: {note.updated_at}")
        else:
            print("Заметка с указанным ID не найдена.")

    def edit_note_by_id_menu(self):
        note_id = int(input("Введите ID заметки для редактирования: "))
        note = self.note_manager.get_note_by_id(note_id)
        if note:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note.update(title, body)
            print("Заметка успешно обновлена!")
        else:
            print("Заметка с указанным ID не найдена.")

    def delete_note_by_id_menu(self):
        note_id = int(input("Введите ID заметки для удаления: "))
        note = self.note_manager.get_note_by_id(note_id)
        if note:
            self.note_manager.delete_note(note)
            print("Заметка успешно удалена!")
        else:
            print("Заметка с указанным ID не найдена.")

    def run(self):
        while True:
            print("Меню:")
            print("1. Создать новую заметку")
            print("2. Просмотреть все заметки")
            print("3. Просмотреть заметку по ID")
            print("4. Редактировать заметку по ID")
            print("5. Удалить заметку по ID")
            print("0. Выход")

            choice = input("Выберите пункт меню: ")
            if choice == "1":
                self.create_note_menu()
            elif choice == "2":
                self.view_all_notes_menu()
            elif choice == "3":
                self.view_note_by_id_menu()
            elif choice == "4":
                self.edit_note_by_id_menu()
            elif choice == "5":
                self.delete_note_by_id_menu()
            elif choice == "0":
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")

menu = Menu()
menu.run()