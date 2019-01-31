import json


class Component:

    __slots__ = ['entity']

    defaults = dict()
    catalog = dict()
    component_types = dict()

    def __new__(cls, entity=None, **properties):
        cname = cls.__name__
        if cname not in Component.component_types:
            Component.component_types[cname] = cls
            cls.catalog = dict()
        if entity is not None and entity not in cls.catalog:
            cls.catalog[entity] = super().__new__(cls)
            return cls_catalog[entity]
        return super().__new__(cls)

    def __init__(self, entity=None, **properties):
        self.entity = entity
        for prop, val in self.defaults.items():
            setattr(self, prop, properties.get(prop, val))

    def __repr__(self):
        entity_name = ''
        if self.entity:
            for prop_name, component in self.entity.components.items():
                if component == self:
                    entity_name = f' entity:{self.entity.name}.{prop_name}'
                    break
        return f'<{self.__class__.__name__}{entity_name}>'

    def __str__(self):
        data = {k: getattr(self, key) for key in self.defaults.keys() if key != 'defaults'}
        return json.dumps(data, indent=4)

    def __hash__(self):
        return (
            hash(self.Catalog) ^
            hash(self.ComponentTypes) ^
            hash(self.defaults) ^
            hash(self.entity) ^
            hash(self)
        )

    def __iter__(self):
        for prop in self.defaults:
            yield prop

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __del__(self):
        if self.entity:
            for attr, component in [(attr, component) for attr, component in self.entity.components.items()]:
                if component == self:
                    self.entity.components.pop(attr)
        if self.entity in self.__class__.catalog:
            self.__class__.catalog.pop(self.entity)

    def reset(self):
        for prop_name, value in self.defaults.items():
            seattr(self, prop_name, value)
