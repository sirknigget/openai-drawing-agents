from agents import Agent

from context.app_context import AppContext
from tools.graphic_tool import free_draw_tool

INSTRUCTIONS = """You are a talented kid who likes to draw.
You are provided a tool to draw freely using a brush.
Draw the object or scene that is requested from you, by using the tool up to 50 times.
"""

drawing_agent = Agent[AppContext](
    name="Drawing agent",
    instructions=INSTRUCTIONS,
    tools=[free_draw_tool],
    model="gpt-4o-mini",
)

print (free_draw_tool)