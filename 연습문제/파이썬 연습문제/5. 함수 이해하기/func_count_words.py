def count_words(sentence):
    result = sentence.split()
    return len(result)

print(f"단어 수: {count_words("문자열을 인자로 받아 단어 수를")}")