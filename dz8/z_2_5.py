"""
2.Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
3.Для дочерних объектов указывайте родительскую директорию.
4.Для каждого объекта укажите файл это или директория.
5.Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий. 
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
"""
import os
import json
import csv
import pickle

__all__ = ['get_dir_info', 'save_dir_info']


def get_dir_info(dir_path: str = '.') -> list[dict]:
    dir_info: list[dict] = []

    for dir_item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, dir_item)
        item_info = {
            'name': dir_item,
            'parent_dir': os.path.abspath(dir_path).split('/')[-1],
        }

        if os.path.isfile(item_path):
            item_info['type'] = 'file'
            item_info['size'] = os.path.getsize(item_path)

        if os.path.isdir(item_path):
            dir_children = get_dir_info(item_path)
            item_info['type'] = 'directory'
            item_info['size'] = sum([child['size'] for child in dir_children])
            item_info['children'] = dir_children

        dir_info.append(item_info)

    return dir_info


def save_dir_info(dir_path: str = '.', json_path: str = '', csv_path: str = '', pickle_path: str = '', ) -> None:
    dir_info = get_dir_info(dir_path)

    if json_path:
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(dir_info, json_file, indent=2, ensure_ascii=False)

    if csv_path:
        with open(csv_path, 'w', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=['name', 'parent_dir', 'type', 'size'],
                                        dialect='excel', quoting=csv.QUOTE_NONNUMERIC, restval='null')
            csv_writer.writeheader()
            for row in tree2rows(dir_info):
                csv_writer.writerow(row)

    if pickle_path:
        with open(pickle_path, 'wb') as pickle_file:
            pickle.dump(dir_info, pickle_file)


def tree2rows(dict_tree: list[dict]) -> list[dict[str, str | int]]:
    rows = []
    for item in dict_tree:
        if 'children' in item.keys():
            dir_item = item.copy()
            dir_children = dir_item.pop('children')
            rows.append(dir_item)
            rows.extend(tree2rows(dir_children))
        else:
            rows.append(item)
    return rows


if __name__ == '__main__':
    save_dir_info('..', json_path='dir_info.json', csv_path='dir_info.csv', pickle_path='dir_info.pickle')