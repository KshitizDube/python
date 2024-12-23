color = ["red","blue","green","yellow","purple","white"]
second_color =["blue","purple","green","pink","black"]
colorss = []
for colors in color:
    if colors not in second_color:
        colorss.append(colors)
print(colorss)