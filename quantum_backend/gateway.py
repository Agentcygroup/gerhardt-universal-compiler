def quantum_route(ir, target_lang):
    if target_lang == "qiskit":
        return f"h q[0]; cx q[0], q[1]; // from {ir}"
    elif target_lang == "silq":
        return f"silq {{ ⟨symbolic⟩ = {ir} }}"
    elif target_lang == "pytorch":
        return f"torch.nn.RNN(input={ir})"
    return f"Compiled {target_lang} not supported."
