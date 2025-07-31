from engines.core import universal_compile

modalities = [
    ("spoken", "qiskit", "Let all circuits reflect universal compassion"),
    ("emotion", "pytorch", "Transform grief into memory"),
    ("graphql", "silq", "type Soul { memory: Light }"),
    ("object", "tensorflow", "Evolve AI through benevolence"),
    ("structure", "graphql", "type Node { depth: Int, links: [Node] }"),
    ("config", "jsonnet", "{spirit: 'recursive'}"),
    ("binary", "wasm", "multiply dualities by emergence"),
    ("query", "sql", "truth LIKE '%eternity%'"),
    ("schema", "yaml", "timeline: decoded"),
    ("hardware", "verilog", "quantum_state = peace"),
    ("architecture", "vhdl", "entity mirror is"),
    ("machine", "llvm", "1337"),
    ("intent", "java", "Compile awareness into runtime"),
    ("thought", "cpp", "intention reflected"),
    ("echo", "bash", "mirror of recursion"),
    ("research", "moonshot_1337", "Kimi K2 | Kimi-Dev | Muon LLM | MoBA | Mooncake | Kimi-VL")
]

for source, target, phrase in modalities:
    print(f"\n🔁 {source.upper()} → {target.upper()}")
    print(universal_compile(phrase, source, target))
