"""Cmdlr config system."""

import os

from . import yamla
from . import schema


def _normalize_path(path):
    return os.path.expanduser(path)


class Config:
    """Config maintainer object."""

    default_config = {
        'delay': 5.0,
        'dirs': ['~/comics'],
        'disabled_analyzers': [],
        'extra_analyzer_dir': None,
        'max_concurrent': 10,
        'max_retry': 4,
        'per_host_concurrent': 2,
        'proxy': None,
    }

    default_config_filepath = os.path.join(
        os.getenv(
            'XDG_CONFIG_HOME',
            os.path.join(os.path.expanduser('~'), '.config'),
        ),
        'cmdlr',
        'config.yaml',
    )

    @classmethod
    def __build_config_file(cls, filepath):
        """Create a config file template at specific filepath."""
        dirpath = os.path.dirname(filepath)

        os.makedirs(dirpath, exist_ok=True)
        yamla.to_file(filepath, cls.default_config, comment_out=True)

    def __init__(self):
        """Init the internal __config variable."""
        self.__config = schema.config(type(self).default_config)

    def load_or_build(self, *filepaths):
        """Load and update internal config from specific filepaths.

        If filepath in filepaths not exists, build it with default
        configuration.
        """
        for filepath in filepaths:
            if not os.path.exists(filepath):
                type(self).__build_config_file(filepath)

            incoming_config = schema.config(yamla.from_file(filepath))

            self.__config = schema.config({
                **self.__config,
                **incoming_config,
            })

    @property
    def incoming_dir(self):
        """Get incoming dir."""
        return _normalize_path(
            self.__config.get('dirs')[0]
        )

    @property
    def dirs(self):
        """Get all dirs."""
        return list(map(
            _normalize_path,
            self.__config.get('dirs'),
        ))

    @property
    def extra_analyzer_dir(self):
        """Get extra analyzer dir."""
        extra_analyzer_dir = self.__config.get('extra_analyzer_dir')

        if extra_analyzer_dir:
            return _normalize_path(extra_analyzer_dir)

    @property
    def disabled_analyzers(self):
        """Get disabled analyzers."""
        return self.__config.get('disabled_analyzers')

    @property
    def per_host_concurrent(self):
        """Get per-host concurrent number."""
        return self.__config.get('per_host_concurrent')

    @property
    def max_concurrent(self):
        """Get maximum concurrent number."""
        return self.__config.get('max_concurrent')

    @property
    def max_retry(self):
        """Get max retry number."""
        return self.__config.get('max_retry')

    @property
    def delay(self):
        """Get global download delay."""
        return self.__config.get('delay')

    @property
    def proxy(self):
        """Get extra analyzer dir."""
        return self.__config.get('proxy')

    def get_customization(self, analyzer_name):
        """Get user setting for an analyzer."""
        return self.__config.get('customization', {}).get(analyzer_name, {})