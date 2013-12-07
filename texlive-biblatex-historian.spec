# revision 19787
# category Package
# catalog-ctan /macros/latex/exptl/biblatex-contrib/biblatex-historian
# catalog-date 2010-08-23 11:17:08 +0200
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-biblatex-historian
Version:	0.4
Release:	6
Summary:	A Biblatex style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/exptl/biblatex-contrib/biblatex-historian
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-historian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-historian.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-2
+ Revision: 749614
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 717925
- texlive-biblatex-historian
- texlive-biblatex-historian
- texlive-biblatex-historian
- texlive-biblatex-historian
- texlive-biblatex-historian

