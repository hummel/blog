Title: Making Maps with Python
date: 2015-01-23 04:00
comments: true
slug: Maps with Python

I made a map!  I recently found a great tutorial on [Beneath Data](http://beneathdata.com) on how to visualize your location history from Google.  I've been wanting to do something like this for a while, so I downloaded my location history for the past few years using [Takeout](https://www.google.com/settings/takeout), and made a quick plot of all the flights I've taken recently.

To do this, you'll need the following Python packages:

- [Matplotlib](http://matplotlib.org/) + [Basemap](http://matplotlib.org/basemap)
- [Numpy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [Shapely](https://pypi.python.org/pypi/Shapely)
- [Fiona](https://pypi.python.org/pypi/Fiona)
- [Descartes](https://pypi.python.org/pypi/descartes)

Far and above the easiest way to acquire these is to use the ``conda`` package manager provided by [Continuum Analytics](https://store.continuum.io/cshop/anaconda/) with the [Anaconda](http://docs.continuum.io/anaconda/) Python Distribution. Once you've got Anaconda installed (which includes matplotlib, numpy and pandas), you can install (almost) all the necessary packages as follows:

    conda install basemap shapely fiona

Unfortunately ``descartes`` isn't available in Continuum's official repositories, but it _is_ available from the community repositories on [binstar.org](binstar.org). Go there, search for 'descartes', and install it from the repository of your choice or just do the following:

On Linux:

	      conda install -c https://conda.binstar.org/auto descartes

On Mac OS X:

	      conda install -c https://conda.binstar.org/asmeurer descartes	   


With everything installed, it was easy to make a map showing all the flights I've taken in the past ~4 or so years by following this [tutorial](http://beneathdata.com/how-to/visualizing-my-location-history/) (scroll down to the second half).  Awesome!

{% img /images/flights.png All flights in the past three years%}

My trip to Japan for the [First Stars IV](http://tpweb2.phys.konan-u.ac.jp/~FirstStar4/) conference dominates the first map; zooming in to just North America helps a bit:

{% img /images/US_flights.png Western Hemisphere Flights%}

