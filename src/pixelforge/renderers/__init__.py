"""Renderers package - Color and effect rendering for ASCII art."""

from .color import (
    colorize_line, gradient_line, rainbow_line,
    render_colored, strip_ansi, supports_color,
    list_colors, list_gradients, COLORS, GRADIENT_PALETTES
)

__all__ = [
    "colorize_line", "gradient_line", "rainbow_line",
    "render_colored", "strip_ansi", "supports_color",
    "list_colors", "list_gradients", "COLORS", "GRADIENT_PALETTES"
]
