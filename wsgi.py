#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from gevent import monkey
# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()

base_path = os.path.dirname(os.path.abspath(__file__))
# Insert local directories into path
sys.path.append(base_path)
sys.path.append(os.path.join(base_path, 'cps'))
sys.path.append(os.path.join(base_path, 'vendor'))

from web import *

