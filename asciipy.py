#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import optparse

from converter import ImageConverter

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('--invert', action='store_true', dest='invert', default=False, help='invert image [default: %default]')
    parser.add_option('--smoothen', type="int", action='store', dest='smoothen', default=0, help='amount of smoothening the image [default: %default]')
    parser.add_option('--ignore', action='store_true', dest='ignore', default=False, help='ignore warnings [default: %default]')
    parser.add_option('--method', action='store', dest='method', default='hamming', help='method of symbol matching [default: %default]')
    parser.add_option('--edgify', action='store_true', dest='edgify', default=False, help='detect edges [default: %default]')
    parser.add_option('--ascii', action='store_true', dest='ascii', default=False, help='use ASCII symbols instead of UNICODE [default: %default]')
    parser.add_option('--bw', action='store_true', dest='bw', default=False, help='turn into B/W [default: %default]')
    opts, args = parser.parse_args()
    
    if len(args) != 3:
        sys.exit('usage: %s [options] <input image> <binary threshold> <output width>' % sys.argv[0])


    ic = ImageConverter(args[0])
    strings = ic.run(int(args[2]), not opts.ascii, ImageConverter.HAMMING if opts.method=='hamming' else ImageConverter.AVERAGE, opts.bw, int(args[1]), int(opts.smoothen), opts.edgify)
    print '\n'.join(strings)

