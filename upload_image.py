import pyimgur
import os
from time import sleep


class UploadImageToImgur(object):
    def run(self):
        # directory scan
        print('# Directory scan started')

        list_of_local_screens = []  # directory scanned list

        for filename in os.listdir("/home/yesspeace/Изображения/screenshots"):
            list_of_local_screens.append(filename)

        print('# directory scanned list ', list_of_local_screens)
        # directory scan

        # sorting list of files

        # reading last upload screen
        last_upload_screen_file = open('last_upload_screen_file.txt', 'a+')
        for line in last_upload_screen_file:
            last_upload_screen = str(line)

        try:
            print('# last upload screenshot:', last_upload_screen)  # if file have a last upload screen
            last_screen_is_here = True

        except NameError:
            print('# last upload screenshot:', 'NotFound')  # if it does not
            last_screen_is_here = False

        # reading last upload screen

        # search that screen in the list

        if last_screen_is_here:
            for file_num in range(len(list_of_local_screens)):
                if list_of_local_screens[file_num] == last_upload_screen:
                    list_of_local_screens = list_of_local_screens[file_num + 1:]  # cutting the list
                    break

        # sorting list of files

        print('# Directory scan and sort finished successfully')

        # tokens
        token_file = open('tokens.txt', 'r')

        i = 0
        for line in token_file:
            if i == 0:
                access_token = str(line[:-1])
                i += 1
            else:
                refresh_token = str(line)
        # tokens

        # tokens check
        try:
            if access_token != refresh_token:
                print('# Tokens for uploading are there')
        except NameError:
            return print('# Tokens for upload are not found. Pleas do authentication')
        # tokens check

        # upload
        for num_screen in range(len(list_of_local_screens)):

            if num_screen // 15 == 0:  # It's cause Imgur have Send limit
                sleep(3)

            try:
                CLIENT_ID = "7d220f48ce3309b"
                PATH = "/home/yesspeace/Изображения/screenshots/" + str(list_of_local_screens[num_screen])
                im = pyimgur.Imgur(CLIENT_ID, access_token=access_token, refresh_token=refresh_token)
                uploaded_image = im.upload_image(PATH, title="auto_uploaded_by_YessPeace_test")
                print(uploaded_image.title)
                print(uploaded_image.link)

            except:
                if len(list_of_local_screens) > 0:
                    last_upload_screen_file.write(list_of_local_screens[num_screen-1])

                return print('Sorry, but imgur have send limit, so you need to wait')

        # upload

        last_upload_screen_file = open('last_upload_screen_file.txt', 'w')

        if len(list_of_local_screens) > 0:
            last_upload_screen_file.write(list_of_local_screens[-1])
            return print('# All screenshots has been upload successfully')
        else:
            return print('# All screenshots has been upload yet')


if __name__ == '__main__':
    UploadImageToImgur.run(self='')
