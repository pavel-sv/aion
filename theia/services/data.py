import pandas as pd
import dateutil

from . import utils
from . import ifs


class DataHandler:

    def __init__(self):
        super().__init__()
        self._columns = ifs.Columns()
        self._to_dataframe = FileToDataFrame()
        self._command = {
            'format': self._format_data
        }

    def data_handler_set_properties(self, data_type, file_path):
        self._file_path = file_path
        self._columns = self._columns.columns[data_type]

    @property
    def execute(self):
        return self._command

    @property
    def formated_data(self):
        return self._formated_data

    @formated_data.setter
    def formated_data(self, data):
        self._formated_data = data

    def _format_data(self):
        _data = self._to_dataframe.execute['csv'](self._file_path)
        _columns_to_remove = utils.remove_set_from_list(
            list(_data.columns),
            self._columns['pre-sellected']
        )
        _data = self._drop_data(_data, _columns_to_remove)
        _exempt_list = list(set(
            self._columns['categorical'] +
            self._columns['datetimes'] +
            self._columns['integer'] +
            self._columns['float']
        ))
        _data = self._to_string(_data, _exempt_list)
        _data = self._group_data_by_order_type(_data, 'Order Type')
        for key in _data:
            del _columns_to_remove
            _columns_to_remove = self._return_list_bad_data_columns(
                _data[key],
                95)
            _data[key] = self._drop_data(_data[key], _columns_to_remove)
            _data[key] = self._to_datetime(
                _data[key],
                self._columns['datetimes'])
            _data[key] = self._to_int(_data[key], self._columns['integer'])
            _data[key] = self._to_float(_data[key], self._columns['float'])
            for item in self._columns['year_month']:
                _data[key][item] = pd.Series(self._create_date_series(
                    _data[key]['Created'],
                    item
                ))
            self.formated_data = _data

    @staticmethod
    def _drop_data(data, drop_items):
        data = data.copy(deep=True)
        data.drop(columns=drop_items, axis=1, inplace=True)
        data.reset_index(drop=True, inplace=True)
        return data

    @staticmethod
    def _to_string(data, exempt_list):
        _data = data.copy(deep=True)
        _items_list = list(_data.columns)
        _error_list = list()
        for item in _items_list:
            if item not in exempt_list:
                try:
                    _data[item] = _data[item].astype('string')
                except ValueError as err:
                    print(err, ':', item)
                    _error_list.append(item)
        return _data

    @staticmethod
    def _group_data_by_order_type(data, key):
        group_dict = {}
        grouped = data.groupby(key)
        for name, group in grouped:
            group_dict[name] = group
            group_dict[name].reset_index(drop=True, inplace=True)
        return group_dict

    @staticmethod
    def _return_list_bad_data_columns(data, value):
        _data = data.copy(deep=True)
        _items_list = list(_data.columns)
        _drop_items = list()
        for item in _items_list:
            if _data[item].isna().any():
                x = _data[item].isna().sum()
                y = len(_data[item])
                _result = (x / y * 100)
                if _result > value:
                    _drop_items.append(item)
        return _drop_items

    @staticmethod
    def _to_categorical(data, items_list):
        _data = data.copy(deep=True)
        _columns_list = list(_data.columns)
        for item in items_list:
            if item in _columns_list:
                _data[item] = _data[item].astype('category')
        return _data

    @staticmethod
    def _to_datetime(data, items_list):
        _data = data.copy(deep=True)
        _datetime_list = items_list.copy()
        _columns_list = list(_data.columns)
        _datetime_list = DataHandler._find_datetime_columns(
            _datetime_list,
            _columns_list,
            'Date')
        _error_list = []
        for item in _datetime_list:
            try:
                _data[item] = _data[item].astype('object')
                _data[item] = _data[item].astype('datetime64')
            except ValueError as err:
                print(format(err), ':', item)
                _error_list.append(item)
        for error in _error_list:
            _data[error] = DataHandler._datetime_error_handling(_data[error])
            _data[error] = _data[error].astype('datetime64')
        return _data

    @staticmethod
    def _find_datetime_columns(datetime_list, columns_list, key):
        _items_list = datetime_list.copy()
        for item in columns_list:
            if key in item:
                _items_list.append(item)
        return _items_list

    @staticmethod
    def _datetime_error_handling(series):
        _items_list = list()
        for item in series:
            x = dateutil.parser.parse(item)
            if x.year < 2000:
                y = DataHandler._return_correct_year(x.year)
                x = x.replace(year=y)
            _items_list.append(x)
        return pd.Series(_items_list)

    @staticmethod
    def _return_correct_year(year):
        _st = str(year)
        if _st[-1] == '4':
            return 2014
        elif _st[-1] == '5':
            return 2015

    @staticmethod
    def _to_int(data, int_list):
        _data = data.copy(deep=True)
        _items_list = list(_data.columns)
        _error_list = []
        for item in int_list:
            if item in _items_list:
                if _data[item].isna().any():
                    _data[item] = _data[item].fillna('0')
                try:
                    _data[item] = _data[item].astype('int')
                except ValueError as err:
                    print(format(err))
                    _error_list.append(item)
        return _data

    @staticmethod
    def _to_float(data, float_list):
        _data = data.copy(deep=True)
        _items_list = list(_data.columns)
        _error_list = []
        for item in float_list:
            if item in _items_list:
                try:
                    _data[item] = _data[item].astype('float')
                except ValueError as err:
                    print(format(err), ':', item)
                    _error_list.append(item)
        for error in _error_list:
            _data[error] = pd.Series(
                utils.remove_space_from_string(_data[error]))
            _data[error] = pd.Series(
                utils.localize_float_units(_data[error]))
            _data[error] = _data[error].astype('float')
        return _data

    @staticmethod
    def _create_date_series(series, name):
        _items_list = list()
        for item in series:
            if name == 'Year':
                _items_list.append(int(item.strftime('%Y')))
            elif name == 'Month':
                _items_list.append(int(item.strftime('%m')))
        return _items_list


class FileToDataFrame:

    def __init__(self):
        super().__init__()
        self._execute = {
            'csv': self._convert_csv_to_dataframe
        }

    @property
    def execute(self):
        return self._execute

    def _convert_csv_to_dataframe(self, file_path):
        return pd.read_csv(
            file_path,
            encoding='unicode-escape',
            low_memory=False)
