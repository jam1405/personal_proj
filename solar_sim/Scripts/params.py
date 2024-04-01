#View Settings
CAMERA_DISTANCE : float = 100


#Physics Settings
#Units of Distance are AU, and mass is Earth Masses, time is in days

g = 8.196655424*10**(-26) #M_earth*AU/day^2
time_step = 0.5 #days
cos_const = 1.1904*10**(-19)
simtime:int = 1000

#Celestial body data lists in units described above
#form of: [name str, mass float, display_radius float, x_initial, y_initial, z_initial floats, x,y,z init Vels]
sun_data:list = ["Sun",332959.9, 1 , 0,0,0,0,0,0]
merc_data:list = ["Mercury",0.055, 1]
ven_data:list = ["Venus",0.815, 1]
ear_data:list = ["Earth",1.0, 1]
mars_data:list = ["Mars",0.107, 1]
jup_data:list = ["Jupiter",317.81, 1]
sat_data:list = ["Saturn", 95.11, 1]
uran_data:list = ["Uranus", 14.53, 1]
nept_data:list =["Neptune",17.08, 1]
plut_data:list = ["Pluto", 0.00218, 1]


#List of Bodies for input
bodies_input:list = [sun_data, merc_data, ven_data, ear_data, mars_data, jup_data, sat_data, nept_data, uran_data, plut_data] 
    

