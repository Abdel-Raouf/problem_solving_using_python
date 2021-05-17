remix = str(input())

if remix.count('WUB') >= 1:
    # Replace every occurence of 'WUB' with space
    original_song = remix.replace('WUB', ' ')
    # split with space and reomve duplicated sapces, then join the string
    print(" ".join(original_song.split()))
else:
    print(remix)
