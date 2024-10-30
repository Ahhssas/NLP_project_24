# Веб-корпус текстов форума woman.ru
Проект выполняли студенты 3 курса ФиКЛ, НИУ ВШЭ: 

- Варвара Ермолина - морфологический анализ, функция поиска
- Владислава Термус - создание сайта и объединение всех составляющих
- Мария Селифанова - парсинг данных, морфологический анализ
- Александра Погожева - обработка данных, функция поиска

## ТУТ ССЫЛКА НА САЙТ
Веб-приложение написано на Flask с использованием фреймворка Bootstrap

## Сбор данных

Мы спарсили сообщения людей в различных тредах на форуме [woman.ru](https://www.woman.ru/forum/). Выбрали тред ["предсказания по ТАРО"](https://www.woman.ru/relations/men/thread/3813429/), содержащий 122k ответов. Из них мы взяли только 700 и разделили их на отдельный предложения. Так, у нас получился корпус объемом ~19k токенов.

**Файлы:**

- `raw_texts.txt` - с "очищенными" предложениями
- `annotated_text.txt` - с аннотированными предложениями
- `parsing.ipynb` – тетрадка с кодом для парсинга ответов пользователей

## Аннотация данных в нашем корпусе

В качестве Pos-теггера был взят Mystem – свободно распространяемый морфологический анализатор для русского языка с закрытым исходным кодом.

Каждому слову в корпусе соответствует аннотация следующего вида: lemma+pos, где lemma – лемма, pos – часть речи

*Пример:*
```
Предложение: Не искушайте больше судьбу, удачи Вам!

Аннотация: не+PART искушать+V больше+ADV судьба+S удача+S вы+SPRO
```
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

## Вывод предложений

На сайте списком выводятся предложения, соответствующие запросу. Метаданные не выводятся, так как все предложения были взяты из одного треда.
