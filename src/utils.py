from rgbmatrix import graphics

def parse_color(hex_str):
    hex_str = hex_str.lstrip("#")
    r, g, b = [int(hex_str[i:i+2], 16) for i in (0, 2, 4)]
    return graphics.Color(r, g, b)

loaded_fonts = {}

def load_and_cache_font(font_path):
    if font_path not in loaded_fonts:
        loaded_fonts[font_path] = graphics.Font()
        loaded_fonts[font_path].LoadFont(font_path)
    return loaded_fonts[font_path]

def load_font(path):
    font = graphics.Font()
    font.LoadFont(path)
    return font