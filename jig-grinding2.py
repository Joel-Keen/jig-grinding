import math

tooltip_diameter = 3 #mm
tooltip_length = 4 #mm
tooltip_radius = tooltip_diameter/2

feedrate_horizontal = 0.005 #mm/s

# OSCILLATE Axis, Peak to Peak displacement, Freq Hz, Number of full sinusoidal cycles

oscillate_displacement = 0.8 #mm

oscillate_frequency = 0.2 #Hz

# Pure chop grinding, assuming vertical motion
oscillate_period = 1/oscillate_frequency
chop_period = oscillate_period/2

chop_cusp_width = chop_period*feedrate_horizontal
print("chop cusp width " + str(chop_cusp_width))

chop_cusp_depth = tooltip_radius - math.sqrt((tooltip_radius**2)-(chop_cusp_width**2))
print("chop cusp Depth " + str(chop_cusp_depth))

# Modified chop grinding, with observed approximation

mod_cusp_width = chop_cusp_width/3
print("mod cusp width " + str(mod_cusp_width))

mod_cusp_depth = chop_cusp_depth*2
print("mod cusp Depth " + str(mod_cusp_depth))

# Sinusoidal grinding effective feedrate

feedrate_effective_maximum = oscillate_displacement*oscillate_frequency*math.pi

print("max feed " + str(feedrate_effective_maximum))

