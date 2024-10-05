class Field:

    def __init__(self):
        self.column_name = None
        self.internal_name = None

    def __set_name__(self, owner, column_name):
        self.column_name = column_name
        self.internal_name = "_" + column_name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, "")

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer:
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


cust = Customer()
print(f"Before: {cust.first_name!r} {cust.__dict__}")
cust.first_name = "Euclid"
print(f"After:  {cust.first_name!r} {cust.__dict__}")
