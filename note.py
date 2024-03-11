import json
import datetime


class Note:
    def __init__(self, note_id, title, body):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.create_date = datetime.datetime.now()


def default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')


def save_notes(notes, file_name):
    with open(file_name, 'w') as file:
        json.dump([note.__dict__ for note in notes], file, default=default)


def load_notes(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return [Note(note['note_id'], note['title'], note['body']) for note in data]
    except FileNotFoundError:
        return []


def add_note(notes, title, body):
    existing_ids = {note.note_id for note in notes}
    new_id = 1

    while new_id in existing_ids:
        new_id += 1

    notes.append(Note(new_id, title, body))


def edit_note(notes, note_id, new_title, new_body):
    for note in notes:
        if note.note_id == note_id:
            note.title = new_title
            note.body = new_body
            note.create_date = datetime.datetime.now()
            break


def delete_note(notes, note_id):
    notes = [note for note in notes if note.note_id != note_id]
    return notes


def read_notes(notes, filter_date=None):
    for note in notes:
        print(f"ID: {note.note_id} | Title: {note.title} | Body: {note.body} | Date: {note.create_date}")


# Просмотр определенной заметки по ID
def view_note_by_id(notes, note_id):
    selected_note = next((note for note in notes if note.note_id == note_id), None)
    if selected_note:
        print(f"{selected_note.title}: {selected_note.body}")
    else:
        print("Заметка с указанным ID не найдена.")


# Загрузка заметок из файла
notes = load_notes('notes.json')

while True:
    print("Выберите действие:")
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Показать список заметок")
    print("5. Просмотреть заметку по ID")
    print("6. Выход")

    choice = input("Введите номер действия: ")

    if choice == '1':
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        add_note(notes, title, body)
        save_notes(notes, 'notes.json')
        print("Заметка успешно добавлена!")

    elif choice == '2':
        note_id = int(input("Введите ID заметки для редактирования: "))
        new_title = input("Введите новый заголовок: ")
        new_body = input("Введите новый текст заметки: ")
        edit_note(notes, note_id, new_title, new_body)
        save_notes(notes, 'notes.json')
        print("Заметка успешно отредактирована!")

    elif choice == '3':
        note_id = int(input("Введите ID заметки для удаления: "))
        notes = delete_note(notes, note_id)
        save_notes(notes, 'notes.json')
        print("Заметка успешно удалена!")

    elif choice == '4':
        read_notes(notes)

    elif choice == '5':
        note_id = int(input("Введите ID заметки для просмотра: "))
        view_note_by_id(notes, note_id)

    elif choice == '6':
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите действие из списка.")
