import sys

sys.path.insert(0,'..')

import matplotlib
from matplotlib import pyplot as plt
# from ..energy_diagram import EnergyDiagram
import energy_diagram as ed


fig, ax = plt.subplots(dpi=150, figsize=(10,5))
# diagram = ed.EnergyDiagram(fig, ax)
diagram = ed.EnergyDiagram(fig, ax)

ground_state  = -252.2388493 *  627.509474
TS4           = -251.9246703 *  627.509474 - ground_state 
GSfinal       = -252.1687934 *  627.509474 - ground_state 
TS3           = -251.9622684 *  627.509474 - ground_state 
TS2_2_fwd     = -252.1354547 *  627.509474 - ground_state 
TS1_2_rev     = -252.0866090 *  627.509474 - ground_state 
TS1_2_fwd_fwd = -252.1355974 *  627.509474 - ground_state 


# zerando o GS
ground_state -= ground_state

# round_to = 3
#f'{ground_state:.2f}'
diagram.energy_level(ground_state,  0,  color='k') #k')
diagram.energy_level(TS4,           1,  color='k') #b')
diagram.energy_level(TS3,           2,  color='k') #r')
diagram.energy_level(TS2_2_fwd,     3,  color='k') #y')
diagram.energy_level(TS1_2_rev,     3,  color='k') #y')
diagram.energy_level(TS1_2_fwd_fwd, 4,  color='k') #g')
diagram.energy_level(GSfinal,       5,  color='k') #k')

diagram.level_text(ground_state,  f'{ground_state:.1f}',  position=0)
diagram.level_text(TS4,           f'{TS4:.1f}',           position=1)
diagram.level_text(TS3,           f'{TS3:.1f}',           position=2)
diagram.level_text(TS2_2_fwd,     f'{TS2_2_fwd:.1f}',     position=3)
diagram.level_text(TS1_2_rev,     f'{TS1_2_rev:.1f}',     position=3)
diagram.level_text(TS1_2_fwd_fwd, f'{TS1_2_fwd_fwd:.1f}', position=4)
diagram.level_text(GSfinal,       f'{GSfinal:.1f}',       position=5)

diagram.level_text(ground_state,  '0', placement='bottom', position=0)
diagram.level_text(TS4,           '4', placement='bottom', position=1)
diagram.level_text(TS3,           '3', placement='bottom', position=2)
diagram.level_text(TS2_2_fwd,     ' ', placement='bottom', position=3)
diagram.level_text(TS1_2_rev,     ' ', placement='bottom', position=3)
diagram.level_text(TS1_2_fwd_fwd, ' ', placement='bottom', position=4)
diagram.level_text(GSfinal,       ' ', placement='bottom', position=5)


alpha = 0.4
diagram.link_levels(0, 1, alpha=alpha)
diagram.link_levels(1, 2, alpha=alpha)
diagram.link_levels(1, 5, alpha=alpha)
diagram.link_levels(1, 3, alpha=alpha)
diagram.link_levels(1, 4, alpha=alpha)
diagram.link_levels(2, 3, alpha=alpha)
diagram.link_levels(2, 4, alpha=alpha)
diagram.link_levels(3, 5, alpha=alpha)
diagram.link_levels(4, 6, alpha=alpha)
diagram.link_levels(5, 6, alpha=alpha)



diagram.plot_diagram(show_ids=True)
# plt.savefig("sym_energy_diagram.png", bbox_inches="tight", dpi=300)
#             show_IDs=True)

plt.show()

# plt.savefig("sym_energy_diagram.png", bbox_inches="tight", dpi=300)
#             show_IDs=True)