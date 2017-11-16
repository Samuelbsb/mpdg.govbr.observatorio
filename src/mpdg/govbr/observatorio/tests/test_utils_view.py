#-*- coding: utf-8 -*-
import unittest
from mpdg.govbr.observatorio.testing import MPDG_GOVBR_OBSERVATORIO_INTEGRATION_TESTING


class UtilsViewTest(unittest.TestCase):

    layer = MPDG_GOVBR_OBSERVATORIO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_utils(self):
        view = self.portal.restrictedTraverse('@@utils-view')
        self.assertTrue(view)