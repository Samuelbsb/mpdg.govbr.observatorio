# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


class MpdgGovbrObservatorioLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import mpdg.govbr.biblioteca
        self.loadZCML(name='testing.zcml', package=mpdg.govbr.biblioteca)
        import mpdg.govbr.observatorio
        self.loadZCML(name='testing.zcml', package=mpdg.govbr.observatorio)

    def setUpPloneSite(self, portal):
        portal.portal_workflow.setChainForPortalTypes(
            ('Folder', ),
            'simple_publication_workflow'
        )
        applyProfile(portal, 'mpdg.govbr.biblioteca:testing')
        applyProfile(portal, 'mpdg.govbr.observatorio:testing')



MPDG_GOVBR_OBSERVATORIO_FIXTURE = MpdgGovbrObservatorioLayer()


MPDG_GOVBR_OBSERVATORIO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MPDG_GOVBR_OBSERVATORIO_FIXTURE,),
    name='MpdgGovbrObservatorioLayer:IntegrationTesting'
)
