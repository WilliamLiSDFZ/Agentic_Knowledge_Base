"""Central LLM config — single source of truth for the chat-completions client.

Provider-agnostic via environment variables; defaults to OpenRouter + Claude Sonnet.
All scripts import `client` and `MODEL` from here instead of constructing their own.

Configure in .env (one change flips providers, e.g. back to DeepSeek-direct):
    LLM_BASE_URL   default https://openrouter.ai/api/v1
    LLM_MODEL      default anthropic/claude-sonnet-4.6
    LLM_API_KEY    your provider key (OpenRouter sk-or-...)

Note: a few callers pass temperature=0. That is accepted by Sonnet 4.6, but would
400 if LLM_MODEL is pointed at Opus 4.7/4.8 or Fable 5 (sampling params removed there).
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "../.env"))

BASE_URL = os.getenv("LLM_BASE_URL", "https://openrouter.ai/api/v1")
API_KEY = os.getenv("LLM_API_KEY") or os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4.6")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
