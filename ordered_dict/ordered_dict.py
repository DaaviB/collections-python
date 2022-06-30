from collections import OrderedDict

if __name__ == '__main__':
    ord_dict= OrderedDict()

    for k in range(10):
            ord_dict.update({k+3:(k+2)})


    for pair in ord_dict.items():
        print(pair)

    ord_dict.move_to_end(4)

    print(ord_dict)
    ord_dict.clear()
    print(ord_dict)
