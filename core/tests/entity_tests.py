import unittest
import uuid

from ..entity import Entity
from ..component import Component


class EnitityTests(unittest.TestCase):

    def test_created_entity_uses_passed_in_name_and_uid(self):
        name = 'player'
        uid = 1
        e = Entity(name=name, uid=uid)
        self.assertEqual(e.name, name)
        self.assertEqual(e.uid, uid)

    def test_uid_is_set_to_a_uuid_if_not_passed_in(self):
        e = Entity('test')
        self.assertValidUUID4(e.uid)

    def test_repr_shows_class_name_and_object_name(self):
        name = 'player'
        uid = uuid.uuid4()
        e = Entity(name=name, uid=uid)
        expected = f'<Entity {name}:{uid}>'
        self.assertEqual(repr(e), expected)

    def test_is_hashable(self):
        uid = uuid.uuid4()
        e = Entity('test', uid=uid)
        expected = hash(uid)
        self.assertEqual(hash(e), expected)

    def test_equality_with_if_entities_have_same_id(self):
        e = Entity('test')
        self.assertTrue(e == e)

    def test_equality_with_different_entities(self):
        e = Entity(name='e')
        o = Entity(name='o')
        self.assertFalse(e == o)

    def test_class_catalog_contains_reference_to_each_instance_by_name(self):
        name = 'player'
        e = Entity(name=name)
        expected = {name: e}
        self.assertEqual(Entity.catalog, expected)

    def test_class_catalog_does_not_add_new_instance_if_same_name(self):
        name = 'player'
        e = Entity(name=name)
        o = Entity(name=name)
        expected = {name: e}
        self.assertEqual(Entity.catalog, expected)

    def test_dictionary_assignment_adds_attribute_to_entity(self):
        class C(Component):
            defaults = {}
        e = Entity(name='player')
        c = C()
        e['some_val'] = c
        self.assertEqual(e.components['some_val'], c)

    def test_dictionary_assignment_sets_entity_if_value_is_a_component(self):
        class A(Component):
            defaults = {'a': 'b'}
        e = Entity(name='player')
        a = A()
        e['some_val'] = a
        self.assertEqual(a.entity, e)

    def test_dictionary_lookup_gets_value(self):
        class C(Component):
            defaults = {}
        e = Entity(name='player')
        c = C()
        e['some_val'] = c
        self.assertEqual(e['some_val'], c)

    def test_dot_assignment_adds_component_attribute_to_entity(self):
        class C(Component):
            defaults = {}
        e = Entity(name='player')
        c = C()
        e.some_val = c
        self.assertEqual(e.components['some_val'], c)

    def test_dot_assignment_gets_attribute_from_entity(self):
        class C(Component):
            defaults = {}
        e = Entity(name='player')
        c = C()
        e.some_val = c
        self.assertEqual(e.some_val, c)

    def test_dot_assignment_sets_entity_if_value_is_a_component(self):
        class A(Component):
            defaults = {'a': 'b'}
        e = Entity(name='player')
        a = A()
        e.some_val = a
        self.assertEqual(a.entity, e)

    def assertValidUUID4(self, uuid_to_test):
        try:
            uuid_obj = uuid.UUID(uuid_to_test, version=4)
        except:
            return False
        return str(uuid_obj) == uuid_to_test
