from cmath import exp, pi


def dft(s_lst):
    _n = len(s_lst)
    for k in range(_n):
        xk = 0
        for s in s_lst:
            xk += s * exp(-1j * 2*pi * k * s_lst.index(s) / _n)
        print("X{} = {}".format(k, xk))
    print('Note: cmath library writes complex numbers in "a+bj" form.')


def in_operate():
    i_lst = input('Please enter your samples (split by "," | complex numbers in "a+bi" format):\n').split(",")
    sample_lst = list()
    for i in i_lst:
        if "i" in i:
            # Make sure the imaginary part of a complex number has an integer.
            if i.index("i") == 0 or (not i[i.index("i") - 1].isdigit()):
                # Replace the idiomatic imaginary unit "i" with the "j" recognized by the cmath library.
                sample_lst.append(complex(i.replace(" ", "").replace("i", "1j")))
        else:
            sample_lst.append(int(i.replace(" ", "")))
    return sample_lst


if __name__ == '__main__':
    # [0, 0, 2, 3, 4, 0, 0, 0]
    # [1, i, -1, -i, 1, i, -1, -i]
    # [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]

    dft(in_operate())


