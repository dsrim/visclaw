
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

import numpy as np
import matplotlib.pyplot as plt

from clawpack.geoclaw import topotools

try:
    TG32412 = np.loadtxt('32412_notide.txt')
except:
    print "*** Could not load DART data file"

#--------------------------
def setplot(plotdata):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    from clawpack.visclaw import colormaps, geoplot
    from numpy import linspace

    plotdata.clearfigures()  # clear any old figures,axes,items data


    # To plot gauge locations on pcolor or contour plot, use this as
    # an afteraxis function:

    #def addgauges(current_data):
    #    from clawpack.visclaw import gaugetools
    #    gaugetools.plot_gauge_locations(current_data.plotdata, \
    #         gaugenos='all', format_string='ko', add_labels=True)
    

    #-----------------------------------------
    # Figure for Slice
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Surface', figno=0)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')        #temporary
    plotaxes.title = 'Surface'
    plotaxes.scaled = True

    plotitem = plotaxes.new_plotitem(plot_type='3d_slice')
    plotitem.pcolor_cmin = -10.0          #temporary keyword pcolor_cmin
    plotitem.pcolor_cmax= 10.0
    plotitem.pcolor_cmap = 'Spectral'
    plotitem.amr_celledges_show = [1,1,0,0,0,0]
    plotitem.amr_max_level = 2                  # set maximum level to plot
    plotitem.update_view = [-1,-1,-1,0,0,0]     # set viewpoint
    plotitem.plot_var = 0

    

    #-----------------------------------------
    
    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    #plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_framenos = [1,2,3,4]       # list of frames to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?
    plotdata.slice3d = True

    return plotdata

