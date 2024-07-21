GEN_FAQ = FAQ_with_ToC__generated.md
SRC_FAQ = FAQ.mdwn
GEN = topic.py
TOC_DIR = github-markdown-toc
TOC_GEN = $(TOC_DIR)/gh-md-toc


all: $(GEN_FAQ)

$(GEN_FAQ): $(SRC_FAQ) $(GEN) $(TOC_GEN)
	python3 $(GEN) --input $< --output $@

$(TOC_GEN):
	git clone https://github.com/ekalinin/github-markdown-toc
	# git clone -b "shlomif-issue100-better-fix" https://github.com/shlomif/github-markdown-toc

DOCBOOK5 = first-version-of-docbook5-FAQ.docbook5.xml
XHTML = xhtml-faq/index.xhtml
X = -o "$@/index.xhtml"

#	docmake --stringparam "docbook.css.source=" --stringparam "root.filename=index.xhtml" -o "xhtml-faq" -v xhtml5 $<

# docmake --ns --trailing-slash=0 -o xhtml-faq/index.xhtml xhtml5 $<

# --basepath /usr/share/sgml/docbook/xsl-ns-stylesheets

$(XHTML): $(DOCBOOK5)
	docmake --ns --trailing-slash=0 -o xhtml-faq/index.xhtml --stringparam "docbook.css.source=" -x lib/sgml/shlomif-docbook/xsl-5-stylesheets/shlomif-essays-5-xhtml-onechunk.xsl xhtml5 $<

html: $(XHTML)

ff-preview: html
	firefox xhtml-faq/index.xhtml

all: html

check: all html
	PYTHONPATH="$${PWD}/t/lib" prove t/*.py

test: check
