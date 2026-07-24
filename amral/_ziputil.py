#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared zip helper for the amral scripts."""


def decoded_names(zf):
    """zipfile decodes a name as CP437 unless the entry's UTF-8 flag bit
    (0x800) is set. Several of these packages store real UTF-8 bytes
    without that flag, so CJK names come back as mojibake — reverse it."""
    names = []
    for info in zf.infolist():
        name = info.filename
        if not (info.flag_bits & 0x800):
            try:
                name = name.encode("cp437").decode("utf-8")
            except (UnicodeEncodeError, UnicodeDecodeError):
                pass
        names.append(name)
    return names


def decoded_infolist(zf):
    """Pairs each ZipInfo with its decoded name: [(name, info), ...]."""
    return list(zip(decoded_names(zf), zf.infolist()))
