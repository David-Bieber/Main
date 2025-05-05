import matplotlib.pyplot as plt

def set_matplotlib_defaults():
    plt.rcParams['axes.titlesize'] = 20  # Title size
    plt.rcParams['axes.labelsize'] = 18  # Label size
    plt.rcParams['xtick.labelsize'] = 16  # X-axis tick label size
    plt.rcParams['ytick.labelsize'] = 16  # Y-axis tick label size
    
    plt.rcParams['figure.figsize'] = (10, 6) # figsize default

    # Default line color cycle (use a color palette)
    plt.rcParams['axes.prop_cycle'] =  plt.cycler(color=[
    '#1b9e77',  # Teal
    '#d95f02',  # Orange
    '#7570b3',  # Purple
    '#e7298a',  # Pink
    '#66a61e',  # Olive green
    '#e6ab02',  # Mustard
    '#a6761d',  # Brown
    '#666666',  # Gray
    '#1f78b4',  # Blue
    '#b2df8a'   # Light green
])
    
    plt.rcParams['grid.color'] = 'gray'  # Set grid color
    plt.rcParams['grid.linestyle'] = '--'  # Set grid line style
    plt.rcParams['grid.linewidth'] = 0.5  # Set grid line width
    
    # Default line width for plot lines
    plt.rcParams['lines.linewidth'] = 2  # Set default line width
    plt.rcParams['lines.marker'] = ''  # Set default marker
    plt.rcParams['lines.markersize'] = 6  # Set default marker size

    # Legends
    plt.rcParams['legend.fontsize'] = 16  # Set legend font size