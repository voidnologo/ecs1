import uuid

from component import Component


class Entity:

    __slots__ = ['uid', 'name', 'components']

    def __init__(self, name=None, uid=None):
        self.name = name or ''
        self.uid = uuid.uuid4() if uid is None else uid
        self.components = dict()

    def __repr__(self):
        name = f'{self.name}:{self.uid}' if self.name else str(self.uid)
        return f'<{self.__class__.__name__} {name}>'

    def __str__(self):
        return str(self.components)

    def __getitem__(self, key):
        self.components[key]

    def __setitem__(self, key, value):
        self.components[key] = value

    def __getattr__(self, key):
        if key in super().__getattribute__('__slots__'):
            return super().__getattr__(key)
        return self.components[key]

    def __setattr__(self, key, value):
        if key in super().__getattribute__('__slots__'):
            super().__setattr__(key, value)
        else:
            if isinstance(value, Component) and value.entity is None:
                value.entity = self
                # update component catalog with self
                catalog = value.__class__.catalog
                for entity, component in catalog.items():
                    if component == value:
                        if self not in catalog:
                            catalog.pop(entity)
                            for relationship_name, comp in self.components.items():
                                if comp == value:
                                    self.components.pop(relationship_name)
                                    break
                        catalog[self] = value
            self.components[key] = value
