#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v25
# autospec commit: 9594167
#
Name     : R-textshaping
Version  : 1.0.1
Release  : 37
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/textshaping_1.0.1.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/textshaping_1.0.1.tar.gz
Summary  : Bindings to the 'HarfBuzz' and 'Fribidi' Libraries for Text
Group    : Development/Tools
License  : MIT
Requires: R-textshaping-lib = %{version}-%{release}
Requires: R-cpp11
Requires: R-lifecycle
Requires: R-stringi
Requires: R-systemfonts
BuildRequires : R-cpp11
BuildRequires : R-lifecycle
BuildRequires : R-stringi
BuildRequires : R-systemfonts
BuildRequires : R-systemfonts-dev
BuildRequires : buildreq-R
BuildRequires : pkgconfig(fribidi)
BuildRequires : pkgconfig(harfbuzz)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
'HarfBuzz' library and the bidirectional algorithm in the 'Fribidi'
    library.  'textshaping' is a low-level utility package mainly for
    graphic devices that expands upon the font tool-set provided by the
    'systemfonts' package.

%package dev
Summary: dev components for the R-textshaping package.
Group: Development
Requires: R-textshaping-lib = %{version}-%{release}
Provides: R-textshaping-devel = %{version}-%{release}
Requires: R-textshaping = %{version}-%{release}

%description dev
dev components for the R-textshaping package.


%package lib
Summary: lib components for the R-textshaping package.
Group: Libraries

%description lib
lib components for the R-textshaping package.


%prep
%setup -q -n textshaping
pushd ..
cp -a textshaping buildavx2
popd
pushd ..
cp -a textshaping buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1746134609

%install
export SOURCE_DATE_EPOCH=1746134609
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/textshaping/DESCRIPTION
/usr/lib64/R/library/textshaping/INDEX
/usr/lib64/R/library/textshaping/LICENSE
/usr/lib64/R/library/textshaping/Meta/Rd.rds
/usr/lib64/R/library/textshaping/Meta/features.rds
/usr/lib64/R/library/textshaping/Meta/hsearch.rds
/usr/lib64/R/library/textshaping/Meta/links.rds
/usr/lib64/R/library/textshaping/Meta/nsInfo.rds
/usr/lib64/R/library/textshaping/Meta/package.rds
/usr/lib64/R/library/textshaping/Meta/vignette.rds
/usr/lib64/R/library/textshaping/NAMESPACE
/usr/lib64/R/library/textshaping/NEWS.md
/usr/lib64/R/library/textshaping/R/textshaping
/usr/lib64/R/library/textshaping/R/textshaping.rdb
/usr/lib64/R/library/textshaping/R/textshaping.rdx
/usr/lib64/R/library/textshaping/doc/c_interface.R
/usr/lib64/R/library/textshaping/doc/c_interface.Rmd
/usr/lib64/R/library/textshaping/doc/c_interface.html
/usr/lib64/R/library/textshaping/doc/index.html
/usr/lib64/R/library/textshaping/help/AnIndex
/usr/lib64/R/library/textshaping/help/aliases.rds
/usr/lib64/R/library/textshaping/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/textshaping/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/textshaping/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/textshaping/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/textshaping/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/textshaping/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/textshaping/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/textshaping/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/textshaping/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/textshaping/help/paths.rds
/usr/lib64/R/library/textshaping/help/textshaping.rdb
/usr/lib64/R/library/textshaping/help/textshaping.rdx
/usr/lib64/R/library/textshaping/html/00Index.html
/usr/lib64/R/library/textshaping/html/R.css
/usr/lib64/R/library/textshaping/lorem/README
/usr/lib64/R/library/textshaping/lorem/arabic.txt
/usr/lib64/R/library/textshaping/lorem/armenian.txt
/usr/lib64/R/library/textshaping/lorem/chinese.txt
/usr/lib64/R/library/textshaping/lorem/cyrillic.txt
/usr/lib64/R/library/textshaping/lorem/devanagari.txt
/usr/lib64/R/library/textshaping/lorem/georgian.txt
/usr/lib64/R/library/textshaping/lorem/greek.txt
/usr/lib64/R/library/textshaping/lorem/hangul.txt
/usr/lib64/R/library/textshaping/lorem/hebrew.txt
/usr/lib64/R/library/textshaping/lorem/kana.txt
/usr/lib64/R/library/textshaping/lorem/latin.txt
/usr/lib64/R/library/textshaping/tests/testthat.R
/usr/lib64/R/library/textshaping/tests/testthat/test-bidi.R

%files dev
%defattr(-,root,root,-)
/usr/lib64/R/library/textshaping/include/textshaping.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/textshaping/libs/textshaping.so
/V4/usr/lib64/R/library/textshaping/libs/textshaping.so
/usr/lib64/R/library/textshaping/libs/textshaping.so
