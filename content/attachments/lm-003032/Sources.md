# SOURCES v0.9

Primary engineering sources checked before implementation:

1. ComfyUI Server Routes / API execution
   - https://docs.comfy.org/development/comfyui-server/comms_routes
   - `/prompt` validates and queues an API-format workflow; `/ws` provides real-time communication.

2. ComfyUI Cloud API overview
   - https://docs.comfy.org/development/cloud/overview
   - Documents API-format workflow submission and WebSocket progress; cloud API is compatible with local ComfyUI API patterns.

3. Hugging Face Diffusers pipeline overview
   - https://huggingface.co/docs/diffusers/main/en/using-diffusers/pipeline_overview
   - DiffusionPipeline is the end-to-end inference abstraction.

4. Diffusers LoRA loaders
   - https://huggingface.co/docs/diffusers/main/api/loaders/lora
   - Documents load_lora_weights(), adapter_name and set_adapters().

5. Diffusers ControlNet
   - https://huggingface.co/docs/diffusers/main/api/pipelines/controlnet
   - Documents ControlNet inputs and optional IP-Adapter image inputs.
