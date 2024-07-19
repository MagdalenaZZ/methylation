# vim: syntax=python tabstop=4 expandtab
# coding: utf-8

__author__ = "Uppsala Universitet"
__copyright__ = "Copyright 2024, Uppsala Universitet"
__email__ = "magdalena.z@scilifelab.uu.se"
__license__ = "GPL-3"


def test_dummy():
    from dummy import dummy
    assert dummy() == 1
