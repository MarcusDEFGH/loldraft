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


# for coordinate in c_bans_t1:
#     MPx,MPy,MPx2,MPy2 = coordinate
#     cv2.rectangle(large_image, (MPx, MPy), (MPx2, MPy2), (0, 0, 255), 2)
# cv2.imshow("cropped", large_image)
# cv2.waitKey(0)


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

    for index,coordinate in enumerate(coordinates_team2):
        MPx, MPy, MPx2, MPy2 = coordinate
        cv2.rectangle(img, (MPx, MPy), (MPx2, MPy2), (0, 0, 255), 2)
        crop_img = img[MPy:MPy2, MPx:MPx2]
        cv2.imwrite('champion{}.png'.format(index), crop_img)
        # cv2.imshow("cropped", crop_img)
        cv2.waitKey(0)

    for index,coordinate in enumerate(coordinates_team1):
        MPx, MPy, MPx2, MPy2 = coordinate
        cv2.rectangle(img, (MPx, MPy), (MPx2, MPy2), (255, 0, 0), 2)
        crop_img = img[MPy:MPy2, MPx:MPx2]
        cv2.imwrite('champion2{}.png'.format(index), crop_img)
        # cv2.imshow("cropped", crop_img)
        cv2.waitKey(0)
# img = cv2.imread('champions.png')
# crop_champions(img)

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


def identify_champions(coordinates):
    team = []

    method = cv2.TM_SQDIFF_NORMED
    img = cv2.imread('champions.png')

    for coordinate in coordinates:
        MPx, MPy, MPx2, MPy2 = coordinate
        crop_img = img[MPy:MPy2, MPx:MPx2]

        from pathlib import Path
        pathlist = Path('champions').glob('**/*.png')
        for champion in pathlist:
            # because path is object not string
            champion = str(champion)
            champion_img = cv2.imread(champion)
            champion_name = champion.strip('champions\\\\').replace('.png', '')
            result = cv2.matchTemplate(champion_img, crop_img, method)
            mn, mx, _, _ = cv2.minMaxLoc(result)


            # for better performance this shouldn't be implemented in such a greedy
            # way, the positions could be popped and the comparisons should be done 
            # only 10 times 

            if mx < 0.4:
                if champion_name not in team:
                    team.append(champion_name)

            if len(team) == 5:
                return team
    return team

img = cv2.imread('champions.png')

print(identify_champions(img, coordinates_team1))
print(identify_champions(img, coordinates_team2))
