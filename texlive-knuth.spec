Name:		texlive-knuth
Version:	20190228
Release:	2
Summary:	Knuth's published errata
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/knuth/dist/errata
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
%doc %{_texmfdistdir}/doc/generic/knuth
#- source
%doc %{_texmfdistdir}/source/generic/knuth

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc source %{buildroot}%{_texmfdistdir}
