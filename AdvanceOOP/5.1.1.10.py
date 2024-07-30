import time

class TimestampMeta (type):
    instantiated_classes = []
    def __new__(mcs , name , bases , dictionary):
        obj = super().__new__(mcs , name , bases , dictionary)
        obj.instantiation_time = time.time()
        
        def get_instantiation_time(obj):
            return obj.instantiation_time
            
            
        obj.get_instantiation_time = classmethod(get_instantiation_time)
        obj.instantiated_classes.append(name)
        return obj

class LegacyClass1(metaclass=TimestampMeta):
    pass

class LegacyClass2(metaclass=TimestampMeta):
    pass

class LegacyClass3(metaclass=TimestampMeta):
    pass

# Instantiate objects
obj1 = LegacyClass1()
obj2 = LegacyClass2()
obj3 = LegacyClass3()

print("LegacyClass1 instantiation time:", LegacyClass1.get_instantiation_time())
print("LegacyClass2 instantiation time:", LegacyClass2.get_instantiation_time())
print("LegacyClass3 instantiation time:", LegacyClass3.get_instantiation_time())

print("\nClasses instantiated by TimestampMeta:")
for class_name in TimestampMeta.instantiated_classes:
    print(class_name)
    
    
    