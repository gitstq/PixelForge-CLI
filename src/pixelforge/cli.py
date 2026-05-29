"""
CLI entry point - Command-line interface for PixelForge.
"""

import sys
import os
import argparse
import textwrap

from . import __version__
from . import __description__
from .fonts import render_text, list_fonts, FONT_META
from .renderers import render_colored, list_colors, list_gradients, strip_ansi, supports_color
from .converters import image_to_ascii, image_to_ascii_color, list_ramps
from .exporters import export, list_formats


def cmd_text(args):
    """Handle text-to-ASCII command."""
    try:
        lines = render_text(args.text, font_name=args.font)
        
        if not lines:
            print("Error: No output generated.", file=sys.stderr)
            return 1
        
        # Apply color effects
        colored_lines = render_colored(
            lines,
            color=args.color,
            gradient=args.gradient,
            rainbow=args.rainbow,
            bold=args.bold,
        )
        
        # Output
        if args.no_ansi or not supports_color():
            output_lines = [strip_ansi(l) for l in colored_lines]
        else:
            output_lines = colored_lines
        
        output = "\n".join(output_lines)
        
        # Export to file if specified
        if args.output:
            export(output_lines, args.output, format=args.format or "txt")
            print(f"✅ Saved to: {args.output}", file=sys.stderr)
        else:
            print(output)
        
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_image(args):
    """Handle image-to-ASCII command."""
    try:
        if args.color_mode:
            lines = image_to_ascii_color(
                args.image,
                width=args.width,
                height=args.height,
                ramp=args.ramp,
                invert=args.invert,
                contrast=args.contrast,
                brightness=args.brightness,
            )
        else:
            lines = image_to_ascii(
                args.image,
                width=args.width,
                height=args.height,
                ramp=args.ramp,
                invert=args.invert,
                contrast=args.contrast,
                brightness=args.brightness,
            )
        
        if not lines:
            print("Error: No output generated.", file=sys.stderr)
            return 1
        
        output = "\n".join(lines)
        
        if args.output:
            export(lines, args.output, format=args.format or "txt")
            print(f"✅ Saved to: {args.output}", file=sys.stderr)
        else:
            print(output)
        
        return 0
    except ImportError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("Install Pillow for image support: pip install Pillow", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_list(args):
    """Handle list command."""
    if args.what == "fonts":
        print("\n🎨 Available Fonts:")
        print("─" * 60)
        for font_info in list_fonts():
            print(f"  {font_info['name']:12} | {font_info['display_name']:10} | "
                  f"{font_info['width']}x{font_info['height']} | {font_info['description']}")
    
    elif args.what == "colors":
        print("\n🌈 Available Colors:")
        print("─" * 40)
        for color in list_colors():
            print(f"  {color}")
    
    elif args.what == "gradients":
        print("\n🌅 Available Gradients:")
        print("─" * 40)
        for grad in list_gradients():
            print(f"  {grad}")
    
    elif args.what == "ramps":
        print("\n📊 Available Character Ramps:")
        print("─" * 60)
        for ramp in list_ramps():
            preview = get_ramp_preview(ramp)
            print(f"  {ramp:12} | {preview}")
    
    elif args.what == "formats":
        print("\n📦 Available Export Formats:")
        print("─" * 40)
        for fmt in list_formats():
            print(f"  {fmt}")
    
    elif args.what == "all":
        cmd_list(type('obj', (object,), {'what': 'fonts'})())
        cmd_list(type('obj', (object,), {'what': 'colors'})())
        cmd_list(type('obj', (object,), {'what': 'gradients'})())
        cmd_list(type('obj', (object,), {'what': 'ramps'})())
        cmd_list(type('obj', (object,), {'what': 'formats'})())
    
    return 0


def cmd_info(args):
    """Show tool information."""
    print(f"""
╔══════════════════════════════════════════════════════════╗
║              🎨 PixelForge-CLI v{__version__}                ║
║  Lightweight Terminal ASCII Art Generation Engine         ║
╚══════════════════════════════════════════════════════════╝

📖 Description:
  {__description__}

🔧 Features:
  • Text-to-ASCII with 9 built-in fonts (zero dependencies)
  • Image-to-ASCII with 5 character ramps
  • 16+ solid colors, 9 gradient palettes, rainbow mode
  • Export to TXT, HTML, JSON, SVG, PNG
  • Cross-platform (Windows, macOS, Linux)

📋 Quick Start:
  pixelforge text "HELLO" --font block --color cyan
  pixelforge text "WORLD" --font shadow --gradient fire
  pixelforge image photo.jpg --width 100 --ramp detailed
  pixelforge text "BANNER" --font banner --output art.txt

📚 Documentation: https://github.com/gitstq/PixelForge-CLI
""")
    return 0


def build_parser():
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        prog="pixelforge",
        description="🎨 PixelForge-CLI - Lightweight Terminal ASCII Art Intelligent Generation & Conversion Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
        Examples:
          pixelforge text "HELLO" --font block --color cyan
          pixelforge text "WORLD" --font shadow --gradient fire --bold
          pixelforge text "LOVE" --font standard --rainbow
          pixelforge image photo.jpg --width 100 --ramp detailed
          pixelforge image photo.jpg --width 80 --color-mode --output art.html
          pixelforge list fonts
          pixelforge list all
          pixelforge info
        """),
    )
    
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Text command
    text_parser = subparsers.add_parser("text", help="Generate ASCII art from text")
    text_parser.add_argument("text", help="Text to convert to ASCII art")
    text_parser.add_argument("-f", "--font", default="standard",
                           help="Font to use (default: standard)")
    text_parser.add_argument("-c", "--color", default=None,
                           help="Solid color (e.g., red, cyan, green)")
    text_parser.add_argument("-g", "--gradient", default=None,
                           help="Gradient palette (e.g., fire, ocean, sunset)")
    text_parser.add_argument("--rainbow", action="store_true",
                           help="Apply rainbow color effect")
    text_parser.add_argument("--bold", action="store_true",
                           help="Apply bold effect")
    text_parser.add_argument("-o", "--output", default=None,
                           help="Output file path")
    text_parser.add_argument("--format", default=None,
                           help="Output format (txt, html, json, svg, png)")
    text_parser.add_argument("--no-ansi", action="store_true",
                           help="Disable ANSI color codes in output")
    
    # Image command
    image_parser = subparsers.add_parser("image", help="Convert image to ASCII art")
    image_parser.add_argument("image", help="Path to image file")
    image_parser.add_argument("-w", "--width", type=int, default=80,
                            help="Output width in characters (default: 80)")
    image_parser.add_argument("--height", type=int, default=None,
                            help="Output height in characters (auto-calculated)")
    image_parser.add_argument("-r", "--ramp", default="detailed",
                            help="Character ramp (simple, detailed, blocks, dots, braille)")
    image_parser.add_argument("--invert", action="store_true",
                            help="Invert brightness")
    image_parser.add_argument("--contrast", type=float, default=1.0,
                            help="Contrast adjustment (default: 1.0)")
    image_parser.add_argument("--brightness", type=float, default=0.0,
                            help="Brightness adjustment (-1.0 to 1.0)")
    image_parser.add_argument("--color-mode", action="store_true",
                            help="Output colored ASCII using image colors")
    image_parser.add_argument("-o", "--output", default=None,
                            help="Output file path")
    image_parser.add_argument("--format", default=None,
                            help="Output format (txt, html, json, svg, png)")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List available resources")
    list_parser.add_argument("what", choices=["fonts", "colors", "gradients", "ramps", "formats", "all"],
                           help="What to list")
    
    # Info command
    subparsers.add_parser("info", help="Show tool information")
    
    return parser


def main():
    """Main CLI entry point."""
    parser = build_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    commands = {
        "text": cmd_text,
        "image": cmd_image,
        "list": cmd_list,
        "info": cmd_info,
    }
    
    handler = commands.get(args.command)
    if handler:
        return handler(args)
    
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
