#!/bin/bash
# test_topic_identifier.sh
# Usage: bash test_topic_identifier.sh

python -c "
import asyncio
from topic_identifier import topic_identifier
with open('test.txt') as f:
    txt = f.read()
print(asyncio.run(topic_identifier(txt)))
"