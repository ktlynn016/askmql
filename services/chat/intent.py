"""Very small rule-based intent classifier. Real chat systems would
use an LLM or a trained classifier here; this keeps things dependency
-free and fast while the rest of the pipeline (retrieval, generation)
is what actually matters for correctness today."""

INTENT_ANNOUNCEMENTS = "announcements"
INTENT_SEARCH = "search"


def classify(text: str) -> str:
    if "announce" in text.lower():
        return INTENT_ANNOUNCEMENTS
    return INTENT_SEARCH
