from pygame import font
'''
Klasse um Text auszugeben
'''
class TextRenderer:
    font.init
    def render_text(textString, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(textString, 0, textColor)

        return newText


    def render_text_aa(textString, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(textString, 1, textColor)

        return newText