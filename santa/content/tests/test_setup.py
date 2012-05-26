from santa.content.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_santa_content_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('santa.content'))

    def test_types_santa_Partner__meta_type(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(item.meta_type, 'Dexterity FTI')

    def test_types_santa_Partner__domain(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(item.i18n_domain, 'santa.content')

    def test_types_santa_Partner__title(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(item.title, 'Partner')

    def test_types_santa_Partner__description(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(item.description, '')

    def test_types_santa_Partner__content_icon(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(item.getIcon(), 'group.png')

    def test_types_santa_Partner__allow_discussion(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertFalse(item.allow_discussion)

    def test_types_santa_Partner__global_allow(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertTrue(item.global_allow)

    def test_types_santa_Partner__filter_content_types(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertTrue(item.filter_content_types)

    def test_types_santa_Partner__allowed_content_types(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(
            item.allowed_content_types,
            ('Document', 'Image')
        )

    def test_types_santa_Partner__schema(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(
            item.schema,
            'santa.content.partner.IPartner'
        )

    def test_types_santa_Partner__klass(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(
            item.klass,
            'plone.dexterity.content.Container'
        )

    def test_types_santa_Partner__add_permssion(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(
            item.add_permission,
            'cmf.AddPortalContent'
        )

    def test_types_santa_Partner__behaviors(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(
            item.behaviors,
            (
                'plone.app.content.interfaces.INameFromTitle',
                'plone.app.dexterity.behaviors.metadata.IDublinCore',
                'plone.app.referenceablebehavior.referenceable.IReferenceable'
            )
        )

    def test_types_santa_Partner__default_view(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(
            item.default_view,
            'view'
        )

    def test_types_santa_Partner__default_view_fallback(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertFalse(item.default_view_fallback)

    def test_types_santa_Partner__view_method(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(
            item.view_methods,
            ('view',)
        )

    def test_types_santa_Partner__alias(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        self.assertEqual(
            item.getMethodAliases(),
            {
                '(Default)': '(dynamic view)',
                'edit': '@@edit',
                'sharing': '@@sharing',
                'view': '@@view',
            }
        )

    def test_types_santa_Partner__action_view__title(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        action = item.getActionObject('object/view')
        self.assertEqual(
            action.title,
            'View'
        )

    def test_types_santa_Partner__action_view__condition_expr(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        action = item.getActionObject('object/view')
        self.assertEqual(
            action.getCondition(),
            ''
        )

    def test_types_santa_Partner__action_view__url_expr(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        action = item.getActionObject('object/view')
        self.assertEqual(
            action.getActionExpression(),
            'string:${folder_url}/'
        )

    def test_types_santa_Partner__action_view__visible(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        action = item.getActionObject('object/view')
        self.assertTrue(action.visible)

    def test_types_santa_Partner__action_edit__title(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        action = item.getActionObject('object/edit')
        self.assertEqual(
            action.title,
            'Edit'
        )

    def test_types_santa_Partner__action_edit__condition_expr(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        action = item.getActionObject('object/edit')
        self.assertEqual(
            action.getCondition(),
            ''
        )

    def test_types_santa_Partner__action_edit__url_expr(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        action = item.getActionObject('object/edit')
        self.assertEqual(
            action.getActionExpression(),
            'string:${object_url}/edit'
        )

    def test_types_santa_Partner__action_edit__visible(self):
        types = getToolByName(self.portal, 'portal_types')
        item = types.getTypeInfo('santa.Partner')
        action = item.getActionObject('object/edit')
        self.assertTrue(action.visible)

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.content'])
        self.failIf(installer.isProductInstalled('santa.content'))

    def test_uninstall__types_santa_Partner(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.content'])
        types = getToolByName(self.portal, 'portal_types')
        self.failIf(types.getTypeInfo('santa.Partner'))
