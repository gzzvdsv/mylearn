import json  # 'codecs', 'decoder', 'detect_encoding', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner'

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

data2 = json.dumps(data)
print(data2)
print(dir(json))

import pandas

# 'api', 'array', 'arrays', 'bdate_range', 'compat', 'concat', 'core', \
# 'crosstab', 'cut', 'date_range', 'describe_option', 'errors', 'eval', \
# 'factorize', 'get_dummies', 'get_option', 'infer_freq', 'interval_range',\
# 'io', 'isna', 'isnull', 'json_normalize', 'lreshape', 'melt', 'merge', 'merge_asof', \
# 'merge_ordered', 'notna', 'notnull', 'offsets', 'option_context', 'options', 'pandas', \
# 'period_range', 'pivot', 'pivot_table', 'plotting', 'qcut', 'read_clipboard', 'read_csv', \
# 'read_excel', 'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json', \
# 'read_orc', 'read_parquet', 'read_pickle', 'read_sas', 'read_spss', 'read_sql', 'read_sql_query',\
# 'read_sql_table', 'read_stata', 'read_table', 'read_xml', 'reset_option', 'set_eng_float_format', \
# 'set_option', 'show_versions', 'test', 'testing', 'timedelta_range', 'to_datetime', 'to_numeric',\
# 'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 'value_counts', 'wide_to_long'
print(dir(pandas))
print('=====================================================')
import numpy

lis = dir(numpy)
zp = 0
for i in lis:
    print(i, end="'  '")
    zp += 1
    if zp % 10 == 0:
        print()

# print()

import selenium

print(dir(selenium))
