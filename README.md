# draw_tree
Рисует деревья (по мотивам дисциплины 4 курса формальные языки и методы трансляции)

Что нужно для работы:
1. файл main.py
2. файл tree.txt
3. папкка images (может иметь любое содержимое)
4. возможно установить библиотеки для питона
    
    <!-- pip install graphviz       # Для визуализации графов/деревьев -->
    <!-- pip install pillow        # Для работы с изображениями (GIF) -->
    <!-- pip install imageio       # Альтернатива для создания GIF (опционально) -->
    <!-- pip install pydot         # Дополнительный интерфейс для graphviz -->
    <!-- pip install pygraphviz    # Еще один интерфейс для graphviz (если нужен) -->
    <!-- pip install fpdf          # Для создания PDF из кадров (в примере с PDF) -->
5. возможно установить библиотеку вне питона

Запуск:

    В файле tree.txt описать свой дерево, как в примере
    выполнить команду python main.py
    
Результат: 

    fixed_size_tree.gif с анимацией построения дерева
    tree.png с простой рисовкой дерева

    В конце кода открывается гифа командой os.system("code fixed_size_tree.gif") (можно закоменить в main.py)

Код работает долго если строит gif, затрачивая много времени на построение каждого отдельного кадра.
Чтобы не строить заново fixed_size_tree.gif можно поменять флаг is_gif = False, тогда будет быстрее, потому что строит только tree.png
