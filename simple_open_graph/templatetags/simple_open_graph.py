from django import template
from django.contrib.sites.models import Site
from django.conf import settings

from ..utils import string_to_dict, roundrobin
register = template.Library()

@register.tag
def opengraph_meta(parser, token):
    try:
        tag_name, properties = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires two arguments" % token.contents.split()[0]
        )
    properties = string_to_dict(properties[1:-1])
    return OpenGraphNode(properties)

class OpenGraphNode(template.Node):

    def __init__(self, properties):
        self.properties = properties

    def render(self, context):        
        site_domain = getattr(settings, "SITE_DOMAIN", None) or Site.objects.get_current().domain
        list_keys = []
        result_list = []
        for key, value in self.properties.items():
            if type(value) == list:
                list_keys.append([(key, item) for item in value])
            else:
                result_list.append(self.render_tag(key, value, context))
        if len(list_keys) > 0:
            for item in roundrobin(*list_keys):
                result_list.append(self.render_tag(item[0], item[1], context))
        return u'\n'.join(result_list)

    def render_tag(self, key, value, context):     
        try:
            value = template.Variable(value).resolve(context)
        except template.base.VariableDoesNotExist:
            pass
        og_layout = u'<meta property="og:{0}" content="{1}" />'
        value = value.replace('"', ' ')
        key = key.replace('"', '')
        # fix absolute links
        if key in [u'url', u'image', u'audio', u'video'] and value and value[0] == u'/':
            value = u'http://{0}{1}'.format(site_domain, value)
        og_formatted = og_layout.format(key, value)
        return og_formatted
    
