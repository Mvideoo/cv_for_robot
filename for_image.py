from PIL import Image, ImageEnhance
import os
import random

# Функция для обрезки изображения с случайными значениями
def crop_image(image, output_path):
    width, height = image.size
    left = random.randint(0, width // 2)
    upper = random.randint(0, height // 2)
    right = random.randint(width // 2, width)
    lower = random.randint(height // 2, height)
    cropped = image.crop((left, upper, right, lower))
    cropped.save(output_path)

# Функция для изменения четкости изображения с случайными значениями
def enhance_image(image, output_path):
    factor = random.uniform(0.5, 2.0)
    enhancer = ImageEnhance.Sharpness(image)
    enhanced = enhancer.enhance(factor)
    enhanced.save(output_path)

# Функция для изменения яркости изображения с случайными значениями
def brightness_image(image, output_path):
    factor = random.uniform(0.5, 2.0)
    enhancer = ImageEnhance.Brightness(image)
    brightened = enhancer.enhance(factor)
    brightened.save(output_path)

# Функция для изменения положения изображения в пределах размеров с случайными значениями
def shift_image(image, output_path):
    width, height = image.size
    left = random.randint(0, width // 3)
    upper = random.randint(0, height // 3)
    right = random.randint(2 * width // 3, width)
    lower = random.randint(2 * height // 3, height)
    shifted = image.crop((left, upper, right, lower))
    shifted.save(output_path)

input_folder = "отенит"
output_folder = "output_folder"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)
    output_base_name = os.path.splitext(file_name)[0]

    image = Image.open(input_path)

    crop_image(image, os.path.join(output_folder, f"{output_base_name}_cropped.jpg"))
    enhance_image(image, os.path.join(output_folder, f"{output_base_name}_enhanced.jpg"))
    brightness_image(image, os.path.join(output_folder, f"{output_base_name}_brightened.jpg"))
    shift_image(image, os.path.join(output_folder, f"{output_base_name}_shifted.jpg"))