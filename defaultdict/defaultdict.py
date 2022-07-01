from collections import defaultdict

default = defaultdict(list)


if __name__ == '__main__':
    default['lista']

    https_v = ['get', 'post', 'put', \
        'patch', 'delete', 'head', 'options']
    for v in https_v:
        default['Minha_lista'].append(v)

    print(default)
