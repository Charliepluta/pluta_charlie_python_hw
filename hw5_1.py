def count_letters_digits (sentence):
    letters = sum(c.isalpha() for c in sentence)
    digits = sum(c.isdigit() for c in sentence)
    return f"LETTERS {letters}\nDIGITS {digits}"

input_sentence = "hello world! 123"
print(count_letters_digits(input_sentence))
