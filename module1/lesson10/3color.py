import random 
def find_colour(colours):
    list_of_colours = []
    for colour in colours:
        if colour['r'] > colour['g'] and colour['r'] > colour['b']:
            list_of_colours.append('red')
        elif colour['g'] > colour['r'] and colour['g'] > colour['b']:
            list_of_colours.append('green')
        elif colour['b'] > colour['r'] and colour['b'] > colour['g']:
            list_of_colours.append('blue')
    return list_of_colours
bitmap =[{'r':random.randint(0,255),'g':random.randint(0,255),'b':random.randint(0,255)} for i in range(20000)]
print(find_colour(bitmap))