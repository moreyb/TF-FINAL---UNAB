SCHEDULER_CONFIG = {
    'job_defaults': {
        'coalesce': False,
        'max_instances': 1
    },
    'executors': {
        'default': {
            'type': 'threadpool',
            'max_workers': 20
        }
    }
}
