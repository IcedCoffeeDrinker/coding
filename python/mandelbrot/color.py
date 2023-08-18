# linear to rgb converter py Philipp himself

def color(number,max,output):

    colorChanger = False
    # output = "hex" # "hex" or "255"
    color = []

    stage1 = max/5
    stage2 = stage1*2
    stage3 = stage1*3
    stage4 = stage1*4
    stage5 = max

    if colorChanger == True:
        if number == 0:
            color = "#480CA8"
            return color
        elif number == 1:
            color = "#560BAD"
            return color
        elif number == 2:
            color = "#7209B7"
            return color

    if number <= stage1:
        rgbNumber = 255/stage1*number

        color = [255,rgbNumber,0]

    elif number <= stage2:
        rgbNumber = number-stage1
        rgbNumber = 255/stage1*rgbNumber

        r = 255-rgbNumber
        color = [r,255,0]

    elif number <= stage3:
        rgbNumber = number-stage2
        rgbNumber = 255/stage1*rgbNumber

        color = [0,255,rgbNumber]

    elif number <= stage4:
        rgbNumber = number-stage3
        rgbNumber = 255/stage1*rgbNumber

        g = 255-rgbNumber
        color = [0,g,255]

    elif number <= stage5:
        rgbNumber = number-stage4
        rgbNumber = 255/stage1*rgbNumber

        b = 255-rgbNumber
        color = [rgbNumber,0,b]

    else:
        print("color error (no color found)")
        color = [255,255,255]

    if output == "hex":
        color = '#%02x%02x%02x' % (int(color[0]), int(color[1]), int(color[2]))

    return color
