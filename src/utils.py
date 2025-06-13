from rgbmatrix import graphics

def parse_color(hex_str):
    hex_str = hex_str.lstrip("#")
    r, g, b = [int(hex_str[i:i+2], 16) for i in (0, 2, 4)]
    return graphics.Color(r, g, b)

def load_font(path):
    font = graphics.Font()
    font.LoadFont(path)
    return font