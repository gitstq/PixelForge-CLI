"""Tests for PixelForge-CLI."""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


def test_font_rendering():
    """Test basic font rendering."""
    from pixelforge.fonts import render_text, list_fonts, get_font
    
    # Test standard font
    lines = render_text("HI", "standard")
    assert len(lines) == 5, f"Expected 5 lines, got {len(lines)}"
    assert all(len(line) > 0 for line in lines), "Empty lines in output"
    print("✅ Standard font rendering: PASS")
    
    # Test block font
    lines = render_text("OK", "block")
    assert len(lines) == 7, f"Expected 7 lines, got {len(lines)}"
    print("✅ Block font rendering: PASS")
    
    # Test shadow font
    lines = render_text("AB", "shadow")
    assert len(lines) == 7, f"Expected 7 lines, got {len(lines)}"
    print("✅ Shadow font rendering: PASS")
    
    # Test thin font
    lines = render_text("CD", "thin")
    assert len(lines) == 5, f"Expected 5 lines, got {len(lines)}"
    print("✅ Thin font rendering: PASS")
    
    # Test banner font
    lines = render_text("EF", "banner")
    assert len(lines) == 7, f"Expected 7 lines, got {len(lines)}"
    print("✅ Banner font rendering: PASS")
    
    # Test slant font
    lines = render_text("GH", "slant")
    assert len(lines) == 6, f"Expected 6 lines, got {len(lines)}"
    print("✅ Slant font rendering: PASS")
    
    # Test small font
    lines = render_text("IJ", "small")
    assert len(lines) == 5, f"Expected 5 lines, got {len(lines)}"
    print("✅ Small font rendering: PASS")
    
    # Test mini font
    lines = render_text("KL", "mini")
    assert len(lines) == 5, f"Expected 5 lines, got {len(lines)}"
    print("✅ Mini font rendering: PASS")
    
    # Test dotmatrix font
    lines = render_text("MN", "dotmatrix")
    assert len(lines) == 7, f"Expected 7 lines, got {len(lines)}"
    print("✅ DotMatrix font rendering: PASS")
    
    # Test unknown font falls back to standard
    lines = render_text("XZ", "nonexistent")
    assert len(lines) == 5, f"Expected 5 lines for fallback, got {len(lines)}"
    print("✅ Font fallback: PASS")
    
    # Test empty text
    lines = render_text("", "standard")
    assert len(lines) == 0, "Expected empty output for empty text"
    print("✅ Empty text handling: PASS")
    
    # Test list fonts
    fonts = list_fonts()
    assert len(fonts) == 9, f"Expected 9 fonts, got {len(fonts)}"
    print("✅ Font listing: PASS")
    
    # Test all characters render
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !.-+:":
        lines = render_text(char, "standard")
        assert len(lines) == 5, f"Failed to render character: {char}"
    print("✅ All characters rendering: PASS")


def test_color_rendering():
    """Test color rendering."""
    from pixelforge.renderers import (
        colorize_line, gradient_line, rainbow_line,
        render_colored, strip_ansi, list_colors, list_gradients
    )
    
    # Test solid color
    colored = colorize_line("HELLO", "red")
    assert "\033[" in colored, "Expected ANSI codes in colored output"
    print("✅ Solid color: PASS")
    
    # Test gradient
    gradient = gradient_line("HELLO WORLD", "fire")
    assert "\033[38;5;" in gradient, "Expected 256-color codes in gradient"
    print("✅ Gradient color: PASS")
    
    # Test rainbow
    rainbow = rainbow_line("PIXELFORGE")
    assert "\033[38;5;" in rainbow, "Expected 256-color codes in rainbow"
    print("✅ Rainbow color: PASS")
    
    # Test strip ANSI
    clean = strip_ansi("\033[31mHELLO\033[0m")
    assert clean == "HELLO", f"Expected 'HELLO', got '{clean}'"
    print("✅ ANSI stripping: PASS")
    
    # Test render_colored
    lines = ["HELLO", "WORLD"]
    colored = render_colored(lines, color="cyan")
    assert len(colored) == 2, "Expected same number of lines"
    print("✅ Render colored: PASS")
    
    # Test list functions
    colors = list_colors()
    assert len(colors) >= 16, f"Expected at least 16 colors, got {len(colors)}"
    gradients = list_gradients()
    assert len(gradients) >= 5, f"Expected at least 5 gradients, got {len(gradients)}"
    print("✅ Color/gradient listing: PASS")


def test_exporters():
    """Test export functionality."""
    from pixelforge.exporters import export_txt, export_json, export_html, list_formats
    import tempfile
    import json
    
    lines = ["HELLO", "WORLD"]
    
    # Test TXT export
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False, mode="w") as f:
        txt_path = f.name
    export_txt(lines, txt_path)
    with open(txt_path) as f:
        content = f.read()
    assert "HELLO" in content and "WORLD" in content
    os.unlink(txt_path)
    print("✅ TXT export: PASS")
    
    # Test JSON export
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
        json_path = f.name
    export_json(lines, json_path, metadata={"font": "standard"})
    with open(json_path) as f:
        data = json.load(f)
    assert data["lines"] == lines
    assert data["height"] == 2
    os.unlink(json_path)
    print("✅ JSON export: PASS")
    
    # Test HTML export
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
        html_path = f.name
    export_html(lines, html_path)
    with open(html_path) as f:
        content = f.read()
    assert "<!DOCTYPE html>" in content
    assert "HELLO" in content
    os.unlink(html_path)
    print("✅ HTML export: PASS")
    
    # Test SVG export
    with tempfile.NamedTemporaryFile(suffix=".svg", delete=False, mode="w") as f:
        svg_path = f.name
    from pixelforge.exporters import export_svg
    export_svg(lines, svg_path)
    with open(svg_path) as f:
        content = f.read()
    assert "<svg" in content
    os.unlink(svg_path)
    print("✅ SVG export: PASS")
    
    # Test list formats
    formats = list_formats()
    assert "txt" in formats and "html" in formats
    print("✅ Format listing: PASS")


def test_image_converter():
    """Test image converter (without actual image)."""
    from pixelforge.converters import list_ramps, get_ramp_preview
    
    # Test list ramps
    ramps = list_ramps()
    assert len(ramps) == 5, f"Expected 5 ramps, got {len(ramps)}"
    print("✅ Ramp listing: PASS")
    
    # Test ramp preview
    preview = get_ramp_preview("simple")
    assert len(preview) > 0
    print("✅ Ramp preview: PASS")
    
    # Test error handling
    try:
        from pixelforge.converters import image_to_ascii
        image_to_ascii("nonexistent.png")
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        print("✅ Image error handling: PASS")
    except ImportError:
        print("✅ Image import error handling: PASS")


def test_version():
    """Test version info."""
    from pixelforge import __version__, __description__
    assert __version__ == "1.0.0"
    assert "ASCII" in __description__
    print("✅ Version info: PASS")


if __name__ == "__main__":
    print("=" * 60)
    print("🧪 PixelForge-CLI Test Suite")
    print("=" * 60)
    print()
    
    try:
        test_version()
        test_font_rendering()
        test_color_rendering()
        test_exporters()
        test_image_converter()
        
        print()
        print("=" * 60)
        print("✅ All tests passed!")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
