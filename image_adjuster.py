from PIL import Image

# Opening an image_path, getting info, and showing the image_path
im = Image.open('.\\rick_thinking.png')
print(im.format, im.size, im.mode)
width, height = im.size
side = min(width, height)
scale_down_factor = 8
# left = 0
# top = height / scale_down_factor
# right = side
# bottom = 3 * height / scale_down_factor
# im1 = im.crop((left, top, right, bottom))

new_size = (max(int(round(width/scale_down_factor)), 1),
            max(int(round(height/scale_down_factor)), 1))
im1 = im.resize(new_size)
im1.save('.\\rick_thinking_small.png', 'PNG')
im1.show()



# # Converting images to jpeg
# if not im.mode == 'RGB':
#     im = im.convert('RGB')  # the original image_path's mode was RGBA (A for transparency), but im.save does not support
#     # saving RGBA as JPEG, so first convert it to plain RGB
# im.save('./screenshot.jpg', 'JPEG')

# im2 = Image.open('./screenshot.jpg')
# print(im2.format, im2.size, im2.mode)
# im2.show()  # note that the jpg was created and im2 shows up as jpeg, but im2.show()'s file shows a tempxx.png
