class ObjectCopier:
    @staticmethod
    def copy_attributes(source, target):
        source_attrs = dir(source)
        for attr in source_attrs:
            if not attr.startswith('__') and hasattr(target, attr):
                setattr(target, attr, getattr(source, attr))