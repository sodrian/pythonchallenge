def shift_the_string(s):
    ret = ''
    for letter in s:
        if ord(letter) in range(97, 97+26):
            pos = (ord(letter) - 97 + 2) % 26 + 97
            letter = chr(pos)
        ret += letter
    return ret

print(shift_the_string(
    '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
    bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
    sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''))
print(shift_the_string('map'))