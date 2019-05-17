GEN_FAQ = FAQ_with_ToC__generated.md
SRC_FAQ = FAQ.mdwn
GEN = topic.py

all: $(GEN_FAQ)

$(GEN_FAQ): FAQ.mdwn $(GEN)
	python3 $(GEN) --input $< --output $@
