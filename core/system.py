from .component import Component


class System:

    components = set()
    catalog = dict()

    def __new__(cls, name=None, components=None):
        components = components or []
        name = cls.__name__ if name is None else name
        if name not in System.catalog:
            system = super().__new__(cls)
            system.catalog[name] = system
        return System.catalog[name]

    def __init__(self, name=None, components=None):
        self.name = name
        if components is not None:
            self.components |= set(components)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name}>'

    def update(self, dt=None):
        raise NotImplemented('System must define its own update')

    @property
    def entities(self):
        return list(set(
            entity
            for component_cls in self.component_classes
            for entity in component_cls.catalog.keys()
            if entity is not None
        ))

    @property
    def component_classes(self):
        return list(set(
            Component.component_types.get(component_name)
            for component_name in self.components
            if component_name in Component.component_types
        ))
