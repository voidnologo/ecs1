import unittest

from ..component import Component


class ComponentTests(unittest.TestCase):

    class Child(Component):
        defaults = {'a': 'b'}

    def test_init_sets_default_values_on_child_classes(self):
        self.assertEqual(self.Child.defaults['a'], 'b')
        c = self.Child()
        self.assertEqual(c.a, 'b')

    def test_init_overrides_default_values_of_child_classes(self):
        self.assertEqual(self.Child.defaults['a'], 'b')
        c = self.Child(a='c')
        self.assertEqual(c.a, 'c')

    def test_init_only_sets_attributes_listed_in_defaults(self):
        c = self.Child(a='c', d='e')
        self.assertEqual(c.a, 'c')
        with self.assertRaises(AttributeError):
            c.d

    def test_component_class_keeps_track_of_child_class_types(self):
        class A(Component):
            defaults = {'a': 'b'}
        class B(Component):
            defaults = {'x': 'y'}
        A()
        B()
        self.assertEqual(Component.component_types, {'A': A, 'B': B, 'Child': self.Child})

    def test_can_get_attributes_by_dictionary_style_lookup(self):
        c = self.Child(a='x')
        self.assertEqual(c['a'], 'x')

    def test_can_get_attributes_by_dot_lookup(self):
        c = self.Child(a='x')
        self.assertEqual(c.a, 'x')

    def test_can_set_attributes_by_dictionary_style_lookup(self):
        c = self.Child()
        c['a'] = 'x'
        self.assertEqual(c['a'], 'x')

    def test_can_set_attributes_by_dot_lookup(self):
        c = self.Child()
        c.a = 'x'
        self.assertEqual(c.a, 'x')

    def test_reset_sets_attributes_back_to_class_defaults(self):
        c = self.Child()
        c.a = 'x'
        self.assertEqual(c.a, 'x')
        c.reset()
        self.assertEqual(c.a, 'b')

    def tests_component_iterates_over_attributes(self):
        class Comp(Component):
            defaults = {'a': 1, 'b': 2, 'c': 3}
        c = Comp()
        self.assertEqual(list(c), ['a', 'b', 'c'])

    def test_component_catalog_keeps_track_of_all_entities_with_component(self):
        c = self.Child(entity='fish')
        self.assertEqual(self.Child.catalog, {'fish': c})

    def test_str_returns_formatted_json_of_attributes(self):
        c = self.Child()
        expected = '{\n    "a": "b"\n}'
        self.assertEqual(str(c), expected)
