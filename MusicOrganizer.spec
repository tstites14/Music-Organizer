# -*- mode: python -*-

import os
import sys

block_cipher = None
basedir = getattr(sys, '_MEIPASS', '')

a = Analysis(['src/py/main.py'],
             binaries=[],
             datas=[('src/ui/main.ui', '.')],
             hiddenimports=['PyQt5.sip', 'mutagen'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MusicOrganizer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False)
