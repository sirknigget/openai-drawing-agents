from agents import trace, Runner
from dotenv import load_dotenv

from context.app_context import AppContext
from my_agents.drawing_agent import drawing_agent
import asyncio
from tools.graphic_canvas import HeadlessCanvas

load_dotenv(override=True)

CANVAS_WIDTH, CANVAS_HEIGHT = 640, 480
OUTPUT_FILE = "agent_output.png"


async def main():
    canvas = HeadlessCanvas()
    canvas.initialize(640, 480)
    app_ctx = AppContext(canvas=canvas)
    with trace("Drawing agent"):
        print("Starting drawing agent")
        result = await Runner.run(drawing_agent,
                                  f"The canvas dimensions are {CANVAS_WIDTH}, {CANVAS_HEIGHT}. Draw a blue 3D diamond.",
                                  context=app_ctx)
        print("Agent response:" + result.final_output)
    canvas.save_and_cleanup(OUTPUT_FILE)


if __name__ == "__main__":
    asyncio.run(main())
