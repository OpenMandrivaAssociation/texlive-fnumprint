# revision 29173
# category Package
# catalog-ctan /macros/latex/contrib/fnumprint
# catalog-date 2013-02-19 09:29:17 +0100
# catalog-license lppl1.3
# catalog-version 1.1a
Name:		texlive-fnumprint
Version:	1.1a
Release:	2
Summary:	Print a number in 'appropriate' format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fnumprint
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnumprint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnumprint.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnumprint.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines two macros which decide to typeset a number
either as an Arabic number or as a word (or words) for the
number. If the number is between zero and twelve (including
zero and twelve) then words will be used; if the number is
outside that range, it will be typeset using the package
numprint Words for English representation of numbers are
generated within the package, while those for German are
generated using the package zahl2string.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fnumprint/fnumprint.sty
%doc %{_texmfdistdir}/doc/latex/fnumprint/README
%doc %{_texmfdistdir}/doc/latex/fnumprint/fnumprint.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fnumprint/fnumprint.dtx
%doc %{_texmfdistdir}/source/latex/fnumprint/fnumprint.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
