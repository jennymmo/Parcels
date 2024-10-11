from parcels import Kernel
import math 

def wind_kernel(particle, fieldset, time):
    # Only execute for floating particles

    vel_u = fieldset.U[time, \
                       particle.depth + particle_ddepth, \
                        particle.lat + particle_dlat, \
                        particle.lon + particle_dlon]
    
    vel_v = fieldset.V[time, \
                       particle.depth + particle_ddepth, \
                        particle.lat + particle_dlat, \
                        particle.lon + particle_dlon]

    if math.fabs(vel_u) < 1e-14 and math.fabs(vel_v) < 1e-14:
        particle_dlon += (fieldset.UWind[time, particle.depth, particle.lat, particle.lon] * particle.dt)
        particle_dlat += (fieldset.VWind[time, particle.depth, particle.lat, particle.lon] * particle.dt)


