GEN_FAQ = FAQ_with_ToC__generated.md
SRC_FAQ = FAQ.mdwn
GEN = topic.py
TOC_DIR = github-markdown-toc
TOC_GEN = $(TOC_DIR)/gh-md-toc


all: $(GEN_FAQ)

$(GEN_FAQ): $(SRC_FAQ) $(GEN) $(TOC_GEN)
	python3 $(GEN) --input $< --output $@

$(TOC_GEN):
	# git clone https://github.com/ekalinin/github-markdown-toc
	git clone -b "shlomif-issue100-better-fix" https://github.com/shlomif/github-markdown-toc
