def hello_name(name):
    return f"Hello {name}!"

def make_abba(a, b):
    return a + b + b + a

def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"

def make_out_word(out, word):
    return out[:2] + word + out[2:]

def extra_end(string):
    return string[-2:] * 3

def first_two(string):
    return string[:2]

def first_half(string):
    return string[:len(string) // 2]

def without_end(string):
    return string[1:-1]

def combo_string(a, b):
    short, long = (a, b) if len(a) < len(b) else (b, a)
    return short + long + short

def left2(string):
    return string[2:] + string[:2]


print(hello_name('Bob'))           # → 'Hello Bob!'
print(hello_name('Alice'))         # → 'Hello Alice!'
print(hello_name('X'))             # → 'Hello X!'

print(make_abba('Hi', 'Bye'))      # → 'HiByeByeHi'
print(make_abba('Yo', 'Alice'))    # → 'YoAliceAliceYo'
print(make_abba('What', 'Up'))     # → 'WhatUpUpWhat'

print(make_tags('i', 'Yay'))       # → '<i>Yay</i>'
print(make_tags('i', 'Hello'))     # → '<i>Hello</i>'
print(make_tags('cite', 'Yay'))    # → '<cite>Yay</cite>'

print(make_out_word('<<>>', 'Yay'))   # → '<<Yay>>'
print(make_out_word('<<>>', 'WooHoo')) # → '<<WooHoo>>'
print(make_out_word('[[]]', 'word'))  # → '[[word]]'

print(extra_end('Hello'))          # → 'lololo'
print(extra_end('ab'))             # → 'ababab'
print(extra_end('Hi'))             # → 'HiHiHi'

print(first_two('Hello'))          # → 'He'
print(first_two('abcdefg'))        # → 'ab'
print(first_two('ab'))             # → 'ab'

print(first_half('WooHoo'))        # → 'Woo'
print(first_half('HelloThere'))    # → 'Hello'
print(first_half('abcdef'))        # → 'abc'

print(without_end('Hello'))        # → 'ell'
print(without_end('java'))         # → 'av'
print(without_end('coding'))       # → 'odin'

print(combo_string('Hello', 'hi')) # → 'hiHellohi'
print(combo_string('hi', 'Hello')) # → 'hiHellohi'
print(combo_string('aaa', 'b'))    # → 'baaab'

print(left2('Hello'))              # → 'lloHe'
print(left2('java'))               # → 'vaja'
print(left2('Hi'))                 # → 'Hi'
