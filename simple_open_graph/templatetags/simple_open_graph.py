from django import template
from django.contrib.sites.models import Site

from ..utils import string_to_dict


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
        og_layout = u'<meta property="og:{0}" content="{1}" />'
        site_domain = Site.objects.get_current().domain
        result_list = []
        for key, value in self.properties.items():
            try:
                value = template.Variable(value).resolve(context)
            except template.base.VariableDoesNotExist:
                continue
            value = value.replace('"', ' ')
            key = key.replace('"', '')
            # fix absolute links
            if key in [u'url', u'image', u'audio', u'video'] and\
               value and value[0] == u'/':
                value = u'http://{0}{1}'.format(site_domain, value)
            og_formatted = og_layout.format(key, value)
            result_list.append(og_formatted)
        return u'\n'.join(result_list)
