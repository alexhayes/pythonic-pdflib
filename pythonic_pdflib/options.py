
class BaseOption(object):
    USE_KEYVALUE = 0
    USE_KEY = 1
    USE_VALUE = 2
    
    use = USE_KEYVALUE

class Options(BaseOption):
    
    def __init__(self, options):
        """
        @param options: Either a dict of options or a list of dicts.
        """
        self.options = options
    
    def __str__(self, *args, **kwargs):
        from .helpers import to_optlist
        return '{%s}' % to_optlist(self.options)

class RGBColor(BaseOption):
    
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def __str__(self, *args, **kwargs):
        return "{rgb %s %s %s}" % (self.percent_red(), self.percent_green(), self.percent_blue())

    def percent_red(self):
        return self.red / 255.0

    def percent_green(self):
        return self.green / 255.0

    def percent_blue(self):
        return self.blue / 255.0
    
class FitTextline(Options): pass