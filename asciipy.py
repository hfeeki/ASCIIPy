#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import optparse
import math

import Image, ImageChops, ImageFilter, ImageMath, ImageFont, ImageDraw

from lib import create_image, dist, Method, edgify

# *** Unicode Symbols ***
# Blockelements
BLOCK_ELEMENTS = [
    u'\u2580', u'\u2581', u'\u2582', u'\u2583',
    u'\u2584', u'\u2585', u'\u2586', u'\u2587',
    u'\u2588', u'\u2589', u'\u258a', u'\u258b',
    u'\u258c', u'\u258d', u'\u258e', u'\u258f',
    u'\u2590', u'\u2591', u'\u2592', u'\u2593',
    u'\u2594', u'\u2595', u'\u2596', u'\u2597',
    u'\u2598', u'\u2599', u'\u259a', u'\u259b',
    u'\u259c', u'\u259d', u'\u259e', u'\u259f',
]

# Miscellaneous Symbols (exerpt)

MISC_SYMBOLS = [
    u'\u2630', u'\u2631', u'\u2632', u'\u2633',
    u'\u2634', u'\u2635', u'\u2636', u'\u2637',
    u'\u268a', u'\u268b', u'\u268c', u'\u268d',
    u'\u268e', u'\u268f',
]

# Geometric Shapes
GEOMETRIC_SHAPES = [
    u'\u25a0', u'\u25a1', u'\u25a2', u'\u25a3',
    u'\u25a4', u'\u25a5', u'\u25a6', u'\u25a7',
    u'\u25a8', u'\u25a9', u'\u25aa', u'\u25ab',
    u'\u25ac', u'\u25ad', u'\u25ae', u'\u25af',
    u'\u25b0', u'\u25b1', u'\u25b2', u'\u25b3',
    u'\u25b4', u'\u25b5', u'\u25b6', u'\u25b7',
    u'\u25b8', u'\u25b9', u'\u25ba', u'\u25bb',
    u'\u25bc', u'\u25bd', u'\u25be', u'\u25bf',
    u'\u25c0', u'\u25c1', u'\u25c2', u'\u25c3',
    u'\u25c4', u'\u25c5', u'\u25c6', u'\u25c7',
    u'\u25c8', u'\u25c9', u'\u25ca', u'\u25cb',
    u'\u25cc', u'\u25cd', u'\u25ce', u'\u25cf',
    u'\u25d0', u'\u25d1', u'\u25d2', u'\u25d3',
    u'\u25d4', u'\u25d5', u'\u25d6', u'\u25d7',
    u'\u25d8', u'\u25d9', u'\u25da', u'\u25db',
    u'\u25dc', u'\u25dd', u'\u25de', u'\u25df',
    u'\u25e0', u'\u25e1', u'\u25e2', u'\u25e3',
    u'\u25e4', u'\u25e5', u'\u25e6', u'\u25e7',
    u'\u25e8', u'\u25e9', u'\u25ea', u'\u25eb',
    u'\u25ec', u'\u25ed', u'\u25ee', u'\u25ef',
    u'\u25f0', u'\u25f1', u'\u25f2', u'\u25f3',
    u'\u25f4', u'\u25f5', u'\u25f6', u'\u25f7',
    u'\u25f8', u'\u25f9', u'\u25fa', u'\u25fb',
    u'\u25fc', u'\u25fd', u'\u25fe', u'\u25ff',
]

GEOM_SHAPES_EXERPT = [
    u'\u25a0', u'\u25aa', u'\u25ac', u'\u25ae',
    u'\u25b2', u'\u25b4', u'\u25b6', u'\u25b8',
    u'\u25bc', u'\u25be', u'\u25c0', u'\u25c2',
    u'\u25c6', u'\u25cf', u'\u25d6', u'\u25d7',
    u'\u25dc', u'\u25dd', u'\u25de', u'\u25df',
    u'\u25e2', u'\u25e3', u'\u25e4', u'\u25e5',
    u'\u25fc', u'\u25fe',
]

# Symbols to use
SYMBOLS = [unicode(c) for c in ' ,.;:/\\\'"-|']
SYMBOLS.extend(BLOCK_ELEMENTS)
SYMBOLS.extend(GEOM_SHAPES_EXERPT)
SYMBOLS.extend(MISC_SYMBOLS)

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('--invert', action='store_true', dest='invert', default=False, help='invert image [default: %default]')
    parser.add_option('--smoothen', type="int", action='store', dest='smoothen', default=0, help='amount of smoothening the image [default: %default]')
    parser.add_option('--ignore', action='store_true', dest='ignore', default=False, help='ignore warnings [default: %default]')
    parser.add_option('--method', action='store', dest='method', default='hamming', help='method of symbol matching [default: %default]')
    opts, args = parser.parse_args()
    
    if len(args) != 3:
        sys.exit('usage: %s [options] <input image> <binary threshold> <output width>' % sys.argv[0])

    image = Image.open(args[0])
    image = edgify(image, int(args[1]), opts.smoothen, opts.invert)

    image.save('%s_edgified.gif' % args[0])

    # dimensions of the output ascii image
    output_width = int(args[2])

    input_width, input_height = image.size

    delta_x = int(round(float(input_width) / float(output_width)))
    delta_y = 2*delta_x

    print "tile size (%d, %d)" % (delta_x, delta_y)
    if delta_x < 3 or delta_y < 3:
        print "WARNING: tiles too small"
        if not opts.ignore:
            sys.exit('exiting (use --ignore to ignore this warning and continue)')

    print "Loading font ..."
    font_name = 'FreeMono.ttf'
    font = ImageFont.truetype('fonts/%s' % font_name, min(delta_x, delta_y))

    print "Generating %d reference images ..." % (len(SYMBOLS))
    im = create_image(SYMBOLS[0], font, delta_x, delta_y)
    ref_images = [im]

    for char in SYMBOLS[1:]:
        im = create_image(char, font, delta_x, delta_y)
        ref_images.append(im)

    print "Generating ASCII/UNICODE image ..."
    s2 = u''
    y = 0
    while True:
        if y*delta_y > input_height:
            break
        for x in range(0, output_width):
            tile = image.crop((x*delta_x, y*delta_y, x*delta_x+delta_x, y*delta_y+delta_y))
            diff = sys.maxint
            idx = -1
            for i, ref_img in enumerate(ref_images):
                if opts.method == 'hamming':
                    new_diff = dist(tile, ref_img, Method.HAMMING)
                elif opts.method == 'zncc':
                    new_diff = dist(tile, ref_img, Method.ZNCC)
                if new_diff < diff:
                    diff = new_diff
                    idx = i
                s2 += SYMBOLS[idx]
        s2 += '\n' 
        y += 1

    print s2
