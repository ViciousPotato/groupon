import logging

# MySQL settings
CONNECTION_STRING = 'mysql://root:@127.0.0.1:3306/groupon?use_unicode=1&charset=utf8'

# Logging level
LOG_LEVEL = logging.INFO
LOG_FILE  = 'log.log'

# Retry times for failed urls
URL_RETRIES = 3

# Update interval in secs
UPDATE_INTERVAL = 10 * 60 # 10 minutes

# Blog update
WP_URL      = 'http://127.0.0.1:8080/wordpress/xmlrpc.php'
WP_USERNAME = 'admin'
WP_PASSWORD = 'admin'
