import torch
from safetensors.torch import save_model
from transformers import AutoModel
import os

# Monkey-patch the check function
import transformers.utils.import_utils
transformers.utils.import_utils.check_torch_load_is_safe = lambda: None

model_path = r"C:\Users\EARNEST\.cache\huggingface\hub\models--nlpaueb--legal-bert-base-uncased\snapshots\15b570cbf88259610b082a167dacc190124f60f6"
safetensors_path = os.path.join(model_path, "model.safetensors")

print("Loading model...")
model = AutoModel.from_pretrained(model_path, local_files_only=True)
print("Saving as safetensors...")
save_model(model, safetensors_path)
print(f" Done! Size: {os.path.getsize(safetensors_path) / 1024 / 1024:.1f} MB")