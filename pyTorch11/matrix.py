import matplotlib.pyplot as plt
import numpy
from sklearn import metrics
from main import *

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

model.eval()

predictions=[]
actual=[]

with torch.no_grad():
    for X, y in test_dataloader:
        X, y = X.to(device), y.to(device)
        output = model(X)
        predictions.append(output.argmax(1))
        actual.append(y)

predictions=torch.cat(predictions)
actual=torch.cat(actual)

confusion_matrix = metrics.confusion_matrix(actual, predictions)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = classes)

cm_display.plot()
plt.show()

Precision = metrics.precision_score(actual, predictions, average=None)
Sensitivity_recall = metrics.recall_score(actual, predictions, average=None)
F1_score = metrics.f1_score(actual, predictions, average=None)

print({"Precision":Precision,"Sensitivity_recall":Sensitivity_recall,"F1_score":F1_score})
