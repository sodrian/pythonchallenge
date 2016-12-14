#!/usr/bin/env python

URL = 'http://www.pythonchallenge.com/pc/return/bull.html'


def _look_and_say_sequence(n):
    seq_el = 1

    for i in xrange(1, n):
        l = list()
        for cur_digit in str(seq_el):
            cur_digit = int(cur_digit)
            try:
                prev_lst_el = l.pop()
            except IndexError:
                prev_lst_el = [0, 0]

            if prev_lst_el[0] != cur_digit:
                if prev_lst_el[0]:
                    l.append(prev_lst_el)
                l.append([cur_digit, 1])
            elif prev_lst_el[0] == cur_digit:
                prev_lst_el[1] += 1
                l.append(prev_lst_el)

        # print('{0} -> {1}\n\n'.format(seq_el, l))

        r = ''
        for el in l:
            r += '{0}{1}'.format(el[1], el[0])
        seq_el = int(r)

    return seq_el


if __name__ == '__main__':
    for i in xrange(1, 32):
        print('{0} -> {1}'.format(i, len(str(_look_and_say_sequence(i)))))