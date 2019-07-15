# 特殊方法 __missing__

# 所有的映射类型在处理找不到键的时候，都会牵扯到__missing__方法
# 基类dict中是没有这个方法的，但是可以在继承类中实现这个方法，当__getitem__找不到键的时候,python就会自己调用

# __missing__只会被__getitem__方法调用
# 如果自己定义一个映射类,更合适的策略是继承collection.UserDict类

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self(str(key))

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default


def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys()



    