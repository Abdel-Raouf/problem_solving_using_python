no_of_lines, color_no = map(int, input().split(" "))
colored_pixels = ['C', 'M', 'Y']
color_state = ''


for i in range(no_of_lines):
    if color_state == "#Color":
        break
    else:
        colors_in_photo = list(map(str, input().split(" ")))
        for j in range(color_no):
            if colors_in_photo[j] == colored_pixels[0] or colors_in_photo[j] == colored_pixels[1] or colors_in_photo[j] == colored_pixels[2]:
                color_state = "#Color"
                break
            else:
                continue

if len(color_state) == 0:
    print('#Black&White')
else:
    print(color_state)

#  Another solution
# we may concate all pohot colors to a string and search in it using (in)
# for "C", "M", "Y" instead of using another loop, but the above solution
# is more on the side of clean & clear code
