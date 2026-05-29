"""
Built-in ASCII font renderer - Zero external dependencies.
Supports multiple font styles: Standard, Shadow, Block, Thin, Banner, Slant, etc.
All fonts are self-contained Python dictionaries mapping characters to ASCII patterns.
"""

from .standard import StandardFont
from .block import BlockFont
from .shadow import ShadowFont
from .thin import ThinFont
from .banner import BannerFont
from .slant import SlantFont
from .small import SmallFont
from .mini import MiniFont
from .dotmatrix import DotMatrixFont

# Font registry mapping
FONT_REGISTRY = {
    "standard": StandardFont,
    "block": BlockFont,
    "shadow": ShadowFont,
    "thin": ThinFont,
    "banner": BannerFont,
    "slant": SlantFont,
    "small": SmallFont,
    "mini": MiniFont,
    "dotmatrix": DotMatrixFont,
}

# Font metadata
FONT_META = {
    "standard": {"name": "Standard", "width": 6, "height": 5, "desc": "Classic ASCII font"},
    "block": {"name": "Block", "width": 6, "height": 7, "desc": "Bold block characters"},
    "shadow": {"name": "Shadow", "width": 7, "height": 7, "desc": "Shadow effect style"},
    "thin": {"name": "Thin", "width": 5, "height": 5, "desc": "Thin line style"},
    "banner": {"name": "Banner", "width": 7, "height": 7, "desc": "Large banner style"},
    "slant": {"name": "Slant", "width": 6, "height": 6, "desc": "Slanted italic style"},
    "small": {"name": "Small", "width": 4, "height": 5, "desc": "Compact small font"},
    "mini": {"name": "Mini", "width": 3, "height": 5, "desc": "Ultra compact mini font"},
    "dotmatrix": {"name": "DotMatrix", "width": 5, "height": 7, "desc": "Dot matrix display style"},
}


def get_font(name: str):
    """Get a font class by name. Returns StandardFont if name not found."""
    name_lower = name.lower()
    if name_lower in FONT_REGISTRY:
        return FONT_REGISTRY[name_lower]
    return StandardFont


def list_fonts() -> list:
    """List all available fonts with metadata."""
    result = []
    for key, meta in FONT_META.items():
        result.append({
            "name": key,
            "display_name": meta["name"],
            "width": meta["width"],
            "height": meta["height"],
            "description": meta["desc"],
        })
    return result


def render_text(text: str, font_name: str = "standard") -> list:
    """
    Render text to ASCII art using the specified font.
    
    Args:
        text: The text string to render
        font_name: Name of the font to use
        
    Returns:
        List of strings, each representing one line of the ASCII art
    """
    font_class = get_font(font_name)
    font = font_class()
    
    if not text:
        return []
    
    lines = font.render(text)
    return lines
