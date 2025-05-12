from llm_engine import dummy_response

def main():
    print("=== AIM - LLM Personal Trainer ===")
    topic = input("O que queres aprender hoje? ")
    response = dummy_response(topic)
    print("\nResposta da IA:")
    print(response)

if __name__ == "__main__":
    main()
