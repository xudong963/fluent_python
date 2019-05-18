# collections.namedtuple

from collections import namedtuple

# 创建一个具名元组需要两个参数:类名，类的各个字段的名字
City = namedtuple('City', 'name country pop coordinates')
tokyo = City('Tokyo', 'Jp', '121', (1212, 1212))
print(type(tokyo))
print(tokyo)

print(tokyo.pop)
print(tokyo[0])


# 具名函数专有的属性: _fields, _make(iterable) , _asdict()

# 生成一个包含这个类所有字段名称的元组
print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')     # 经纬度
delhi_data= ('Delhi NCR', 'IN', 21.4, LatLong(216, 311))

delhi = City._make(delhi_data)   # 生成city类的实例 等价于 delhi = City(*delhi_data)
print(delhi._asdict())      # 生成 collections.OrderedDict
# Output: OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('pop', 21.4), ('coordinates', LatLong(lat=216, long=311))])

for key, value in delhi._asdict().items():
    print(key + ':', value)



