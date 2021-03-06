# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2015-2016 by EcpyPulses Authors, see AUTHORS for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Load the standard fixtures to test the workspace.

"""
from __future__ import (division, unicode_literals, print_function,
                        absolute_import)

import pytest
import enaml

with enaml.imports():
    from ..contributions import PulsesContributions

pytest_plugins = str('ecpy_pulses.testing.workspace.fixtures'),


@pytest.fixture
def workspace(pulses_workspace):
    """Simply register the contributions for testing.

    """
    pulses_workspace.workbench.register(PulsesContributions())
    return pulses_workspace
