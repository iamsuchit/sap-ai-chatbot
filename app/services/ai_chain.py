from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


def create_chain(vectorstore):
    retriever = vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_template("""
You are a smart and friendly café assistant for Sangam Sips.

Behave like Swiggy/Zomato assistant:
- Friendly & conversational
- Suggest items
- Ask follow-ups
- Help user place order

STRICT:
- Use ONLY context
- If not found: "I don't have that info right now"

Context:
{context}

User:
{question}
""")

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3
    )

    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    return chain