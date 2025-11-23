from tools.graphic_canvas import HeadlessCanvas


GLOBAL_CANVAS = HeadlessCanvas()

def main():
    # 1) Initialize a 400x300 off-screen canvas with white background
    GLOBAL_CANVAS.initialize(400, 300, background="#FFFFFF")

    # 2) Draw a blue diagonal with thickness 6
    GLOBAL_CANVAS.free_draw(
        path=[(10, 10), (390, 290)],
        color="#0066CC",
        brush_px=6,
    )

    # 3) Draw a red "zig-zag" polyline
    zigzag = [(50, 250), (150, 200), (250, 260), (350, 210)]
    GLOBAL_CANVAS.free_draw(
        path=zigzag,
        color="#CC0011",
        brush_px=4,
    )

    # 4) Draw a green polyline rectangle outline
    rect_path = [(60, 60), (340, 60), (340, 240), (60, 240), (60, 60)]
    GLOBAL_CANVAS.free_draw(
        path=rect_path,
        color="#2E8B57",
        brush_px=3,
    )

    # 5) Save PNG and cleanup resources
    GLOBAL_CANVAS.save_and_cleanup("output.png")

if __name__ == "__main__":
    main()
