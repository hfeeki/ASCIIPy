ASCIIPy
-------

Install
-------

Try this first:

    python setup.py install

If you get this:

    IOError: decoder jpeg not available.

you need to install libjpeg-dev and then re-install PIL from source like so:

    sudo apt-get install libjpeg-dev

    wget http://effbot.org/downloads/Imaging-1.1.7.tar.gz
    tar xvf Imaging-1.1.7
    cd Imaging-1.1.7

Open setup.py in an editor of your choice,

    vim setup.py

find the line containing

    JPEG_ROOT = None

and change "None" to the path containing the libjpeg library. On my system it is this (of course, this may differ from system to system):

    JPEG_ROOT = '/usr/lib32'

Then quit the editor and install PIL:

    python setup.py install

