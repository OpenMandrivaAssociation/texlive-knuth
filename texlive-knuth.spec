# revision 23389
# category Package
# catalog-ctan /systems/knuth/dist/errata
# catalog-date 2008-07-11 09:05:11 +0200
# catalog-license knuth
# catalog-version undef
Name:		texlive-knuth
Version:	20080711
Release:	1
Summary:	Knuth's published errata
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/errata
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
These files are details of problems reported in the 'Computers
and Typesetting' series of books, for the Computer Modern
fonts, and for TeX, MetaFont and related programs.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/knuth/errata/cm85.bug
%doc %{_texmfdistdir}/doc/generic/knuth/errata/errata.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/errata/errorlog.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/errata/mf84.bug
%doc %{_texmfdistdir}/doc/generic/knuth/errata/tex82.bug
%doc %{_texmfdistdir}/doc/generic/knuth/etc/vftovp.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/etc/vptovf.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/mf/mf.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/mf/trapman.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/mfware/gftodvi.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/mfware/gftopk.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/mfware/gftype.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/mfware/mft.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/tex/glue.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/tex/tex.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/tex/tripman.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/texware/dvitype.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/texware/pltotf.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/texware/pooltype.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/texware/tftopl.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/web/tangle.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/web/weave.pdf
%doc %{_texmfdistdir}/doc/generic/knuth/web/webman.pdf
#- source
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.eight
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.eleven
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.five
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.four
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.nine
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.one
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.seven
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.six
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.ten
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.tex
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.three
%doc %{_texmfdistdir}/source/generic/knuth/errata/errata.two
%doc %{_texmfdistdir}/source/generic/knuth/errata/errorlog.tex
%doc %{_texmfdistdir}/source/generic/knuth/errata/logmac.tex
%doc %{_texmfdistdir}/source/generic/knuth/tex/glue.web
%doc %{_texmfdistdir}/source/generic/knuth/web/webman.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc source %{buildroot}%{_texmfdistdir}
