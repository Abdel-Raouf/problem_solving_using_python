direction = str(input()).lower()
mole_wrong_seq = list(input().lower())
wrong_seq_leng = len(mole_wrong_seq)

special_aplhabet = "qwertyuiopasdfghjkl;zxcvbnm,./"

str_concant = ""

for i in range(wrong_seq_leng):
    if direction == "r":
        if mole_wrong_seq[i] == "q":
            str_concant += "q"
        else:
            right_letter_index = special_aplhabet.find(mole_wrong_seq[i])
            right_letter = special_aplhabet[right_letter_index - 1]
            str_concant += right_letter
    else:
        if mole_wrong_seq[i] == "/":
            str_concant += "/"
        else:
            right_letter_index = special_aplhabet.find(mole_wrong_seq[i])
            right_letter = special_aplhabet[right_letter_index + 1]
            str_concant += right_letter

print(str_concant)
