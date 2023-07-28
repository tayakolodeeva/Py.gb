"""
1.Решить задачи, которые не успели решить на семинаре.

7.Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os

FILE_CATEGORIES = {
    'video': ['mov', 'mpeg', 'mpg', 'mp4', 'avi', 'mkv'],
    'image': ['jpg', 'jpeg', 'gif', 'png'],
    'text': ['txt', 'rtf']
}


def sort_files_to_dirs(files_dir: str, ext_categories: dict[str:list[str]]):
    for file in filter(lambda item: os.path.isfile(os.path.join(files_dir, item)), os.listdir(files_dir)):
        extension = file.split('.')[-1]
        for category, ext_list in ext_categories.items():
            if extension in ext_list:
                new_cat_dir = os.path.join(files_dir, category)
                make_dir(new_cat_dir)
                os.replace(os.path.join(files_dir, file), os.path.join(os.getcwd(), new_cat_dir, file))
                break


def make_dir(files_dir) -> None:
    if not os.path.exists(files_dir):
        os.mkdir(files_dir)


sort_files_to_dirs('sem_06_dir', FILE_CATEGORIES)