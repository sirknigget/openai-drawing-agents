from typing import List, Tuple, Union, Sequence
from agents import function_tool
from tools.graphic_canvas import HeadlessCanvas  # OpenAI Agents SDK

# Global instance for tools
GLOBAL_CANVAS = HeadlessCanvas()

ColorLike = Union[str, Sequence[int]]

@function_tool
def free_draw_tool(
    path: List[Tuple[float, float]],
    color: ColorLike = "#000000",
    brush_px: int = 3,
) -> str:
    """
    Draw a thick polyline on the global headless canvas.

    Args:
        path: List of (x, y) coordinates in pixels to connect in order.
        color: Stroke color as "#RRGGBB", a (r,g,b) tuple, or a named color.
        brush_px: Line thickness in pixels.

    Returns:
        A status message indicating success.
    """
    # Assumes GLOBAL_CANVAS.initialize(...) was called earlier in the app lifecycle
    GLOBAL_CANVAS.free_draw(path=path, color=color, brush_px=brush_px)
    return "free_draw completed"
