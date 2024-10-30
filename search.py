import re
from pymystem3 import Mystem

m_stem = Mystem()


def annotating(texts):
    """
    params: list of raw sentences
    ---\
    returns: list of annotated sentences
    """
    annotated = []
    pos_list = ["–"]

    for sent in texts:
        annotation = []
        ana = m_stem.analyze(sent)

        for an in ana:
            if 'analysis' in an and an['analysis'] != []:
                gr = an['analysis'][0]['gr']
                pos = gr.split('=')[0].split(',')[0]
                if pos == 'V':
                    if 'прич' in gr.split('=')[1]:
                        pos = 'PARTCP'
                    elif 'деепр' in gr.split('=')[1]:
                        pos = 'GER'

                lemma = an['analysis'][0]['lex']
                annotation.append(f'{lemma}+{pos}')
                if pos not in pos_list:
                    pos_list.append(pos)
            elif 'analysis' not in an:
                pass
            else:
                # for unknown words put token '-'
                annotation.append('–')
        annotated.append(' '.join(annotation))
    return annotated, pos_list


def prepare_query(query):

    ideal_query = []
    to_remember = []
    for token in query.split():
        if '+' in token or token.isupper():
            ideal_query.append(token.split())
        else:
            if '"' in token:
                to_remember.append(token.strip('"'))
            ideal_query.append(annotating([token.strip('"')])[0])

    return ideal_query, to_remember


def matches_token(sent_token, ideal_token):
    if ideal_token[0].isupper():
        return sent_token.endswith(f'+{ideal_token[0]}')
    return sent_token == ideal_token[0]


def search_func(query):
    ideal_query, to_remember = prepare_query(query)
    len_q = len(ideal_query)
    result = []

    with open('annotated_text.txt', 'r', encoding='utf-8') as file:
        texts = file.read().splitlines()

    with open('raw_text.txt', 'r', encoding='utf-8') as file:
        raw_texts = file.read().splitlines()

    for i, sent in enumerate(texts):
        if all(item in raw_texts[i] for item in to_remember):
            first = ideal_query[0][0]
            indexes = [ind for ind, val in enumerate(sent.split()) if val == first or val.endswith(first)]

            for element in indexes:
                if element + len_q > len(sent.split()):
                    continue

                sent_to_check = sent.split()[element:element + len_q]
                if all(matches_token(sent_to_check[num], ideal_query[num]) for num in range(len_q)):
                    result.append(raw_texts[i])
                    break

    return result


def check(query):
    if len(query) == 0:
        return "Неверный ввод: пустая строка"
    elif not re.fullmatch(r'[а-яA-Zё\s"+]+', query):
        return "Неверный ввод: запрещённые символы"
    return 1
