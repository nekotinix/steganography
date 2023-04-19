
from PIL import Image

def hide_file_in_image(image_path, file_path, bit_rate):
    # Открытие изображения и файла
    image = Image.open(image_path)
    file = open(file_path, 'rb').read()

    # Получение размеров изображения
    width, height = image.size

    # Проверка на достаточность места для встраивания файла
    if len(file) > (width * height * bit_rate // 8):
        raise ValueError("File is too large to be hidden in this image")

    # Конвертация файла в бинарный формат
    binary_file = ''.join(format(byte, '08b') for byte in file)

    # Встраивание файла в пиксели изображения
    pixels = image.load()
    index = 0
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            if index < len(binary_file):
                r &= ~(1 << (bit_rate - 1))
                r |= int(binary_file[index]) << (bit_rate - 1)
                index += 1
            if index < len(binary_file):
                g &= ~(1 << (bit_rate - 1))
                g |= int(binary_file[index]) << (bit_rate - 1)
                index += 1
            if index < len(binary_file):
                b &= ~(1 << (bit_rate - 1))
                b |= int(binary_file[index]) << (bit_rate - 1)
                index += 1
            pixels[i, j] = (r, g, b)

    # Сохранение измененного изображения
    image.save('image_with_file.png')
def reveal_file_from_image(image_path, bit_rate):
    # Открытие изображения
    image = Image.open(image_path)

    # Получение размеров изображения
    width, height = image.size

    # Извлечение файла из пикселей изображения
    binary_file = ''
    pixels = image.load()
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            binary_file += str(r >> (bit_rate - 1) & 1)
            binary_file += str(g >> (bit_rate - 1) & 1)
            binary_file += str(b >> (bit_rate - 1) & 1)

    # Конвертация бинарного файла в байты
    file_bytes = bytearray()
    for i in range(0, len(binary_file), 8):
        byte = binary_file[i:i+8]
        file_bytes.append(int(byte, 2))

    # Сохранение извлеченного файла
    open('extracted_file.txt', 'wb').write(file_bytes)
