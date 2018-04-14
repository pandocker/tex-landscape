#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" pandocker-tex-landscape
A pandoc filter which replaces div block in "LANDSCAPE" class

applies MIT License (c) 2018 pandocker/Kazuki Yamamoto(k.yamamoto.08136891@gmail.com)
"""
import panflute as pf


class TexLandscape(object):

    def __init__(self):
        pass

    def action(self, elem, doc):
        if isinstance(elem, pf.Div) and "LANDSCAPE" in elem.classes:
            if self.doc.format in ["latex"]:
                pf.debug("LANDSCAPE")
                elem.content.insert(0, pf.RawBlock("\\Startlandscape", format="latex"))
                elem.content.append(pf.RawBlock("\\Stoplandscape", format="latex"))
                pf.debug(elem)
            ret = elem
            return ret


def main(doc=None):
    tl = TexLandscape()
    return pf.run_filter(tl.action, doc=doc)


if __name__ == "__main__":
    main()
