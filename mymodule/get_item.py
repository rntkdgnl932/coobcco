import time

import requests
import json
# import os
import sys
sys.path.append('C:/nightcrow/mymodule')

import variable as v_

season_count = 0

def get_items(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen, item_open
        from schedule import myQuest_play_add

        if cla == "one":
            potion = v_.mypotion_1
        else:
            potion = v_.mypotion_2



        print("아이템 받기 시작")

        # 시즌패스 받기
        get_season_pass(cla)
        # 이벤트 받기
        get_event(cla)
        # 업적 받기
        get_upjuk(cla)
        # 우편 받기
        get_post(cla)
        # 가방 아이템 정리
        item_open(cla)

        myQuest_play_add(cla, "각종템받기")
        clean_screen(cla)
        print("오케잇!!!!!!!!")



    except Exception as e:
        print(e)

def get_post(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen, menu_open

        in_post_ = False
        while in_post_ is False:
            full_path = "c:\\nightcrow\\imgs\\get_item\\post_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 40, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("우편함", imgs_)

                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 75, 420, 110, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("point1", imgs_)

                    click_pos_2(350, 105, cla)
                    time.sleep(1)
                    system_post = False
                    while system_post is False:
                        full_path = "c:\\nightcrow\\imgs\\get_item\\post_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(810, 140, 960, 210, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(910, 180, cla)

                            time.sleep(0.3)
                            full_path = "c:\\nightcrow\\imgs\\get_item\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 570, 640, 640, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            full_path = "c:\\nightcrow\\imgs\\get_item\\confirm_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 680, 640, 740, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            system_post = True

                            full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(110, 75, 155, 110, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("point2", imgs_)
                                click_pos_2(80, 105, cla)
                            else:
                                in_post_ = True
                        time.sleep(0.3)
                time.sleep(0.7)
                get_post_sever_ = False
                while get_post_sever_ is False:
                    full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(110, 75, 155, 110, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(80, 105, cla)
                        full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(900, 120, 960, 330, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("point2", imgs_)
                            in_post_ = True
                            click_pos_2(880, 1010, cla)
                            time.sleep(0.5)
                            click_pos_2(880, 1010, cla)
                            clean_screen(cla)
                    else:
                        in_post_ = True
                        get_post_sever_ = True
                        click_pos_2(930, 60, cla)
                        # click_pos_2(80, 105, cla)
                    time.sleep(0.3)




            else:
                menu_open(cla)

                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(720, 970, 780, 1030, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(750, 1000, cla)
                else:
                    full_path = "c:\\nightcrow\\imgs\\check\\point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(720, 970, 780, 1030, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(750, 1000, cla)
                    else:
                        print("우편에 빨강점이 안보여!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        in_post_ = True
            time.sleep(0.5)

    except Exception as e:
        print(e)

def get_season_pass(cla):
    try:
        global season_count
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos, drag_pos_reg
        from action import clean_screen
        import random

        clean_screen(cla)
        time.sleep(1)
        complete_ = False
        while complete_ is False:
            season_count += 1
            if season_count > 20:
                complete_ = True
                season_count = 0

            full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(150, 0, 220, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("시즌패스", imgs_)
                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)

                a = 0
                b = 420
                get_season = False
                while get_season is False:
                    season_count += 1
                    if season_count > 20:
                        get_season = True
                        season_count = 0
                    full_path = "c:\\nightcrow\\imgs\\get_item\\pass_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 500, 800, 800, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        get_season = True

                        get_season_start = False
                        while get_season_start is False:
                            season_count += 1
                            if season_count > 20:
                                get_season_start = True
                                season_count = 0
                            a = b
                            b = a + 50
                            if b < 750:

                                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(150, a, 250, b, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                                    time.sleep(0.4)

                                    get_season_last = False
                                    while get_season_last is False:
                                        season_count += 1
                                        if season_count > 20:
                                            get_season_last = True
                                            season_count = 0
                                        full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(150, a, 250, b, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:

                                            full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(250, 400, 880, 680, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x - 20, imgs_.y + 45, cla)
                                                time.sleep(0.2)
                                                click_pos_2(860, 410, cla)
                                                time.sleep(0.3)
                                            else:
                                                print("1")

                                                result_int = random.randint(150, 200)

                                                full_path = "c:\\nightcrow\\imgs\\get_item\\checked.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(250, 400, 880, 680, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    drag_pos_reg(imgs_.x, imgs_.y, imgs_.x + result_int, imgs_.y, cla)

                                                full_path = "c:\\nightcrow\\imgs\\get_item\\num_2.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(350, 600, 450, 680, cla, img, 0.88)
                                                if imgs_ is not None and imgs_ != False:
                                                    get_season_last = True

                                                    full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(250, 400, 880, 680, cla, img, 0.85)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("?>???", imgs_)
                                                        click_pos_reg(imgs_.x - 20, imgs_.y + 45, cla)
                                                        time.sleep(0.2)
                                                        click_pos_2(860, 410, cla)
                                                        time.sleep(0.3)
                                                    else:
                                                        get_season_last = True
                                            time.sleep(1)
                                        else:
                                            get_season_last = True


                            else:
                                print("3")
                                get_season_start = True
                                full_path = "c:\\nightcrow\\imgs\\get_item\\pass_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 500, 800, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(860, 370, cla)
                                else:
                                    clean_screen(cla)
                            time.sleep(1)
                    else:
                        full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 0, 220, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("시즌패스", imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(2)
            else:
                complete_ = True

            time.sleep(2)
        clean_screen(cla)

    except Exception as e:
        print(e)

def get_event(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen

        clean_screen(cla)
        time.sleep(1)
        complete_ = False
        while complete_ is False:
            full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 0, 830, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("이벤트", imgs_)
                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)

                a = 0
                b = 395
                get_season = False
                while get_season is False:
                    full_path = "c:\\nightcrow\\imgs\\get_item\\event_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 300, 550, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        get_season = True

                        get_season_start = False
                        while get_season_start is False:
                            a = b
                            b = a + 55
                            if b < 750:

                                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(150, a, 250, b, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                                    time.sleep(0.4)

                                    get_season_last = False
                                    while get_season_last is False:

                                        full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(280, 460, 880, 720, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                            time.sleep(0.2)
                                            click_pos_2(860, 410, cla)
                                            time.sleep(0.3)
                                        else:
                                            print("1")
                                            # get_season_start = True
                                            get_season_last = True
                                        time.sleep(1)
                            else:
                                print("3")
                                get_season_start = True
                                full_path = "c:\\nightcrow\\imgs\\get_item\\event_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 300, 550, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(870, 335, cla)
                                else:
                                    clean_screen(cla)
                            time.sleep(1)
                    else:
                        full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 0, 830, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("이벤트", imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(2)
            else:
                complete_ = True

            time.sleep(2)
        clean_screen(cla)

    except Exception as e:
        print(e)

def get_upjuk(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import clean_screen, menu_open

        get_upjuk_ = False
        while get_upjuk_ is False:
            full_path = "c:\\nightcrow\\imgs\\get_item\\upjuk_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 400, 535, 480, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                get_upjuk_ = True
                print("업적", imgs_)
                # 성장
                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(220, 470, 280, 520, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("성장", imgs_)
                    click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                    sungjang = False
                    while sungjang is False:
                        full_path = "c:\\nightcrow\\imgs\\get_item\\upjuk_sungjang.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 90, 240, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(850, 130, cla)
                            time.sleep(0.2)
                            sungjang = True
                            back_ = False
                            while back_ is False:
                                full_path = "c:\\nightcrow\\imgs\\get_item\\upjuk_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 535, 480, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sungjang = True
                                    back_ = True
                                else:
                                    click_pos_2(30, 55, cla)
                # 협동
                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 470, 840, 520, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("협동", imgs_)
                    click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                    sungjang = False
                    while sungjang is False:
                        full_path = "c:\\nightcrow\\imgs\\get_item\\upjuk_hyubdong.PNG.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 90, 240, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(850, 130, cla)
                            time.sleep(0.2)
                            sungjang = True
                            back_ = False
                            while back_ is False:
                                full_path = "c:\\nightcrow\\imgs\\get_item\\upjuk_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 535, 480, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sungjang = True
                                    back_ = True
                                else:
                                    click_pos_2(30, 55, cla)
                # 장비
                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(220, 700, 280, 740, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("장비", imgs_)
                    click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                    sungjang = False
                    while sungjang is False:
                        full_path = "c:\\nightcrow\\imgs\\get_item\\upjuk_jangbi.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 90, 240, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(850, 130, cla)
                            time.sleep(0.2)
                            sungjang = True
                            back_ = False
                            while back_ is False:
                                full_path = "c:\\nightcrow\\imgs\\get_item\\upjuk_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 535, 480, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sungjang = True
                                    back_ = True
                                else:
                                    click_pos_2(30, 55, cla)
                # 모험
                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 700, 840, 740, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("모험", imgs_)
                    click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                    sungjang = False
                    while sungjang is False:
                        full_path = "c:\\nightcrow\\imgs\\get_item\\upjuk_mohum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 90, 240, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(850, 130, cla)
                            time.sleep(0.2)
                            sungjang = True
                            back_ = False
                            while back_ is False:
                                full_path = "c:\\nightcrow\\imgs\\get_item\\upjuk_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 535, 480, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sungjang = True
                                    back_ = True
                                else:
                                    click_pos_2(30, 55, cla)
                # 주요 업적
                last_upjuk_ = False
                while last_upjuk_ is False:
                    full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 600, 560, 660, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("주요업적", imgs_)
                        click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                        time.sleep(0.5)
                        click_pos_2(480, 730, cla)
                    else:
                        last_upjuk_ = True
                        clean_screen(cla)


            else:
                menu_open(cla)

                full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(780, 160, 825, 195, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(790, 190, cla)
                else:
                    get_upjuk_ = True



    except Exception as e:
        print(e)