"""
2.Напишите функцию группового переименования файлов. Она должна:
3.принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
4.принимать параметр количество цифр в порядковом номере.
5.принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
6.принимать параметр расширение конечного файла.
7.принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 
"""

import os

__all__ = ['rename_files']


def rename_files(files_dir: str, num_digits: int, source_ext: str, target_ext: str,
                 source_name_start: int, source_name_end: int, new_file_name: str = '') -> None:
    filtered_files = filter(lambda file: file.split('.')[-1] == source_ext, os.listdir(files_dir))
    for i, file_name in enumerate(filtered_files):
        file_number = ''.join('0' for _ in range(num_digits - len(str(i + 1)))) + str(i + 1)
        old_name = ''.join(file_name.split('.')[:-1])
        new_name = f'{old_name[source_name_start + 1:source_name_end + 1]}{new_file_name}{file_number}.{target_ext}'
        os.rename(os.path.join(files_dir, file_name), os.path.join(files_dir, new_name))


if __name__ == '__main__':
    rename_files('../PY.O.DZ.GB/sem_06_dir', 3, 'jpeg', 'jpg', 2, 5, 'image')

