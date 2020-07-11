#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:56:13 2020

@author: amelielaurens
"""

from math import *


def exit_velocity(reduced_diameter_length, mu, rho, orifice_radius, omega , largest_diameter_length):
    """RJS

    :Input:
    - *reduced_diameter_length* (float) - Reduced diameter length (m)
    - *mu* (float) -  Viscosity (Pa.s)
    - *rho* (float) - Density (kg/m^3)
    - *orifice_radius* (float) - Radius of the orifice (m)
    - *omega* (float) - Angular velocity of the spinneret (rounds per second)
    - *largest_diameter_length* (float) - Distance of the reservoir wall from the center of rotation (m)


    :Returns:
    (float) - Exit velocity (m/s)

    """
    spinneret_radius = reduced_diameter_length + largest_diameter_length
    return -8*reduced_diameter_length*mu/(rho*orifice_radius**2)+sqrt(256*(reduced_diameter_length*mu/(rho*orifice_radius**2))**2+4*omega**2*(largest_diameter_length**2+2*reduced_diameter_length*(spinneret_radius-reduced_diameter_length/2)))/2