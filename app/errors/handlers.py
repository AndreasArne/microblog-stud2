"""
Contains error handlers
"""
from flask import render_template, current_app
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    """
    Error handler for code 404
    """
    current_app.logger.info(error)
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    """
    Error handler for code 500
    """
    current_app.logger.info(error)
    db.session.rollback()
    return render_template('errors/500.html'), 500

import subprocess


def run(cmd):
    """Bad on purpose, Bandit B602"""
    return subprocess.call(cmd, shell=True)
