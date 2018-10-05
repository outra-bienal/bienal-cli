from bienal import Collection, ImageAnalysis
from test_constants import COLLECTION_DATA


def test_images_property():
    collection = Collection(COLLECTION_DATA)

    assert 1 == len(collection.images)
    for i, img in enumerate(collection.images):
        assert isinstance(img, ImageAnalysis)
        assert COLLECTION_DATA['images'][i] == img.data

def test_get_aws_services_data():
    collection = Collection(COLLECTION_DATA)
    image = collection.images[0]

    faces_data = image.aws.faces
    celebs_data = image.aws.celebs
    labels_data = image.aws.labels

    assert faces_data == COLLECTION_DATA['images'][0]['amazonRekog']['faces']
    assert celebs_data == COLLECTION_DATA['images'][0]['amazonRekog']['celebs']
    assert labels_data == COLLECTION_DATA['images'][0]['amazonRekog']['labels']

def test_get_ibm_services_data():
    collection = Collection(COLLECTION_DATA)
    image = collection.images[0]

    faces_data = image.ibm.faces
    main_data = image.ibm.main

    assert faces_data == COLLECTION_DATA['images'][0]['ibmwatson']['faces']
    assert main_data == COLLECTION_DATA['images'][0]['ibmwatson']['main']

def test_get_google_services_data():
    collection = Collection(COLLECTION_DATA)
    image = collection.images[0]

    web_detection_data = image.google.web_detection
    text_data = image.google.text_annotations
    full_text_data = image.google.full_text_annotation
    label_data = image.google.label_annotation
    crop_hint_data = image.google.crop_hint_annotation
    safe_search_data = image.google.safe_search_annotation
    image_properties_data = image.google.image_properties_annotation


    assert web_detection_data == COLLECTION_DATA['images'][0]['googlecloud']['webDetection']
    assert text_data == COLLECTION_DATA['images'][0]['googlecloud']['textAnnotations']
    assert full_text_data == COLLECTION_DATA['images'][0]['googlecloud']['fullTextAnnotation']
    assert label_data == COLLECTION_DATA['images'][0]['googlecloud']['labelAnnotations']
    assert crop_hint_data == COLLECTION_DATA['images'][0]['googlecloud']['cropHintsAnnotation']
    assert safe_search_data == COLLECTION_DATA['images'][0]['googlecloud']['safeSearchAnnotation']
    assert image_properties_data == COLLECTION_DATA['images'][0]['googlecloud']['imagePropertiesAnnotation']

def test_get_azure_services_data():
    collection = Collection(COLLECTION_DATA)
    image = collection.images[0]

    faces_data = image.azure.faces
    tags_data = image.azure.tags
    adult_data = image.azure.adult
    color_data = image.azure.color
    categories_data = image.azure.categories
    description_data = image.azure.description

    assert faces_data == COLLECTION_DATA['images'][0]['microsoftazure']['main']['faces']
    assert tags_data == COLLECTION_DATA['images'][0]['microsoftazure']['main']['tags']
    assert adult_data == COLLECTION_DATA['images'][0]['microsoftazure']['main']['adult']
    assert color_data == COLLECTION_DATA['images'][0]['microsoftazure']['main']['color']
    assert categories_data == COLLECTION_DATA['images'][0]['microsoftazure']['main']['categories']
    assert description_data == COLLECTION_DATA['images'][0]['microsoftazure']['main']['description']

def test_get_deep_ai_services_data():
    collection = Collection(COLLECTION_DATA)
    image = collection.images[0]

    data = image.deep_ai.dense_cap

    assert data == COLLECTION_DATA['images'][0]['deepAi']['DenseCap']

def test_get_clarifai_services_data():
    collection = Collection(COLLECTION_DATA)
    image = collection.images[0]

    nsfw_data = image.clarifai.nsfw
    general_data = image.clarifai.general
    moderation_data = image.clarifai.moderation
    celebrities_data = image.clarifai.celebrities
    demographics_data = image.clarifai.demographics

    assert nsfw_data == COLLECTION_DATA['images'][0]['clarifai']['nsfw']
    assert general_data == COLLECTION_DATA['images'][0]['clarifai']['general']
    assert moderation_data == COLLECTION_DATA['images'][0]['clarifai']['moderation']
    assert celebrities_data == COLLECTION_DATA['images'][0]['clarifai']['celebrities']
    assert demographics_data == COLLECTION_DATA['images'][0]['clarifai']['demographics']
