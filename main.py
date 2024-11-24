import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Функції для шифрування та дешифрування
def caesar_encrypt(text, key, alphabet):
    """Шифрує текст шифром Цезаря"""
    result = ''
    for char in text:
        if char.upper() in alphabet:
            # Знаходимо індекс символу в алфавіті
            original_index = alphabet.index(char.upper())
            # Додаємо зміщення
            shifted_index = (original_index + key) % len(alphabet)
            # Отримуємо новий символ
            new_char = alphabet[shifted_index]
            # Зберігаємо регістр символу
            result += new_char if char.isupper() else new_char.lower()
        else:
            # Якщо символ не в алфавіті, залишаємо його без змін
            result += char
    return result

def caesar_decrypt(text, key, alphabet):
    """Розшифровує текст шифром Цезаря"""
    return caesar_encrypt(text, -key, alphabet)


# Функції для роботи з інтерфейсом
def get_selected_alphabet():
    """Отримує обраний алфавіт для шифрування/дешифрування."""
    selected_alphabet = alphabet_choice.get()
    if selected_alphabet == "Англійський":
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:  # Український
        return 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'


def encrypt_text():
    try:
        key = int(entry_key.get())
        text = text_area.get("1.0", tk.END).strip()
        alphabet = get_selected_alphabet()
        encrypted_text = caesar_encrypt(text, key, alphabet)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Помилка", "Ключ повинен бути цілим числом!")

def decrypt_text():
    try:
        key = int(entry_key.get())
        text = text_area.get("1.0", tk.END).strip()
        alphabet = get_selected_alphabet()
        decrypted_text = caesar_decrypt(text, key, alphabet)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Помилка", "Ключ повинен бути цілим числом!")



def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text_area.get("1.0", tk.END).strip())

def print_file():
    content = text_area.get("1.0", tk.END).strip()
    print(content)

def show_info():
    info_text = (
        "Шифр Цезаря - це один з найдавніших шифрів, названий на честь Гая Юлія Цезаря.\n"
        "При шифруванні кожен символ зміщується на фіксовану кількість позицій в алфавіті.\n\n"
        "Розробник: Кривоконь Агата\n"
        "E-mail: agathakrivokon@gmail.com\n"
        "Дата: 2024\n"
    )
    messagebox.showinfo("Про програму", info_text)

def exit_program():
    root.destroy()

# Створення графічного інтерфейсу
root = tk.Tk()
root.title("Шифр Цезаря")

# Вибір алфавіту
frame_alphabet = tk.Frame(root)
frame_alphabet.pack(pady=10)

tk.Label(frame_alphabet, text="Алфавіт:", font=("Arial", 14)).pack(side=tk.LEFT)
alphabet_choice = tk.StringVar(value="Український")
tk.OptionMenu(frame_alphabet, alphabet_choice, "Український", "Англійський").pack(side=tk.LEFT, padx=5)

# Рамка для ключа
frame_key = tk.Frame(root)
frame_key.pack(pady=10)

tk.Label(frame_key, text="Ключ:", font=("Arial", 14)).pack(side=tk.LEFT)
entry_key = tk.Entry(frame_key, width=10, font=("Arial", 14))
entry_key.pack(side=tk.LEFT, padx=5)

# Панель інструментів: перший ряд кнопок
frame_buttons_top = tk.Frame(root)
frame_buttons_top.pack(pady=5)

tk.Button(frame_buttons_top, text="Шифрувати", command=encrypt_text, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons_top, text="Дешифрувати", command=decrypt_text, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons_top, text="Відкрити файл", command=open_file, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)

# Панель інструментів: другий ряд кнопок
frame_buttons_bottom = tk.Frame(root)
frame_buttons_bottom.pack(pady=5)

tk.Button(frame_buttons_bottom, text="Зберегти файл", command=save_file, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons_bottom, text="Друкувати", command=print_file, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons_bottom, text="Інформація", command=show_info, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons_bottom, text="Вихід", command=exit_program, font=("Arial", 14), width=15).pack(side=tk.LEFT, padx=5)

# Текстова область
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Arial", 14))
text_area.pack(padx=10, pady=10)

if __name__ == "__main__":
    root.mainloop()
