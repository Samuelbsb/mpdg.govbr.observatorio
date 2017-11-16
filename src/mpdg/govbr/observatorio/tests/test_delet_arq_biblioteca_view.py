#-*- coding: utf-8 -*-
import unittest
from mpdg.govbr.observatorio.testing import MPDG_GOVBR_OBSERVATORIO_INTEGRATION_TESTING


class TestDeletarArgBibliotecaView(unittest.TestCase):

    layer = MPDG_GOVBR_OBSERVATORIO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_deletar_arq_biblioteca(self):
        view = self.portal.restrictedTraverse('@@deletar_arq_biblioteca')
        self.assertTrue(view)