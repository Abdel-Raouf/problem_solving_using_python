word_str = input().lower()
vowels = 'aoyeui'
final_str = ''

for letter in word_str:
    if letter in vowels:
        continue
    else:
        final_str += '.' + letter


print(final_str)
