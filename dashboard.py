from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard

# to activate your index dashboard add the following to your settings.py:
#
# ADMIN_TOOLS_INDEX_DASHBOARD = 'openeats.dashboard.CustomIndexDashboard'

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for openeats.
    """
   
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        
        #append a link list module for "quick links"
        self.children.append(modules.LinkList(
            title=_('Quick links'),
            layout='inline',
            css_classes=['collapse', 'closed','column_1'],
            children=[
                {
                    'title': _('Return to site'),
                    'url': '/',
                },
                {
                    'title': _('Change password'),
                    'url': reverse('admin:password_change'),
                },
                {
                    'title': _('Log out'),
                    'url': reverse('admin:logout')
                },
            ]
        ))
        
        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            title=_('Administration'),
            include_list=('django.contrib','registration','openeats.accounts'),
            css_classes=['collapse', 'open','column_1'],
        ))

         # append an openeats list module for "Applications"
        self.children.append(modules.AppList(
            title=_('OpenEats'),
            exclude_list=('django.contrib', 'registration', 'openeats.accounts',),
            include_list=('openeats', 'recipe'),
            css_classes=['collapse', 'open','column_1'],
        ))
        
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            title=_('Third-Party Apps'),
            exclude_list=('django.contrib','openeats', 'recipe'),
            css_classes=['collapse', 'open','column_1'],
        ))
          
        # append a recent actions module
        self.children.append(modules.RecentActions(
            column=2,
            title=_('Recent Actions'),
            css_classes=['collapse', 'open','column_2'],
            limit=5
        ))

        # append a feed module
        self.children.append(modules.Feed(
            column=2,
            title=_('Latest OpenEats News'),
            feed_url='http://oe2.openeats.org/blog/feeds/latest/',
            limit=5,
            css_classes=['collapse', 'open','column_2' ]
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            column=2,
            title=_('Support'),
            css_classes=['collapse', 'open','column_2'],
            children=[
                    {
                    'title': _('OpenEats Forum'),
                    'url': 'http://oe2.openeats.org/forum/',
                    'external': True,
                },
                {
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Django "django-users" mailing list'),
                    'url': 'http://groups.google.com/group/django-users',
                    'external': True,
                },
              
            ]
        ))

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass


# to activate your app index dashboard add the following to your settings.py:
#
# ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'openeats.dashboard.CustomAppIndexDashboard'

class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for openeats.
    """
    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # we disable title because its redundant with the model list module
        self.title = ''

        # append a model list module
        self.children.append(modules.ModelList(
            title=self.app_title,
            css_classes=['column_1'],
            models=self.models,
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            column=2,
            title=_('Recent Actions'),
            css_classes=['column_2'],
            include_list=self.get_app_content_types(),
        ))

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass