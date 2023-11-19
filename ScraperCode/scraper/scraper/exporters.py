from scrapy.exporters import CsvItemExporter


class CustomCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
            kwargs['delimiter'] = ';'
            super(CustomCsvItemExporter, self).__init__(*args, **kwargs)

    def serialize_field(self, field, name, value):
        if name == 'Image_URLs':
            return ','.join(value) if value else ''
        else:
            return super().serialize_field(field, name, value)
