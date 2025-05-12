# llm_engine.py

def dummy_response(topic: str) -> str:
    """
    Devolve uma resposta fictícia baseada no tema escolhido,
    usado enquanto a API da LLM não está integrada.
    """
    return f"[Simulação de resposta da IA sobre: {topic}]"
