import json


class Component:

    defaults = dict()
    catalog = dict()
    component_types = dict()

    def __new__(cls, entity=None, **properties):
        cname = cls.__name__
        if cname not in Component.component_types:
            Component.component_types[cname] = cls
            cls.catalog = dict()
        if entity not in cls.catalog:
            cls.catalog[entity] = super().__new__(cls)
        return cls.catalog[entity]

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

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def reset(self):
        for prop_name, value in self.defaults.items():
            seattr(self, prop_name, value)
