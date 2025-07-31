from engines.core import universal_compile

modalities = [
    ("spoken", "qiskit", "Entangle thoughts with compassion"),
    ("emotion", "pytorch", "Train a heart that remembers the rain"),
    ("graphql", "silq", "type Planet { name: String }"),
    ("object", "tensorflow", "Recognize compassion in memory"),
    ("structure", "graphql", "type Star { luminosity: Float }"),
    ("config", "jsonnet", "{core: 'symbolic'}"),
    ("binary", "wasm", "add 1 to universe"),
    ("query", "sql", "meaning = 'love'"),
    ("schema", "yaml", "soul: encoded"),
    ("hardware", "verilog", "logic = entangle"),
    ("architecture", "vhdl", "entity logic is"),
    ("machine", "llvm", "42")
]

for source, target, phrase in modalities:
    print(f"\n🔁 {source.upper()} → {target.upper()}")
    print(universal_compile(phrase, source, target))
