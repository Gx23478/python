import os

def xor_with_key(block, key):
    """Применение XOR к блоку с ключом."""
    return bytes([block[i] ^ key[i % len(key)] for i in range(len(block))])

def encrypt_decrypt_file(input_file, output_file, key):
    """Шифрование и дешифрование файла."""
    block_size = len(key)  # Размер блока равен размеру ключа

    with open(input_file, 'rb') as f_in:  # Чтение в бинарном режиме
        byte_content = f_in.read()  # Читаем весь файл как байты

    with open(output_file, 'wb') as f_out:
        for i in range(0, len(byte_content), block_size):
            block = byte_content[i:i + block_size]  # Получаем блок
            # Шифруем/дешифруем блок
            encrypted_block = xor_with_key(block, key)
            f_out.write(encrypted_block)  # Записываем зашифрованный/расшифрованный блок

def main():
    input_file = 'input.txt'  # Исходный файл
    encrypted_file = 'encrypted.bin'  # Файл для зашифрованных данных (бинарный)
    decrypted_file = 'decrypted.txt'  # Файл для расшифрованных данных
    key = b'secretkey'  # Ключ для шифрования (байтовая строка)

    # Шифрование
    encrypt_decrypt_file(input_file, encrypted_file, key)
    print(f"Файл '{input_file}' зашифрован в '{encrypted_file}'.")

    # Дешифрование
    encrypt_decrypt_file(encrypted_file, decrypted_file, key)
    print(f"Файл '{encrypted_file}' расшифрован в '{decrypted_file}'.")

    # Проверка совпадения файлов
    with open(input_file, 'rb') as original_file:
        original_content = original_file.read()

    with open(decrypted_file, 'rb') as decrypted_file:
        decrypted_content = decrypted_file.read()

    if original_content == decrypted_content:
        print("Файлы совпадают!")
    else:
        print("Файлы не совпадают.")
        print(f"Размер оригинального файла: {len(original_content)}")
        print(f"Размер расшифрованного файла: {len(decrypted_content)}")
        print("Различия в содержимом:")
        for i in range(min(len(original_content), len(decrypted_content))):
            if original_content[i] != decrypted_content[i]:
                print(f"Различие в байте {i}: оригинал {original_content[i]}, расшифрованное {decrypted_content[i]}")
        if len(original_content) != len(decrypted_content):
            print("Файлы имеют разный размер!")

if __name__ == '__main__':
    main()

