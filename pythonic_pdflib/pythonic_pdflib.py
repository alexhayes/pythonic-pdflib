from PDFlib import PDFlib
from contextlib import contextmanager
from .helpers import to_optlist, default

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

    def add_locallink(self, llx, lly, urx, ury, page, options=None):
        super(PythonicPDFlib, self).add_locallink(llx, lly, urx, ury, page, to_optlist(options))

    def add_nameddest(self, name, options=None):
        super(PythonicPDFlib, self).add_locallink(name, to_optlist(options))

    def add_path_point(self, path, x, y, type, options=None):
        super(PythonicPDFlib, self).add_path_point(path, x, y, type, to_optlist(options))

    def add_pdflink(self, llx, lly, urx, ury, filename, page, options=None):
        super(PythonicPDFlib, self).add_pdflink(llx, lly, urx, ury, filename, page, to_optlist(options))

    def add_portfolio_file(self, folder, filename, options=None):
        super(PythonicPDFlib, self).add_portfolio_file(folder, filename, to_optlist(options))

    def add_portfolio_folder(self, parent, foldername, options=None):
        super(PythonicPDFlib, self).add_portfolio_folder(parent, foldername, to_optlist(options))

    def add_table_cell(self, column, row, text, table=-1, options=None):
        return super(PythonicPDFlib, self).add_table_cell(table, column, row, text, to_optlist(options))

    @contextmanager
    def table_headers(self, headers, options=None):
        table = -1
        for col, header in enumerate(headers):
            if col == 0:
                table = self.add_table_cell(col+1, 1, header, options=options)
            else:
                self.add_table_cell(col+1, 1, header, options=options, table=table)
        yield table

    @contextmanager
    def table_rows(self, table, rows, row_options=None, col_options=[]):
        for rowi, row in enumerate(rows):
            for coli, col in enumerate(row):
                try:
                    options = col_options[coli]
                except IndexError:
                    options = row_options
                self.add_table_cell(coli+1, rowi+2, col, table=table, options=options)
        yield table

    def add_textflow(self, text, textflow=None, options=None):
        return super(PythonicPDFlib, self).add_textflow(default(textflow, -1), 
                                                        text, 
                                                        to_optlist(options))

    @contextmanager
    def document(self, filename, begin_options=None, end_options=None):
        self.begin_document(filename, begin_options)
        yield
        self.end_document(end_options)

    def begin_document(self, filename, options=None):
        return super(PythonicPDFlib, self).begin_document(filename, to_optlist(options))

    @contextmanager
    def dpart(self, options=None):
        """
        Manage calls to begin_dpart and end_depart
        """
        self.begin_dpart(options)
        yield
        self.end_dpart(options)

    def begin_dpart(self, options=None):
        optlist = to_optlist(options)
        super(PythonicPDFlib, self).begin_dpart(to_optlist(options))

    def end_dpart(self, options=None):
        optlist = to_optlist(options)
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
        super(PythonicPDFlib, self).begin_font(fontname, a, b, c, d, e, f, to_optlist(options))

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
        super(PythonicPDFlib, self).begin_glyph_ext(uv, to_optlist(options))

    @contextmanager
    def item(self, tagname, options=None):
        """
        Manage calls to begin_item and end_item.
        """
        item_id = self.begin_item(tagname, options)
        yield item_id
        self.end_item(item_id)

    def begin_item(self, tagname, options=None):
        return super(PythonicPDFlib, self).begin_item(tagname, to_optlist(options))
    
    @contextmanager
    def mc(self, tagname, options=None):
        """
        Contextmanage a marked content sequence with optional properties.
        """
        self.begin_mc(tagname, options)
        yield
        self.end_mc()
        
    def begin_mc(self, tagname, options=None):
        super(PythonicPDFlib, self).begin_mc(tagname, to_optlist(options))

    @contextmanager
    def page_ext(self, width, height, suspend=False, options=None):
        self.begin_page_ext(width, height, options)
        yield
        if suspend:
            self.suspend_page(options)
        else:
            self.end_page_ext(options)

    def begin_page_ext(self, width, height, options=None):
        super(PythonicPDFlib, self).begin_page_ext(width, height, to_optlist(options))

    @contextmanager
    def template_ext(self, width, height, options=None):
        template = self.begin_template_ext(width, height, options)
        yield template
        self.end_template_ext()

    def begin_template_ext(self, width, height, options=None):
        return super(PythonicPDFlib, self).begin_template_ext(width, height, to_optlist(options))

    def end_template_ext(self, width=0, height=0):
        super(PythonicPDFlib, self).end_template_ext(width, height)

    def convert_to_unicode(self, inputformat, inputstring, options=None):
        return super(PythonicPDFlib, self).convert_to_unicode(inputformat, inputstring, to_optlist(options))

    def create_3dview(self, username, options=None):
        return super(PythonicPDFlib, self).create_3dview(username, to_optlist(options))

    def create_action(self, type, options=None):
        return super(PythonicPDFlib, self).create_action(type, to_optlist(options))

    def create_annotation(self, llx, lly, urx, ury, type, options=None):
        super(PythonicPDFlib, self).create_annotation(llx, lly, urx, ury, type, to_optlist(options))

    def create_bookmark(self, text, options=None):
        return super(PythonicPDFlib, self).create_bookmark(text, to_optlist(options))

    def create_field(self, llx, lly, urx, ury, name, type, options=None):
        super(PythonicPDFlib, self).create_field(llx, lly, urx, ury, name, type, to_optlist(options))

    def create_fieldgroup(self, name, options=None):
        super(PythonicPDFlib, self).create_fieldgroup(name, to_optlist(options))

    def create_gstate(self, options=None):
        return super(PythonicPDFlib, self).create_gstate(to_optlist(options))

    def create_pvf(self, filename, data, options=None):
        super(PythonicPDFlib, self).create_pvf(filename, data, to_optlist(options))

    def create_textflow(self, text, options=None):
        return super(PythonicPDFlib, self).create_textflow(text, to_optlist(options))

    def define_layer(self, name, options=None):
        return super(PythonicPDFlib, self).define_layer(name, to_optlist(options))

    def delete_table(self, table, options=None):
        super(PythonicPDFlib, self).delete_table(table, to_optlist(options))

    def draw_path(self, path, x, y, options=None):
        super(PythonicPDFlib, self).draw_path(path, x, y, to_optlist(options))

    def elliptical_arc(self, x, y, rx, ry, options=None):
        super(PythonicPDFlib, self).elliptical_arc(x, y, rx, ry, to_optlist(options))

    def end_document(self, options=None):
        super(PythonicPDFlib, self).end_document(to_optlist(options))

    def end_page_ext(self, options=None):
        super(PythonicPDFlib, self).end_page_ext(to_optlist(options))

    def fill_graphicsblock(self, page, blockname, graphics, options=None):
        return super(PythonicPDFlib, self).fill_graphicsblock(page, blockname, graphics, to_optlist(options))

    def fill_imageblock(self, page, blockname, image, options=None):
        return super(PythonicPDFlib, self).fill_imageblock(page, blockname, image, to_optlist(options))

    def fill_pdfblock(self, page, blockname, contents, options=None):
        return super(PythonicPDFlib, self).fill_pdfblock(page, blockname, contents, to_optlist(options))

    def fill_textblock(self, page, blockname, text, options=None):
        return super(PythonicPDFlib, self).fill_textblock(page, blockname, text, to_optlist(options))

    def fit_graphics(self, graphics, x, y, options=None):
        super(PythonicPDFlib, self).fit_graphics(graphics, x, y, to_optlist(options))

    def fit_image(self, image, x, y, options=None):
        super(PythonicPDFlib, self).fit_image(image, x, y, to_optlist(options))

    def fit_pdi_page(self, page, x, y, options=None):
        super(PythonicPDFlib, self).fit_pdi_page(page, x, y, to_optlist(options))

    def fit_table(self, table, llx, lly, urx, ury, options=None):
        return super(PythonicPDFlib, self).fit_table(table, llx, lly, urx, ury, to_optlist(options))

    def fit_textflow(self, textflow, llx, lly, urx, ury, options=None):
        return super(PythonicPDFlib, self).fit_textflow(textflow, llx, lly, urx, ury, to_optlist(options))

    def fit_textline(self, text, x, y, options=None):
        super(PythonicPDFlib, self).fit_textline(text, x, y, to_optlist(options))

    def get_option(self, keyword, options=None):
        return super(PythonicPDFlib, self).get_option(keyword, to_optlist(options))

    def get_string(self, idx, options=None):
        return super(PythonicPDFlib, self).get_string(idx, to_optlist(options))

    def info_font(self, font, keyword, options=None):
        return super(PythonicPDFlib, self).info_font(font, keyword, to_optlist(options))

    def info_graphics(self, graphics, keyword, options=None):
        return super(PythonicPDFlib, self).info_graphics(graphics, keyword, to_optlist(options))

    def info_image(self, image, keyword, options=None):
        return super(PythonicPDFlib, self).info_image(image, keyword, to_optlist(options))

    def info_path(self, path, keyword, options=None):
        return super(PythonicPDFlib, self).info_path(path, keyword, to_optlist(options))

    def info_pdi_page(self, page, keyword, options=None):
        return super(PythonicPDFlib, self).info_pdi_page(page, keyword, to_optlist(options))

    def info_textline(self, text, keyword, options=None):
        return super(PythonicPDFlib, self).info_textline(text, keyword, to_optlist(options))

    def load_3ddata(self, filename, options=None):
        return super(PythonicPDFlib, self).load_3ddata(filename, to_optlist(options))

    def load_asset(self, type, filename, options=None):
        return super(PythonicPDFlib, self).load_asset(type, filename, to_optlist(options))

    def load_font(self, fontname, encoding, options=None):
        return super(PythonicPDFlib, self).load_font(fontname, encoding, to_optlist(options))

    def load_graphics(self, type, filename, options=None):
        return super(PythonicPDFlib, self).load_graphics(type, filename, to_optlist(options))

    def load_iccprofile(self, profilename, options=None):
        return super(PythonicPDFlib, self).load_iccprofile(profilename, to_optlist(options))

    def load_image(self, imagetype, filename, options=None):
        return super(PythonicPDFlib, self).load_image(imagetype, filename, to_optlist(options))

    @contextmanager
    def image(self, imagetype, filename, options=None):
        image = self.load_image(imagetype, filename, options)
        yield image
        self.close_image(image)

    def mc_point(self, tagname, options=None):
        super(PythonicPDFlib, self).mc_point(tagname, to_optlist(options))

    @contextmanager
    def pdi_document(self, filename, options=None):
        doc = self.open_pdi_document(filename, options)
        yield doc
        self.close_pdi_document(doc)

    def open_pdi_document(self, filename, options=None):
        return super(PythonicPDFlib, self).open_pdi_document(filename, to_optlist(options))

    @contextmanager
    def pdi_page(self, doc, pagenumber, options=None):
        page = self.open_pdi_page(doc, pagenumber, options)
        yield page
        self.close_pdi_page(page)

    def open_pdi_page(self, doc, pagenumber, options=None):
        return super(PythonicPDFlib, self).open_pdi_page(doc, pagenumber, to_optlist(options))

    def pcos_get_stream(self, doc, optlist, path):
        return super(PythonicPDFlib, self).pcos_get_stream(doc, optlist, path)

    def poca_delete(self, container, options=None):
        super(PythonicPDFlib, self).poca_delete(container, to_optlist(options))

    def poca_insert(self, container, options=None):
        super(PythonicPDFlib, self).poca_insert(container, to_optlist(options))

    def poca_new(self, options=None):
        return super(PythonicPDFlib, self).poca_new(to_optlist(options))

    def poca_remove(self, container, options=None):
        super(PythonicPDFlib, self).poca_remove(container, to_optlist(options))

    def process_pdi(self, doc, page, options=None):
        return super(PythonicPDFlib, self).process_pdi(doc, page, to_optlist(options))

    @contextmanager
    def resume_page(self, page_no=None, close=False, options={}, suspend_page_options=None, end_page_ext_options=None):
        if page_no:
            options.update({'pagenumber': page_no})
        super(PythonicPDFlib, self).resume_page(to_optlist(options))
        yield
        if close:
            self.end_page_ext(to_optlist(end_page_ext_options))
        else:
            self.suspend_page(to_optlist(suspend_page_options))

    def set_graphics_option(self, options=None):
        super(PythonicPDFlib, self).set_graphics_option(to_optlist(options))

    def set_layer_dependency(self, type, options=None):
        super(PythonicPDFlib, self).set_layer_dependency(type, to_optlist(options))

    def set_text_option(self, options=None):
        super(PythonicPDFlib, self).set_text_option(to_optlist(options))

    def setdashpattern(self, options=None):
        super(PythonicPDFlib, self).setdashpattern(to_optlist(options))

    def shading(self, shtype, x_0, y_0, x_1, y_1, c_1, c_2, c_3, c_4, options=None):
        return super(PythonicPDFlib, self).shading(shtype, x_0, y_0, x_1, y_1, c_1, c_2, c_3, c_4, to_optlist(options))

    def shading_pattern(self, shading, options=None):
        return super(PythonicPDFlib, self).shading_pattern(shading, to_optlist(options))

    def suspend_page(self, options=None):
        super(PythonicPDFlib, self).suspend_page(to_optlist(options))


