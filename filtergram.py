from filters import *

def main():
    img = load_img("water.jpg")
    show_img(img)
    input()
    gray_circle(img, 100)
    show_img(img)
    img.save_img("water_circle.jpg")

main()
