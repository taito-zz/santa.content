from santa.content import _
from plone.app.textfield import RichText
from plone.directives import form
from z3c.form.browser.radio import RadioFieldWidget
from z3c.form.interfaces import IAddForm
from z3c.form.interfaces import IEditForm
# from zope import schema
from zope.schema.vocabulary import SimpleVocabulary


class IFolder(form.Schema):
    """Generic container content type for versatile content."""

    text = RichText(
        title=_(u'Body text'),
        required=False)

    # form.omitted('show_in_navigation')
    # form.no_omit(IEditForm, 'show_in_navigation')
    # form.no_omit(IAddForm, 'show_in_navigation')
    # form.widget(show_in_navigation=RadioFieldWidget)
    # show_in_navigation = schema.Choice(
    #     title=_(u'Show in navigation?'),
    #     description=_(u'Choose whether to show this item in the site navigation or not.'),
    #     default=False,
    #     vocabulary=SimpleVocabulary([
    #         SimpleVocabulary.createTerm(True, '1', _(u'Yes')),
    #         SimpleVocabulary.createTerm(False, '0', _(u'No'))]))

