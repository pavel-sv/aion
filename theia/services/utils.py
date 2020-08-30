from datetime import datetime
import locale


def request_to_dict(request) -> dict:
    q_dict = {}
    a = request.dict()
    for item in a:
        q_dict[item] = request.getlist(item)
    for item in q_dict:
        if len(q_dict[item]) == 1:
            q_dict[item] = q_dict[item][0]
    return q_dict


def return_dated_file_name(file_name) -> str:
    name = datetime_tostring() + '_' + file_name
    return name


def datetime_tostring() -> str:
    return str(datetime.now().strftime("%Y-%m-%d__%H:%M:%S"))


def remove_set_from_list(items_list, sellected_items):
    f_inital_list = items_list.copy()
    f_sellected_list = sellected_items.copy()
    set_1 = set(f_inital_list)
    set_2 = set(f_sellected_list)
    updated_set = set_1.difference(set_2)
    return list(updated_set)


def get_file_extension(file_name: str) -> str:
    split_str = file_name.split('.')
    return split_str[1]


def remove_space_from_string(series):
    _items_list = list()
    for item in series:
        if ' ' in item:
            item = item.replace(' ', '')
            _items_list.append(item)
        else:
            _items_list.append(item)
    return _items_list


def localize_float_units(series):
    locale.setlocale(locale.LC_ALL, '')
    _locale = locale.getlocale()
    _items_list = list()
    for item in series:
        if _locale[0] == 'en_US':
            x = item.replace(',', '.')
            _items_list.append(x)
    return _items_list
