#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-textshaping
Version  : 0.1.2
Release  : 1
URL      : https://cran.r-project.org/src/contrib/textshaping_0.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/textshaping_0.1.2.tar.gz
Summary  : Bindings to the 'HarfBuzz' and 'Fribidi' Libraries for Text
Group    : Development/Tools
License  : MIT
Requires: R-textshaping-lib = %{version}-%{release}
Requires: R-cpp11
Requires: R-systemfonts
BuildRequires : R-cpp11
BuildRequires : R-systemfonts
BuildRequires : buildreq-R
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(fribidi)
BuildRequires : pkgconfig(harfbuzz)

%description
library and the bidirectional algorithm in the 'Fribidi' library. 
    'textshaping' is a low-level utility package mainly for graphic devices that 
    expands upon the font tool-set provided by the 'systemfonts' package.

%package lib
Summary: lib components for the R-textshaping package.
Group: Libraries

%description lib
lib components for the R-textshaping package.


%prep
%setup -q -c -n textshaping
cd %{_builddir}/textshaping

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603381168

%install
export SOURCE_DATE_EPOCH=1603381168
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library textshaping
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library textshaping
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library textshaping
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc textshaping || :


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
/usr/lib64/R/library/textshaping/help/paths.rds
/usr/lib64/R/library/textshaping/help/textshaping.rdb
/usr/lib64/R/library/textshaping/help/textshaping.rdx
/usr/lib64/R/library/textshaping/html/00Index.html
/usr/lib64/R/library/textshaping/html/R.css
/usr/lib64/R/library/textshaping/include/textshaping.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/textshaping/libs/textshaping.so
