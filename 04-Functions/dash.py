def f(text):
    new_text = ''
    for i in text:
        if text.endswith(i):
            new_text = new_text + i
        else:
            new_text = new_text + i + '-'
    return new_text

print(f("University"))