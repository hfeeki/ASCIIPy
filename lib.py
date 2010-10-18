import math

import Image, ImageChops, ImageDraw, ImageMath, ImageFilter

class Method(object):
    HAMMING = 0
    ZNCC = 1

def edgify(image, binary_threshold=150, smoothen=0, invert=False):
    '''Converts an image into a B/W edge representation'''
    image = image.convert('L')
    image = image.filter(ImageFilter.FIND_EDGES)
    image = ImageChops.invert(image)
    for i in range(0, smoothen):
        image = image.filter(ImageFilter.SMOOTH)
    image = image.point(lambda i: i>binary_threshold and 255 or 0)
    if invert:
        image = ImageChops.invert(image)
    return image

def mean_intensity_value(image):
    colors = image.getcolors()
    if len(colors) > 2:
        raise ValueError, 'image must only contain two colors, 0 and 255'
    if len(colors) == 1:
        return colors[0][1]
    else:
        return (colors[0][0] * colors[0][1] + colors[1][0] * colors[1][1]) / (colors[0][0] + colors[1][0])

def zncc(image1, image2, x=0, y=0):
    a = 0.0
    b = 0.0
    c = 0.0
    width, height = image2.size
    subimage = image1.crop((x, y, x+width, y+height))
    mu_i_c = mean_intensity_value(subimage)
    mu_t = mean_intensity_value(image2)
    image1_pix = image1.load()
    image2_pix = image2.load()
    for j in range(0, height):
        for i in range(0, width):
            m = image1_pix[x+i, y+j] - mu_i_c
            n = image2_pix[i, j] - mu_t
            a += m*n
            b += m**2
            c += n**2
    b = math.sqrt(b)
    c = math.sqrt(c)
    if b*c == 0:
        return 0
    return a / (b*c)
def dist(image, reference_image, method=Method.HAMMING):
    ''' Calculates the distance of an image to a reference image'''
    if method == Method.HAMMING:
        xor = ImageChops.difference(image, reference_image).getcolors()
        if len(xor) > 2:
            raise ValueError, 'The images must only contain two colors, 0 and 255'
        for cnt, color in xor:
            if color==255:
                return cnt
        return 0
    elif method == Method.ZNCC:
        return 100 - zncc(image, reference_image)
    else:
        return ValueError, 'Unknown method'

def create_image(char, font, x, y):
    im = Image.new('1', (x, y), 255)
    dr = ImageDraw.Draw(im)
    dr.text( (0,0), char, font=font)
    del dr
    return im

