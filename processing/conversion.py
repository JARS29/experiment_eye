#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Part of the PsychoPy library
# Copyright (C) 2015 Jonathan Peirce
# Distributed under the terms of the GNU General Public License (GPL).

"""Functions and classes related to unit conversion respective to a particular
monitor"""


import numpy as np
from numpy import array, sin, cos, tan, pi, radians, degrees, hypot

# Maps supported coordinate unit type names to the function that converts


# Built in conversion functions follow ...


def cm2deg(cm, correctFlat=False):
    """Convert size in cm to size in degrees for a given Monitor object
    """

    dist = 70
    if correctFlat:
        return np.degrees(np.arctan((cm/dist)))
    else:
        return (cm)/(dist * 0.017455)


def deg2cm(degrees, correctFlat=False):
    """Convert size in degrees to size in pixels for a given Monitor object.

    If `correctFlat == False` then the screen will be treated as if all
    points are equal distance from the eye. This means that each "degree"
    will be the same size irrespective of its position.

    eccentric vertices will be spaced further apart.
    """
    # check we have a monitor
    # get monitor dimensions
    scrsize = [2560, 1440]
    width = 38.20
    dist = 70
        # the size of 1 deg at screen centre
    return np.array(degrees) * dist * 0.017455


def cm2pix(cm):
    """Convert size in degrees to size in pixels for a given Monitor object
    """
    # check we have a monitor
    # get monitor params and raise error if necess
    scrSizePix = [2560, 1440]
    scrWidthCm = 38.20

    return cm * scrSizePix[0] / float(scrWidthCm)


def pix2cm(pixels):
    """Convert size in pixels to size in cm for a given Monitor object
    """
    # check we have a monitor
    # get monitor params and raise error if necess
    scrSizePix = [2560, 1440]
    scrWidthCm = 38.20

    return pixels * float(scrWidthCm) / scrSizePix[0]


def deg2pix(degrees, correctFlat=False):
    """Convert size in degrees to size in pixels for a given Monitor object
    """
    # get monitor params and raise error if necess
    scrSizePix = [2560, 1440]
    scrWidthCm = 38.20


    cmSize = deg2cm(degrees, correctFlat)
    return cmSize * scrSizePix[0] / float(scrWidthCm)


def pix2deg(pixels, correctFlat=False):
    """Convert size in pixels to size in degrees for a given Monitor object
    """
    # get monitor params and raise error if necess
    scrSizePix = [2560, 1440]
    scrWidthCm =  38.20
    cmSize = pixels * float(scrWidthCm) / scrSizePix[0]
    return round(cm2deg(cmSize, correctFlat),3)