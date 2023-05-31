import matplotlib
from matplotlib import pyplot as plt
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
diagram.energy_level(ground_state,  0,  level_color='k') #k')
diagram.energy_level(TS4,           1,  level_color='k') #b')
diagram.energy_level(TS3,           2,  level_color='k') #r')
diagram.energy_level(TS2_2_fwd,     3,  level_color='k') #y')
diagram.energy_level(TS1_2_rev,     3,  level_color='k') #y')
diagram.energy_level(TS1_2_fwd_fwd, 4,  level_color='k') #g')
diagram.energy_level(GSfinal,       5,  level_color='k') #k')

diagram.add_text_to_level(ground_state,  f'{ground_state:.1f}',  text_position=0)
diagram.add_text_to_level(TS4,           f'{TS4:.1f}',           text_position=1)
diagram.add_text_to_level(TS3,           f'{TS3:.1f}',           text_position=2)
diagram.add_text_to_level(TS2_2_fwd,     f'{TS2_2_fwd:.1f}',     text_position=3)
diagram.add_text_to_level(TS1_2_rev,     f'{TS1_2_rev:.1f}',     text_position=3)
diagram.add_text_to_level(TS1_2_fwd_fwd, f'{TS1_2_fwd_fwd:.1f}', text_position=4)
diagram.add_text_to_level(GSfinal,       f'{GSfinal:.1f}',       text_position=5)

diagram.add_text_to_level(ground_state,  '0', text_placement='bottom', text_position=0)
diagram.add_text_to_level(TS4,           '4', text_placement='bottom', text_position=1)
diagram.add_text_to_level(TS3,           '3', text_placement='bottom', text_position=2)
diagram.add_text_to_level(TS2_2_fwd,     ' ', text_placement='bottom', text_position=3)
diagram.add_text_to_level(TS1_2_rev,     ' ', text_placement='bottom', text_position=3)
diagram.add_text_to_level(TS1_2_fwd_fwd, ' ', text_placement='bottom', text_position=4)
diagram.add_text_to_level(GSfinal,       ' ', text_placement='bottom', text_position=5)


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



diagram.plot_diagram()
# plt.savefig("sym_energy_diagram.png", bbox_inches="tight", dpi=300)
#             show_IDs=True)

plt.show()

# plt.savefig("sym_energy_diagram.png", bbox_inches="tight", dpi=300)
#             show_IDs=True)