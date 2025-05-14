def count_words(text):
    words = text.split()
    count = len(words)
    return count

def count_chars(text):
    letter_count = {}
    for char in text.lower():
        if char in letter_count:
           letter_count[char] += 1
        else:
           letter_count[char] = 1
    return letter_count

def sorted_chars(letter_count):
    char_report = []
    for char, count in letter_count.items():
        if char.isalpha():
            char_report.append({'char':char, 'num':count})
    char_report.sort(key=lambda d: d['num'], reverse=True)
    return char_report
