"""
TUI (Terminal User Interface) - Interactive dashboard for PixelForge.
Built with zero external dependencies using ANSI escape codes.
"""

import sys
import os


# ANSI escape codes
class ANSI:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    REVERSE = "\033[7m"
    
    # Cursor movement
    CLEAR = "\033[2J\033[H"
    CLEAR_LINE = "\033[2K"
    HOME = "\033[H"
    UP = "\033[A"
    DOWN = "\033[B"
    RIGHT = "\033[C"
    LEFT = "\033[D"
    
    # Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    
    # 256-color
    def color256(fg: int) -> str:
        return f"\033[38;5;{fg}m"
    
    def bg256(bg: int) -> str:
        return f"\033[48;5;{bg}m"
    
    # RGB color
    def rgb(r: int, g: int, b: int) -> str:
        return f"\033[38;2;{r};{g};{b}m"
    
    def bg_rgb(r: int, g: int, b: int) -> str:
        return f"\033[48;2;{r};{g};{b}m"


def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write(ANSI.CLEAR)
    sys.stdout.flush()


def move_cursor(row: int, col: int):
    """Move cursor to specific position."""
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()


def hide_cursor():
    """Hide the terminal cursor."""
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def show_cursor():
    """Show the terminal cursor."""
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


def get_terminal_size() -> tuple:
    """Get terminal dimensions (width, height)."""
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except Exception:
        return 80, 24


def draw_box(x: int, y: int, width: int, height: int, 
             title: str = None, border_color: str = None) -> str:
    """
    Draw a box in the terminal.
    
    Args:
        x: Starting column
        y: Starting row
        width: Box width
        height: Box height
        title: Optional title for the box
        border_color: ANSI color code for the border
        
    Returns:
        String representation of the box
    """
    color = border_color or ANSI.CYAN
    reset = ANSI.RESET
    
    lines = []
    
    # Top border
    top = f"{color}┌"
    if title:
        title_str = f" {title} "
        remaining = width - len(title_str) - 2
        if remaining > 0:
            left_fill = remaining // 2
            right_fill = remaining - left_fill
            top += "─" * left_fill + title_str + "─" * right_fill
        else:
            top += f" {title} " + "─" * max(0, width - len(title) - 5)
    else:
        top += "─" * (width - 2)
    top += f"┐{reset}"
    lines.append(top)
    
    # Middle rows
    for i in range(height - 2):
        lines.append(f"{color}│{reset}" + " " * (width - 2) + f"{color}│{reset}")
    
    # Bottom border
    bottom = f"{color}└" + "─" * (width - 2) + f"┘{reset}"
    lines.append(bottom)
    
    return "\n".join(lines)


def draw_progress_bar(value: float, width: int = 40, 
                      filled_char: str = "█", empty_char: str = "░",
                      color: str = None) -> str:
    """Draw a progress bar."""
    color = color or ANSI.GREEN
    filled = int(value * width)
    empty = width - filled
    bar = f"{color}{filled_char * filled}{ANSI.DIM}{empty_char * empty}{ANSI.RESET}"
    return f"[{bar}] {value * 100:.0f}%"


def draw_table(headers: list, rows: list, padding: int = 2) -> str:
    """Draw a simple text table."""
    # Calculate column widths
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Build table
    lines = []
    
    # Header separator
    sep = "+" + "+".join("─" * (w + padding * 2) for w in col_widths) + "+"
    lines.append(sep)
    
    # Header
    header_line = "|"
    for i, h in enumerate(headers):
        header_line += " " * padding + str(h).ljust(col_widths[i]) + " " * padding + "|"
    lines.append(f"{ANSI.BOLD}{header_line}{ANSI.RESET}")
    lines.append(sep)
    
    # Rows
    for row in rows:
        row_line = "|"
        for i, cell in enumerate(row):
            if i < len(col_widths):
                row_line += " " * padding + str(cell).ljust(col_widths[i]) + " " * padding + "|"
        lines.append(row_line)
    
    lines.append(sep)
    return "\n".join(lines)


def draw_banner(text: str, color: str = None) -> str:
    """Draw a centered banner text."""
    color = color or ANSI.CYAN
    width, _ = get_terminal_size()
    padding = max(0, (width - len(text)) // 2)
    return f"{color}{'═' * width}{ANSI.RESET}\n{' ' * padding}{ANSI.BOLD}{text}{ANSI.RESET}\n{color}{'═' * width}{ANSI.RESET}"


def color_text(text: str, color: str) -> str:
    """Apply color to text."""
    return f"{color}{text}{ANSI.RESET}"


def bold_text(text: str) -> str:
    """Apply bold to text."""
    return f"{ANSI.BOLD}{text}{ANSI.RESET}"


def dim_text(text: str) -> str:
    """Apply dim to text."""
    return f"{ANSI.DIM}{text}{ANSI.RESET}"
