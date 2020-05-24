from pathlib import Path
from zensols.pybuild import SetupUtil

su = SetupUtil(
    setup_path=Path(__file__).parent.absolute(),
    name="zensols.dbpg",
    package_names=['zensols', 'resources'],
    # package_data={'': ['*.html', '*.js', '*.css', '*.map', '*.svg']},
    description='PostgreSQL Implementation of the dbutil library.',
    user='plandes',
    project='dbutilpg',
    keywords=['tooling'],
    has_entry_points=False,
).setup()
