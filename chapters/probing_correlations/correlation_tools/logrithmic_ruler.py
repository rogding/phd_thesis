with sns.plotting_context('talk'), sns.axes_style('ticks'):
    a0 = 5.2917721067e-2
    savekwargs = {'bbox_inches':'tight','dpi':500}
    f,ax = plt.subplots()

    ax2 = ax.twiny()

    ax.set_xlabel('Interparticle Separation (nm)')
    ax2.set_xlabel('Interparticle Separation ($a_0$)')
    ax.set_xscale('log')
    ax2.set_xscale('log')
    ax.set_xlim(0.5,2500)
    ax2.set_xlim(ax.get_xlim()[0]/a0,ax.get_xlim()[1]/a0)
    ax2.tick_params(which='both',direction='in',pad=0)
    ax.tick_params(which='both',direction='in',pad=3)
    ax.set_ylim(0,1)
    ax.yaxis.set_ticks([])
    f.savefig('blank.png',**savekwargs)
    
    ax.hlines(y=0.1,xmin=1,xmax=10,color='red')
    ax.annotate(xy=(3,0.14),s='PAS$\sim R_{vdW}$',ha='center',va='center')
    ax.annotate(s='3-body Loss$\sim R=0$',xy=(.5,0.25),xytext=(7,0.25),
                ha='center',va='center',arrowprops={'arrowstyle':'simple','color':'k'})
    
    f.savefig('short_range.png', **savekwargs)
    
    ax.hlines(y=0.7,xmin=250,xmax=1064,color='red')
    ax.annotate(s='QGM$\sim \lambda/2$',xy=(525,0.74),ha='center',va='center')
    f.savefig('long_range.png',**savekwargs)
    
    ax.hlines(y=0.5, xmin=1.8*(20-3.37)**2*a0, xmax=1.8*(100-3.37)**2*a0,color='blue')
    ax.annotate(s='Rydberg Molecules$\sim 2n^2$', xy=(150,0.54),ha='center',va='center')
    ax.annotate(s='$n=20$',xy=(1.8*(20-3.37)**2*a0,0.45),ha='center',va='center')
    ax.annotate(s='$n=100$', xy=(1.8*(100-3.37)**2*a0,0.45),ha='center',va='center')
    
    f.savefig('ryd_molecules.png',**savekwargs)