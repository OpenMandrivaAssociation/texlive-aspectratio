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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides fonts (both as Adobe Type 1 format, and as Metafont
source) for the 'AR' symbol (for Aspect Ratio) used by aeronautical
scientists and engineers. Note that the package supersedes the package
ar

