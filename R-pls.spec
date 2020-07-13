#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pls
Version  : 2.7.2
Release  : 30
URL      : https://cran.r-project.org/src/contrib/pls_2.7-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pls_2.7-2.tar.gz
Summary  : Partial Least Squares and Principal Component Regression
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
Partial Least Squares Regression (PLSR), Principal Component
	Regression (PCR) and Canonical Powered Partial Least Squares (CPPLS).

%prep
%setup -q -c -n pls
cd %{_builddir}/pls

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589536410

%install
export SOURCE_DATE_EPOCH=1589536410
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pls
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pls
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pls
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pls/DESCRIPTION
/usr/lib64/R/library/pls/INDEX
/usr/lib64/R/library/pls/Meta/Rd.rds
/usr/lib64/R/library/pls/Meta/data.rds
/usr/lib64/R/library/pls/Meta/features.rds
/usr/lib64/R/library/pls/Meta/hsearch.rds
/usr/lib64/R/library/pls/Meta/links.rds
/usr/lib64/R/library/pls/Meta/nsInfo.rds
/usr/lib64/R/library/pls/Meta/package.rds
/usr/lib64/R/library/pls/Meta/vignette.rds
/usr/lib64/R/library/pls/NAMESPACE
/usr/lib64/R/library/pls/NEWS.Rd
/usr/lib64/R/library/pls/R/pls
/usr/lib64/R/library/pls/R/pls.rdb
/usr/lib64/R/library/pls/R/pls.rdx
/usr/lib64/R/library/pls/data/Rdata.rdb
/usr/lib64/R/library/pls/data/Rdata.rds
/usr/lib64/R/library/pls/data/Rdata.rdx
/usr/lib64/R/library/pls/doc/index.html
/usr/lib64/R/library/pls/doc/pls-manual.R
/usr/lib64/R/library/pls/doc/pls-manual.Rnw
/usr/lib64/R/library/pls/doc/pls-manual.pdf
/usr/lib64/R/library/pls/help/AnIndex
/usr/lib64/R/library/pls/help/aliases.rds
/usr/lib64/R/library/pls/help/paths.rds
/usr/lib64/R/library/pls/help/pls.rdb
/usr/lib64/R/library/pls/help/pls.rdx
/usr/lib64/R/library/pls/html/00Index.html
/usr/lib64/R/library/pls/html/R.css
/usr/lib64/R/library/pls/tests/RUnit/common/create_refmodels.R
/usr/lib64/R/library/pls/tests/RUnit/common/ref_multiresp.RData
/usr/lib64/R/library/pls/tests/RUnit/common/ref_singresp.RData
/usr/lib64/R/library/pls/tests/RUnit/common/runit.CV.R
/usr/lib64/R/library/pls/tests/RUnit/common/runit.algorithms.R
/usr/lib64/R/library/pls/tests/RUnit/common/runit.jackknife.R
/usr/lib64/R/library/pls/tests/RUnit/common/runit.mvrVal.R
/usr/lib64/R/library/pls/tests/RUnit/common/runit.options.R
/usr/lib64/R/library/pls/tests/RUnit/common/runit.predict.R
/usr/lib64/R/library/pls/tests/RUnit/common/utils.R
/usr/lib64/R/library/pls/tests/RUnit/import/runit.fit.R
/usr/lib64/R/library/pls/tests/RUnit/import/runit.options.R
/usr/lib64/R/library/pls/tests/RUnit/library/runit.CV.R
/usr/lib64/R/library/pls/tests/RUnit/library/runit.mvr_wrappers.R
/usr/lib64/R/library/pls/tests/test_import.R
/usr/lib64/R/library/pls/tests/test_library.R
/usr/lib64/R/library/pls/tests/testthat.R
/usr/lib64/R/library/pls/tests/testthat/pred.cppls.rds
/usr/lib64/R/library/pls/tests/testthat/pred.pcr.rds
/usr/lib64/R/library/pls/tests/testthat/pred.pls.rds
/usr/lib64/R/library/pls/tests/testthat/pred.pls.widekernel.rds
/usr/lib64/R/library/pls/tests/testthat/pred_nocenter.cppls.rds
/usr/lib64/R/library/pls/tests/testthat/pred_nocenter.oscorepls.rds
/usr/lib64/R/library/pls/tests/testthat/pred_nocenter.pcr.rds
/usr/lib64/R/library/pls/tests/testthat/pred_nocenter.pls.rds
/usr/lib64/R/library/pls/tests/testthat/pred_nocenter.pls.widekernel.rds
/usr/lib64/R/library/pls/tests/testthat/test_basic_pls.R
/usr/lib64/R/library/pls/tests/testthat/yarn.cppls.rds
/usr/lib64/R/library/pls/tests/testthat/yarn.oscorespls.rds
/usr/lib64/R/library/pls/tests/testthat/yarn.pcr.rds
/usr/lib64/R/library/pls/tests/testthat/yarn.pls.rds
/usr/lib64/R/library/pls/tests/testthat/yarn.pls.widekernel.rds
/usr/lib64/R/library/pls/tests/testthat/yarn.simpls.rds
