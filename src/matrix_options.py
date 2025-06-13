from rgbmatrix import RGBMatrixOptions

def GetOptions():
    options = RGBMatrixOptions()
    options.rows = 64
    options.cols = 64
    options.chain_length = 2
    options.parallel = 2
    options.hardware_mapping = 'regular'
    options.gpio_slowdown = 4
    options.led_rgb_sequence = 'BRG'
    options.brightness = 50
    options.limit_refresh_rate_hz = 120
    options.pixel_mapper_config = "Rotate:180"
    return options