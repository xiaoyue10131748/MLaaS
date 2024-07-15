from huggingface_hub import ModelCard


card = ModelCard.load('keras-io/mobile-vit-xxs')
print(card.text)
