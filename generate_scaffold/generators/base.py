from generate_scaffold.utils.modules import import_child


FIELD_ALIASES = {
    'autofield': ['auto', 'autofield'],
    'bigintegerfield': [
        'bigint', 'biginteger', 'bigintfield', 'bigintegerfield'
    ],
    'booleanfield': ['bool', 'boolean', 'booleanfield'],
    'charfield': ['string', 'char', 'charfield'],
    'commaseparatedintegerfield': [
        'comma', 'commaseparatedint', 'commaseparatedinteger',
        'commaseparatedintegerfield'
    ],
    'datefield': ['date', 'datefield'],
    'datetimefield': ['datetime', 'datetimefield'],
    'decimalfield': ['decimal', 'decimalfield'],
    'emailfield': ['email', 'emailfield'],
    'filefield': ['file', 'filefield'],
    'filepathfield': ['path', 'filepath', 'filepathfield'],
    'floatfield': ['float', 'floatfield'],
    'foreignkey': ['foreign', 'foreignkey', 'foreignkeyfield'],
    'genericipaddressfield': [
        'genericip', 'genericipaddress', 'genericipaddressfield'
    ],
    'imagefield': ['image', 'imagefield'],
    'integerfield': ['int', 'integer', 'integerfield'],
    'ipaddressfield': ['ip', 'ipaddress', 'ipaddressfield'],
    'manytomanyfield': ['many', 'manytomany', 'manytomanyfield'],
    'nullbooleanfield': ['nullbool', 'nullboolean', 'nullbooleanfield'],
    'onetoonefield': ['one', 'onetoone', 'onetoonefield'],
    'positiveintegerfield': [
        'posint', 'positiveint', 'positiveinteger', 'positiveintegerfield'
    ],
    'slugfield': ['slug', 'slugfield'],
    'smallintegerfield': ['smallint', 'smallinteger', 'smallintegerfield'],
    'textfield': ['text', 'textfield'],
    'timefield': ['time', 'timefield'],
    'urlfield': ['url', 'urlfield'],
}


RELATIONSHIP_FIELDS = set(['foreignkey', 'manytomanyfield', 'onetoonefield'])


class GeneratorError(Exception):
    pass


class BaseGenerator(object):

    def __init__(self, app_name):
        self.app_name = app_name

    def get_app_module(self, module_name):
        import_path = '{0}.{1}'.format(self.app_name, module_name)

        try:
            module = import_child(import_path)
        except ImportError:
            raise GeneratorError('Could not import {0}.'.format(import_path))

        return module