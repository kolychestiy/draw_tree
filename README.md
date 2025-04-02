# draw_tree
Рисует деревья (по мотивам дисциплины 4 курса формальные языки и методы трансляции)

Что нужно для работы:
1. файл main.py
2. файл tree.txt
3. папкка images (может иметь любое содержимое)
4. Но также потребуется установить саму программу Graphviz (не Python-библиотеку):

Windows: 

    Скачайте с официального [сайта](https://graphviz.org/download/) и добавьте в PATH.
    Распаковать и добавить в переменные PATH путь до папки bin (рекомендую распаковывать архив в program files)

Linux (Ubuntu/Debian):
    
    sudo apt-get install graphviz

MacOS (через Homebrew):

    brew install graphviz

5. Установить библиотеки для питона
    
    pip install anytree
    
    pip install graphviz

Запуск:

    В файле tree.txt описать свой дерево, как в примере
    выполнить команду python main.py
    
Результат: 

    fixed_size_tree.gif с анимацией построения дерева
    tree.png с простой рисовкой дерева

    В конце кода открывается гифа командой os.system("code fixed_size_tree.gif") (можно закоменить в main.py)

Код работает долго если строит gif, затрачивая много времени на построение каждого отдельного кадра.
Чтобы не строить заново fixed_size_tree.gif можно поменять флаг is_gif = False, тогда будет быстрее, потому что строит только tree.png
