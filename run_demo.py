from engines.core import universal_compile

print("🎤 Spoken → Quantum OpenQASM")
print(universal_compile("Entangle thoughts with compassion", "spoken", "qiskit"))

print("\n📜 Poetic Prompt → PyTorch LSTM")
print(universal_compile("Train a heart that remembers the rain", "emotion", "pytorch"))

print("\n🔁 Schema → Silq")
print(universal_compile("type Planet { name: String }", "graphql", "silq"))
