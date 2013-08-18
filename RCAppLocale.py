# Creates a right-click context menu to launch an application under a specified
# foreign language code-page, specified below. This script is used solely to
# create the right-click item.
# 17 Aug 13 - @bbaskin
import _winreg as wreg
import os

AppLocale = r"%SystemRoot%\AppPatch\AppLoc.exe"

# Language = "0401" # Arabic
# Language = "0402" # Bulgarian
# Language = "0404" # Traditional Chinese
# Language = "0405" # Czech
# Language = "0406" # Danish
# Language = "0407" # German
# Language = "0408" # Greek
# Language = "040b" # Finnish
# Language = "040c" # French (Standard)
# Language = "040d" # Hebrew
# Language = "040e" # Hungarian
# Language = "0410" # Italian
# Language = "0411" # Japanese
# Language = "0412" # Korean
# Language = "0413" # Dutch (Standard)
# Language = "0414" # Norwegian
# Language = "0415" # Polish
# Language = "0416" # Portuguese (Brazil)
# Language = "0418" # Romanian
# Language = "0419" # Russian
# Language = "041a" # Croatian
# Language = "041b" # Slovak
# Language = "041d" # Swedish
# Language = "041e" # Thai
# Language = "041f" # Turkish
# Language = "0424" # Slovenian
# Language = "0425" # Estonian
# Language = "0426" # Latvian
# Language = "0427" # Lithuanian
Language = "0804" # Simplified Chinese (GB2312)
# Language = "0816" # Portuguese (Standard)
# Language = "0c0a" # Spanish (Modern Sort)


def CreateContextMenuEntry(AL_path, language):
    cmdline = '%s "%%1" /L%s' % (AL_path, language)
    try:
        shellkey = wreg.OpenKey(wreg.HKEY_CLASSES_ROOT, r"exefile\shell", 0, wreg.KEY_ALL_ACCESS)
    except WindowsError:
        print "[!] Error: Could not open key. Ensure script is ran as Administrator"
        return False
    appkey = wreg.CreateKey(shellkey, "Execute with AppLocale")
    cmdkey = wreg.CreateKey(appkey, "command")
    wreg.SetValue(cmdkey, "", wreg.REG_SZ, cmdline)
    return True


if __name__ == "__main__":
    try:
        print "Using language %s" % Language
    except NameError:
        print "[!] Language variable not set"
        print "[!] Edit this script with a text editor and uncomment the desired language."
        quit()
    
    AppLocale_path = os.path.expandvars(AppLocale)
    if not os.path.exists(AppLocale_path):
        print "Unable to find AppLocale.exe. Expected at: %s" % AppLocale_path
        print "If AppLocale is not installed, retrieve from: http://www.microsoft.com/en-us/download/details.aspx?id=13209"
        quit()
    result = CreateContextMenuEntry(AppLocale_path, str(Language))
    if not result:
        print "Error setting registry key"
    else:
        print "Right-click context menu set successfully as 'Execute with AppLocale'"