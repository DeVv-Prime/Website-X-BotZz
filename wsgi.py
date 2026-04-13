#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WSGI Entry Point for Vectro Cloud
"""

import os
import sys

# Add project directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, socketio

# This is what Gunicorn looks for
application = app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    socketio.run(application, host='0.0.0.0', port=port, debug=False, allow_unsafe_werkzeug=True)
