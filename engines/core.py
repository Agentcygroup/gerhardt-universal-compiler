from maps.lineage import translate
from quantum_backend.gateway import quantum_route

def universal_compile(input_code, source_lang, target_lang):
    ir = translate(input_code, source_lang)
    compiled = quantum_route(ir, target_lang)
    return compiled
