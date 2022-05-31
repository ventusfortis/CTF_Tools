
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"


def dec_to_base(dec, base):
    if dec < base:
        return ALPHABET[dec]
    else:
        return dec_to_base(dec // base, base) + ALPHABET[dec % base]

def numeric(source, from_, to, delimiter=" "):
    from_ = int(from_)
    to = int(to)
    source = source.split(delimiter)
    dec = list(map(lambda t: int(t,base=from_), source))
    max_digits = len(str(dec_to_base(max(dec), to)))
    result = " ".join(list(map(lambda t: dec_to_base(t,to).zfill(max_digits), dec)))
    return result

def rotx(source, x):
    plain_text = source.lower()
    number = int(x)
    text = "abcdefghijklmnopqrstuvwxyz"
    final = ""
    finalencrypted = ''
    rotation = text[number:] + text[:number]
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            final = rotation[text.index(plain_text[i])]
            finalencrypted += final
        else:
            finalencrypted += plain_text[i]
    return finalencrypted

def xor_str(data, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(data,key)])

def xor_num(data, key):
    return "".join([chr(ord(c1) ^ key) for c1 in data])

def from_hex(data, delimiter):
    return "".join(list(map(lambda _ : chr(int(_, 16)), data.split(delimiter))))

def to_hex(data, delimeter):
    return delimeter.join(list(map(lambda _: dec_to_base(_,16), list(map(lambda t : ord(t), data)))))

def add_line_numbers(data):
    data = data.split("\n")
    return "\n".join(list(map(lambda i: str(i) + " " + data[i], range(len(data)))))

def remove_line_numbers(data):
    data = data.split('\n')
    return "\n".join(list(map(lambda i: data[i][data[i].index(" ") + 1:], range(len(data)))))