from tkinter import *


root = Tk()
canvas = Canvas(root, height=327, width=500, background="skyblue")
canvas.pack()

canvas.create_arc(14, 84, 41, 64, start=0, extent=180, fill="#feecec", outline="")
canvas.create_arc(30, 58, 74, 90, start=0, extent=180, fill="#feecec", outline="")
canvas.create_arc(64, 84, 101, 64, start=0, extent=180, fill="#feecec", outline="")

canvas.create_arc(257, 20, 276, 36, start=0, extent=180, fill="#feecec", outline="")
canvas.create_arc(273, 15, 295, 41, start=0, extent=180, fill="#feecec", outline="")
canvas.create_arc(290, 20, 312, 36, start=0, extent=180, fill="#feecec", outline="")
canvas.create_arc(309, 23, 320, 33, start=0, extent=180, fill="#feecec", outline="")

canvas.create_arc(350, 56, 395, 100, start=0, extent=180, fill="#feecec", outline="")
canvas.create_arc(390, 62, 427, 94, start=0, extent=180, fill="#feecec", outline="")
canvas.create_arc(422, 64, 447, 92, start=0, extent=180, fill="#feecec", outline="")

canvas.create_oval(146, 41, 230, 127, fill="#feb94a", outline="#feb94a")

canvas.create_polygon(0, 174, 109, 44, 230, 174, fill="#475e64")
canvas.create_polygon(0, 174, 109, 44, 34, 174, fill="#3d4457")
canvas.create_polygon(153, 95, 187, 74, 290, 174, 153, 174, fill="#475e64")
canvas.create_polygon(216, 174, 337, 42, 474, 174, fill="#475e64")
canvas.create_polygon(381, 95, 414, 73, 500, 174, 381, 174, fill="#475e64")
canvas.create_polygon(154, 95, 187, 73, 186, 98, 182, 97, 180, 123, fill="#3d4457")
canvas.create_polygon(387, 92, 414, 73, 413, 117, fill="#3d4457")
canvas.create_rectangle(0, 174, 501, 328, fill="lightgrey", outline="")

canvas.create_polygon(20, 174, 32, 122, 43, 174, fill="#66979e")
canvas.create_polygon(42, 174, 55, 107, 70, 174, fill="#66979e")
canvas.create_polygon(194, 174, 210, 105, 224, 174, fill="#65989c")
canvas.create_polygon(216, 174, 226, 93, 242, 174, fill="#65989c")


canvas.create_rectangle(59, 172, 122, 237, fill="#673c43", outline="")
canvas.create_polygon(121, 237, 172, 234, 172, 172, 146, 143, 122, 170, fill="#b4524c")
canvas.create_polygon(122, 172, 59, 172, 81, 143, 146, 143, fill="#feecec")
canvas.create_rectangle(63, 179, 80, 195, outline='', fill="black")
canvas.create_rectangle(94, 179, 109, 196, outline='', fill="black")
canvas.create_rectangle(63, 209, 80, 226, outline='', fill="black")
canvas.create_rectangle(94, 209, 109, 226, outline='', fill="black")
canvas.create_rectangle(128, 177, 142, 197, width=2, fill="black", outline="#caa27f")
canvas.create_rectangle(149, 177, 163, 197, width=2, fill='black', outline="#caa27f")
canvas.create_rectangle(137, 210, 157, 226, fill="black")
canvas.create_oval(137, 200, 157, 220, fill="black")
canvas.create_rectangle(63, 179, 68, 195, fill="#caa27f", outline="")
canvas.create_rectangle(63, 209, 68, 226, fill="#caa27f", outline="")
canvas.create_rectangle(94, 179, 98, 196, fill="#caa27f", outline="")
canvas.create_rectangle(94, 209, 98, 226, fill="#caa27f", outline="")


canvas.create_rectangle(67, 260, 150, 300, fill="#b4524c", outline="#b4524c")
canvas.create_polygon(67, 260, 100, 225, 180, 225, 150, 260, fill="#feecec")
canvas.create_polygon(150, 260, 180, 225, 214, 260, 214, 300, 150, 301, fill="#caa27f")
canvas.create_rectangle(170, 265, 193, 300, fill="#673c43", outline="")
canvas.create_oval(170, 257, 192, 273, fill="#673c43", outline="")
canvas.create_rectangle(76, 268, 88, 285, fill="black", outline="#69979b", width=2)
canvas.create_rectangle(96, 268, 108, 285, fill="black", outline="#69979b", width=2)
canvas.create_rectangle(116, 268, 128, 285, fill="black", outline="#69979b", width=2)
canvas.create_polygon(354, 174, 502, 97, 502, 174, fill="#475e64")


canvas.create_polygon(222, 263, 234, 205, 246, 263, 258, 185, 269, 261, 276, 217, 286, 263, fill="#69979b")

canvas.create_polygon(384, 208, 384, 146, 406, 105, 419, 146, 419, 210, fill="#b35245")
canvas.create_polygon(406, 105, 434, 147, 434, 211, 418, 212, 419, 146, fill="#cca180")
canvas.create_oval(399, 143, 409, 153, fill="#673c43")


canvas.create_rectangle(372, 199, 434, 261, fill="#673c43", outline="")
canvas.create_polygon(324, 261, 372, 261, 372, 199, 346, 172, 324, 200, fill="black")
canvas.create_polygon(346, 172, 370, 199, 433, 199, 410, 172, fill="#feecec")
canvas.create_rectangle(381, 208, 397, 220, fill="black", outline="")
canvas.create_rectangle(411, 208, 427, 220, fill="black", outline="")
canvas.create_rectangle(381, 233, 397, 245, fill="black", outline="")
canvas.create_rectangle(411, 233, 427, 245, fill="black", outline="")
canvas.create_rectangle(391, 208, 397, 220, fill="brown", outline="")
canvas.create_rectangle(421, 208, 427, 220, fill="brown", outline="")
canvas.create_rectangle(391, 233, 397, 245, fill="brown", outline="")
canvas.create_rectangle(421, 233, 427, 245, fill="brown", outline="")
canvas.create_rectangle(338, 234, 355, 261, fill="#673c43")
canvas.create_rectangle(328, 206, 342, 225, fill="black", outline="#caa27f", width=2)
canvas.create_rectangle(352, 206, 366, 225, fill="black", outline="#caa27f", width=2)


canvas.create_oval(314, 240, 350, 270, fill="#d2c8be", outline="")
canvas.create_oval(304, 250, 320, 270, fill="#d2c8be", outline="")
canvas.create_oval(342, 250, 365, 270, fill="#d2c8be", outline="")

canvas.create_line(38, 250, 38, 320, width=3, fill="brown")
canvas.create_polygon(10, 295, 39, 257, 68, 295, fill="#673c43")
canvas.create_polygon(10, 270, 39, 225, 68, 270, fill="#673c43")
canvas.create_polygon(20, 235, 39, 205, 60, 235, fill="#673c43")

canvas.create_line(99, 297, 99, 327, width=3, fill="brown")
canvas.create_polygon(82, 320, 98, 297, 117, 320, fill="#475e64")
canvas.create_polygon(82, 308, 117, 308, 100, 276, fill="#475e64")
canvas.create_polygon(86, 288, 112, 288, 100, 263, fill="#475e64")


canvas.create_polygon(220, 327, 306, 327, 306, 290, 262, 262, 220, 290, fill="#673c43")
canvas.create_rectangle(306, 290, 416, 327, fill="#b35245", outline="")
canvas.create_polygon(262, 262, 306, 290, 416, 290, 376, 262, fill="#feecec")
canvas.create_rectangle(238, 294, 254, 316, fill="black", outline="#475e64", width=2)
canvas.create_rectangle(268, 294, 284, 316, fill="black", outline="#475e64", width=2)
canvas.create_rectangle(239, 295, 244, 316, fill="#feecec", outline="")
canvas.create_rectangle(269, 295, 274, 316, fill="#feecec", outline="")

canvas.create_rectangle(343, 274, 425, 327, fill="#b35245", outline="")
canvas.create_rectangle(349, 292, 356, 312, fill="#cca180", outline="")
canvas.create_rectangle(356, 292, 371, 312, fill="black", outline="")
canvas.create_rectangle(399, 292, 416, 312, fill="#cca180", outline="")
canvas.create_rectangle(406, 292, 421, 312, fill="black", outline="")
canvas.create_polygon(424, 274, 456, 240, 488, 275, 488, 327, 424, 327, fill="#cca180")
canvas.create_polygon(343, 274, 376, 240, 456, 240, 425, 274, fill="#feecec")
canvas.create_rectangle(451, 258, 461, 268, fill="black")
canvas.create_rectangle(445, 300, 469, 326, fill="#673c43", outline="")
canvas.create_oval(445, 280, 468, 320, fill="#673c43", outline="")

canvas.create_line(466, 176, 466, 236, fill="brown", width=3)
canvas.create_polygon(442, 218, 493, 218, 467, 180, fill="#673c43")
canvas.create_polygon(442, 192, 493, 192, 467, 154, fill="#673c43")
canvas.create_polygon(449, 162, 487, 161, 467, 136, fill="#673c43")

root.mainloop()
