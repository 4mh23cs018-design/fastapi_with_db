try:
    from azure.ai.inference import ChatCompletionsClient
    print("Import successful")
except ImportError as e:
    print(f"Import failed: {e}")
