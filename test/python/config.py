from zensols.config import ExtendedInterpolationEnvConfig


class AppConfig(ExtendedInterpolationEnvConfig):
    @staticmethod
    def instance():
        return AppConfig('test-resources/db.conf')
