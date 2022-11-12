Name:		texlive-biblatex-historian
Version:	19787
Release:	1
Summary:	A Biblatex style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/exptl/biblatex-contrib/biblatex-historian
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-historian.r19787.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-historian.doc.r19787.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A biblatex style, based on the Turabian Manual (a version of
Chicago).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-historian/historian.bbx
%{_texmfdistdir}/tex/latex/biblatex-historian/historian.cbx
%{_texmfdistdir}/tex/latex/biblatex-historian/historian.lbx
%doc %{_texmfdistdir}/doc/latex/biblatex-historian/README.txt
%doc %{_texmfdistdir}/doc/latex/biblatex-historian/historian.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-historian/historian.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
