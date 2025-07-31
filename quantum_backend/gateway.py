def quantum_route(ir, target_lang):
    routes = {
        "qiskit": lambda ir: f"h q[0]; cx q[0], q[1]; // from {ir}",
        "silq": lambda ir: f"silq {{ ⟨symbolic⟩ = {ir} }}",
        "pytorch": lambda ir: f"torch.nn.RNN(input={ir})",
        "tensorflow": lambda ir: f"tf.keras.Sequential([tf.keras.layers.LSTM(32)]) # {ir}",
        "graphql": lambda ir: f"schema {{ query: RootQuery }} // {ir}",
        "jsonnet": lambda ir: f"local config = {ir};",
        "wasm": lambda ir: f"(module (func  (result i32) ;; {ir}))",
        "sql": lambda ir: f"SELECT * FROM data WHERE info LIKE '%{ir}%';",
        "yaml": lambda ir: f"data: {ir}",
        "verilog": lambda ir: f"module auto; // {ir} endmodule",
        "vhdl": lambda ir: f"ENTITY GATEWAY IS -- {ir} END;",
        "llvm": lambda ir: f"define i32 @main() {{ ret i32 {ir} }}",
    }
    return routes.get(target_lang, lambda ir: f"Compiled {target_lang} not supported.")(ir)
