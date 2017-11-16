#-*- coding: utf-8 -*-
import unittest
from mpdg.govbr.observatorio.testing import MPDG_GOVBR_OBSERVATORIO_INTEGRATION_TESTING


class ComentadorViewTest(unittest.TestCase):

    layer = MPDG_GOVBR_OBSERVATORIO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_contador(self):
        view = self.portal.restrictedTraverse('@@contador-view')
        self.assertTrue(view)