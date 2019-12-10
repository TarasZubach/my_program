import re
from statistics import median


def main():

    with open('task1.txt') as file:
        text = file.read()

    # Medians
    list_with_text = re.split(r'[.?!]', text.replace('\n', ''))
    list_with_text = list(filter(lambda x : x != '', list_with_text))

    median_words = median([len(word.split()) for word in list_with_text])

    list_words = ' '.join(list_with_text).split(' ')
    for word in list_words:
        if word == '':
            list_words.remove(word)

    new_spl = []
    for word in ' '.join(list_words).split('.'):
        if word.startswith(' '):
            new_spl.append(word[1:])
        else:
            new_spl.append(word)
    new_spl = ''.join(new_spl).split(' ')

    count_words = len(new_spl) / len(list_with_text)

    dict_words = {word: list_words.count(word) for word in list_words}

    num_tuple = ('2', '3', '4')
    for words, count in dict_words.items():
        if str(count)[-1] in num_tuple:
            print('Слово - {} повторяется: {} разa'.format(words, count))
        else:
            print('Слово - {} повторяется: {} раз'.format(words, count))

    if list_words:
        print('Среднее количество слов в предложении: {:0.2f}'.format(float(count_words)))

    print('Медианное количество слов в предложение: {}'.format(median_words))


if __name__ == '__main__':
    main()