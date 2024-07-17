import math

def diag(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    return math.sqrt(a**2 + b**2 + c**2)

def volume(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    return (a * b * c)

def surface_area(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    return (2 * (a * b + a * c + b * c))

def alpha(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = diag(a, b, c)
    return math.acos(a/d)

def beta(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = diag(a, b, c)
    return math.acos(b/d)

def gamma(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = diag(a, b, c)
    return math.acos(c/d)

def radius_described_sphere(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = diag(a, b, c)
    return d/2

def volume_described_sphere(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    radius = radius_described_sphere(a, b, c)
    return 4/3 * (math.pi) * (radius**3)



from time import sleep

pict_list = ['MY FIRST SKRIPT\n\n',
              '    *********',
              '   *       **',
              '  *       * *',
              ' *********  *',
              ' *       *  *',
              ' *       *  *',
              ' *       * *',
              ' *********',
             '\n\nI LOVE PYTHON']
for i in pict_list:
  sleep(.4)
  print(i)

#Пункт Первый

import os
import json

# Получаем путь к текущей директории, где находится скрипт
current_dir = os.path.dirname(os.path.abspath(__file__))

# Определяем имя файла JSON
filename = 'parallelepipeds_iliadorr.json'

# Построение полного пути к файлу
file_path = os.path.join(current_dir, filename)

# Чтение и парсинг файла JSON
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print("Оригинальные данные:", data)
except FileNotFoundError:
    print(f"Файл {file_path} не найден.")




#Пункт второй
# Данные для новых файлов JSON
new_data1 = {}

for key, value in data.items():
        new_value = {
            "diag": str(diag(value["a"], value["b"], value["c"])),
            "volume": str(volume(value["a"], value["b"], value["c"])),
            "surface_area": str(surface_area(value["a"], value["b"], value["c"])),
            "alpha": str(alpha(value["a"], value["b"], value["c"])),
            "beta": str(beta(value["a"], value["b"], value["c"])),
            "gamma": str(gamma(value["a"], value["b"], value["c"])),
            "radius_described_sphere": str(radius_described_sphere(value["a"], value["b"], value["c"])),
            "volume_described_sphere": str(volume_described_sphere(value["a"], value["b"], value["c"])),
        }
        new_data1[key] = new_value

new_data2 = {}

sum_diag = 0
sum_volume = 0
sum_surface_area = 0
sum_alpha = 0
sum_beta = 0
sum_gamma = 0
sum_radius_described_sphere = 0
sum_volume_described_sphere = 0

for key, value in new_data1.items():
    sum_diag += float(value["diag"])
    sum_volume += float(value["volume"])
    sum_surface_area += float(value["surface_area"])
    sum_alpha += float(value["alpha"])
    sum_beta += float(value["beta"])
    sum_gamma += float(value["gamma"])
    sum_radius_described_sphere += float(value["radius_described_sphere"])
    sum_volume_described_sphere += float(value["volume_described_sphere"])

new_data2 = {
    "avg_diag": str(sum_diag/100),
    "avg_volume": str(sum_volume/100),
    "avg_surface_area": str(sum_surface_area/100),
    "avg_alpha": str(sum_alpha/100),
    "avg_beta": str(sum_beta/100),
    "avg_gamma": str(sum_gamma/100),
    "avg_radius_described_sphere": str(sum_radius_described_sphere/100),
    "avg_volume_described_sphere": str(sum_volume_described_sphere/100)
}

# Определение имен новых файлов
new_filename1 = 'characteristics_iliadorr.json'
new_filename2 = 'statistics_iliadorr.json'

# Построение полного пути к новым файлам
new_file_path1 = os.path.join(current_dir, new_filename1)
new_file_path2 = os.path.join(current_dir, new_filename2)

# Запись новых данных в файлы JSON
with open(new_file_path1, 'w', encoding='utf-8') as new_file1:
    json.dump(new_data1, new_file1, ensure_ascii=False, indent=4)

with open(new_file_path2, 'w', encoding='utf-8') as new_file2:
    json.dump(new_data2, new_file2, ensure_ascii=False, indent=4)

print(f"Новые файлы сохранены как {new_file_path1} и {new_file_path2}.")




#Пункт третий
    # Подсчет количества ключей в JSON объекте
figure_count = len(data)
print(f"Total number of figures: {figure_count}")



#Пункт четвертый
#В конце запринтит красиво полученные усредненные значения о которых пойдет речь далее.
print("The average of diagonals is: " + new_data2["avg_diag"])
print("The average of volumes is: " + new_data2["avg_volume"])
print("The average of surface areas is: " + new_data2["avg_surface_area"])
print("The average of alphas is: " + new_data2["avg_alpha"])
print("The average of betas is: " + new_data2["avg_beta"])
print("The average of gammas is: " + new_data2["avg_gamma"])
print("The average of radiuses is: " + new_data2["avg_radius_described_sphere"])
print("The average of volumes of spheres is: " + new_data2["avg_volume_described_sphere"])