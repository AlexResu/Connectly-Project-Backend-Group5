from django.test import TestCase
from singletons.config_manager import ConfigManager


class ConfigManagerTest(TestCase):

    def test_singleton_instance(self):
        config1 = ConfigManager()
        config2 = ConfigManager()

        self.assertIs(config1, config2)

        config1.set_setting("DEFAULT_PAGE_SIZE", 50)
        self.assertEqual(config2.get_setting("DEFAULT_PAGE_SIZE"), 50)

