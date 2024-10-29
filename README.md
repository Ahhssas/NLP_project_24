# Веб-корпус текстов форума woman.ru
Проект выполняли студенты 3 курса ФиКЛ, НИУ ВШЭ: Варвара Ермолина, Владислава Термус, Мария Селифанова, Александра Погожева

В качестве Pos-теггера был взят Mystem

## Сбор данных

Мы спарсили сообщения людей в различных тредах на форуме [woman.ru](https://www.woman.ru/forum/). Выбрали тред "предсказания по ТАРО". Выделили отдельные предложения для корпуса. 

**Файлы:**

- `raw_texts.txt` - с "очищенными" предложениями
- `annotated_text.txt` - с аннотированными предложениями

## Аннотация данных в нашем корпусе

Каждому слову в корпусе соответствует аннотация следующего вида: lemma+pos, где lemma – лемма, pos – часть речи

*Пример:*

Предложение: Не искушайте больше судьбу, удачи Вам!

Аннотация: не+PART искушать+V больше+ADV судьба+S удача+S вы+SPRO

**Список частей речи, размеченных в корпусе:**

| Обозначение | Часть речи |
| ------------- | ------------- |
| A  | прилагательное|
| ADV  | наречие  |
| ADVPRO  | местоименное наречие  |
| ANUM  | числительное-прилагательное  |
| APRO  | местоимение-прилагательное  |
| COM  | часть композита - сложного слова  |
| CONJ  | союз  |
| INTJ  | междометие  |
| NUM  | числительное  |
| PART  | частица  |
| PR  | предлог  |
| S  | существительное  |
| SPRO  | местоимение-существительное  |
| V  | глагол  |
| PARTCP  | причастие  |
| GER  | деепричастие  |

## Функционал поиска

- дом – поиск по лемме (без кавычек всегда вводится лемма)
- "дом" – поиск по словоформе
- дом+NOUN - поиск по лемме, принадлежащей к определенной части речи
- ADV – поиск по части речи
- S ADV V – поиск последовательности 
