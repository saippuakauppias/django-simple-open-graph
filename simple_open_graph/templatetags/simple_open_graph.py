from django import template

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
        result_list = []
        for key, value in self.properties.items():
            value = template.Variable(value).resolve(context)
            value = value.replace('"', ' ')
            key = key.replace('"', '')
            og_formatted = og_layout.format(key, value)
            result_list.append(og_formatted)
        return u'\n'.join(result_list)
