from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import os
from PIL import Image

def space_num(n):
    s = ""
    for i in range(6):
        s += "\u00A0" if n % 2 else "\u202F"
        n >>= 1
    return s

frames = []
def parse_tree_from_file(filename, build_gif):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    root = None
    stack = []  # Стек для отслеживания текущего уровня вложенности

    i = -1
    for line in lines:
        i += 1
        line = line.rstrip()  # Удаляем переносы строк
        if not line:
            continue  # Пропускаем пустые строки

        # Определяем уровень вложенности по отступам
        indent_level = len(line) - len(line.lstrip())
        name = ""
        name += space_num(i) + "\n"
        name += line.strip()
        # name += "\n" + space_num(i)

        # Создаём новый узел
        node = Node(name)

        if indent_level == 0:
            # Корневой узел
            root = node
            stack = [(indent_level, node)]
        else:
            # Ищем родителя в стеке
            while stack and stack[-1][0] >= indent_level:
                stack.pop()

            if stack:
                parent = stack[-1][1]
                node.parent = parent
                stack.append((indent_level, node))
            else:
                raise ValueError("Некорректный отступ в файле")

        if build_gif:
            draw_clean_tree(root, f"images/tree_step_{i}.png")
            frames.append(Image.open(f'images/tree_step_{i}.png'))

    if build_gif:
        draw_clean_tree(root, f"images/tree_step_{i + 1}.png")
        z = Image.open(f'images/tree_step_{i + 1}.png')
        for _ in range(4):
            frames.append(z)
    return root


def draw_clean_tree(root, file_name):
    DotExporter(
        root,
        options=[
            # "rankdir=LR",
            # "newrank=true",
            # "splines=ortho",      # Прямые соединительные линии
            # "concentrate=false",  # Отключает объединение линий
            # "pad=0.5",  # Отступ от границ изображения
        ],
        nodeattrfunc=lambda node: (
            f"fontcolor=black; shape=none"
            if not node.is_leaf else
            f"fontcolor=blue; shape=none"
        ),
    ).to_dotfile("tree.dot")

    os.system(f"dot -Tpng tree.dot -o {file_name}")


# Пример использования
if __name__ == "__main__":
    # Теперь парсим файл
    is_gif = True
    root = parse_tree_from_file("tree.txt", is_gif)

    if is_gif:
        # Находим максимальные размеры
        max_width = max(img.width for img in frames)
        max_height = max(img.height for img in frames)

        # Ресайзим все кадры под один размер
        resized_frames = []
        for img in frames:
            new_img = Image.new('RGB', (max_width, max_height), (255, 255, 255))
            new_img.paste(img, ((max_width - img.width) // 2, 
                            (max_height - img.height) // 2))
            resized_frames.append(new_img)

        # Сохраняем GIF
        resized_frames[0].save(
            'fixed_size_tree.gif',
            save_all=True,
            append_images=resized_frames[1:],
            duration=700,
            loop=0,
            quality=100
        )

        # Очистка
        # for i in range(len(frames)):
        #     os.remove(f'images/tree_step_{i}.png')

    # Выводим результат
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")

    draw_clean_tree(root, "tree.png")
    os.system("code fixed_size_tree.gif")
