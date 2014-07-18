# -*- coding: utf-8 -*-

"""
this is an integration "unit" test.
"""

import unittest

from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from ploneconf2014.theme.config import PROJECTNAME, DEPENDENCIES
from ploneconf2014.theme.testing import INTEGRATION_TESTING

class InstallTestCase(unittest.TestCase):
	"""
	The class that tests the installation of a particular products
	"""

	layer = INTEGRATION_TESTING

	def setUp(self):
		self.portal = self.layer['portal']
		self.qi = api.portal.get_tool(name='portal_quickinstaller')

	def test_installed(self):
		"""
		this method test the default genericsetup profile of this package
		"""
		self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

	def test_dependencies_installed(self):
		"""
		This method test that dependences products are installed of
		"""

		expected = set(DEPENDENCIES)
		installed = self.qi.listInstalledProducts(showHidden=True)
		installed = set([products['id'] for products in installed])
		result = sorted(expected - installed)

		self.assertTrue(
			result,
			"These dependencies are not installed: " + ", ".join(result)

		)

