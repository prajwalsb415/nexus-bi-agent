from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document

def get_default_policy_documents():
    return [
        Document(
            page_content=(
                "NexusRetail Refund Policy:\n"
                "- Standard Tier: 14-day refund window from delivery date. 15% restocking fee applies.\n"
                "- Pro Tier: 30-day refund window. Restocking fee is waived.\n"
                "- Enterprise Tier: 45-day satisfaction guarantee window with full cash refund and zero restocking fees."
            ),
            metadata={"category": "Refunds"}
        ),
        Document(
            page_content=(
                "NexusRetail Service Level Agreement (SLA):\n"
                "- Platform Uptime: Minimum guaranteed monthly uptime is 99.5% for Enterprise and 99.0% for Pro.\n"
                "- SLA Violations: If uptime falls below 99.5%, Enterprise clients receive a 10% credit discount on the next billing invoice.\n"
                "- Support Response: Enterprise tickets receive human response within 1 hour; Pro within 4 hours; Standard within 24 hours."
            ),
            metadata={"category": "SLA"}
        ),
        Document(
            page_content=(
                "NexusRetail Freight & Shipping Terms:\n"
                "- Complimentary expedited freight shipping applies automatically to all single orders over $5,000.\n"
                "- Standard ground shipping costs $150 flat fee for orders under $5,000 unless customer is in Enterprise Tier."
            ),
            metadata={"category": "Shipping"}
        )
    ]

def build_vector_store():
    # Instant, zero-download BM25 retriever: no PyTorch hang, no 90MB Hugging Face download
    docs = get_default_policy_documents()
    retriever = BM25Retriever.from_documents(docs)
    retriever.k = 2
    return retriever
