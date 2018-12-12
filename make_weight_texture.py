
from os.path import join, dirname

import bpy
from mathutils import Color


def weight_to_color(weight):
	color = Color()
	color.hsv = 0.66 * (1 - weight), 1, 1
	return color


def make_weight_map_texture(filename, size):
	width, height = size
	img = bpy.data.images.new("WeightMap", width=width, height=height, alpha=True)

	pixels = list(img.pixels)

	for y in range(height):
		for x in range(width):
			weight = x / (width - 1)
			r, g, b = weight_to_color(weight)
			i = (x + y * width) * 4
			pixels[i:i+4] = r, g, b, 1

	img.pixels[:] = pixels
	img.update()

	img.filepath_raw = filename
	img.file_format = "PNG"
	img.save()


if __name__ == "__main__":
	blend_file = bpy.data.filepath
	assert blend_file

	filename = join(dirname(blend_file), "weight_map.png")

	make_weight_map_texture(filename, (128, 32))
