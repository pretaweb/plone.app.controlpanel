# -*- coding: utf-8 -*-
"""Functional Doctests for plone.app.controlpanel.
"""
import doctest

import unittest2 as unittest
import pprint

from plone.testing import layered

from plone.app.controlpanel.testing import \
    PLONE_APP_CONTROLPANEL_FUNCTIONAL_TESTING


optionflags = (
    doctest.ELLIPSIS | \
    doctest.NORMALIZE_WHITESPACE | \
    doctest.REPORT_ONLY_FIRST_FAILURE)
normal_testfiles = [
    'calendar.txt',
    'editing.txt',
    'filter.txt',
    'mail.txt',
    'maintenance.txt',
    'security_enable_user_folder.txt',
    'search.txt',
    'site.txt',
    'skins.txt',
    'markup.txt',
    'navigation.txt',
    'types.txt',
]


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite(test,
                                     optionflags=optionflags,
                                     globs={'pprint': pprint.pprint,
                                            }
                                     ),
                layer=PLONE_APP_CONTROLPANEL_FUNCTIONAL_TESTING)
        for test in normal_testfiles])
    return suite
