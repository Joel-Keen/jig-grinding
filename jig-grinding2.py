import math

tooltip_diameter = 1.5 #mm
tooltip_length = 4 #mm
tooltip_radius = tooltip_diameter/2

feedrate_horizontal = 0.005 #mm/s

# OSCILLATE Axis, Peak to Peak displacement, Freq Hz, Number of full sinusoidal cycles

oscillate_displacement = 0.2 #mm

oscillate_frequency = 0.15 #Hz

# Pure chop grinding, assuming vertical motion
oscillate_period = 1/oscillate_frequency
chop_period = oscillate_period/2

chop_cusp_width = chop_period*feedrate_horizontal
print("cusp width " + str(chop_cusp_width))
chop_cusp_depth = tooltip_radius - math.sqrt((tooltip_radius**2)-(chop_cusp_width**2))
print("cusp Depth " + str(chop_cusp_depth))

# Sinusoidal grinding effective feedrate

feedrate_effective_maximum = oscillate_displacement*oscillate_frequency*math.pi

print("max feed " + str(feedrate_effective_maximum))

