from santa.content.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_santa_content_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('santa.content'))

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.content'])
        self.failIf(installer.isProductInstalled('santa.content'))
