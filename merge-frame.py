import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
import matplotlib.gridspec as gridspec
from matplotlib.patches import ConnectionPatch
import os
# Frames you want to make. You must have the same number of plots and MD-snapshots
frames=3
# Starting time step
cur_ns = 1
for f in range(frames):

    fig = plt.figure(figsize=(30,15))
    fig.subplots_adjust(top=0.98, bottom=0.02, right=0.98, left=0.02)
    # Adding divider and sub divider 
    gs = gridspec.GridSpec(1,2, figure=fig, hspace=0,wspace=0)
    sub_gs = gs[0].subgridspec(2,1, hspace=0,wspace=0)
    # Linking gridspace to snapshot
    ax = fig.add_subplot(gs[1])
    # Linking gridspace to plot  
    ax2 = fig.add_subplot(sub_gs[0])
    ax3 = fig.add_subplot(sub_gs[1])
    
    # Adding the MD simulation snapshots
    image = plt.imread('md-snapshots/frame.%04d.ppm' % (membrane,protein,config,f))
    # Adding the plots
    image2 = plt.imread('plots/depth_%04d.png'%(f))
    image3 = plt.imread("plots/contacts_%04d.png"%(f))
    

    ax.imshow(image)
    ax2.imshow(image2)
    ax3.imshow(image3)
    
    ax.axis('off')
    ax2.axis('off')
    ax3.axis('off')
    # Adding the text in each frame
    ax.text(0.3, 0.95, 'Membrane = %s'%membranelabel[k], fontsize=28,transform=ax.transAxes, ha='right', va='bottom')
    ax.text(0.345, 0.91, 'Protein = %s'%proteinlabel[j], fontsize=28,transform=ax.transAxes, ha='right', va='bottom')
    ax2.text(0.5, 1, 'Time = %04d ns' % (cur_ns), fontsize=32,transform=ax2.transAxes, ha='right', va='bottom')
    
    # Saving the merge file with snapshot and plots
    plt.savefig('finalframe.%04d.png' % f, dpi=100)
    plt.close(fig)
    
    cur_ns = cur_ns+1
exit()