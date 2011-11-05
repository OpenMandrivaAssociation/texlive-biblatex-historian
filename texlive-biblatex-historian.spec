# revision 19787
# category Package
# catalog-ctan /macros/latex/exptl/biblatex-contrib/biblatex-historian
# catalog-date 2010-08-23 11:17:08 +0200
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-biblatex-historian
Version:	0.4
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A biblatex style, based on the Turabian Manual (a version of
Chicago).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-historian/historian.bbx
%{_texmfdistdir}/tex/latex/biblatex-historian/historian.cbx
%{_texmfdistdir}/tex/latex/biblatex-historian/historian.lbx
%doc %{_texmfdistdir}/doc/latex/biblatex-historian/README.txt
%doc %{_texmfdistdir}/doc/latex/biblatex-historian/historian.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-historian/historian.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
