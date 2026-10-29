"""
Contains error handlers
"""
from datetime import datetime, timezone
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
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    return render_template('errors/500.html', now=now), 500
