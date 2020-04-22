#!/bin/sh

set -eu

name=git-interactive-rebase-tool
version=1.2.1

spec=$name.spec
basename=$name-$version
url=https://github.com/MitMaro/git-interactive-rebase-tool/archive/$version/$basename.tar.gz
tarball=$basename.tar.gz
crates=$basename-crates.tar.xz

curl -sSfL "$url" -o $(basename "$url")

tar xf "$tarball"
cd $basename

cargo vendor

install -d .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
cd ..

tar cJf $crates $basename/{vendor,Cargo.lock,.cargo}
rm -rf $basename

./builder -5 $spec
test -x ./dropin && ./dropin $crates
