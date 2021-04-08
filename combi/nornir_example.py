from nornir import InitNornir
nr = InitNornir(
    config_file="config.yaml",
    runner={
        "plugin": "threaded",
        "options": {
            "num_workers": 50,
        },
    },
)

nr.config.runner.options["num_workers"]