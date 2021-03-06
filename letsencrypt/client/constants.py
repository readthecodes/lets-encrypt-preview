"""Let's Encrypt constants."""
import pkg_resources

from letsencrypt.acme import challenges


EXCLUSIVE_CHALLENGES = frozenset([frozenset([
    challenges.DVSNI, challenges.SimpleHTTPS])])
"""Mutually exclusive challenges."""


ENHANCEMENTS = ["redirect", "http-header", "ocsp-stapling", "spdy"]
"""List of possible :class:`letsencrypt.client.interfaces.IInstaller`
enhancements.

List of expected options parameters:
- redirect: None
- http-header: TODO
- ocsp-stapling: TODO
- spdy: TODO

"""


APACHE_MOD_SSL_CONF = pkg_resources.resource_filename(
    "letsencrypt.client.plugins.apache", "options-ssl.conf")
"""Path to the Apache mod_ssl config file found in the Let's Encrypt
distribution."""

APACHE_REWRITE_HTTPS_ARGS = [
    "^.*$", "https://%{SERVER_NAME}%{REQUEST_URI}", "[L,R=permanent]"]
"""Apache rewrite rule arguments used for redirections to https vhost"""


NGINX_MOD_SSL_CONF = pkg_resources.resource_filename(
    "letsencrypt.client.plugins.nginx", "options-ssl.conf")
"""Path to the Nginx mod_ssl config file found in the Let's Encrypt
distribution."""


CONFIG_DIRS_MODE = 0o755
"""Directory mode for ``.IConfig.config_dir`` et al."""

TEMP_CHECKPOINT_DIR = "temp_checkpoint"
"""Temporary checkpoint directory (relative to IConfig.work_dir)."""

IN_PROGRESS_DIR = "IN_PROGRESS"
"""Directory used before a permanent checkpoint is finalized (relative to
IConfig.work_dir)."""

CERT_KEY_BACKUP_DIR = "keys-certs"
"""Directory where all certificates and keys are stored (relative to
IConfig.work_dir. Used for easy revocation."""

ACCOUNTS_DIR = "accounts"
"""Directory where all accounts are saved."""

ACCOUNT_KEYS_DIR = "keys"
"""Directory where account keys are saved. Relative to ACCOUNTS_DIR."""

REC_TOKEN_DIR = "recovery_tokens"
"""Directory where all recovery tokens are saved (relative to
IConfig.work_dir)."""

NETSTAT = "/bin/netstat"
"""Location of netstat binary for checking whether a listener is already
running on the specified port (Linux-specific)."""
