import unittest

from hw1 import connect_to_media_cloud, my_api_key

class MediaCloudTest(unittest.TestCase):

    def testConnect(self):
        self.assertTrue(connect_to_media_cloud(my_api_key) is not None)

if __name__ == '__main__':
    unittest.main()
