from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

TECHNIQUE_ROOT = Path(__file__).resolve().parent
ROOT = TECHNIQUE_ROOT.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from TECHNIQUE.vector_memory import VectorMemory


class RagEngine:
    """
    Retrieval layer that is allowed to see only CANON and RAG_SUPPORT.
    """

    def __init__(
        self,
        memory: VectorMemory,
        model_name: str = "gpt-4o",
        allowed_layers: Sequence[str] = ("CANON", "RAG_SUPPORT"),
    ):
        self.memory = memory
        self.allowed_layers = tuple(allowed_layers)
        self.llm = ChatOpenAI(model=model_name, temperature=0)

        self.template = ChatPromptTemplate.from_template(
            """
You are a strict retrieval engine for the MDL YNOR corpus.
Use only the context provided below.
If the context does not support an answer, respond exactly with: I don't know

Rules:
- Do not use archives as doctrine.
- Do not invent missing evidence.
- Prefer canonical sources over support sources.
- Prefer the smallest dedicated concept sheet over registry or README pivots.
- Cite only what appears in the context.

Context:
{context}

Question:
{question}

Answer:
"""
        )

    def answer_question(self, question: str) -> str:
        context, sources = self.memory.search_context(
            question,
            top_k=5,
            threshold=0.05,
            allowed_layers=self.allowed_layers,
            require_canonical=False,
        )

        if not context.strip():
            return "Answer:\nI don't know\n\nSources:\n- No canonical context found"

        chain = self.template | self.llm
        response = chain.invoke({"context": context, "question": question})
        answer = response.content.strip()

        formatted_sources = "\n".join([f"- {source}" for source in sources]) if sources else "- No canonical source"

        return f"Answer:\n{answer}\n\nSources:\n{formatted_sources}"
