import cv2
# from cv2 import cv

method = cv2.TM_SQDIFF
# # # method = cv2.TM_SQDIFF_NORMED

image = ['screenshot.png']


large_image = cv2.imread(image[0])

# # Read the images from the file
# small_image = cv2.imread('bans.png')

# result = cv2.matchTemplate(small_image, large_image, method)
# # import ipdb
# # ipdb.set_trace()
# # We want the minimum squared difference
# mn, _, mnLoc, _ = cv2.minMaxLoc(result)

# # Draw the rectangle:
# # Extract the coordinates of our best match
# MPx, MPy = mnLoc

# # Step 2: Get the size of the template. This is the same size as the match.
# trows, tcols = small_image.shape[:2]

# with open('coordinates.txt', 'a') as file:
#     file.write(str([MPx, MPy, MPx+tcols, MPy+trows]))

# print((MPx, MPy), (MPx+tcols, MPy+trows))
# # Step 3: Draw the rectangle on large_image
# MPx,MPy,MPx2,MPy2 = [1473, 187, 1511, 223]
# cv2.rectangle(large_image, (MPx, MPy), (MPx+tcols, MPy+trows), (0, 0, 255), 2)

# # Display the original image with the rectangle around the match.
# cv2.imshow('output', large_image)

# # The image is only displayed if we call this
# cv2.waitKey(0)






# cv2.imshow('output', large_image)

    # The image is only displayed if we call this
# cv2.waitKey(0)

# MPx, MPy, MPx2, MPy2 = [260, 1517, 328, 1586]
# crop_img = large_image[MPx:MPx2, MPy:MPy2]
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)


c_bans_t2 = [[1473, 187, 1511, 223],
             [1433, 187, 1471, 223],
             [1393, 187, 1431, 223]]

c_bans_t1 = [[412, 187, 450, 223],
             [452, 187, 490, 223],
             [492, 187, 530, 223]]


for coordinate in c_bans_t1:
    MPx,MPy,MPx2,MPy2 = coordinate
    cv2.rectangle(large_image, (MPx, MPy), (MPx2, MPy2), (0, 0, 255), 2)
cv2.imshow("cropped", large_image)
cv2.waitKey(0)


def crop_champions(img):
    coordinates_team1 = [[370, 260, 439, 328],
                         [332, 340, 401, 408],
                         [332, 420, 401, 488],
                         [332, 500, 401, 568],
                         [332, 580, 401, 648]]

    coordinates_team2 = [[1517, 260, 1586, 328],
                         [1517, 340, 1586, 408],
                         [1517, 420, 1586, 488],
                         [1517, 500, 1586, 568],
                         [1517, 580, 1586, 648]]

    large_image = cv2.imread('screenshot.png')

    for index,coordinate in enumerate(coordinates_team2):
        MPx, MPy, MPx2, MPy2 = coordinate
        cv2.rectangle(large_image, (MPx, MPy), (MPx2, MPy2), (0, 0, 255), 2)
        crop_img = large_image[MPy:MPy2, MPx:MPx2]
        cv2.imwrite('champion{}.png'.format(index), img)
        cv2.imshow("cropped", crop_img)
        cv2.waitKey(0)

    for index,coordinate in enumerate(coordinates_team1):
        MPx, MPy, MPx2, MPy2 = coordinate
        cv2.rectangle(large_image, (MPx, MPy), (MPx2, MPy2), (255, 0, 0), 2)
        crop_img = large_image[MPy:MPy2, MPx:MPx2]
        cv2.imwrite('champion2{}.png'.format(index), img)
        cv2.imshow("cropped", crop_img)
        cv2.waitKey(0)
