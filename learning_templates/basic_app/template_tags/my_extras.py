from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value,arg):
    """
    This cuts out all values of arg fromt he string
    """

    return value.replace(arg,'')

# first arg is what it will be called, second is the name of the function you created above
# register.filter('cut', cut)