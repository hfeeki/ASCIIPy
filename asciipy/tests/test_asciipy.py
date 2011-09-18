import os

from asciipy.lib.converter import ImageConverter

BASE = os.path.dirname(__file__)

A_STRS = [
'                                                  ',
'                                                  ',
'                                                  ',
'                  OOOOOOOOOOOO:                   ',
'                 O8888888888888.                  ',
'                :888888888888888                  ',
'               .8888888888888888O                 ',
'               888888888888888888:                ',
'              O88888888O.888888888.               ',
'             :888888888  o888888888               ',
'            .888888888:   888888888O              ',
'            888888888O    .888888888:             ',
'           o888888888      o888888888.            ',
'          :888888888.       O888888888            ',
'         .888888888o        .888888888o           ',
'         8888888888o:::::::::O888888888:          ',
'        o8888888888888888888888888888888          ',
'       :88888888888888888888888888888888O         ',
'       8888888888888888888888888888888888o        ',
'      O888888888.               o888888888:       ',
'     o888888888:                 8888888888       ',
'    .888888888O                  .888888888O      ',
'    oOOOOOOOOO                    :OOOOOOOOO.     ',
'                                                  ',
'                                                  ',
]


class TestASCIIPy(object):
    def test_convert_image(self):
        ic = ImageConverter(os.path.join(BASE, 'A.gif'))
           res = ic.run(width=50, unic=False, method=ImageConverter.AVERAGE, bw=False, bw_threshold=200, smoothen=0, edgify=False)

        assert len(res) == len(A_STRS), 'Expected no. of lines to be %d, but got %d' % (len(A_STRS), len(res))

        for i, line in enumerate(res):
            assert line == A_STRS[i], 'Expected line no. %d to be:\n\n"%s"\n\nbut got:\n\n"%s"' % (i, A_STRS[i], line)

