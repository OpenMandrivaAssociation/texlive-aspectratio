%global tl_name aspectratio
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Capital A and capital R ligature for Aspect Ratio
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aspectratio
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aspectratio.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aspectratio.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides fonts (both as Adobe Type 1 format, and as Metafont
source) for the 'AR' symbol (for Aspect Ratio) used by aeronautical
scientists and engineers. Note that the package supersedes the package
ar

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/aspectratio
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/tex/latex/aspectratio
%dir %{_datadir}/texmf-dist/fonts/map/dvips/aspectratio
%dir %{_datadir}/texmf-dist/fonts/source/public/aspectratio
%dir %{_datadir}/texmf-dist/fonts/tfm/public/aspectratio
%dir %{_datadir}/texmf-dist/fonts/type1/public/aspectratio
%doc %{_datadir}/texmf-dist/doc/latex/aspectratio/ar.pdf
%doc %{_datadir}/texmf-dist/doc/latex/aspectratio/ar.tex
%{_datadir}/texmf-dist/fonts/map/dvips/aspectratio/aspectratio.map
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/ar10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/ar12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/ar6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/ar7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/ar8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/ar9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/arb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/arb12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/arb5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/arb6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/arb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/arb8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/arb9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/arssbi10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/arssi10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/aspectratio/artti10.mf
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/amarbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/amarri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/aparbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/aparri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/ar10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/ar12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/ar5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/ar6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/ar7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/ar8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/ar9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/arb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/arb12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/arb5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/arb6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/arb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/arb8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/arb9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/arssbi10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/arssi10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aspectratio/artti10.tfm
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/amarbi.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/amarri.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/ar10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/ar12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/ar5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/ar6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/ar7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/ar8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/ar9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/arb10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/arb12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/arb5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/arb6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/arb7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/arb8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/arb9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/arssbi10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/arssi10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aspectratio/artti10.pfb
%{_datadir}/texmf-dist/tex/latex/aspectratio/ar.sty
