# git_rpm
Config files to build rpm packages of git.

## Download package from Github Release
### RPM package
```bash
$ curl -s https://api.github.com/repos/mozzzzy/git_rpm/releases | \
  jq '.[].assets[] | select(.name == "git-2.33.0-0.el7.x86_64.rpm")' | \
  jq '.url' | \
  xargs curl -vLJO -H 'Accept: application/octet-stream'
```

## Build
### Get source code of git
```bash
$ git submodule update --init
```

### Build rpm packages
```bash
$ make all
```
Then the rpm packages are created in `rpmbuild/RPMS/x86_64` and `rpmbuild/SRPMS`.
```bash
$ tree rpmbuild/ -I BUILD
rpmbuild/
|-- BUILDROOT
|-- RPMS
|   `-- x86_64
|       |-- git-2.33.0-0.el7.x86_64.rpm
|       `-- git-debuginfo-2.33.0-0.el7.x86_64.rpm
|-- SOURCES
|   `-- git.tar.gz
|-- SPECS
|   `-- git.spec
`-- SRPMS
    `-- git-2.33.0-0.el7.src.rpm

    6 directories, 5 files
```
