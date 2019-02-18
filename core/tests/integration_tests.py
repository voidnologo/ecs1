import unittest

from ..entity import Entity
from ..component import Component


class ComponentEntityTests(unittest.TestCase):

    def test_adding_a_component_to_an_entity_addes_the_entity_to_the_components_catalog(self):
        Component.catalog = {}
        class C(Component):
            defaults = {'a': 'b'}
        e = Entity('player')
        c = C()
        e.comp = c
        self.assertEqual(C.catalog, {e: c})

    def test_adding_compenent_to_entity_replaces_entry_in_component_catalog(self):
        Component.catalog = {}
        class C(Component):
            defaults = {'a': 'b'}
        e = Entity('player')
        c1 = C()
        e.comp = c1
        c2 = C()
        e.other_comp = c2
        self.assertEqual(C.catalog, {e: c2})


