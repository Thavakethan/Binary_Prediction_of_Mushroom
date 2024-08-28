import multiprocessing

# Bind to 0.0.0.0 to make the app accessible from outside the container
bind = '0.0.0.0:8000'

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Number of threads per worker
threads = 2

# Log file locations (optional)
accesslog = '-'  # '-' means logs to stdout
errorlog = '-'  # '-' means logs to stdout
loglevel = 'info'  # Choose from: debug, info, warning, error, critical

# Timeout for workers
timeout = 120

# Daemonize (optional): run Gunicorn in the background
# daemon = True
