import matplotlib
from matplotlib.lines import Line2D
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter



class EnergyDiagram:
    """
    EnergyDiagram class.
        
    Contains the methods to plot a chemistry energy diagram.
    
    Initialization parameters:
    
    fig -> object
    The initialized Matplotlib figure object from the subplot method 
    with the desired dimensions and dpi.
    
    ax -> object
    The axis of the initialized Matplolib figure object, from the subplot 
    method.
    
    level_size -> float
    The size of the energy level. Since the levels are automatically
    scale by Matplotlib, the size is proportional to the other adjusting
    values. It shoudn't in general be changed.
    
    space -> float
    The size of the space between the levels.
    
    vertical_offset -> float
    The amount of vertical space between the level and the top and bottom
    texts. Is is a percentage of the difference between the max and min
    energy values.
    
    horizontal_offset -> float
    The amount of horizontal space between the text and the end of each 
    level. It is not a percentage, but the distance in x axis units.
    
    link_end_offset -> float
    The percentage of increase in distance between the end of the linking
    line and the start of the energy level. It is needed because otherwise
    they do not match.
    
    link_begin_offset -> float
    The same as link_end_offset, but for the beginning of the link.
"""

    def __init__(self, 
                 fig,
                 ax,
                 level_size=30,
                 space=20,
                 vertical_offset=0.02,
                 horizontal_offset=6,
                 link_end_offset=1.021,
                 link_begin_offset=1.02):

        
        # Define the arrays to store the parameters
        self.ID = []
        self.energy = []
        self.positions = []
        self.text = []
        self.text_energy = []
        self.text_position = []
        self.text_placement = []
        self.text_color = []
        self.links = []
        self.link_alpha = []
        self.link_width = []
        self.level_colors = []
        self.link_colors = []
        self.level_linestyle = []
        self.link_linestyle = []
        self.position_names = []
        self.text_offset = []

        # Define class atributes to store the init variabes
        self.fig = fig
        self.ax = ax
        self.level_size = level_size
        self.space = space
        self.h_offset = horizontal_offset
        self.v_offset = vertical_offset
        self.link_end_offset = link_end_offset
        self.link_begin_offset = link_begin_offset
    
    
    
    def energy_level(self, 
                     energy,
                     position,
                     level_color = 'k',
                     level_style = '-'):
        '''
        Method of the EnergyDiagram class.
        
        It adds a energy level at a certain energy and position, 
        with color and style of the line as parameters.
        
        Arguments:
        
        energy   -> float 
            y value for the added energy level.                        
        
        position -> integer
            Position of the level in the graph. The position starts
            at 0 and indicates where should the energy level be inserted.
            A reaction with reactants, transition state and products would
            have three positions for each step, 0, 1, 2 respectively.
            Multiple energy levels can have the same position.
        
        level_color -> string
            Level color following Matplotlib standards.
        
        level_style -> string
            Level style following Matplotlib standards.           
        '''
        
        self.energy.append(energy)
        self.positions.append(position)
        self.level_colors.append(level_color)
        self.level_linestyle.append(level_style)
        
        

    def add_text_to_level(self,
                          energy,
                          text,
                          position = 0,
                          color = 'k',
                          placement = 'top',
                          text_offset = -1):
        """
        Method of the EnergyDiagram class. It adds text to a level,
        with a certain energy(y value).

        Arguments:

        energy -> float
        Y position for the text.

        text -> string
        Text to be inserted in the diagram.

        text_color -> string
        Color of the text in the Matplotlib standard.

        text_position -> integer
        Position of the text in relation to the number of 
        steps in the reaction or diagram. If the reaction has
        3 steps, reactant, transition state and products, 
        there would be three positions, labeled 0, 1 and two
        for each step respectively.

        text_placement -> string
        Placement for the text around the level. The choices are
        'top', 'bottom', 'left' and 'right'.

        text_offset -> float
        Amount of extra space from the central point of the level
        that the text will be. It works horizontally for the left
        and right text, and vertically for the top and bottom texts.
        """
        
        if placement not in ['top', 'bottom', 'left', 'right']:
            raise ValueError('The variable text_placement must be one of the followin:\n"top", "bottom", "left" and "right".')
        
        if placement in ['top', 'bottom'] and text_offset == -1:
            text_offset = self.v_offset
        
        if placement in ['left', 'right'] and text_offset == -1:
            text_offset = self.h_offset
        
        
        self.text_energy.append(energy)
        self.text.append(text)
        self.text_color.append(color)
        self.text_placement.append(placement)
        self.text_position.append(position)
        self.text_offset.append(text_offset)
            
            
    def link_levels(self,
                    ID1,
                    ID2,
                    color='k',
                    link_style='--',
                    link_width=1,
                    alpha=0.6):
        """
        Method of the EnergyDiagram class. It adds a link between
        two levels.

        Arguments:

        ID1 -> integer
        The ID number of the first level. The ID is the entry number
        of a level. If the user adds three levels, they would be 
        level 0, 1 and 2, respectively, independent of the position
        in the diagram each has.

        ID2 -> integer
        Same as ID1.

        link_color -> string
        The color of the linking line. Follows Matplotlib standards.

        link_style -> string
        The style of the linking line. Follows Matplotlib standards.

        link_width -> float
        The width of the linking line. Follows Matplotlib standards.

        alpha -> float
        The opacity of the linking line, ranging from 0 to 1.
        """
        if ID1 > ID2:
            ID1, ID2 = ID2, ID1
        
        self.links.append([ID1, ID2])
        self.link_colors.append(color)
        self.link_linestyle.append(link_style)
        self.link_width.append(link_width)
        self.link_alpha.append(alpha)
    
    
    def plot_diagram(self,
                     top_spine=False,
                     right_spine=False,
                     bottom_spine=True,
                     left_spine=True,
                     x_axis_visible=False,
                     y_axis_visible=True,
                     fig_title='',
                     x_axis_label='',
                     y_axis_label='',
                     x_axis_ticks = [],
                     x_axis_ticks_labelsize=13,
                     number_y_bins=0,
                     figure_size=[], 
                     y_limit_offset=0.05):
        """
        Method of the EnergyDiagram class. It plots all the previously inserted
        energy levels, texts and links.
        
        Arguments:
        
        top_spine -> boolean
        Indicates whether to show or hide the top spine.
        
        right_spine -> boolean
        Indicates whether to show or hide the right spine.
        
        bottom_spine -> boolean
        Indicates whether to show or hide the bottom spine.
        
        left_spine -> boolean
        Indicates whether to show or hide the left spine.
        
        
        x_axis_visible -> boolean
        Indicates whether to show or hide the x axis.
        
        y_axis_visible -> boolean
        Indicates whether to show or hide the y axis.
        
        fig_title -> string
        The title of the diagram. It is left empty in case one doesn't want
        a title.
        
        x_axis_label -> string
        The label of the x axis, if needed.
        
        y_axis_label -> string
        The label of the y axis, if needed.
        
        x_axis_ticks -> list of strings
        List of custom string to serve as the ticks in the x axis. Example 
        of strings can be 'TS', of 'React.', 'Add.'. 
        
        x_axis_ticks_labelsize -> integer
        The size of the custom string ticks.
        
        number_y_bins -> integer
        The number of bins for the y axis.
        
        figure_size -> [float, float]
        A list with the dimensions of the diagram figure.
        
        y_limit_offset -> float
        The text over the level is not part of the scaling in Matplotlib. So
        in order to keep it below the top spine, the y axis must be increased
        by a small percentage, which is the y_limit_offset. 
        
"""
        
        
        

        # Plotting the energy levels
        level_bounds = self.level_size / 2
        for i in range(len(self.energy)):
            # The position is the initial point plus a multiple of the size of the 
            # energy levels plus the space between the levels. This multiple is the
            # the position, which is defined when adding the level.
            # First we find the x position of the center of the level:
            center_pos = level_bounds + (self.level_size + self.space)*self.positions[i]
            # Then we plot it
            self.ax.plot([center_pos+level_bounds,center_pos-level_bounds],
                         [self.energy[i], self.energy[i]],
                         color=self.level_colors[i],
                         linestyle=self.level_linestyle[i])
        
        
        

        # Plotting the links between the levels
        ID1 = 0
        ID2 = 1
        for i in range(len(self.links)):
            # We need to set the end of the level from which the link starts
            # and the beginning of the level from which the link ends. But
            # there is a catch, if we do not offset the starting link by 0.02
            # of the level size, it begins before the end of the level.
            #                                                           / position of the beginning of the level                      /
            ID1_level_end = self.level_size * self.link_begin_offset + (self.level_size + self.space)*self.positions[self.links[i][ID1]] 
            #                 / minus a percentage of the level size      /   / position of the beginning of the level                        /
            ID2_level_begin = -self.level_size * (self.link_end_offset - 1) + (self.level_size + self.space)*self.positions[self.links[i][ID2]] 
            
            self.ax.plot([ID1_level_end, ID2_level_begin],
                         [self.energy[self.links[i][ID1]],self.energy[self.links[i][ID2]]],
                         color=self.link_colors[i],
                         linestyle=self.link_linestyle[i],
                         linewidth=self.link_width[i],
                         alpha=self.link_alpha[i])
        
        
      
        # Plotting the texts
        voffset = (max(self.energy) - min(self.energy)) * self.v_offset
        for i in range(len(self.text)):
            valignment = 'center'
            halignment = 'center'
            # We need to define each of the positions (top, bottom, left and
            # right) alignment. The vertical alignement of the left and right
            # placements are center, and of the top and bottom are bottom and
            # top respectively (it's the bottom and top of the text!)
            if self.text_placement[i] == 'top':
                valignment = 'bottom'
            elif self.text_placement[i] == 'bottom':
                valignment = 'top'
            elif self.text_placement[i] == 'left':
                halignment = 'right'
            elif self.text_placement[i] == 'right':
                halignment = 'left'
            
            
            level_bounds = self.level_size / 2
            # Setting the position of the texts. For the top and bottom it is just
            # the center of the level, horizontally aligned. 
            if self.text_placement[i] in ['top', 'bottom']:
                # Center of level
                text_x_position = level_bounds + (self.level_size + self.space)*self.text_position[i]
                # Offset the text y position to make it prettier
                if self.text_placement[i] == 'top':
                    self.text_energy[i] += voffset
                else:
                    self.text_energy[i] -= voffset
                    
            
            # For the left and right placements, it is the center of the level, 
            # plus or minus half the level size times a offset.
            if self.text_placement[i] == 'left':
                text_x_position = (self.level_size + self.space)*self.text_position[i] - self.h_offset
            if self.text_placement[i] == 'right':
                text_x_position = self.level_size + (self.level_size + self.space)*self.text_position[i] + self.h_offset
            self.ax.text(text_x_position,
                         self.text_energy[i], # para o top e bottom a energia ainda não esta muit boa
                         self.text[i],
                         horizontalalignment=halignment,
                         verticalalignment=valignment,
                         fontsize='medium',
                         color=self.text_color[i])

            
            
        # Setting the options for the graph
        # Figure size:
        if figure_size:
            self.fig.set_size_inches(figure_size[0], figure_size[1])
        
        # Hide spines?
        self.ax.spines.top.set_visible(top_spine)
        self.ax.spines.bottom.set_visible(bottom_spine)
        self.ax.spines.left.set_visible(left_spine)
        self.ax.spines.right.set_visible(right_spine)
        
        # Hide x axis?
        x_axis = self.ax.axes.get_xaxis()
        x_axis.set_visible(x_axis_visible)
        
        # Set new y limits so the text falls within the graph box
        y_lim = self.ax.get_ylim()
        y_range = y_lim[1] - y_lim[0]
        # Change the upper y limit to a percentage of the range
        self.ax.set_ylim([y_lim[0], y_lim[1] + y_range * y_limit_offset])
        
        # Set the x axis ticks 
        if x_axis_ticks:
            xticks = list(set([ self.level_size / 2 + (self.level_size + self.space)*x for x in self.positions]))
            xticks.sort()
            self.ax.set_xticks(xticks)
            self.ax.set_xticklabels(x_axis_ticks)
            self.ax.tick_params(axis='x', labelsize=x_axis_ticks_labelsize)
        
        # Set the figure Title, and x and y labels
        self.ax.set(xlabel=x_axis_label, ylabel=y_axis_label, title=fig_title)
            
            
        return self.fig, self.ax
