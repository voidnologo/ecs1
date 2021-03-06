import uuid

from .component import Component


class Entity:

    __slots__ = ['uid', 'name', 'components']
    catalog = dict()

    def __new__(cls, name=None, uid=None):
        if name not in cls.catalog:
            entity = super().__new__(cls)
            cls.catalog[name] = entity
        return cls.catalog[name]


    def __init__(self, name, uid=None):
        self.name = name
        self.uid = uuid.uuid4() if uid is None else uid
        self.components = dict()

    def __repr__(self):
        name = f'{self.name}:{self.uid}' if self.name else str(self.uid)
        return f'<{self.__class__.__name__} {name}>'

    def __str__(self):
        return str(self.components)

    def __hash__(self):
        return hash(self.uid)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.uid == other.uid
        return False

    def __getitem__(self, key):
        return self.components[key]

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getattr__(self, key):
        return self.components[key]

    def __setattr__(self, key, value):
        if key in super().__getattribute__('__slots__'):
            super().__setattr__(key, value)
        if isinstance(value, Component):
            value.entity = self
            # update component catalog with self
            value.__class__.catalog[self] = value
            self.components[key] = value

    # def __del__(self):
    #     for attr, component in self.components.items():
    #         if hasattr(component, 'entity'):
    #             component.entity = None
    #             component.__class__.catalog.pop(self, None)
    #     self.__class__.catalog.pop(self.name)
