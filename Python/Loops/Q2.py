color_list_1 = set(["White", "Black", "Red"])

color_list_2 = set(["Red", "Green"])
answer = set({})
for color in color_list_1:
    if color in color_list_2:
        pass
    else:
        answer.add(color)
print(answer)