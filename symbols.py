# Unicode symbols

_BLOCK_ELEMENTS = [
    u'\u2580', u'\u2581', u'\u2582', u'\u2583',
    u'\u2584', u'\u2585', u'\u2586', u'\u2587',
    u'\u2588', u'\u2589', u'\u258a', u'\u258b',
    u'\u258c', u'\u258d', u'\u258e', u'\u258f',
    u'\u2590',
    u'\u2594', u'\u2595', u'\u2596', u'\u2597',
    u'\u2598', u'\u2599', u'\u259a', u'\u259b',
    u'\u259c', u'\u259d', u'\u259e', u'\u259f',
]

_GEOM_SHAPES_EXERPT = [
    u'\u25a0', u'\u25ac', u'\u25ae',
    u'\u25b2', u'\u25b6', 
    u'\u25bc', u'\u25c0', 
    u'\u25e2', u'\u25e3', u'\u25e4', u'\u25e5',
    u'\u25fc', u'\u25fe',
]

SYMBOLS = [u'\u0020']
SYMBOLS.extend(_BLOCK_ELEMENTS)
SYMBOLS.extend(_GEOM_SHAPES_EXERPT)

AVG_SYMBOLS = {'ascii':  [' ', '.', ':', 'o', 'O', '8'],
               'unicode': [' ',       u'\u2581', u'\u2582', u'\u2583',
                           u'\u2584', u'\u2585', u'\u2586', u'\u2587',
                           u'\u2588'
                          ]
}

