import json

from conf import BEARER_TOKEN
from hypothesis_python import *


def usage_search_annotations():
    hypothesis = HypothesisPython(BEARER_TOKEN)
    result = hypothesis.search_annotations("Heron", TypeSearchEnum.ANY)
    print(result)


def usage_get_annotation():
    hypothesis = HypothesisPython(BEARER_TOKEN)
    result = hypothesis.get_annotation('YhmUPA3MEeykOos1eHfhOA')
    print(result)


def usage_new_annotation():
    hypothesis = HypothesisPython(BEARER_TOKEN)
    result = hypothesis.new_annotation(json.dumps(JSON_TEST))
    print(result)


def usage_delete_annotation():
    hypothesis = HypothesisPython(BEARER_TOKEN)
    result = hypothesis.delete_annotation('wJZy7hNQEeyq9GPQTGxYDA')
    print(result)


if __name__ == "__main__":
    usage_search_annotations()
    usage_get_annotation()
    usage_new_annotation()
    usage_delete_annotation()
