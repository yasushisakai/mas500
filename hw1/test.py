import unittest, compare

class TestCompare (unittest.TestCase):
	vals = {}
	def testReadArgsNoArgs (self):
		sys.argv = ['compare.py']
		res = MC_HW1intermediate.call_media_cloud()
		assert res!=None
	def testReadArgsOK (self):
		sys.argv = ['compare.py','cats', 'dogs']
		res = compare.readArgs()
		assert res == 'cats AND dogs'
	def testReadConfig (self):
		self.vals = compare.readConfigFile()
		assert vals!=None
	def testcallMediaCloudAPI (self):
		res = compare.callMediaCloudAPI(self.vals)
		self.assertEquals(len(res),2)
		assert res!=None

if __name__ == "__main__":
    unittest.main()