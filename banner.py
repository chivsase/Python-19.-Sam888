import pyfiglet
import time

# Custom text to be converted to ASCII art
custom_text = """
Sam888
"""

# List of font styles available in pyfiglet (including additional styles)
font_styles = [
    # 'standard', '3-d', '3x5', '5lineoblique', 'alphabet', 'banner3-D',
    # 'doh', 'isometric1', 'letters', 'alligator', 'dotmatrix', 'bubble',
    # 'bulbhead', 'digital', 'ivrit', 'lean', 'mini', 'script', 'shadow',
    # 'slant', 'small', 'smscript', 'smshadow', 'smslant', 'speed', 'starwars',
    # 'acrobatic', 'alligator2', 'block', 'caligraphy', 'coinstak', 'cricket',
    # 'drpepper', 'eftichess', 'firefont-k', 'fourtops', 'funface', 'goofy',
    # 'graffiti', 'katakana', 'larry3d', 'madrid', 'marquee', 'mike',
    # 'nancyj-fancy', 'nancyj-underlined', 'pawp', 'peaks', 'rectangles',
    # 'relief', 'roman', 'rounded', 'rowancap', 'script', 'serifcap', 'slscript',
    # 'stellar', 'taiwanes', 'tanja', 'threepoint', 'ticks', 'ticksslant', 'trek',
    # 'tsalagi', 'twopoint', 'univers', 'usaflag', 'weird'
    'cricket',
]

# Print ASCII art banners for each font style
for style in font_styles:
    try:
        ascii_banner = pyfiglet.figlet_format(custom_text, font=style)
        print(f"Font style: {style}")
        print(ascii_banner)
        print("\n")
    except pyfiglet.FontNotFound:
        print(f"Font style '{style}' not found in pyfiglet.")
        print("\n")

# Pause for 10 seconds before closing the cmd window
# time.sleep(100)
