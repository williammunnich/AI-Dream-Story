#everything outside of the function is an example and for testing
#this function takes text input and wraps it inside of a precreated rectangle
#credit Rabbid76 https://stackoverflow.com/questions/64273966/python-pygame-make-text-in-pygame-wrap-when-in-leaves-the-window
textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3
"""
import pygame

pygame.init()
font = pygame.font.SysFont(None, 15)

msg = "Simple function that will draw text and wrap it to fit the rect passed.  If there is any text that will not fit into the box, the remaining text will be returned."
textRect = pygame.Rect(100, 100, 300, 300)

window = pygame.display.set_mode((500, 500))
run = True
"""
#surface is the original scrren variable
#text is the content of the message

def drawText(surface, text, color, rect, font, align=textAlignLeft, aa=False, bkg=None):
    lineSpacing = -2
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = text.split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList: image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, aa, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for image in imageList:
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for lineLen, lineImages in zip(lineLenList, lineList):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages)-1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages)-1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages)-1)
        if lineBottom + fontHeight > rect[1] + rect[3]:
            break
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + i*spaceWidth, lineBottom
            surface.blit(image, (round(x), y))
            lineLeft += image.get_width() 
        lineBottom += fontHeight + lineSpacing

    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]: remainingText += text + " "
        return remainingText
    return ""

"""
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 0), textRect, 1)
    drawTextRect = textRect.inflate(-5, -5)
    drawText(window, msg, (0, 0, 0), drawTextRect, font, textAlignBlock, True)
    pygame.display.flip()
"""