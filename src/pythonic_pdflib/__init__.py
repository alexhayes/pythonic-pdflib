from PDFlib import PDFlib
from contextlib import contextmanager

class PythonicPDFlib(PDFlib):
    """
    A more pythonic API for PDFlib.
    """
    
    def __init__(self, options=None):
        super(PythonicPDFlib, self).__init__()
        
        if 'errorpolicy' not in options:
            options.update({'errorpolicy': 'exception'})

        for option, value in options.iteritems():
            self.set_option(option, value)

    def set_option(self, option, value):
        super(PythonicPDFlib, self).set_option("%s=%s" % (option, value))

    def _default_value(self, value, default=None):
        if value is None:
            return default
        return value

    def _to_optlist(self, options=None):
        """
        Convert a dict of options to a PDFlib optlist string.
        """
        if bool(options) == False:
            return ''
        elif isinstance(options, basestring):
            return options
        else:
            return " ".join([self._optlist_value(key, value) for key, value in options.iteritems()])

    def _optlist_value(self, key, value):
        if isinstance(value, BaseOption):
            if value.use == BaseOption.USE_VALUE:
                return "%s" % value
            elif value.use == BaseOption.USE_KEY:
                return "%s" % key
            else:
                return "%s=%s" % (key, value)
        elif value is None:
            return key
        else:
            return "%s=%s" % (key, value)

    def add_locallink(self, llx, lly, urx, ury, page, options=None):
        super(PythonicPDFlib, self).add_locallink(llx, lly, urx, ury, page, self._to_optlist(options))

    def add_nameddest(self, name, options=None):
        super(PythonicPDFlib, self).add_locallink(name, self._to_optlist(options))

    def add_path_point(self, path, x, y, type, options=None):
        super(PythonicPDFlib, self).add_path_point(path, x, y, type, self._to_optlist(options))

    def add_pdflink(self, llx, lly, urx, ury, filename, page, options=None):
        super(PythonicPDFlib, self).add_pdflink(llx, lly, urx, ury, filename, page, self._to_optlist(options))

    def add_portfolio_file(self, folder, filename, options=None):
        super(PythonicPDFlib, self).add_portfolio_file(folder, filename, self._to_optlist(options))

    def add_portfolio_folder(self, parent, foldername, options=None):
        super(PythonicPDFlib, self).add_portfolio_folder(parent, foldername, self._to_optlist(options))

    def add_table_cell(self, table, column, row, text, options=None):
        super(PythonicPDFlib, self).add_table_cell(table, column, row, text, self._to_optlist(options))

    def add_textflow(self, text, textflow=None, options=None):
        return super(PythonicPDFlib, self).add_textflow(self._default_value(textflow, -1), 
                                                        text, 
                                                        self._to_optlist(options))

    @contextmanager
    def document(self, filename, options=None):
        self.begin_document(filename, options)
        yield
        self.end_document(options)

    def begin_document(self, filename, options=None):
        return super(PythonicPDFlib, self).begin_document(filename, self._to_optlist(options))

    @contextmanager
    def dpart(self, options=None):
        """
        Manage calls to begin_dpart and end_depart
        """
        self.begin_dpart(options)
        yield
        self.end_dpart(options)

    def begin_dpart(self, options=None):
        optlist = self._to_optlist(options)
        super(PythonicPDFlib, self).begin_dpart(self._to_optlist(options))

    def end_dpart(self, options=None):
        optlist = self._to_optlist(options)
        super(PythonicPDFlib, self).end_dpart(optlist)        

    @contextmanager
    def font(self, fontname, a, b, c, d, e, f, options=None):
        """
        Manage calls to begin_font and end_font
        """
        self.begin_font(fontname, a, b, c, d, e, f, options)
        yield
        self.end_font()

    def begin_font(self, fontname, a, b, c, d, e, f, options=None):
        super(PythonicPDFlib, self).begin_font(fontname, a, b, c, d, e, f, self._to_optlist(options))

    @contextmanager
    def glyph(self, uv, options=None):
        """
        Manage calls to begin_glyph_ext and end_glyph.
        
        Note that begin_glyph is deprecated in favour of begin_glyph_ext.
        """
        self.begin_glyph_ext(uv, options)
        yield
        self.end_glyph()
    
    def begin_glyph_ext(self, uv, options=None):
        super(PythonicPDFlib, self).begin_glyph_ext(uv, self._to_optlist(options))

    @contextmanager
    def item(self, tagname, options=None):
        """
        Manage calls to begin_item and end_item.
        """
        item_id = self.begin_item(tagname, options)
        yield item_id
        self.end_item(item_id)

    def begin_item(self, tagname, options=None):
        return super(PythonicPDFlib, self).begin_item(tagname, self._to_optlist(options))
    
    @contextmanager
    def mc(self, tagname, options=None):
        """
        Contextmanage a marked content sequence with optional properties.
        """
        self.begin_mc(tagname, options)
        yield
        self.end_mc()
        
    def begin_mc(self, tagname, options=None):
        super(PythonicPDFlib, self).begin_mc(tagname, self._to_optlist(options))

    @contextmanager
    def page_ext(self, width, height, options=None):
        self.begin_page_ext(width, height, options)
        yield
        self.end_page_ext(options)

    def begin_page_ext(self, width, height, options=None):
        super(PythonicPDFlib, self).begin_page_ext(width, height, self._to_optlist(options))

    @contextmanager
    def template_ext(self, width, height, options=None):
        template = self.begin_template_ext(width, height, options)
        yield template
        self.end_template_ext()

    def begin_template_ext(self, width, height, options=None):
        return super(PythonicPDFlib, self).begin_template_ext(width, height, self._to_optlist(options))

    def end_template_ext(self, width=0, height=0):
        super(PythonicPDFlib, self).end_template_ext(width, height)

    def convert_to_unicode(self, inputformat, inputstring, options=None):
        return super(PythonicPDFlib, self).convert_to_unicode(inputformat, inputstring, self._to_optlist(options))

    def create_3dview(self, username, options=None):
        return super(PythonicPDFlib, self).create_3dview(username, self._to_optlist(options))

    def create_action(self, type, options=None):
        return super(PythonicPDFlib, self).create_action(type, self._to_optlist(options))

    def create_annotation(self, llx, lly, urx, ury, type, options=None):
        super(PythonicPDFlib, self).create_annotation(llx, lly, urx, ury, type, self._to_optlist(options))

    def create_bookmark(self, text, options=None):
        return super(PythonicPDFlib, self).create_bookmark(text, self._to_optlist(options))

    def create_field(self, llx, lly, urx, ury, name, type, options=None):
        super(PythonicPDFlib, self).create_field(llx, lly, urx, ury, name, type, self._to_optlist(options))

    def create_fieldgroup(self, name, options=None):
        super(PythonicPDFlib, self).create_fieldgroup(name, self._to_optlist(options))

    def create_gstate(self, options=None):
        return super(PythonicPDFlib, self).create_gstate(self._to_optlist(options))

    def create_pvf(self, filename, data, options=None):
        super(PythonicPDFlib, self).create_pvf(filename, data, self._to_optlist(options))

    def create_textflow(self, text, options=None):
        return super(PythonicPDFlib, self).create_textflow(text, self._to_optlist(options))

    def define_layer(self, name, options=None):
        return super(PythonicPDFlib, self).define_layer(name, self._to_optlist(options))

    def delete_table(self, table, options=None):
        super(PythonicPDFlib, self).delete_table(table, self._to_optlist(options))

    def draw_path(self, path, x, y, options=None):
        super(PythonicPDFlib, self).draw_path(path, x, y, self._to_optlist(options))

    def elliptical_arc(self, x, y, rx, ry, options=None):
        super(PythonicPDFlib, self).elliptical_arc(x, y, rx, ry, self._to_optlist(options))

    def end_document(self, options=None):
        super(PythonicPDFlib, self).end_document(self._to_optlist(options))

    def end_page_ext(self, options=None):
        super(PythonicPDFlib, self).end_page_ext(self._to_optlist(options))

    def fill_graphicsblock(self, page, blockname, graphics, options=None):
        return super(PythonicPDFlib, self).fill_graphicsblock(page, blockname, graphics, self._to_optlist(options))

    def fill_imageblock(self, page, blockname, image, options=None):
        return super(PythonicPDFlib, self).fill_imageblock(page, blockname, image, self._to_optlist(options))

    def fill_pdfblock(self, page, blockname, contents, options=None):
        return super(PythonicPDFlib, self).fill_pdfblock(page, blockname, contents, self._to_optlist(options))

    def fill_textblock(self, page, blockname, text, options=None):
        return super(PythonicPDFlib, self).fill_textblock(page, blockname, text, self._to_optlist(options))

    def fit_graphics(self, graphics, x, y, options=None):
        super(PythonicPDFlib, self).fit_graphics(graphics, x, y, self._to_optlist(options))

    def fit_image(self, image, x, y, options=None):
        super(PythonicPDFlib, self).fit_image(image, x, y, self._to_optlist(options))

    def fit_pdi_page(self, page, x, y, options=None):
        super(PythonicPDFlib, self).fit_pdi_page(page, x, y, self._to_optlist(options))

    def fit_table(self, table, llx, lly, urx, ury, options=None):
        return super(PythonicPDFlib, self).fit_table(table, llx, lly, urx, ury, self._to_optlist(options))

    def fit_textflow(self, textflow, llx, lly, urx, ury, options=None):
        return super(PythonicPDFlib, self).fit_textflow(textflow, llx, lly, urx, ury, self._to_optlist(options))

    def fit_textline(self, text, x, y, options=None):
        super(PythonicPDFlib, self).fit_textline(text, x, y, self._to_optlist(options))

    def get_option(self, keyword, options=None):
        return super(PythonicPDFlib, self).get_option(keyword, self._to_optlist(options))

    def get_string(self, idx, options=None):
        return super(PythonicPDFlib, self).get_string(idx, self._to_optlist(options))

    def info_font(self, font, keyword, options=None):
        return super(PythonicPDFlib, self).info_font(font, keyword, self._to_optlist(options))

    def info_graphics(self, graphics, keyword, options=None):
        return super(PythonicPDFlib, self).info_graphics(graphics, keyword, self._to_optlist(options))

    def info_image(self, image, keyword, options=None):
        return super(PythonicPDFlib, self).info_image(image, keyword, self._to_optlist(options))

    def info_path(self, path, keyword, options=None):
        return super(PythonicPDFlib, self).info_path(path, keyword, self._to_optlist(options))

    def info_pdi_page(self, page, keyword, options=None):
        return super(PythonicPDFlib, self).info_pdi_page(page, keyword, self._to_optlist(options))

    def info_textline(self, text, keyword, options=None):
        return super(PythonicPDFlib, self).info_textline(text, keyword, self._to_optlist(options))

    def load_3ddata(self, filename, options=None):
        return super(PythonicPDFlib, self).load_3ddata(filename, self._to_optlist(options))

    def load_asset(self, type, filename, options=None):
        return super(PythonicPDFlib, self).load_asset(type, filename, self._to_optlist(options))

    def load_font(self, fontname, encoding, options=None):
        return super(PythonicPDFlib, self).load_font(fontname, encoding, self._to_optlist(options))

    def load_graphics(self, type, filename, options=None):
        return super(PythonicPDFlib, self).load_graphics(type, filename, self._to_optlist(options))

    def load_iccprofile(self, profilename, options=None):
        return super(PythonicPDFlib, self).load_iccprofile(profilename, self._to_optlist(options))

    def load_image(self, imagetype, filename, options=None):
        return super(PythonicPDFlib, self).load_image(imagetype, filename, self._to_optlist(options))

    def mc_point(self, tagname, options=None):
        super(PythonicPDFlib, self).mc_point(tagname, self._to_optlist(options))

    @contextmanager
    def pdi_document(self, filename, options=None):
        doc = self.open_pdi_document(filename, options)
        yield doc
        self.close_pdi_document(doc)

    def open_pdi_document(self, filename, options=None):
        return super(PythonicPDFlib, self).open_pdi_document(filename, self._to_optlist(options))

    @contextmanager
    def pdi_page(self, doc, pagenumber, options=None):
        page = self.open_pdi_page(doc, pagenumber, options)
        yield page
        self.close_pdi_page(page)

    def open_pdi_page(self, doc, pagenumber, options=None):
        return super(PythonicPDFlib, self).open_pdi_page(doc, pagenumber, self._to_optlist(options))

    def pcos_get_stream(self, doc, optlist, path):
        return super(PythonicPDFlib, self).pcos_get_stream(doc, optlist, path)

    def poca_delete(self, container, options=None):
        super(PythonicPDFlib, self).poca_delete(container, self._to_optlist(options))

    def poca_insert(self, container, options=None):
        super(PythonicPDFlib, self).poca_insert(container, self._to_optlist(options))

    def poca_new(self, options=None):
        return super(PythonicPDFlib, self).poca_new(self._to_optlist(options))

    def poca_remove(self, container, options=None):
        super(PythonicPDFlib, self).poca_remove(container, self._to_optlist(options))

    def process_pdi(self, doc, page, options=None):
        return super(PythonicPDFlib, self).process_pdi(doc, page, self._to_optlist(options))

    def resume_page(self, options=None):
        super(PythonicPDFlib, self).resume_page(self._to_optlist(options))

    def set_graphics_option(self, options=None):
        super(PythonicPDFlib, self).set_graphics_option(self._to_optlist(options))

    def set_layer_dependency(self, type, options=None):
        super(PythonicPDFlib, self).set_layer_dependency(type, self._to_optlist(options))

    def set_text_option(self, options=None):
        super(PythonicPDFlib, self).set_text_option(self._to_optlist(options))

    def setdashpattern(self, options=None):
        super(PythonicPDFlib, self).setdashpattern(self._to_optlist(options))

    def shading(self, shtype, x_0, y_0, x_1, y_1, c_1, c_2, c_3, c_4, options=None):
        return super(PythonicPDFlib, self).shading(shtype, x_0, y_0, x_1, y_1, c_1, c_2, c_3, c_4, self._to_optlist(options))

    def shading_pattern(self, shading, options=None):
        return super(PythonicPDFlib, self).shading_pattern(shading, self._to_optlist(options))

    def suspend_page(self, options=None):
        super(PythonicPDFlib, self).suspend_page(self._to_optlist(options))

class BaseOption(object):
    USE_KEYVALUE = 0
    USE_KEY = 1
    USE_VALUE = 2
    
    use = USE_KEYVALUE

class RGBColor(BaseOption):
    
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def __str__(self, *args, **kwargs):
        return "{rgb %s %s %s}" % (
            self.red / 255,
            self.green / 255,
            self.blue / 255,
        )