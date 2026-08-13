%global tl_name aspectratio
%global tl_revision 79461
%global tl_version 2.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Capital A and capital R ligature for Aspect Ratio
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aspectratio
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aspectratio.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aspectratio.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides fonts (both as Adobe Type 1 format, and as Metafont
source) for the 'AR' symbol (for Aspect Ratio) used by aeronautical
scientists and engineers. Note that the package supersedes the package
ar


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from aspectratio:
Map aspectratio.map
TL_DROPIN_EOF
