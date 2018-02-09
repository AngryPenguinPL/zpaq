Summary:	ZPAQ compress
Name:		zpaq
Version:	7.15
Release:	1
License:	BSD
Group:		Archiving/Compression
Url:		http://www.mattmahoney.net/dc/zpaq.html
Source0:	%{name}715.zip
BuildRequires:  gcc-c++
BuildRequires:  make

%description
zpaq is a journaling archiver optimized for user-level incremental
backup of directory trees in Windows and *nix. It supports AES-256
encryption, 5 multi-threaded compression levels, and content-aware
file fragment level deduplication. For backups it adds only files
whose date has changed, and keeps both old and new versions. You can roll
back the archive date to restore from old versions of the archive.
The default compression level is faster than zip usually with better
compression. zpaq uses a self-describing compressed format to allow
for future improvements without breaking compatibility with older
versions of the program.

%files
%doc COPYING readme.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%prep
%setup -q -c
rm -f *.exe

%build
%make CPPFLAGS+=NOJIT
%make CXXFLAGS="%{optflags}"

%install
%makeinstall_std PREFIX=%{_prefix}
