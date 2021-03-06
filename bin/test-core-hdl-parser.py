#! /usr/bin/env python3

####################################################################################################
#
# PyCpuSimulator - AVR Simulator
# Copyright (C) 2015 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

"""Test the HDL parser for instruction operations.
"""

# Fixme: Some operations are supported !!!

####################################################################################################
#
# Logging
#

import PyCpuSimulator.Logging.Logging as Logging

logger = Logging.setup_logging('pysimavr')

####################################################################################################

from PyCpuSimulator.Core.CoreHdlParser import Parser

####################################################################################################

parser = Parser()

with open('data/operations.txt') as f:
    source = f.read()
    # parser.test_lexer(source)
    for line_number, line in enumerate(source.split('\n')):
        if line and not line.startswith('#'):
            print()
            print('='*80)
            print(line_number, ':', line)
            # print()
            # parser.test_lexer(line)
            # try:
            program = parser.parse(line + ';')
            print()
            print(program)
            # except:
            #     print("Parse error")
