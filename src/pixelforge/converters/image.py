"""
Image to ASCII converter - Convert images to ASCII art.
Optional dependency: Pillow (pip install Pillow)
"""

import os


# ASCII character density ramps (from lightest to darkest)
ASCII_RAMP_SIMPLE = " .:-=+*#%@"
ASCII_RAMP_DETAILED = " .'`^\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ASCII_RAMP_BLOCKS = " ░▒▓█"
ASCII_RAMP_DOTS = " ⠁⠃⠇⡇⣇⣧⣷⣿"
ASCII_RAMP_BRAILLE = "⠀⠁⠂⠃⠄⠅⠆⠇⡀⡁⡂⡃⡄⡅⡆⡇⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿"

RAMPS = {
    "simple": ASCII_RAMP_SIMPLE,
    "detailed": ASCII_RAMP_DETAILED,
    "blocks": ASCII_RAMP_BLOCKS,
    "dots": ASCII_RAMP_DOTS,
    "braille": ASCII_RAMP_BRAILLE,
}


def _check_pillow():
    """Check if Pillow is available."""
    try:
        from PIL import Image
        return True, Image
    except ImportError:
        return False, None


def image_to_ascii(image_path: str, width: int = 80, height: int = None,
                   ramp: str = "detailed", invert: bool = False,
                   contrast: float = 1.0, brightness: float = 0.0) -> list:
    """
    Convert an image file to ASCII art.
    
    Args:
        image_path: Path to the image file
        width: Output width in characters
        height: Output height in characters (auto-calculated if None)
        ramp: Character ramp to use ('simple', 'detailed', 'blocks', 'dots', 'braille')
        invert: Invert brightness (dark on light vs light on dark)
        contrast: Contrast adjustment factor (1.0 = normal)
        brightness: Brightness adjustment (-1.0 to 1.0)
        
    Returns:
        List of strings, each representing one line of ASCII art
    """
    has_pillow, Image = _check_pillow()
    if not has_pillow:
        raise ImportError(
            "Pillow is required for image-to-ASCII conversion. "
            "Install it with: pip install Pillow"
        )
    
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    # Select ramp
    ramp_chars = RAMPS.get(ramp, ASCII_RAMP_DETAILED)
    if invert:
        ramp_chars = ramp_chars[::-1]
    
    # Open and process image
    img = Image.open(image_path)
    img = img.convert("L")  # Convert to grayscale
    
    # Calculate dimensions
    orig_width, orig_height = img.size
    aspect_ratio = orig_height / orig_width
    
    if height is None:
        # Character aspect ratio is roughly 2:1 (height:width)
        height = int(width * aspect_ratio * 0.5)
    
    # Resize image
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    
    # Get pixel data
    pixels = list(img.getdata())
    
    # Apply brightness and contrast
    adjusted_pixels = []
    for p in pixels:
        # Apply brightness
        val = p + (brightness * 255)
        # Apply contrast
        val = ((val - 128) * contrast) + 128
        val = max(0, min(255, val))
        adjusted_pixels.append(val)
    
    # Map pixels to ASCII characters
    result = []
    for row in range(height):
        line = ""
        for col in range(width):
            pixel_val = adjusted_pixels[row * width + col]
            # Map brightness to character index
            idx = int((pixel_val / 255) * (len(ramp_chars) - 1))
            idx = max(0, min(idx, len(ramp_chars) - 1))
            line += ramp_chars[idx]
        result.append(line)
    
    return result


def image_to_ascii_color(image_path: str, width: int = 80, height: int = None,
                         ramp: str = "detailed", invert: bool = False,
                         contrast: float = 1.0, brightness: float = 0.0) -> list:
    """
    Convert an image to colored ASCII art using ANSI escape codes.
    
    Args:
        Same as image_to_ascii, plus:
        
    Returns:
        List of colored strings with ANSI escape codes
    """
    has_pillow, Image = _check_pillow()
    if not has_pillow:
        raise ImportError(
            "Pillow is required for image-to-ASCII conversion. "
            "Install it with: pip install Pillow"
        )
    
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    ramp_chars = RAMPS.get(ramp, ASCII_RAMP_DETAILED)
    if invert:
        ramp_chars = ramp_chars[::-1]
    
    # Open and process image (keep RGB for color output)
    img = Image.open(image_path)
    img_rgb = img.convert("RGB")
    img_gray = img.convert("L")
    
    orig_width, orig_height = img.size
    aspect_ratio = orig_height / orig_width
    
    if height is None:
        height = int(width * aspect_ratio * 0.5)
    
    img_rgb = img_rgb.resize((width, height), Image.Resampling.LANCZOS)
    img_gray = img_gray.resize((width, height), Image.Resampling.LANCZOS)
    
    rgb_pixels = list(img_rgb.getdata())
    gray_pixels = list(img_gray.getdata())
    
    result = []
    for row in range(height):
        line = ""
        for col in range(width):
            idx = row * width + col
            pixel_val = gray_pixels[idx]
            r, g, b = rgb_pixels[idx]
            
            # Apply brightness and contrast
            val = pixel_val + (brightness * 255)
            val = ((val - 128) * contrast) + 128
            val = max(0, min(255, val))
            
            char_idx = int((val / 255) * (len(ramp_chars) - 1))
            char_idx = max(0, min(char_idx, len(ramp_chars) - 1))
            char = ramp_chars[char_idx]
            
            if char.strip():
                line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            else:
                line += char
        result.append(line)
    
    return result


def list_ramps() -> list:
    """List all available character ramps."""
    return list(RAMPS.keys())


def get_ramp_preview(ramp_name: str) -> str:
    """Get a preview string of a character ramp."""
    ramp_chars = RAMPS.get(ramp_name, ASCII_RAMP_DETAILED)
    return ramp_chars
