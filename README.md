# Блокнот на Python

Программа блокнота на Python предоставляет функционал для создания, редактирования, удаления и просмотра заметок с поддержкой сохранения данных в файл в формате JSON. Этот блокнот поможет вам организовать свои заметки эффективно.

### Функции программы:

1. Добавить заметку
    - Функция add_note добавляет новую заметку в блокнот. Если ID заметки уже существует, автоматически выбирается следующий доступный ID.

2. Редактировать заметку
    - Функция edit_note позволяет редактировать информацию о существующей заметке по её ID.

3. Удалить заметку
    - Функция delete_note удаляет заметку из блокнота по указанному ID.

4. Показать список заметок
    - Функция read_notes выводит на экран список всех заметок в блокноте.

5. Просмотреть заметку по ID
    - Функция view_note_by_id позволяет просмотреть содержимое конкретной заметки по её ID.

### Работа с файлом JSON:

Данные о заметках сохраняются в файле notes.json в формате JSON. Каждая заметка представлена в виде JSON объекта со следующими полями: note_id, title, body и create_date.

### Использование программы:

1. Добавление заметки:
    - Пользователю предлагается ввести заголовок и текст заметки. Пример:
    ```
    Выберите действие:
    1. Добавить заметку
    ...
    Введите номер действия: 1
    Введите заголовок заметки: Новая задача
    Введите текст заметки: Завершить проект к следующему понедельнику
    Заметка успешно добавлена!
    ```

2. Редактирование заметки:
    - Пользователю предлагается ввести ID заметки, новый заголовок и текст заметки. Пример:
    ```
    Выберите действие:
    2. Редактировать заметку
    ...
    Введите номер действия: 2
    Введите ID заметки для редактирования: 1
    Введите новый заголовок: Обновленная задача
    Введите новый текст заметки: Завершить проект к среде
    Заметка успешно отредактирована!
    ```

3. Удаление заметки:
    - Пользователю предлагается ввести ID заметки для удаления. Пример:
    ```
    Выберите действие:
    3. Удалить заметку
    ...
    Введите номер действия: 3
    Введите ID заметки для удаления: 2
    Заметка успешно удалена!
    ```

4. Показать список заметок:
    - Выводится список всех заметок в блокноте. Пример:
    ```
    Выберите действие:
    4. Показать список заметок
    ...
    ID: 1 | Title: Новая задача | Body: Завершить проект к следующему понедельнику | Date: 2024-03-15 14:30:00
    ID: 2 | Title: Обновленная задача | Body: Завершить проект к среде | Date: 2024-03-15 14:32:00
    ```

5. Просмотр заметки по ID:
    - Пользователю предлагается ввести ID заметки для просмотра. Пример:
    ```
    Выберите действие:
    5. Просмотреть заметку по ID
    ...
    Введите номер действия: 5
    Введите ID заметки для просмотра: 1
    Новая задача: Завершить проект к следующему понедельнику
    ```

### Пример использования программы и результаты:

- Добавление заметки:
    - Пользователь добавляет новую заметку "Позвонить Марии" с текстом "Узнать о встрече на следующей неделе". Результат: Заметка успешно добавлена!

- Редактирование заметки:
    - Пользователь редактирует заметку с ID 2, меняя заголовок на "Планы на выходные" и текст на "Пойти в кино с друзьями". Результат: Заметка успешно отредактирована!

- Удаление заметки:
    - Пользователь удаляет заметку с ID 3. Результат: Заметка успешно удалена!