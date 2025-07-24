class InfoClassMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = ', '.join(f"{key}: {value}" for key, value in self.__dict__.items())
        return f"{class_name}({attrs})"
