=======
ASCIIPy
=======

ASCIIPy is a small library for turning images into ASCII or UNICODE art images.

Converting an image
-------------------

ASCIIPy comes with a console script called "asciipy", which should be available after installation. Try its "--help" option.

Examples
--------

Here is an example of how to convert the test gif into a Unicode art image:

::

	(asciipy)sven@slartibartfast:~/envs/asciipy/src/asciipy$ asciipy asciipy/tests/A.gif 127 50
							  
							  
							  
			  ▇▇▇▇▇▇▇▇▇▇▇▇▖                   
			 ▟█████████████▖                  
			▐██████████████▙                  
		       ▗████████████████▙                 
		       ██████████████████▖                
		      ▟████████▛▝█████████▖               
		     ▐█████████  ▜████████▙               
		    ▗█████████▘   ▜████████▙              
		    █████████▛    ▝█████████▖             
		   ▟█████████      ▐█████████▖            
		  ▐█████████▘       ▜████████▙            
		 ▗█████████▛        ▝█████████▙           
		 ▟█████████▄▄▄▄▄▄▄▄▄▄▟█████████▖          
		▟███████████████████████████████          
	       ▗████████████████████████████████▙         
	      ▗██████████████████████████████████▌        
	      ▟█████████▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▜█████████▖       
	     ▟█████████▍                 ██████████       
	    ▗█████████▛                  ▝█████████▙      
	    ▀▀▀▀▀▀▀▀▀▀                    ▀▀▀▀▀▀▀▀▀▀▎     
							  

Here is an example of how to convert the test gif into a Unicode art image, using the faster "average" method:

::                                              

	(asciipy)sven@slartibartfast:~/envs/asciipy/src/asciipy$ asciipy asciipy/tests/A.gif 127 50 --method=AVERAGE
							  
							  
							  
			  ▆▇▇▇▇▇▇▇▇▇▇▇▄                   
			 ▆█████████████▂                  
			▄███████████████                  
		       ▁████████████████▆                 
		       ▇█████████████████▃                
		      ▆████████▆▂█████████▁               
		     ▃█████████▁ ▅████████▇               
		    ▁█████████▃   ▇████████▆              
		    ▇████████▆    ▁█████████▃             
		   ▅█████████      ▄█████████▁            
		  ▃█████████▂       ▇████████▇            
		 ▁█████████▅        ▁█████████▅           
		 ▇█████████▄▄▄▄▄▄▄▄▄▄▇█████████▃          
		▅███████████████████████████████▁         
	       ▃████████████████████████████████▇         
	      ▁██████████████████████████████████▅        
	      ▇█████████▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅█████████▃       
	     ▅█████████▄                 ██████████▁      
	    ▂█████████▆                  ▂█████████▇      
	    ▅▆▆▆▆▆▆▆▆▆▁                   ▄▆▆▆▆▆▆▆▆▆▂     
							  

Finally, here is an example of how to convert the test gif into an ASCII art image:

::

	(asciipy)sven@slartibartfast:~/envs/asciipy/src/asciipy$ asciipy asciipy/tests/A.gif 127 50 --method=AVERAGE --ascii
							  
							  
							  
			  OOOOOOOOOOOO:                   
			 O8888888888888.                  
			:888888888888888                  
		       .8888888888888888O                 
		       888888888888888888:                
		      O88888888O.888888888.               
		     :888888888  o888888888               
		    .888888888:   888888888O              
		    888888888O    .888888888:             
		   o888888888      o888888888.            
		  :888888888.       O888888888            
		 .888888888o        .888888888o           
		 8888888888o:::::::::O888888888:          
		o8888888888888888888888888888888          
	       :88888888888888888888888888888888O         
	       8888888888888888888888888888888888o        
	      O888888888.               o888888888:       
	     o888888888:                 8888888888       
	    .888888888O                  .888888888O      
	    oOOOOOOOOO                    :OOOOOOOOO.     
							  
							  


Install / Troubleshooting
-------------------------

Try to install ASCIIPy and run the test suite:

::

    cd asciipy
    python setup.py install
    easy_install nose
    nosetests

If you get this:

::

    IOError: decoder jpeg not available.

you need to install libjpeg-dev and then re-install PIL from source like so:

::

    sudo apt-get install libjpeg-dev

    wget http://effbot.org/downloads/Imaging-1.1.7.tar.gz
    tar xvf Imaging-1.1.7
    cd Imaging-1.1.7

Open setup.py in an editor of your choice,

::

    vim setup.py

find the line containing

::

    JPEG_ROOT = None

and change "None" to the path containing the libjpeg library. On my system it is this (of course, this may differ from system to system):

::

    JPEG_ROOT = '/usr/lib32'

Then quit the editor and install PIL:

::

    python setup.py install

