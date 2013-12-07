# revision 25243
# category Package
# catalog-ctan /macros/latex/contrib/aspectratio
# catalog-date 2012-01-28 10:04:30 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-aspectratio
Version:	2.0
Release:	3
Summary:	Capital A and capital R ligature for Aspect Ratio
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aspectratio
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aspectratio.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aspectratio.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides fonts (both as Adobe Type 1 format, and as
Metafont source) for the 'AR' symbol (for Aspect Ratio) used by
aeronautical scientists and engineers.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/aspectratio/aspectratio.map
%{_texmfdistdir}/fonts/source/public/aspectratio/ar10.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/ar12.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/ar6.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/ar7.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/ar8.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/ar9.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb10.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb12.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb5.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb6.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb7.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb8.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb9.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arssbi10.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arssi10.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/artti10.mf
%{_texmfdistdir}/fonts/tfm/public/aspectratio/amarbi.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/amarri.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/aparbi.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/aparri.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar10.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar12.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar5.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar6.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar7.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar8.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar9.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb10.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb12.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb5.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb6.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb7.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb8.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb9.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arssbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/artti10.tfm
%{_texmfdistdir}/fonts/type1/public/aspectratio/amarbi.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/amarri.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/ar10.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/ar12.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/ar5.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/ar6.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/ar7.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/ar8.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/ar9.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/arb10.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/arb12.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/arb5.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/arb6.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/arb7.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/arb8.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/arb9.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/arssbi10.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/arssi10.pfb
%{_texmfdistdir}/fonts/type1/public/aspectratio/artti10.pfb
%{_texmfdistdir}/tex/latex/aspectratio/ar.sty
%doc %{_texmfdistdir}/doc/latex/aspectratio/ar.pdf
%doc %{_texmfdistdir}/doc/latex/aspectratio/ar.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 770109
- texlive-aspectratio
- texlive-aspectratio

