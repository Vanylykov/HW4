import colorama
import inspect

colorama.init()

all_members = inspect.getmembers(colorama)

print("Усі атрибути та методи бібліотеки colorama:")
for name, obj in all_members:
    print(f"- {name}: {type(obj)}")

print("\nНайважливіші атрибути та методи на мою думку:")

important_members = [
    ('Fore', colorama.Fore, "Клас, що містить константи для кольорів тексту."),
    ('Back', colorama.Back, "Клас, що містить константи для кольорів фону."),
    ('Style', colorama.Style, "Клас, що містить константи для стилів тексту (жирний, тьмяний, тощо)."),
    ('init', colorama.init, "Функція для ініціалізації colorama. Необхідна для коректної роботи кольорів у Windows."),
    ('deinit', colorama.deinit, "Функція для деініціалізації colorama. Рекомендується викликати при завершенні роботи з кольорами."),
    ('reinit', colorama.reinit, "Функція для повторної ініціалізації colorama, якщо стандартні потоки були перенаправлені."),
    ('AnsiToWin32', colorama.AnsiToWin32, "Клас-обгортка для перетворення ANSI-escape-послідовностей у відповідні виклики Win32 API на Windows.")
]

for name, obj, doc in important_members:
    print(f"\n- {name}: {type(obj)}")
    print(f"  Опис: {doc}")
    if inspect.isclass(obj):
        class_members = inspect.getmembers(obj)
        color_attributes = [(n, o) for n, o in class_members if not n.startswith('__') and isinstance(o, str)]
        if color_attributes:
            print("  Константи кольорів:")
            for attr_name, attr_value in color_attributes:
                print(f"    - {attr_name}: '{attr_value}'")
    elif inspect.isfunction(obj):
        signature = inspect.signature(obj)
        print(f"  Сигнатура: {signature}")

colorama.deinit()