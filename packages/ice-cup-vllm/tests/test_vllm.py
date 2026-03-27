import pytest
import os

def test_model_loading(model_weights_path):
    if model_weights_path is None:
        pytest.skip("No model weights provided via --weights")
        
    assert os.path.exists(model_weights_path)
    
    from vllm import LLM, SamplingParams

    # Initialize the vLLM engine.
    llm = LLM(model=model_weights_path)

    prompts = [
        "Hello,",
    ]
    sampling_params = SamplingParams(max_tokens=2, temperature=1.0)
    
    outputs = llm.generate(prompts, sampling_params=sampling_params)
    assert outputs
    assert len(outputs[0].outputs[0].token_ids) == 2
