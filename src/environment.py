from environs import Env


class Environment:
    env = Env()
    env.read_env()

    def __init__(self):
        self.fastapi_host = self.env.str('FASTAPI_HOST', default='127.0.0.1')
        self.fastapi_port = self.env.int('FASTAPI_PORT', default=5000)
        self.fastapi_log_level = self.env.str('FASTAPI_LOG_LEVEL', default='info')


env = Environment()
