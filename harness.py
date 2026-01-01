#!/usr/bin/env python

if (__name__ == '__main__'):
    from zensols.cli import ConfigurationImporterCliHarness
    harness = ConfigurationImporterCliHarness(
        src_dir_name='src',
        app_factory_class='zensols.dbutilpg.ApplicationFactory',
        config_path='test-resources/dbutilpg.conf',
        proto_args='proto',
        proto_factory_kwargs={'reload_pattern': r'^zensols.dbutilpg'},
    )
    harness.run()
