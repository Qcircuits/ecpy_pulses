# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2015-2016 by EcpyPulses Authors, see AUTHORS for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Check that the manifest does register the tasks.

"""
from __future__ import (division, unicode_literals, print_function,
                        absolute_import)

import enaml

with enaml.imports():
    from ecpy_pulses.tasks.manifest import PulsesTasksManifest

pytest_plugins = (str('ecpy.testing.tasks.fixtures'),)


def test_manifest(task_workbench):
    """Test the addition of the sequence editor.

    """
    task_workbench.register(PulsesTasksManifest())
    pl = task_workbench.get_plugin('ecpy.tasks')

    assert pl.get_task_infos('ecpy_pulses.TransferPulseSequenceTask')
