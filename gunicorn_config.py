from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

workers = 2
worker_class = "sync"
bind = "0.0.0.0:5000"

def child_exit(server, worker):
    GunicornInternalPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)
