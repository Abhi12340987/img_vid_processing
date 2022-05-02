from cv2 import cv2

img_1 = cv2.imread("img_vid_processing/sample_images/galaxy.jpg", 0)
img_2 = cv2.imread("img_vid_processing/sample_images/kangaroos-rain-australia_71370_990x742.jpg", 0)
img_3 = cv2.imread("img_vid_processing/sample_images/Lighthouse.jpg", 0)
img_4 = cv2.imread("img_vid_processing/sample_images/Moon sinking, sun rising.jpg", 0)

#print(type(img))
#print(img)
#print(img.shape)
#print(img.ndim)

resized_image_1 = cv2.resize(img_1, (100, 100))
resized_image_2 = cv2.resize(img_2, (100, 100))
resized_image_3 = cv2.resize(img_3, (100, 100))
resized_image_4 = cv2.resize(img_4, (100, 100))

cv2.imshow("Galaxy1", resized_image_1)
cv2.imshow("Galaxy2", resized_image_2)
cv2.imshow("Galaxy3", resized_image_3)
cv2.imshow("Galaxy4", resized_image_4)

cv2.imwrite("img_vid_processing/img_resized/galaxy_resized.jpg", resized_image_1)
cv2.imwrite(
    "img_vid_processing/img_resized/kangaroos_resized-rain-australia_71370_990x742.jpg", resized_image_2)
cv2.imwrite("img_vid_processing/img_resized/Lighthouse_resized.jpg", resized_image_3)
cv2.imwrite(
    "img_vid_processing/img_resized/Moon sinking resized, sun rising.jpg", resized_image_4)


cv2.waitKey(0)
cv2.destroyAllWindows()
