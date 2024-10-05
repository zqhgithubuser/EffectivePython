class LazyRecord:

    def __init__(self):
        self.exists = 5

    # 实例属性不存在时调用
    def __getattr__(self, name):
        value = f"Value for {name}"
        setattr(self, name, value)
        return value

class LoggingLazyRecord(LazyRecord):
    
    def __getattr__(self, name):
        print(
            f"* Called __getattr__({name!r}), "
            f"populating instance dictionary"
        )
        result = super().__getattr__(name)
        print(f"* Returning {result!r}")
        return result

class ValidatingRecord:

    def __init__(self):
        self.exists = 5

    # 每次访问实例属性时都会调用
    def __getattribute__(self, name):
        print(f"* Called __getattribute__({name!r})")
        try:
            value = super().__getattribute__(name)
            print(f"* Found {name!r}, returning {value!r}")
            return value
        except AttributeError:
            value = f"Value for {name}"
            print(f"* Setting {name!r} to {value!r}")
            setattr(self, name, value)
            return value

class SavingRecord:

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

class LoggingSavingRecord(SavingRecord):

    # 每次设置实例属性时都会调用
    def __setattr__(self, name, value):
        print(f"* Called __setattr__({name!r}, {value!r})")
        super().__setattr__(name, value)

# data = LazyRecord()
# print("Before:", data.__dict__)
# print("foo:   ", data.foo)
# print("After :", data.__dict__)

print("-" * 50)
data = LoggingLazyRecord()
print("exists:         ", data.exists)
print("Before:         ", data.__dict__)
# print("First foo:      ", data.foo)
print("Has first foo:  ", hasattr(data, "foo")) # 属性不存在时，hasattr也会调用__getattr__方法
# print("Second foo:     ", data.foo)
print("After:          ", data.__dict__)
print("Has second foo: ", hasattr(data, "foo"))

print("-" * 50)
data = ValidatingRecord()
print("exists:         ", data.exists)
# print("First foo:      ", data.foo)
print("Has first foo:  ", hasattr(data, "foo")) # hasattr每次都会调用__getattribute__方法
# print("Second foo:     ", data.foo)
print("Has second foo: ", hasattr(data, "foo"))

print("-" * 50)
data = LoggingSavingRecord()
print("Before: ", data.__dict__)
data.foo = 5
print("After:  ", data.__dict__)
data.foo = 7
print("Finally:", data.__dict__)