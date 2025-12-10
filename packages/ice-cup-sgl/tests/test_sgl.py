import pytest
import os

def test_model_loading(model_weights_path):
    if model_weights_path is None:
        pytest.skip("No model weights provided via --weights")
        
    assert os.path.exists(model_weights_path)
    
    import asyncio
    import sglang as sgl

    llm = sgl.Engine(model_path=model_weights_path)
    prompts = [
        "Hello,",
    ]
    outputs = llm.generate(prompts, {
        "max_new_tokens": 2,
        "temperature": 1.0,
    })
    assert outputs
    assert len(outputs[0]["output_ids"]) == 2
