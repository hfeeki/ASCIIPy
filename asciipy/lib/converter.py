import sys
import os

import Image, ImageChops, ImageFilter

from symbols import SYMBOLS, AVG_SYMBOLS

BASE = os.path.dirname(__file__)
print BASE

class ImageConverter(object):
    AVERAGE = 0
    HAMMING = 1

    _ref_images = [Image.open(os.path.join(BASE, 'ref_images/u%s.gif' % str(char.__repr__())[4:8])) for char in SYMBOLS]

    def __init__(self, image_file_name):
        self.image = Image.open(image_file_name).convert('L')

    def run(self, width=80, unic=True, method=HAMMING, bw=True, bw_threshold=150, smoothen=0, edgify=False):
        # pre-process image
        if edgify:
            temp_image = self.image.filter(ImageFilter.FIND_EDGES)
            temp_image = ImageChops.invert(temp_image)
        else:
            temp_image = self.image
        for i in range(0, smoothen):
            temp_image = temp_image.filter(ImageFilter.SMOOTH)
        if bw:
            temp_image = temp_image.point(lambda i: i > bw_threshold and 255 or 0)

        delta_x = int(round(float(temp_image.size[0]) / float(width)))
        delta_y = 2*delta_x

        y = 0
        strings = []

        # convert image into ascii/unicode strings
        while True:
            if y*delta_y > temp_image.size[1]:
                break
            s = ''
            for x in range(0, width):
                tile = temp_image.crop((x*delta_x, y*delta_y, x*delta_x+delta_x, y*delta_y+delta_y))
                if method == self.HAMMING:
		    s += self._find_symbol(tile)
                elif method == self.AVERAGE:
                    if not unic:
                        avg_symbols = AVG_SYMBOLS['ascii']
                    else:
                        avg_symbols = AVG_SYMBOLS['unicode']
                    t = self._average(tile)
                    idx = (255-t) / (255/len(avg_symbols))
                    idx = min(idx, len(avg_symbols)-1)
                    s += avg_symbols[idx]
                del tile
            strings.append(s)
            y += 1

        del temp_image

        return strings

    def _find_symbol(self, tile):
        diff = sys.maxint
        idx = -1
        for i, ref_img in enumerate(self._ref_images):
            new_diff = self._dist(tile, ref_img)
            if new_diff < diff:
                diff = new_diff
                idx = i
        return SYMBOLS[idx]

    def _dist(self, tile, reference_image):
        ''' Calculates the distance of an image to a reference image'''
        reference_image = reference_image.resize(tile.size, Image.NEAREST)
        xor = ImageChops.difference(tile, reference_image).getcolors()
        for cnt, color in xor:
            if color==255:
                return cnt
        return 0

    def _average(self, tile):
        colors = tile.getcolors()
        avg = 0 
        su  = 0
        for color in colors:
            su += color[0]
            avg += color[0]*color[1]
        avg /= su
        return avg


