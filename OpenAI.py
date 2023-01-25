# OpenAI
# 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

import os

import openai

openai.api_key = {"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"}
openai.Edit.create(
  model="text-davinci-edit-001",
  input="What day of the week is it?",
  instruction="Fix the spelling mistakes"
)