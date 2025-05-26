from django.core.files.base import ContentFile
from django.test import TestCase


class MediaStorageTest(TestCase):
    def test_upload_and_download_file(self):
        from django.core.files.storage import default_storage

        # Prepare test data
        test_filename = "test_upload.txt"
        test_content = b"Hello, media storage!"
        file = ContentFile(test_content)

        # Upload file
        saved_path = default_storage.save(test_filename, file)
        self.assertTrue(default_storage.exists(saved_path))

        # Download file
        with default_storage.open(saved_path, "rb") as f:
            downloaded_content = f.read()
        self.assertEqual(downloaded_content, test_content)

        # Clean up
        default_storage.delete(saved_path)


class CacheTest(TestCase):
    def test_cache_operations(self):
        from django.core.cache import cache

        # Test setting a value
        cache.set("test_key", "test_value", timeout=300)

        # Test getting a value
        cached_value = cache.get("test_key")
        self.assertEqual(cached_value, "test_value")

        # Test deleting a value
        cache.delete("test_key")
        self.assertIsNone(cache.get("test_key"))

        # Test default value when key doesn't exist
        non_existent = cache.get("does_not_exist", "default")
        self.assertEqual(non_existent, "default")
