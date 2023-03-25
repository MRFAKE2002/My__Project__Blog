from django import template

register = template.library()

@register.filter
def number(value):
    
    """
    Use this function to convert a english number to persian number.
    """
    number = str(value)
    
    english_to_persian = number.maketrans('0123456789', '۰١٢٣٤٥٦٧٨٩')
    
    return number.translate(english_to_persian)

