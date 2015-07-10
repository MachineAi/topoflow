from topoflow.components import channels_kinematic_wave

# Kinematic Wave
wave = channels_kinematic_wave.channels_component()

wave.initialize(cfg_file="cfg/Treynor_channels_kinematic_wave.cfg")

wave.P_rain = 100
wave.SM = 0
wave.ET = 0
wave.GW = 0
wave.IN = 0
wave.MR = 0
wave.rho_H2O = 1000
wave.update()

wave.finalize()

##################################################################################

# Copying a variable from  kinematic wave because of formatting

S_free = wave.S_bed

from topoflow.components import channels_diffusive_wave

# Diffusive Wave
wave = channels_diffusive_wave.channels_component()

wave.initialize(cfg_file="cfg/Treynor_channels_diffusive_wave.cfg")

wave.P_rain = 100
wave.SM = 0
wave.ET = 0
wave.GW = 0
wave.IN = 0
wave.MR = 0
wave.rho_H2O = 1000
wave.S_free = S_free
wave.update()

wave.finalize()


##################################################################################

from topoflow.components import channels_dynamic_wave

# Dynamic Wave
wave = channels_dynamic_wave.channels_component()

wave.initialize(cfg_file="cfg/Treynor_channels_dynamic_wave.cfg")

# declared variable dinv inside chanels_dynamic_wave.py - don't know what this is and not defined in ANY file in the repo
wave.P_rain = 100
wave.SM = 0
wave.ET = 0
wave.GW = 0
wave.IN = 0
wave.MR = 0
wave.rho_H2O = 1000
wave.S_free = S_free
wave.update()

wave.finalize()


##################################################################################

from topoflow.components import snow_energy_balance
        
snow = snow_energy_balance.snow_component()

snow.P_snow = 0
snow.rho_H2O = 1000
snow.rho_air = 1
snow.Cp_air = 1
snow.T_air = 10
snow.T_surf = 20
snow.Q_sum = 1
snow.initialize(cfg_file="cfg/Treynor_snow_energy_balance.cfg")

snow.update()

snow.finalize()



##################################################################################

from topoflow.components import snow_degree_day
        
snow = snow_degree_day.snow_component()

snow.P_snow = 0
snow.rho_H2O = 1000
snow.T_air = 10
snow.initialize(cfg_file="cfg/Treynor_snow_degree_day.cfg")

snow.update()

snow.finalize()



##################################################################################

from topoflow.components import diversions_fraction_method
        
dive = diversions_fraction_method.diversions_component()

dive.initialize(cfg_file="cfg/Treynor_diversions_fraction_method.cfg")
dive.update()
dive.finalize()



##################################################################################

from topoflow.components import evap_energy_balance
        
evap = evap_energy_balance.evap_component()

evap.h_snow = 1
evap.Q_sum = 1
evap.Qe = 1
evap.T_air = 10
evap.T_surf = 20

evap.initialize(cfg_file="cfg/Treynor_evap_energy_balance.cfg")
evap.update()
evap.finalize()



##################################################################################

from topoflow.components import evap_priestley_taylor
        
evap = evap_priestley_taylor.evap_component()

evap.T_air = 10
evap.T_surf = 20
evap.Qn_SW = 1
evap.Qn_LW = 1
evap.initialize(cfg_file="cfg/Treynor_evap_priestley_taylor.cfg")

evap.update()

evap.finalize()


##################################################################################

# from topoflow.components import infil_beven
        
# infil = infil_beven.infil_component()
# ############# Code is unfinished! ##########

# infil.initialize(cfg_file="cfg/Treynor_infil_green_ampt.cfg")
# infil.update()
# infil.finalize()



##################################################################################

from topoflow.components import infil_green_ampt
        
infil = infil_green_ampt.infil_component()

infil.P_rain = 1
infil.SM = 0
infil.h_table = 1
infil.elev = 10

infil.initialize(cfg_file="cfg/Treynor_infil_green_ampt.cfg")
infil.update()
infil.finalize()



##################################################################################

from topoflow.components import infil_richards_1D
        
infil = infil_richards_1D.infil_component()

infil.P_rain = 1
infil.SM = 0
infil.ET = 1
infil.initialize(cfg_file="cfg/Treynor_infil_richards_1d.cfg")

infil.update()

infil.finalize()



##################################################################################

from topoflow.components import infil_smith_parlange
        
infil = infil_smith_parlange.infil_component()

infil.P_rain = 1
infil.SM = 0
infil.h_table = 1
infil.initialize(cfg_file="cfg/Treynor_infil_smith_parlange.cfg")

infil.elev = 10
infil.update()

infil.finalize()



##################################################################################

from topoflow.components import satzone_darcy_layers

sat = satzone_darcy_layers.satzone_component()

sat.initialize(cfg_file="cfg/Treynor_satzone_darcy_layers.cfg")

sat.Rg = 1
sat.update()

sat.finalize()



##################################################################################

from topoflow.components import soil_base
# just functions called by infil_richards_1D

soil = soil_base.soil_base()

soil.initialize()



##################################################################################

from topoflow.components import topoflow_driver
import numpy as np

topo = topoflow_driver.topoflow_driver()

topo.Q_outlet = np.array(1) # numpy array

topo.initialize(cfg_file = "cfg/Treynor_topoflow.cfg")
topo.update()
# topo.finalize() # prints reports and logs, wants to know variables from other components



##################################################################################

from topoflow.components import d8_global

d8 = d8_global.d8_component()

d8.initialize(cfg_file = "cfg/Treynor_d8_global.cfg")

d8.update()

d8.finalize()



##################################################################################

from topoflow.components import d8_local

d8 = d8_local.d8_component()

d8.initialize(cfg_file = "cfg/Treynor_d8_local.cfg")

d8.update()

# had to change np as a variable name to npx in d8_local because it conflicted with numpy as np
d8.finalize()



##################################################################################

from topoflow.components import erode_d8_global

erode = erode_d8_global.erosion_component()

# copied the cfg file for d8_global into the inputs dir (/in) because it's where it was looking for it but the erode cfg doesn't have the option to specify it
erode.initialize(cfg_file="cfg/Treynor_erode_global.cfg")

# erode.update()
# this fails because of a size difference between arrays in d8_global
# >>578 self.parent_ID_grid = self.ID_grid + self.inc_map[self.d8_grid]
# d8_global, by itself, works, so one of those grids must be modified (and broken) by erode



##################################################################################

from topoflow.components import erode_d8_local

erode = erode_d8_local.erosion_component()

# erased the cfg_prefix argument from the call to d8.initialize in erode_d8_local (because d8_base.initialize does not accept a cfg_prefix)
# copied the d8_local cfg file to the input directory because there's no option to specify its location
# erode.initialize(cfg_file="cfg/Treynor_erode_local.cfg")
# fails with a different in grid size while calculating slopes in erode_d8_local.initialize_slope_grid



##################################################################################

from topoflow.components import ice_base

ice = ice_base.ice_component()

ice.initialize(cfg_file='cfg/Treynor_ice_valley_glacier.cfg')

# ice.update()
# fails in filter_2D in gc2D

