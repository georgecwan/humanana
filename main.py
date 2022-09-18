import coremltools as ct
from PIL import Image
image_input = ct.ImageType(shape=(1, 256, 256, 1), scale=1/255)

classifier_config = ct.ClassifierConfig(class_labels=['banana', 'human'])

mlmodel = ct.convert('model.mlmodel', source="tensorflow", inputs=[image_input], classifier_config=classifier_config)
# mlmodel.save('banana.mlmodel')
print(mlmodel.get_spec().description)
exim = Image.open('../images/IMG_6639.jpeg').resize((256, 256))
out_dict = mlmodel.predict({"rescaling_1_input": exim})
print(out_dict)
