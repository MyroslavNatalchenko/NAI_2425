import sys
import torch
import cv2

from main import test_data, device, NeuralNetwork

model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("model_2_abnormal_ADAM.pth", weights_only=True))

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

image_path = sys.argv[1]
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (28, 28))
# inverted_image=255 - image
tensor_img = torch.tensor(image, dtype=torch.float32).unsqueeze(0).unsqueeze(0)

model.eval()
with torch.no_grad():
    pred = model(tensor_img)
    predicted = classes[pred[0].argmax(0)]
    print(f'Predicted: "{predicted}"')