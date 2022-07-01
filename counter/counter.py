from collections import Counter

text = 'Aqui está o meu texto, vamos ver o que acontece.'
counter = Counter(text)

if __name__ == '__main__':
    print(counter)

    print('=' * 30)

    print('Mais comum: ', counter.most_common(5))

    print('=' * 30)

    total_de_caracteres = 0
    for value in counter.values():
        total_de_caracteres += value

    print('Counter Total: ', counter.total())

    print('=' * 30)

    print('MyTotal: ', total_de_caracteres)
