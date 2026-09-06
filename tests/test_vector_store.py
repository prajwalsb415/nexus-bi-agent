from src.vector_store import build_vector_store

def test_retriever_returns_relevant_context():
    retriever = build_vector_store()
    results = retriever.invoke("What is the refund period for Enterprise?")
    assert len(results) > 0
    assert any("45-day" in doc.page_content for doc in results)
