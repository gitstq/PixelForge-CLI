"""
Color renderer - Add ANSI color support to ASCII art output.
Supports solid colors, gradients, and rainbow effects.
"""

import sys


# ANSI color codes
COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
}

# 256-color gradient palette (indices)
GRADIENT_PALETTES = {
    "fire": [196, 202, 208, 214, 220, 226, 227, 228, 229, 230],
    "ocean": [17, 19, 20, 21, 24, 25, 26, 27, 31, 38],
    "forest": [22, 28, 34, 40, 46, 76, 106, 142, 148, 154],
    "sunset": [52, 88, 124, 160, 196, 202, 208, 214, 220, 226],
    "rainbow": [196, 202, 208, 214, 220, 226, 118, 82, 46, 21],
    "purple": [54, 92, 129, 134, 163, 164, 183, 183, 219, 225],
    "cyber": [21, 27, 33, 39, 45, 51, 50, 49, 48, 47],
    "pastel": [177, 180, 186, 191, 187, 183, 179, 178, 183, 188],
    "grayscale": [232, 234, 236, 238, 240, 242, 244, 246, 248, 250],
}

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"


def colorize_line(line: str, color: str = None) -> str:
    """Apply a solid color to an entire line."""
    if not color or color.lower() == "none":
        return line
    color_lower = color.lower()
    if color_lower in COLORS:
        return f"{COLORS[color_lower]}{line}{RESET}"
    return line


def gradient_line(line: str, palette_name: str = "fire") -> str:
    """Apply a gradient color effect to a line based on character position."""
    if palette_name not in GRADIENT_PALETTES:
        palette_name = "fire"
    palette = GRADIENT_PALETTES[palette_name]
    
    result = []
    length = max(len(line), 1)
    for i, char in enumerate(line):
        # Map character position to palette index
        idx = int((i / length) * (len(palette) - 1))
        color_code = palette[min(idx, len(palette) - 1)]
        if char != ' ':
            result.append(f"\033[38;5;{color_code}m{char}")
        else:
            result.append(char)
    result.append(RESET)
    return "".join(result)


def rainbow_line(line: str) -> str:
    """Apply rainbow color effect to a line."""
    rainbow_colors = [196, 202, 208, 214, 220, 226, 118, 82, 46, 21]
    result = []
    length = max(len(line), 1)
    for i, char in enumerate(line):
        if char != ' ':
            idx = i % len(rainbow_colors)
            result.append(f"\033[38;5;{rainbow_colors[idx]}m{char}")
        else:
            result.append(char)
    result.append(RESET)
    return "".join(result)


def render_colored(lines: list, color: str = None, gradient: str = None, 
                   rainbow: bool = False, bold: bool = False) -> list:
    """
    Render ASCII art lines with color effects.
    
    Args:
        lines: List of ASCII art lines
        color: Solid color name (e.g., 'red', 'cyan')
        gradient: Gradient palette name (e.g., 'fire', 'ocean')
        rainbow: Whether to apply rainbow effect
        bold: Whether to apply bold effect
        
    Returns:
        List of colored lines
    """
    if not lines:
        return []
    
    result = []
    for line in lines:
        if rainbow:
            colored = rainbow_line(line)
        elif gradient:
            colored = gradient_line(line, gradient)
        elif color:
            colored = colorize_line(line, color)
        else:
            colored = line
        
        if bold and not rainbow and not gradient:
            colored = f"{BOLD}{colored}"
        
        result.append(colored)
    
    return result


def strip_ansi(text: str) -> str:
    """Remove ANSI escape codes from text."""
    import re
    ansi_escape = re.compile(r'\033\[[0-9;]*m')
    return ansi_escape.sub('', text)


def supports_color() -> bool:
    """Check if the terminal supports color output."""
    if sys.platform == "win32":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            return kernel32.GetConsoleMode(kernel32.GetStdHandle(-11)) & 0x0004
        except Exception:
            return False
    if not hasattr(sys.stdout, 'isatty'):
        return False
    return sys.stdout.isatty()


def list_colors() -> list:
    """List all available color names."""
    return list(COLORS.keys())


def list_gradients() -> list:
    """List all available gradient palette names."""
    return list(GRADIENT_PALETTES.keys())
