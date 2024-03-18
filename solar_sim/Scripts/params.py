#View Settings
CAMERA_DISTANCE : float = 100


#Physics Settings
#Units of Distance are AU, and mass is Earth Masses, time is in days
#g = 9.81 #kg*m/s^2
g = 8.196655424*10**(-26) #M_earth*AU/day^2
time_step = 0.5 #days
#cos_const = 6.67430*10**(-11) # N*m^2/kg^2
cos_const = 1.1904*10**(-19)

#Celestial body data lists in units described above
#form of: [name str, mass float, display_radius float, x_initial, y_initial, z_initial floats]
sun_data:list = []
merc_data:list = []
ven_data:list = []
ear_data:list = []
mars_data:list = []
jup_data:list = []
sat_data:list = []
nept_data:list = []
uran_data:list =[]
plut_data:list = []


#List of Bodies for input
bodies_input:list = [sun_data, merc_data, ven_data, ear_data, mars_data, jup_data, sat_data, nept_data, uran_data, plut_data ] 
    

