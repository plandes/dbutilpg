# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [Unreleased]


## [1.5.0] - 2025-12-31
### Removed
- Python 3.11 support.

### Added
- Python 3.13 support.

### Changed
- Switch build tools to [pixi].
- Upgrade [zensols.util] to v1.16.2.


## [1.4.0] - 2025-01-11
### Removed
- Support for Python 3.10.

### Changed
- Upgraded to [zensols.util] version 1.15.


## [1.3.0] - 2024-01-17
### Changed
- Relax requirements for [zensols.dbutil] version 1.3.0.


## [1.2.0] - 2023-12-05
### Changed
- Upgrade the Postgres driver module `psycopg2`.
- Upgrade to [zensols.dbutil] version 1.2.0

### Added
- Support for Python 3.11.

### Removed
- Support for Python 3.9.


## [1.1.0] - 2023-08-16
Functional and downstream moderate risk update release.

### Changed
- [zensols.dbutil] dependency, which has other downstream dependencies that
  changes how configuration is handled.


## [1.0.0] - 2023-02-02
### Changed
- Fix tests after upgrading `zensols.dbutil` .
- Updated [zensols.db] to 1.0.0.


## [0.1.0] - 2022-10-01
First stable feature release.

### Added
- Identity row factory.

### Changed
- Switch to new `DBError` in place of generic error.
- Inline `dataclass` field documentation.
- New dependencies and doc.

### Removed
- Support for Python 3.7 and 3.8.


## [0.0.5] - 2021-01-12
### Added
- [Pandas] data frame read access in `DbPersister`.


## [0.0.4] - 2020-12-09
### Added
- Sphinx documentation, which includes API docs.


## [0.0.3] - 2020-05-05
### Changed
- Remove `ConnectionManagerConfigurer` as a part of upgrading to `zensol.util`
  per v. 1.2.3.


## [0.0.2] - 2020-04-25
### Changed
- Upgrade to `zensols.util` 1.2.0.


## [0.0.1] - 2019-08-07
### Added
- Initial version.


<!-- links -->
[Unreleased]: https://github.com/plandes/dbutilpg/compare/v1.5.0...HEAD
[1.5.0]: https://github.com/plandes/dbutilpg/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/plandes/dbutilpg/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/plandes/dbutilpg/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/plandes/dbutilpg/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/plandes/dbutilpg/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/plandes/dbutilpg/compare/v0.1.0...v1.0.0
[0.1.0]: https://github.com/plandes/dbutilpg/compare/v0.0.5...v0.1.0
[0.0.5]: https://github.com/plandes/dbutilpg/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/plandes/dbutilpg/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/plandes/dbutilpg/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/plandes/dbutilpg/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/plandes/dbutilpg/compare/v0.0.0...v0.0.1


[Pandas]: https://pandas.pydata.org
[zensols.dbutil]: https://github.com/plandes/dbutil
[pixi]: https://pixi.sh
