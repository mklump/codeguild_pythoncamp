"""
    Python Coding Bootcamp (pdxcodeguild)
    Code File for rotate_image.py
    by: Matthew James K on 5/9/2016
"""
from PIL import Image

def main():
    """
    Main function/test driver main single thread of execution for this console program.
    All stack traces on raised exceptions start here.
    """
    src_im = Image.open("any_name_image_file.jpg")
    angle = 45
    #size = 100, 100

    dst_im = Image.new("RGBA", (196,283), "blue" )
    im = src_im.convert('RGBA')
    rot = im.rotate( angle, expand=1 ).resize(size)
    dst_im.paste( rot, (50, 50), rot )
    dst_im.save("rotated.png")

if __name__ == "__main__":
    sys.exit(int(main() or 0))