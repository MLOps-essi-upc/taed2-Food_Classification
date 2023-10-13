from prediction import predict_image


def check_output_values(image):
    prob, target = predict_image(image)
    assert(target < 29 and target >= 0)



