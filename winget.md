## Winget - Windows Package manager..



```
Installing WinGet :
# You should find winget installed on your windows 11 computer,
# and it is supported on Windows 10 version 1709 build 16299 or
# later.
# If for any reason, you need to install winget, as in you cannot find
# it on your system, you can either get it from the Microsoft store:

https://www.microsoft.com/store/productId/9NBLGGH4NNS1
or from github:
https://github.com/microsoft/winget-cli/releases

Searching for applications:
winget search "term"
# The search is performed in a case insensitive manner,
# for the provided search term, as a substring,
# in any of the application name, publisher,
# tag, nickname.
winget search notepad
# The result is a tabular format, listing the found
# applications names, IDs, versions, match,
# which can be a tag or a nickname, and
# sources.
# You can limit the search to the application
# name by using --name, to the application ID
# by using --id, and to the application nickname
# by using --moniker.
# You can specify the repository on which the
# search is performed, by using --source.
winget search --name "notepad" --source msstore
# If no search term is specified, as in using:
winget search | more
# this will list all the available applications,
# from the default sources, which are:
# msstore, and winget.

Installing applications:
winget install "application"
# Install the application with the provided
# name or ID or nickname.
winget install sumatrapdf
# To get an application ID or nickname,
# winget search can be used.
# An application ID, can be for example formed
# of the publisher’s name, followed by a dot,
# followed by the application’s name, or
# it can be just a unique random string.
winget install Google.Chrome
# If more than one application match the
# same name, or nickname, or if applications
# with the same ID are available from different
# stores, nothing is installed, but matching
# applications are listed.
# To install an application from a specific
# store, you can use the --source option, as in:
winget install TobySuggate.GitFiend --source winget
# If you want to install a specific version
# of an application, you can use --version
# as in:
winget install "Notepad++.Notepad++" --source winget --version 8.3.1
# A package agreement can be accepted using:
--accept-package-agreements
# A source agreement can be accepted using:
--accept-source-agreements

Listing installed applications:
winget list
# Will list all applications installed on
# your system, be it using winget or
# not.
# The result is a table containing the application
# name, ID, version, available version, and
# source.
# If a term is specified, applications which names,
# or IDs, or nicknames, or tags, that the term matches
# as a substring, in a case insensitive manner,
# will be listed.
winget list notepad
# Besides this, you can use --id to match on id,
# --name to match on name, --moniker to match
# on nickname, --tag to match on tag,
# and --source to match on source.
# Matching on name, ID, moniker, and
# tag, is done as a substring, in a case
# insensitive manner.
winget list --name Notepad --source winget

Uninstalling applications:
winget uninstall "application"
# Uninstall the application with the
# provided name or id or nickname,
# even if it was not installed using winget.
winget uninstall virtualbox
# If there is ambiguity, nothing is
# uninstalled, but the tool will only list
# the matching applications.
# In such a case, you can refine the exactitude,
# by using --name to match an application
# name, --id to match an application ID,
# --moniker to match an application
# nickname.
winget uninstall --moniker firefox

Upgrading applications:
winget upgrade "application"
# Upgrade the specified application to the
# newest version, even if this application
# was not installed using winget.
# Applications which are not installed using
# winget, can also be upgraded.
winget upgrade VLC
# If more than one application is a match,
# matching applications are listed, and
# you can use --name, --id, --moniker,
# to resolve any ambiguity.
winget upgrade VideoLAN.VLC
# To upgrade all applications, you can use
# --all, as in:
winget upgrade --all
# If used without anything, as in using:
winget upgrade
# winget will list all applications, that have
# a newer version available.

Applications information:
winget show "application"
# Shows information related to an application,
# be it installed or not, such as its description,
# its homepage, its nickname, its release
# notes ...
winget show lunacy
# If the provided term has more than one result,
# no information is showed, but only matching
# results are listed.
# --id, or --name, or --moniker, or --source
# can be used to refine the term
# accuracy.
winget show --id icons8.lunacy --source winget

Exporting / Importing :
winget export destination
# Creates a JSON file, containing the IDs
# of the applications which are installed,
# and their sources.
# If an application does not have a valid
# source, it is ignored.
winget export myapps.json
# If you want to additionally save the
# applications versions, so that you
# can reinstall the exact same versions,
# you can use --include-versions, and to
# save applications only from a specific
# source, you can use the --source
# option.
winget export myapps.json --include-versions --source winget

winget import source
# Install applications found in an
# export list, created using
# winget export.
winget import myapps.json
# Packages licenses can be accepted using
# --accept-package-agreements, sources
# licenses can be accepted using
# --accept-source-agreements, specified
# versions in the export list, can be ignored using
# --ignore-versions, and errors caused by
# unavailable apps, can be ignored using
# --ignore-unavailable.
winget import myapps.json --accept-package-agreements --accept-source-agreements --ignore-versions --ignore-unavailable

Help:
winget --help
# To get help about the available winget
# commands, you can use:
winget --help
# To get a help about a specific winget
# command, you can use:
# winget command_name --help
as in:
winget install --help

Settings
winget settings
# This will open notepad, and allows
# you to edit settings related to winget.
# Examples of settings that can be edited,
# are if the applications are installed for the
# current user, this is default behavior, or
# for all users, additionally you can configure
# telemetry as enabled or disabled, and many
# other things…

{
    "$schema": "https://aka.ms/winget-settings.schema.json",
    // For documentation on these settings, see: https://aka.ms/winget-settings
    "installBehavior": { "preferences": { "scope": "machine" }},
    "telemetry": { "disable": true }
}        
    
Sources
winget source list
# List the names, the URLs or PATHs, of
# the sources which are configured.
# A source is just a catalogue of applications
# that can be installed.
# To view information about a specific source,
# you can use the –name option, as in:
winget source list --name msstore

winget source add name URL
# can be used to add a source, by specifying
# its named and URL, as in:
winget source add winget https://winget.azureedge.net/cache

winget source update
# Updates all the configured sources.
# If you wish to update a specific source,
# you can use:
winget source update --name winget

winget source remove name
# Remove the named source, for
# example:
winget source remove --name msstore

winget source reset
# Resets winget to its default configuration,
# keeping only the default sources, which are: msstore, and winget.




```
