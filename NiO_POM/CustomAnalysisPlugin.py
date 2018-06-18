#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:04:17 2018

@author: abel
"""
#custom analyzer: TOF and selectivity


class KMCAnalysisPlugin(object):
    """
    Class for providing an interface to easily extend and customize
    the behaviour of the on-the-fly analysis functionality of KMCLib.
    """

    def __init__(self):
        """
        The constructor of the base-class.
        """
        pass

    def setup(self, step, time, configuration):
        """
        Function called right before the start of the KMC loop to allow for
        custom setup of the analysis object.

        :param step: The simulation step number.
        :type step: int

        :param time: The simulation time.
        :type time: float

        :param configuration: The up to date configuration of the simulation.
        :type configuration: KMCConfiguration
        """
        pass

    def registerStep(self, step, time, configuration):
        """
        Called from the KMC loop after each step.

        :param step: The simulation step number.
        :type step: int

        :param time: The simulation time.
        :type time: float

        :param configuration: The up to date configuration of the simulation.
        :type configuration: KMCConfiguration
        """
        pass

    def finalize(self):
        """
        Called after the KMC loop to allow for custom finalization and
        post-processing of collected data.
        """
        pass
