#View Settings
CAMERA_DISTANCE : float = 100


#Physics Settings
#Units of Distance are AU, and mass is Earth Masses, time is in days

g = 8.196655424*10**(-26) #M_earth*AU/day^2
time_step = 0.5 #days
cos_const = 1.1904*10**(-19)

#Celestial body data lists in units described above
#form of: [name str, mass float, display_radius float, x_initial, y_initial, z_initial floats, x,y,z init Vels]
sun_data:list = ["Sun",]
merc_data:list = ["Mercury",]
ven_data:list = ["Venus",]
ear_data:list = ["Earth",]
mars_data:list = ["Mars",]
jup_data:list = ["Jupiter",]
sat_data:list = ["Saturn",]
uran_data:list = ["Uranus",]
nept_data:list =["Neptune",]
plut_data:list = ["Pluto",]


#List of Bodies for input
bodies_input:list = [sun_data, merc_data, ven_data, ear_data, mars_data, jup_data, sat_data, nept_data, uran_data, plut_data] 
    

