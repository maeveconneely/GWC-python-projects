from PIL import Image
import math

def load_img(filename):
    img = Image.open(filename)
    return img

def show_img(open_filename):
    open_filename.show()

def save_img(open_filename, save_as):
    open_filename.save(save_as)

def obama_self(open_filename):
    pixels = open_filename.getdata()
    new_pixels = []
    for i in pixels:
        value = 0
        for j in i:
            value += j

        if value < 200:
            new_pixels.append((0, 51, 76))
        elif value < 365:
            new_pixels.append((217, 26, 33))
        elif value < 600:
            new_pixels.append((112, 150, 158))
        else:
            new_pixels.append((252, 227, 166))

    open_filename.putdata(new_pixels)

def gray_circle(open_filename, radius):
    middle_pixel = (int(round(open_filename.width/2)),
                    int(round(open_filename.height/2)))

    for x in range(open_filename.width):
        for y in range(open_filename.height):

            distance_m = math.sqrt(math.pow(x - middle_pixel[0], 2) +
                    math.pow(y - middle_pixel[1], 2))


            if distance_m > radius:
                grey = 0
                for i in open_filename.getpixel((x, y)):
                    grey += i
                grey //= 3
                open_filename.putpixel((x, y), (grey, grey, grey))

            else:
                pixel_red = open_filename.getpixel((x, y))[0]
                pixel_green  = open_filename.getpixel((x, y))[1]
                pixel_blue  = open_filename.getpixel((x, y))[2]

                if (pixel_red + 30 < 255 and pixel_blue + 30 < 255 and
                pixel_green + 30 < 255):
                    open_filename.putpixel((x, y), (pixel_red + 30,
                                                    pixel_green + 30,
                                                    pixel_blue + 30))
