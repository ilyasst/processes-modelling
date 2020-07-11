#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 01:03:49 2020

@author: amelielaurens
"""

# Predict the exit velocity

from complex_models_RJS import *

#If we want the user to enter its own values
reduced_diameter_length = float(input("Enter the reduced diameter length in m : "))
mu = float(input("Enter the viscosity of the polymer in Pa.s : "))
rho = float(input("Enter the density of the polymer in kg/m^3 : "))
orifice_radius = float(input("Enter the radius of the orifice in m : "))
omega = float(input("Enter the angular velocity of the spinneret in rounds per second : "))
largest_diameter_length = float(input("Enter the distance of the reservoir wall from the center of rotation in m : "))

exit_velocity = exit_velocity(reduced_diameter_length, mu, rho, orifice_radius, omega , largest_diameter_length)
print('The exit velocity is : %s (in m/s).' %(exit_velocity))

