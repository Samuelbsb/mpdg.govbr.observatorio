#-*- coding: utf-8 -*-
import unittest
from mpdg.govbr.observatorio.testing import MPDG_GOVBR_OBSERVATORIO_INTEGRATION_TESTING


class NovaBoaPraticaViewTest(unittest.TestCase):

    layer = MPDG_GOVBR_OBSERVATORIO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_nova_boa_pratica(self):
        view = self.portal.restrictedTraverse('@@nova-boa-pratica')
        self.assertTrue(view)