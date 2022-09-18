import coremltools as ct
from PIL import Image, ImageOps

image_input = ct.ImageType(shape=(1, 256, 256, 1), scale=1/255, color_layout='G')
classifier_config = ct.ClassifierConfig(class_labels=["banana", "human"])
mlmodel = ct.convert('model', source="tensorflow", inputs=[image_input], classifier_config=classifier_config)

exImage = Image.open('banana_stock.jpg').resize((256, 256))
exImage = ImageOps.grayscale(exImage)
out_dict = mlmodel.predict({'rescaling_1_input': exImage})
print(out_dict)
