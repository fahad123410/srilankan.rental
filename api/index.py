"""
Vercel serverless entrypoint.

Vercel's Python runtime looks for a module under /api that exposes a WSGI app.
We import the Flask app object from app.py (root) without running app.run().
"""

from app import app  # noqa: F401

