from datetime import datetime
from plone.directives import form
from plone.namedfile.field import NamedImage
from santa.content import _
from santa.content.config import COUNTRIES
from zope.schema import Choice
from zope.schema import List
from zope.schema import TextLine
from zope.schema import URI
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


countries = SimpleVocabulary(
    [
        SimpleTerm(
            value=code,
            title=COUNTRIES[code]
        ) for code in COUNTRIES.keys()
    ]
)

current_year = datetime.now().year
years = range(current_year, 1999, -1)


class IPartner(form.Schema):
    """Generic container content type for versatile content."""

    image = NamedImage(
        title=_(u'Logo'),
        description=_(u'Upload your organization logo.'),
        required=False,
    )

    address = TextLine(
        title=_(u'Street Address'),
        required=True,
    )

    post_code = TextLine(
        title=_(u'Post Code'),
        required=False,
    )

    country = Choice(
        title=_(u'Country'),
        required=True,
        vocabulary=countries,
        default=u'fi',
    )

    email = List(
        title=_(u'E-mail'),
        description=_(u"Input e-mail line by line putting representative e-mail on the top."),
        value_type=TextLine(),
        required=True,
    )

    link = URI(
        title=_(u'Link'),
        description=_(u'Link to the organization.'),
        required=False,
    )

    year = Choice(
        title=_(u'Partner since'),
        description=_(u'Select the year when the organization became the partner.'),
        required=True,
        values=years,
        default=current_year,
    )
