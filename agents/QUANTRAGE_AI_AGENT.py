import random
from engines.core import universal_compile

def quantrage_compile(input_text):
    sources = ["spoken", "emotion", "object", "query", "schema", "config"]
    targets = ["moonshot_{}".format(random.randint(0,14999)), "qiskit", "tensorflow", "graphql", "sql"]
    result = universal_compile(input_text, random.choice(sources), random.choice(targets))
    return result

if __name__ == "__main__":
    print("\n⚡ QUANTRAGE AI AGENT INITIATED ⚡")
    input_text = "Optimize quantum arbitrage across symbolic routes"
    output = quantrage_compile(input_text)
    print(output)
