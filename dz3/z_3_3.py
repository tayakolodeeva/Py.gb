"""
3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.
"""
FREQUENT_QTY = 10
PUNCTUATION = '''.,;:!?#@%&*+=\\/()[]{}<>-—«»'"'''
some_text = '''Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.
Python is dynamically typed and garbage-collected.
It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. 
It is often described as a "batteries included" language due to its comprehensive standard library.
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. 
Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, 
released in 2020, was the last release of Python 2.
Python consistently ranks as one of the most popular programming languages.Python users are colloquially called pythonistas.
'''
pretty_text = some_text.lower()
for symbol in PUNCTUATION:
    pretty_text = pretty_text.replace(symbol, ' ')

words = pretty_text.split()
words_qty = {word: words.count(word) for word in words}
words_sorted = sorted(words_qty, key=words_qty.get, reverse=True)

frequent_words = {}
for word in words_sorted[:min(FREQUENT_QTY, len(words_qty))]:
    frequent_words[word] = words_qty[word]
print(f'{FREQUENT_QTY} cамых частых слов:\n{frequent_words}')