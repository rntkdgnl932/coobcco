# import numpy as np
# import cv2
# import os.path
import time
# import random

import sys
sys.path.append('C:/coobcco/mymodule')
# from function import *
# from action import go_alrim_yes, now_hunting_is, now_hunting
# from where import go_worldmap

import variable as v_

def go_test(cla):
    print('hi test! dungeon', cla)



def go_jadong_in(world_, where, force_required, drag, moglog, select, delay, cla):
    try:
        from function import imgs_set, random_int, click_pos_2, drag_pos, go_auto
        from where import go_worldmap
        from clean import clean_screen
        from action import now_hunting_is
        from massenger import line_to_me
        import numpy as np
        import cv2

        go_ = False

        delay = int(delay)

        # 스케쥴 초기화 관련t ttttttttttttttttttttttttttttttttttttt
        # if os.path.isfile(file_path) == True:
        #     # 파일 읽기
        #     with open(file_path, "r", encoding='UTF8') as file:
        #         lines_ = file.read().splitlines()
        #         lines = ' '.join(lines_).split()

        # go_jadong_in(where, 14500, drag, 550, 875, cla)
        # go_jadong_in(마을, 장소, 요구전투력, 드래그여부, 목록, 선택, 딜레이, cla)
        if cla == 'one':
            jadong_power = int(v_.mypower_1)
        if cla == 'two':
            jadong_power = int(v_.mypower_2)

        if jadong_power >= force_required:
            print("good my Power")
        # else:
        #     why = "요구 전투력 : " + str(force_required) + " / " + "내 전투력 : " + str(jadong_power)
        #     line_to_me(cla, why)
        # 파워 오류로 측정없이 무조건 보내기
        isJadong = False
        while isJadong is False:
            thisWorld = False
            print("자동장소", where)
            full_path = "c:\\coobcco\\imgs\\worldmap_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(1, 30, 100, 80, cla, img)
            if imgs_ is None or imgs_ == False:
                print("월드맵 아니닷")

                full_path = "c:\\coobcco\\imgs\\worldmap_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("월드맵 아니닷2")
                else:
                    print("월드맵이닷2", imgs_)
                    thisWorld = True
            else:
                print("월드맵이닷", imgs_)
                thisWorld = True

            time.sleep(random_int())

            if thisWorld == True:
                full_path = "c:\\coobcco\\imgs\\bbaln_move.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(400, 400, 540, 500, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("빠른이동이 안보여")
                    # 시작
                    result_2 = go_worldmap(cla, "world_moglog")
                    time.sleep(0.5)
                    if result_2 == False:
                        print("아직 월드맵 목록이 아니여")
                        click_pos_2(130, 215, cla)  # 중복


                    time.sleep(random_int())  # 중복
                    if world_ == 'yotoon':
                        full_path = "c:\\coobcco\\imgs\\jadong_yotoon.png"
                    if world_ == 'midgard':
                        full_path = "c:\\coobcco\\imgs\\world_midgard.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(400, 965, 580, 1010, cla, img)
                    if imgs_ is None or imgs_ == False:
                        if world_ == 'yotoon':
                            print("요툰하임이 안보여")
                        if world_ == 'midgard':
                            print("미드가르드가 안보여")

                        click_pos_2(80, 956, cla)  # 중복
                        time.sleep(1)  # 중복
                        if world_ == 'yotoon':
                            click_pos_2(280, 450, cla)
                        if world_ == 'midgard':
                            click_pos_2(160, 515, cla)

                        time.sleep(1)  # 중복
                        click_pos_2(550, 994, cla)  # 중복
                        time.sleep(1)  # 중복
                    else:
                        if world_ == 'yotoon':
                            print("요툰하임이 보여")
                        if world_ == 'midgard':
                            print("미드가르드가 보여")

                        result_2 = go_worldmap(cla, "world_moglog")
                        time.sleep(2)
                        if result_2 == False:
                            print("아직 월드맵 목록이 아니여")
                            click_pos_2(30, 110, cla)  # 중복
                            time.sleep(1)  # 중복
                        else:
                            print("월드맵 목록이 맞당께")


                            if drag == True:
                                # 드래그
                                drag_pos(135, 745, 135, 210, cla)
                                time.sleep(1)

                            click_pos_2(135, moglog, cla)
                            time.sleep(2)  # 중복
                            click_pos_2(705, select, cla)
                            time.sleep(2)  # 중복
                            click_pos_2(892, 1004, cla)  # 중복
                            time.sleep(2)  # 중복
                else:
                    print("빠른이동이 보여")
                    isJadong = True
                    go_ = False


                    # 이후 도착했는지 파악하기
                    is8285 = False
                    while is8285 is False:
                        full_path = "c:\\coobcco\\imgs\\bbaln_move.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(400, 400, 540, 500, cla, img)
                        if imgs_ is None or imgs_ == False:
                            is8285 = True
                        else:
                            click_pos_2(545, 610, cla)  # 중복
                            time.sleep(random_int())

            else:
                full_path = "c:\\coobcco\\imgs\\bbaln_move.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(400, 400, 540, 500, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("빠른이동이 안보여")
                    time.sleep(1)
                    result_world = go_worldmap(cla, 'world')
                    if result_world == True:
                        click_pos_2(30, 110, cla)
                        time.sleep(1)
                    else:
                        # click_pos_2(920, 55, cla)
                        # time.sleep(random_int())
                        clean_screen(cla, "go_jadong_in")
                        click_pos_2(130, 215, cla)  # 중복
                        time.sleep(1)
                else:
                    print("빠른이동이 보여")
                    isJadong = True
                    go_ = False
                    is8285 = False
                    while is8285 is False:
                        full_path = "c:\\coobcco\\imgs\\bbaln_move.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(400, 400, 540, 500, cla, img)
                        if imgs_ is None or imgs_ == False:
                            # auto
                            isresultauto = False
                            while isresultauto is False:
                                resultauto = go_auto(cla, '10')
                                if resultauto == False:
                                    print("사냥터 미도착")
                                    time.sleep(random_int())
                                else:

                                    isresultauto = True
                                    print("사냥터 도착", delay)
                                    time.sleep(delay + random_int())
                                    click_pos_2(900, 890, cla)
                                    time.sleep(random_int())
                                    result_hunting = now_hunting_is(where, cla)
                                    is8285 = True
                                    time.sleep(random_int())
                        else:

                            click_pos_2(545, 610, cla)  # 중복
                            time.sleep(random_int())


        # else:
        #     print("요구투력 보다 낮아 자동 장소로 변경")
        #     # go_jadong_in(마을, 장소, 요구전투력, 드래그여부, 목록, 선택, 딜레이, cla)
        #     # jadong_cla_ready(cla, '바위해안')
        #     go_jadong_cla_mypower(cla)
        #     # go_jadong_in('yotoon', where, 0, False, 300, 850, cla)



        return go_
    except Exception as e:
        print(e)
        return 0


def start_ready_in_jadong(cla):
    try:
        from clean import clean_screen
        #def nowtestt
        print("start_ready_in_jadong")
        print("1")
        clean_screen(cla, "start_ready_in_jadong")

        # jadong_cla_ready(cla, '바위해안')
        go_jadong_cla_mypower(cla)
        #auto



    except Exception as e:
        print(e)
        return 0


def jadong_cla_play(cla, where):
    try:
        from function import imgs_set, random_int, click_pos_2, drag_pos, myPotion_check
        from clean import clean_screen
        from action import now_hunting

        nowPlay = 'jadong'


        clean_screen(cla, "jadong_cla_play")
        result_ = now_hunting(nowPlay, cla)  # False는 현재 노사냥, True는 현재 사냥중
        print("result_ = now_hunting(nowPlay, cla)", result_)
        print("jadong_cla_play : ", where)
        if result_ == False:
            jadong_cla_ready(cla, where)  # False는 자동사냥 진행, True는 자동사냥 노진행
            print("자동사냥 시작")
            time.sleep(10 + random_int())
            # click_pos_2(900, 888, cla)
            # time.sleep(1 + random_int())
            myPotion_check(nowPlay, cla)
            if cla == 'one':
                v_.one_cla_ing = nowPlay
            if cla == 'two':
                v_.two_cla_ing = nowPlay
            time.sleep(5 + random_int())
            print("자동사냥 체크 끝")
            # 여기에 초기화 시간 넣어서 코딩하기(시간함수)
            # 시간

        time.sleep(1 + random_int())
        jadong_0_check = False

    except Exception as e:
        print(e)
        return 0

def dunjeon_cla_ready(cla, dunjeon):
    try:
        from function import imgs_set, random_int, click_pos_2, drag_pos, menuOpenCheck
        from clean import clean_screen
        import numpy as np
        import cv2
        # test
        dunjeon_list_ready = False
        isdungeon_ing = False

        while isdungeon_ing is False:

            result = menuOpenCheck(cla, "dunjeon_cla_ready")
            if result == True:
                click_pos_2(740, 375, cla)
                time.sleep(2 + random_int())



                full_path = "c:\\coobcco\\imgs\\mangdog.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(80, 345, 250, 410, cla, img)
                time.sleep(random_int())
                if imgs_ is None or imgs_ == False:
                    print("맹독의 뱀 둥지 안 보임...")
                    click_pos_2(920, 55, cla)
                    time.sleep(random_int())

                else:
                    print("맹독의 뱀 둥지 보임...")
                    click_pos_2(240, 105, cla)
                    time.sleep(random_int())

                    full_path = "c:\\coobcco\\imgs\\mangdog.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(80, 345, 250, 410, cla, img)
                    time.sleep(random_int())
                    if imgs_ is None or imgs_ == False:
                        print("맹독의 뱀 둥지 안 보임2...")
                        drag_pos(800, 522, 200, 522, cla)
                        time.sleep(random_int())
                        drag_pos(800, 522, 200, 522, cla)
                        time.sleep(random_int())


                        if dunjeon == 'gonghu':
                            full_path = "c:\\coobcco\\imgs\\gonghu.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(70, 350, 220, 410, cla, img)
                            time.sleep(random_int())
                            if imgs_ is None or imgs_ == False:
                                print("공허던전 안 보임...")
                                drag_pos(800, 522, 200, 522, cla)
                                time.sleep(random_int())
                                full_path = "c:\\coobcco\\imgs\\gonghu.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(70, 350, 220, 410, cla, img)

                                if imgs_ is None or imgs_ == False:
                                    print("공허던전 안 보임2...")
                                else:
                                    print("imgs", imgs_)
                                    print('공허던전 진입 전2')
                                    dunjeon_list_ready = True
                                    isdungeon_ing = True
                            else:
                                print("imgs", imgs_)
                                print('공허던전 진입 전')
                                dunjeon_list_ready = True
                                isdungeon_ing = True
                        if dunjeon == 'nanjang':
                            full_path = "c:\\coobcco\\imgs\\nanjang.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(370, 350, 550, 410, cla, img)

                            if imgs_ is None or imgs_ == False:
                                print("난쟁던전 안 보임...")
                                drag_pos(800, 522, 200, 522, cla)
                                time.sleep(random_int())
                                full_path = "c:\\coobcco\\imgs\\nanjang.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(370, 350, 550, 410, cla, img)

                                if imgs_ is None or imgs_ == False:
                                    print("난쟁던전 안 보임2...")
                                else:
                                    print("imgs", imgs_)
                                    print('난쟁던전 진입 전2')
                                    dunjeon_list_ready = True
                                    isdungeon_ing = True
                            else:
                                print("imgs", imgs_)
                                print('난쟁던전 진입 전')
                                dunjeon_list_ready = True
                                isdungeon_ing = True
                        if dunjeon == 'underprison':
                            full_path = "c:\\coobcco\\imgs\\underprison.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(710, 350, 830, 410, cla, img)

                            if imgs_ is None or imgs_ == False:
                                print("지감던전 안 보임...")
                                drag_pos(800, 522, 200, 522, cla)
                                time.sleep(random_int())
                                full_path = "c:\\coobcco\\imgs\\underprison.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(710, 350, 830, 410, cla, img)

                                if imgs_ is None or imgs_ == False:
                                    print("지감던전 안 보임2...")
                                else:
                                    print("imgs", imgs_)
                                    print('지감던전 진입 전2')
                                    dunjeon_list_ready = True
                                    isdungeon_ing = True
                            else:
                                print("imgs", imgs_)
                                print('지감던전 진입 전')
                                dunjeon_list_ready = True
                                isdungeon_ing = True


            else:
                clean_screen(cla, "dunjeon_cla_ready")
                click_pos_2(920, 55, cla)
                time.sleep(1)

        return dunjeon_list_ready
    except Exception as e:
        print(e)
        return 0
def in_dunjeon_list(cla, dunjeon):
    try:
        from function import random_int, click_pos_2
        from schedule import myQuest_play_check

        datas = 'check'
        start_ready = myQuest_play_check(cla, datas)

        if '_' in start_ready[0][2]:
            print("_", "hello '_'")
            dunjeon_spl_ = start_ready[0][2].split("_")
            print("dunjeon_spl_[0]", dunjeon_spl_[0])
            print("dunjeon_spl_[1]", dunjeon_spl_[1])
            dunjeon_level = int(dunjeon_spl_[1])

        step = 'none'

        y_ = 170

        if cla == 'one':
            level_ = v_.mylevel_1
            power_ = v_.mypower_1
        if cla == 'two':
            level_ = v_.mylevel_2
            power_ = v_.mypower_2
        if dunjeon == 'gonghu':
            # 전투력 및 레벨 체크 후 클릭
            # if level_ >= 70 and power_ >= 30000:
            #     y_ = 400
            #     click_pos_2(160, 400, cla)
            #     time.sleep(1 + random_int())
            #     step = '광기의 균열'
            # elif level_ >= 64 and power_ >= 26000:
            #     y_ = 345
            #     click_pos_2(160, 345, cla)
            #     time.sleep(1 + random_int())
            #     step = '분쟁의 신전'
            # elif power_ >= 23000 and level_ >= 56:
            #     y_ = 285
            #     click_pos_2(160, 285, cla)
            #     time.sleep(1 + random_int())
            #     step = '공포의 내리막'
            # elif power_ >= 17000 and level_ >= 48:
            #     y_ = 230
            #     click_pos_2(160, 230, cla)
            #     time.sleep(1 + random_int())
            #     step = '혼돈의 동굴'
            # elif power_ >= 14000 and level_ >= 35:
            #     y_ = 170
            #     click_pos_2(160, 170, cla)
            #     time.sleep(1 + random_int())
            #     step = '악취 나는 통로'
            # else:
            #     click_pos_2(160, 115, cla)
            #     time.sleep(1 + random_int())
            #     step = '균열의 입구'
            if dunjeon_level == 6:
                y_ = 400
                click_pos_2(160, 400, cla)
                time.sleep(1 + random_int())
                step = '광기의 균열'
            elif dunjeon_level == 5:
                y_ = 345
                click_pos_2(160, 345, cla)
                time.sleep(1 + random_int())
                step = '분쟁의 신전'
            elif dunjeon_level == 4:
                y_ = 285
                click_pos_2(160, 285, cla)
                time.sleep(1 + random_int())
                step = '공포의 내리막'
            elif dunjeon_level == 3:
                y_ = 230
                click_pos_2(160, 230, cla)
                time.sleep(1 + random_int())
                step = '혼돈의 동굴'
            elif dunjeon_level == 2:
                y_ = 170
                click_pos_2(160, 170, cla)
                time.sleep(1 + random_int())
                step = '악취 나는 통로'
            else:
                click_pos_2(160, 115, cla)
                time.sleep(1 + random_int())
                step = '균열의 입구'
        elif dunjeon == 'nanjang':
            # 전투력 및 레벨 체크 후 클릭
            # if level_ >= 71 and power_ >= 30000:
            #     y_ = 400
            #     click_pos_2(160, 400, cla)
            #     time.sleep(1 + random_int())
            #     step = '불타버린 길'
            # elif level_ >= 65 and power_ >= 26000:
            #     y_ = 345
            #     click_pos_2(160, 345, cla)
            #     time.sleep(1 + random_int())
            #     step = '울부짖는 길'
            # elif power_ >= 23000 and level_ >= 57:
            #     y_ = 285
            #     click_pos_2(160, 285, cla)
            #     time.sleep(1 + random_int())
            #     step = '상처입은 길'
            # elif power_ >= 17000 and level_ >= 49:
            #     y_ = 230
            #     click_pos_2(160, 230, cla)
            #     time.sleep(1 + random_int())
            #     step = '얼어붙은 길'
            # elif power_ >= 14000 and level_ >= 36:
            #     y_ = 170
            #     click_pos_2(160, 170, cla)
            #     time.sleep(1 + random_int())
            #     step = '속삭이는 길'
            # else:
            #     click_pos_2(160, 115, cla)
            #     time.sleep(1 + random_int())
            #     step = '저주받은 길'
            if dunjeon_level == 6:
                y_ = 400
                click_pos_2(160, 400, cla)
                time.sleep(1 + random_int())
                step = '불타버린 길'
            elif dunjeon_level == 5:
                y_ = 345
                click_pos_2(160, 345, cla)
                time.sleep(1 + random_int())
                step = '울부짖는 길'
            elif dunjeon_level == 4:
                y_ = 285
                click_pos_2(160, 285, cla)
                time.sleep(1 + random_int())
                step = '상처입은 길'
            elif dunjeon_level == 3:
                y_ = 230
                click_pos_2(160, 230, cla)
                time.sleep(1 + random_int())
                step = '얼어붙은 길'
            elif dunjeon_level == 2:
                y_ = 170
                click_pos_2(160, 170, cla)
                time.sleep(1 + random_int())
                step = '속삭이는 길'
            else:
                click_pos_2(160, 115, cla)
                time.sleep(1 + random_int())
                step = '저주받은 길'
        elif dunjeon == 'underprison':
            # 전투력 및 레벨 체크 후 클릭
            # if power_ >= 60000:
            #     y_ = 575
            #     click_pos_2(160, 575, cla)
            #     time.sleep(1 + random_int())
            #     step = '혼돈의 전당'
            # elif power_ >= 50000:
            #     y_ = 520
            #     click_pos_2(160, 520, cla)
            #     time.sleep(1 + random_int())
            #     step = '최악의 심연'
            # elif power_ >= 40000:
            #     y_ = 460
            #     click_pos_2(160, 460, cla)
            #     time.sleep(1 + random_int())
            #     step = '나태의 지옥'
            # elif power_ >= 30000:
            #     y_ = 400
            #     click_pos_2(160, 400, cla)
            #     time.sleep(1 + random_int())
            #     step = '식탐의 방'
            # elif power_ >= 25000:
            #     y_ = 345
            #     click_pos_2(160, 345, cla)
            #     time.sleep(1 + random_int())
            #     step = '음욕의 나락'
            # elif power_ >= 20000:
            #     y_ = 285
            #     click_pos_2(160, 285, cla)
            #     time.sleep(1 + random_int())
            #     step = '분노의 처형터'
            # elif power_ >= 17000:
            #     y_ = 230
            #     click_pos_2(160, 230, cla)
            #     time.sleep(1 + random_int())
            #     step = '질투의 고문소'
            # elif power_ >= 14000:
            #     y_ = 170
            #     click_pos_2(160, 170, cla)
            #     time.sleep(1 + random_int())
            #     step = '탐욕의 묘지'
            # else:
            #     click_pos_2(160, 115, cla)
            #     time.sleep(1 + random_int())
            #     step = '교만의 감옥'
            # 지하감옥은 자체로 6층 까지만 열어두자
            # if dunjeon_level == 9:
            #     y_ = 575
            #     click_pos_2(160, 575, cla)
            #     time.sleep(1 + random_int())
            #     step = '혼돈의 전당'
            # elif dunjeon_level == 8:
            #     y_ = 520
            #     click_pos_2(160, 520, cla)
            #     time.sleep(1 + random_int())
            #     step = '최악의 심연'
            # elif dunjeon_level == 7:
            #     y_ = 460
            #     click_pos_2(160, 460, cla)
            #     time.sleep(1 + random_int())
            #     step = '나태의 지옥'
            if dunjeon_level == 6:
                y_ = 400
                click_pos_2(160, 400, cla)
                time.sleep(1 + random_int())
                step = '식탐의 방'
            elif dunjeon_level == 5:
                y_ = 345
                click_pos_2(160, 345, cla)
                time.sleep(1 + random_int())
                step = '음욕의 나락'
            elif dunjeon_level == 4:
                y_ = 285
                click_pos_2(160, 285, cla)
                time.sleep(1 + random_int())
                step = '분노의 처형터'
            elif dunjeon_level == 3:
                y_ = 230
                click_pos_2(160, 230, cla)
                time.sleep(1 + random_int())
                step = '질투의 고문소'
            elif dunjeon_level == 2:
                y_ = 170
                click_pos_2(160, 170, cla)
                time.sleep(1 + random_int())
                step = '탐욕의 묘지'
            else:
                click_pos_2(160, 115, cla)
                time.sleep(1 + random_int())
                step = '교만의 감옥'

        return step, y_
    except Exception as e:
        print(e)
        return 0

def dunjeon_in_cla_ready(cla, dunjeon):
    try:
        from function import imgs_set, random_int, click_pos_2, click_pos_reg
        from action import go_alrim_yes
        from clean import clean_screen
        from schedule import myQuest_play_check, myQuest_play_add
        import numpy as np
        import cv2

        print("던전준비", cla)
        print("던전준비", dunjeon)
        step = "none"
        isdungeon_ing = True
        if cla == 'one':
            myid_ = v_.myId_1
            if dunjeon == 'gonghu':
                now_dunjeon = v_.gonghu_1
            if dunjeon == 'nanjang':
                now_dunjeon = v_.nanjang_1
            if dunjeon == 'underprison':
                now_dunjeon = v_.underprison_1
        if cla == 'two':
            myid_ = v_.myId_2
            if dunjeon == 'gonghu':
                now_dunjeon = v_.gonghu_2
            if dunjeon == 'nanjang':
                now_dunjeon = v_.nanjang_2
            if dunjeon == 'underprison':
                now_dunjeon = v_.underprison_2

        isdunjeonclaready = False
        dunjeon_0_check = True
        while isdunjeonclaready is False:

            # select_stair = False
            print("점검--28----------------------던전화면으로 이동")
            result_d = dunjeon_cla_ready(cla, dunjeon)
            print("점검--29----------------------던전화면 체크")

            if result_d == True:
                time.sleep(0.5)
                full_path = "c:\\coobcco\\imgs\\dunjeon_lock.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

                # 여기 던전마다 이미지 위치 달라져야 한다
                if dunjeon == 'gonghu':
                    imgs_ = imgs_set(80, 440, 220, 580, cla, img)
                if dunjeon == 'nanjang':
                    imgs_ = imgs_set(390, 440, 530, 580, cla, img)
                if dunjeon == 'underprison':
                    imgs_ = imgs_set(710, 440, 850, 580, cla, img)

                if imgs_ is None or imgs_ == False:
                    time.sleep(random_int())
                    full_path = "c:\\coobcco\\imgs\\zero.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

                    # 여기 던전마다 이미지 위치 달라져야 한다
                    if dunjeon == 'gonghu':
                        imgs_ = imgs_set(100, 645, 200, 685, cla, img)
                    if dunjeon == 'nanjang':
                        imgs_ = imgs_set(410, 645, 510, 685, cla, img)
                    if dunjeon == 'underprison':
                        imgs_ = imgs_set(730, 645, 830, 685, cla, img)



                    if imgs_ is None or imgs_ == False:
                        print("없..")
                        # 여기 던전마다 클릭 위치 달라져야 한다.
                        if dunjeon == 'gonghu':
                            click_pos_2(160, 520, cla)
                        if dunjeon == 'nanjang':
                            click_pos_2(460, 520, cla)
                        if dunjeon == 'underprison':
                            click_pos_2(760, 520, cla)
                        time.sleep(3 + random_int())

                        # 여기서 화면 넘어갔는지 확인인
                        full_path = "c:\\coobcco\\imgs\\jungye.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(30, 30, 140, 80, cla, img)
                        if imgs_ is None or imgs_ == False:
                            print("정예던전이 없다. 클릭")
                            # 여기 던전마다 클릭 위치 달라져야 한다.
                            if dunjeon == 'gonghu':
                                click_pos_2(160, 520, cla)
                            if dunjeon == 'nanjang':
                                click_pos_2(460, 520, cla)
                            if dunjeon == 'underprison':
                                click_pos_2(760, 520, cla)
                            time.sleep(3 + random_int())
                        else:
                            print("정예던전이 있다. 진행..")
                            #실수로 들어왔을 경우 한번더 체크(끝난 던전인지.../////////////////////////////////////////////////////////////////////////////////////////////////)
                            full_path = "c:\\coobcco\\imgs\\dunjeon\\dungeon_clear_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(660, 960, 740, 1000, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                print("dungeon_clear_1", imgs_)
                                isdunjeonclaready = True
                                print("imgs", imgs_)
                                print("여기 " + str(dunjeon) + " 이미 끝나 있음.")
                                dunjeon_0_check = False
                                isdungeon_ing = False
                            else:
                                print("dungeon_clear_1 없")
                                # 여기 던전마다 저장위치 달라져야 한다.
                                if cla == 'one':
                                    if dunjeon == 'gonghu':
                                        v_.gonghu_1 = False
                                        now_dunjeon = v_.gonghu_1
                                    if dunjeon == 'nanjang':
                                        v_.nanjang_1 = False
                                        now_dunjeon = v_.nanjang_1
                                    if dunjeon == 'underprison':
                                        v_.underprison_1 = False
                                        now_dunjeon = v_.underprison_1
                                if cla == 'two':
                                    if dunjeon == 'gonghu':
                                        v_.gonghu_2 = False
                                        now_dunjeon = v_.gonghu_2
                                    if dunjeon == 'nanjang':
                                        v_.nanjang_2 = False
                                        now_dunjeon = v_.nanjang_2
                                    if dunjeon == 'underprison':
                                        v_.underprison_2 = False
                                        now_dunjeon = v_.underprison_2



                                # 여긴 던전마다 다른 포인트...
                                step = in_dunjeon_list(cla, dunjeon)
                                print('step', step)
                                time.sleep(1)

                                click_pos_2(840, 992, cla)
                                time.sleep(2)

                                # click_pos_2(160, step[1]-60, cla)
                                # time.sleep(1)
                                # click_pos_2(840, 992, cla)
                                # time.sleep(1)
                                result_ = go_alrim_yes(cla)
                                if result_[0] == True:
                                    click_pos_reg(result_[1], result_[2], cla)
                                else:
                                    click_pos_2(550, 610, cla)
                                # print(gonghu_1_[0])
                                time.sleep(3 + random_int())
                                #여기서 화면 넘어갔는지 체크?
                                full_path = "c:\\coobcco\\imgs\\jungye.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(30, 30, 140, 80, cla, img)
                                if imgs_ is not None:
                                    print("정예던전이 있다. 클릭")
                                    isdunjeonclaready = True
                                    click_pos_2(160, step[1] - 60, cla)
                                    time.sleep(1)
                                    click_pos_2(840, 992, cla)
                                    time.sleep(1)
                                    result_ = go_alrim_yes(cla)
                                    if result_[0] == True:
                                        click_pos_reg(result_[1], result_[2], cla)
                                    else:
                                        click_pos_2(550, 610, cla)
                                else:
                                    print("정예던전이 없다. 진행..")


                                    time.sleep(2 + random_int())
                                    if step[0] != 'none':
                                        time.sleep(2 + random_int())
                                        full_path = "c:\\coobcco\\imgs\\jungye.png"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set(30, 30, 140, 80, cla, img)

                                        if imgs_ is None or imgs_ == False:
                                            isdunjeonclaready = True
                                            print("여기 " + str(dunjeon) + " 던전 진입 중")
                                            # while 끝
                                        else:
                                            isdunjeonclaready = True
                                            dunjeon_0_check = False
                                            isdungeon_ing = False
                                            print(dunjeon+ "던전 끝?인듯..")
                                            # while 끝


                                # start_ = text_check_get(200, 390, 290, 415, cla)
                                # started_ = start_.split("\n")
                                # if len(started_) != 0:
                                #     end_ = ''.join(started_)
                                #     print("공허 이미 끝?", end_)
                                #     for list in end_:
                                #         try:
                                #             if list == '레' or list == '벨':
                                #                 dunjeon_0_check = False
                                #                 isdungeon_ing = False
                                #                 print("공허 끝?", end_)
                                #
                                #         except:
                                #             pass
                    else:
                        isdunjeonclaready = True
                        # while 끝
                        print("imgs", imgs_)
                        print("여기 " + str(dunjeon) + " 던전 끝")
                        dunjeon_0_check = False
                        isdungeon_ing = False

                else:
                    isdunjeonclaready = True
                    # while 끝
                    print("imgs", imgs_)
                    print("여기 " + str(dunjeon) + " 던전 열리지 않았음. 던전 완료로 간주.")
                    dunjeon_0_check = False
                    isdungeon_ing = False
            else:

                clean_screen(cla, "dunjeon_in_cla_ready")
                # dunjeon_cla_ready(cla, dunjeon)

            if dunjeon_0_check == False:
                print(dunjeon + " 끝???남...")

                # 여기에서 다음 던전 있는지 판단 후 바로 들어가기...
                # myQuest_play_add(cla, dunjeon)
                # result_sch = myQuest_play_check(cla, "dunjeon")
                # if int(result_sch[0][1]) == int(myid_):
                #     if str(result_sch[0][2]) == "공허" or str(result_sch[0][2]) == "난쟁이" or str(result_sch[0][2]) == "지하감옥":
                #         print("g")



                click_pos_2(930, 60, cla)
                # 현재 던전 트루, 펄스 체크
                if cla == 'one':
                    v_.one_cla_ing = 'check'
                    if dunjeon == 'gonghu':
                        v_.gonghu_1 = True
                        now_dunjeon = v_.gonghu_1
                    if dunjeon == 'nanjang':
                        v_.nanjang_1 = True
                        now_dunjeon = v_.nanjang_1
                    if dunjeon == 'underprison':
                        v_.underprison_1 = True
                        now_dunjeon = v_.underprison_1


                if cla == 'two':
                    v_.two_cla_ing = 'check'
                    if dunjeon == 'gonghu':
                        v_.gonghu_2 = True
                        now_dunjeon = v_.gonghu_2
                    if dunjeon == 'nanjang':
                        v_.nanjang_2 = True
                        now_dunjeon = v_.nanjang_2
                    if dunjeon == 'underprison':
                        v_.underprison_2 = True
                        now_dunjeon = v_.underprison_2


                time.sleep(random_int())
        # now_dunjeon => True는 완료, isdungeon_ing => False는 완료
        return now_dunjeon, step[0], isdungeon_ing
    except Exception as e:
        print(e)
        return 0




def jadong_low_power(cla):
    try:
        from function import imgs_set, random_int, click_pos_2
        print('들소황무지')
        click_pos_2(130, 215, cla)
        time.sleep(3 + random_int())
        click_pos_2(80, 956, cla)
        time.sleep(3 + random_int())

        click_pos_2(280, 450, cla)
        time.sleep(3 + random_int())
        click_pos_2(550, 994, cla)
        time.sleep(5 + random_int())
        click_pos_2(28, 106, cla)
        time.sleep(3 + random_int())
        click_pos_2(135, 300, cla)
        time.sleep(3 + random_int())

        click_pos_2(700, 850, cla)
        time.sleep(3 + random_int())
        click_pos_2(892, 1004, cla)
        time.sleep(3 + random_int())
        click_pos_2(545, 610, cla)
        time.sleep(20 + random_int())
        time.sleep(25 + random_int())
    except Exception as e:
        print(e)
        return 0
def go_jadong_cla_mypower(cla):
    try:
        import os.path
        import random

        hunt_where = "none"
        jadong_power = 0
        if cla == 'one':
            jadong_power = v_.mypower_1
            jadong_now = v_.jadong_1
        if cla == 'two':
            jadong_power = v_.mypower_2
            jadong_now = v_.jadong_2


        dir_path = "C:\\coobcco"
        file_path12 = dir_path + "\\jadong\\jadong_random.txt"

        if os.path.isfile(file_path12) == True:
            # 파일 읽기
            with open(file_path12, "r", encoding='UTF8') as file:
                lines_ = file.read().splitlines()
                lines = ' '.join(lines_).split()

        # print("random list_1", random.choice(lines))
        # print("random list_2", random.choice(lines))

        for i in range(len(lines)):
            result_hunt = lines[i].split(":")

            if int(jadong_power) >= int(result_hunt[0]):
                print("내 전투력 " + str(result_hunt[0]) + " 이상")
                hunt_where = random.choice(result_hunt[1].split("/"))
                break

        print("당첨된 장소 : ", hunt_where)
        if hunt_where != "none":
            jadong_cla_ready(cla, str(hunt_where))
        else:
            jadong_cla_ready(cla, '바위해안')




    except Exception as e:
        print(e)
        return 0
def jadong_cla_ready(cla, where):
    try:
        import os.path

        if cla == 'one':
            jadong_power = v_.mypower_1
            jadong_now = v_.jadong_1
        if cla == 'two':
            jadong_power = v_.mypower_2
            jadong_now = v_.jadong_2

        none_where = True

        print("자동사냥 준비(내 전투력 : )", jadong_power)
        print("자동사냥 준비(장소 : )", where)

        # go_jadong_in(마을, where, 14500, drag, 550, 875, cla)
        # go_jadong_in(마을 ,장소, 요구전투력, 드래그여부, 목록, 선택, 딜레이, cla)
        dir_path = "C:\\coobcco"
        file_path = dir_path + "\\jadong\\jadong_in.txt"

        if os.path.isfile(file_path) == True:
            # 파일 읽기
            with open(file_path, "r", encoding='UTF8') as file:
                lines_ = file.read().splitlines()
                lines = ' '.join(lines_).split()
                print('lines', lines)
                print('lines[0]', lines[0])
                # result_ = []
                for i in range(len(lines)):
                    result_file = lines[i].split(':')
                    # print('lines', lines[i])
                    # print('result_file[0]', result_file[0]) # 마을
                    # print('result_file[1]', result_file[1]) # 장소
                    # print('result_file[2]', result_file[2]) # 요구전투력
                    # print('result_file[3]', result_file[3]) # 드래그
                    # print('result_file[4]', result_file[4]) # 목록
                    # print('result_file[5]', result_file[5]) # 선택
                    # print('result_file[6]', result_file[6]) # 딜레이
                    if result_file[1] == where:
                        result_ = result_file
                        none_where = False
                if none_where == False:
                    print("result_", result_)
                    if result_[3] == 'true':
                        re_ = True
                    else:
                        re_ = False
                    result = go_jadong_in(result_[0], result_[1], int(result_[2]), re_, int(result_[4]), int(result_[5]), int(result_[6]), cla)
                    print("go_jadong_result", result)
                else:
                    # jadong_cla_ready(cla, '바위해안')
                    go_jadong_cla_mypower(cla)


        return jadong_now
    except Exception as e:
        print(e)
        return 0





def dunjeon_cla_play(cla, data, dunjeon):
    try:
        from clean import clean_screen
        from function import random_int, click_pos_2
        from action import now_hunting, now_hunting_is
        print("현재 던전 : " + str(dunjeon) + " 진행중")
        print(str(dunjeon) + " 진행중? " + str(data))
        print("data!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", data)

        clean_screen(cla, "dunjeon_cla_play")
        questcomplete = False

        if data == dunjeon:
            same_ = True
        else:
            same_ = False

        if same_ == False:
            # 던전 입장하기
            result = dunjeon_in_cla_ready(cla, dunjeon)
            time.sleep(random_int())
            print("던전체크", result)
            # [0] True면 해당던전완료, [1] 현재 돌고 있는 곳, [2] False 면 완료

            if result[2] == True:

                if cla == 'one':
                    print("cla_ing!!!!!!!!!!!!!", v_.one_cla_ing)
                    v_.one_cla_ing = dunjeon
                    print("cla_ing222!!!!!!!!!!!!!", v_.one_cla_ing)
                if cla == 'two':
                    print("cla_ing!!!!!!!!!!!!!", v_.two_cla_ing)
                    v_.two_cla_ing = dunjeon
                    print("cla_ing222!!!!!!!!!!!!!", v_.two_cla_ing)



            if result[0] == True:
                questcomplete = True
                print(data + " : 끝")
                if cla == 'one':
                    if dunjeon == 'gonghu':
                        v_.gonghu_1 = True
                    if dunjeon == 'nanjang':
                        v_.nanjang_1 = True
                    if dunjeon == 'underprison':
                        v_.underprison_1 = True
                if cla == 'two':
                    if dunjeon == 'gonghu':
                        v_.gonghu_2 = True
                    if dunjeon == 'nanjang':
                        v_.nanjang_2 = True
                    if dunjeon == 'underprison':
                        v_.underprison_2 = True


        # 아래는 same == True 일때 썼던...
        if questcomplete == False:
            resurlt_ = dunjeonCheck(cla, dunjeon, same_)
            time.sleep(1)

            if resurlt_ == False:
                if cla == 'one':
                    print("cla_ing!!!!!!!!!!!!!", v_.one_cla_ing)
                    v_.one_cla_ing = 'check'
                    print("cla_ing222!!!!!!!!!!!!!", v_.one_cla_ing)
                if cla == 'two':
                    print("cla_ing!!!!!!!!!!!!!", v_.two_cla_ing)
                    v_.two_cla_ing = 'check'
                    print("cla_ing222!!!!!!!!!!!!!", v_.two_cla_ing)
            else:
                now_hunting_is(data, cla)
                print("던전 중")

            # # True는 계속 사냥 잘하고 있음. False는 정상적인 사냥을 못하고 있는 상황
            # if resurlt_ == False:
            #     clean_screen(cla, "dunjeon_cla_play_middle")
            #     resurlted_ = now_hunting(data, cla)
            #     # resulted_=> True 현재 사냥중
            #     if resurlted_== True:
            #         print("던전 끝내고 어디에선가 사냥중")
            #     else:
            #         print("dunjeon_cla_play가만히 있는 중 or 다른화면")
            #         click_pos_2(930, 55, cla)
            #         time.sleep(random_int())
            #         clean_screen(cla, "dunjeon_cla_play_end")
            #
            #     if cla == 'one':
            #         print("cla_ing!!!!!!!!!!!!!", v_.one_cla_ing)
            #         v_.one_cla_ing = 'check'
            #         print("cla_ing222!!!!!!!!!!!!!", v_.one_cla_ing)
            #     if cla == 'two':
            #         print("cla_ing!!!!!!!!!!!!!", v_.two_cla_ing)
            #         v_.two_cla_ing = 'check'
            #         print("cla_ing222!!!!!!!!!!!!!", v_.two_cla_ing)
            #
            # else:
            #     print("던전 사냥중 이상무~!")
            #     now_hunting_is(data, cla)
        return questcomplete
    except Exception as e:
        print(e)
        return 0


def dunjeonCheck(cla, data, same):
    try:
        from function import random_int, click_pos_2, myPotion_check, imgs_set
        from where import go_worldmap
        from clean import clean_screen, game_event_popup
        from action import now_hunting_is, go_potion_off
        import pyautogui
        import numpy as np
        import cv2

        print("def dunjeonCheck(cla, data, same): start", same)
        # data = gonghu, nanjang, underprison
        isdunjeonCheck = False
        dungeon_decision = False
        # data는 해당던전 종류(공허, 난쟁, 지하감옥)

        # 던전내에서 순간이동, 자동사냥, 지도 클릭 => 진행중일땐 최초 1회만...
        isIndungeon = False
        while isdunjeonCheck is False:
            if same == False:
                while isIndungeon is False:

                    result = mydungeon_check(cla, 'in_check')
                    if result == False:
                        print("def dunjeonCheck(cla, data, same): False => 던전 진입 전")
                        click_pos_2(120, 210, cla)
                        time.sleep(5)
                        result_world = go_worldmap(cla, 'world') #월드보기
                        if result_world == True:
                            isIndungeon = True
                            if cla == 'one':
                                v_.one_cla_ing = 'check'
                            if cla == 'two':
                                v_.two_cla_ing = 'check'
                            clean_screen(cla, "dunjeonCheck")
                    else:
                        time.sleep(random_int())
                        game_event_popup(cla)
                        click_pos_2(585, 985, cla)
                        # 여기서 가방화면 나오면 곤란...

                        isIndungeon = True
                        isSoongan = False
                        while isSoongan is False:
                            result_ = mydungeon_check(cla, 'in_check')
                            if result_ == False:
                                print("def dunjeonCheck(cla, data, same): 던전 진입 중, 순간이동 하는 중")
                                # 만약 현재 월드맵일 경우 다시 던전에 재진입 해야함.
                                thisWorld = False
                                full_path = "c:\\coobcco\\imgs\\worldmap_1.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                                if imgs_ is None or imgs_ == False:
                                    print("월드맵 아니닷, clean_screen")

                                    full_path = "c:\\coobcco\\imgs\\worldmap_2.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                                    if imgs_ is None or imgs_ == False:
                                        print("월드맵 아니닷2, clean_screen")
                                        full_path = "c:\\coobcco\\imgs\\worldmap_3.png"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                                        if imgs_ is None or imgs_ == False:
                                            print("월드맵 아니닷3, clean_screen")
                                            full_path = "c:\\coobcco\\imgs\\worldmap_4.png"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                                            if imgs_ is None or imgs_ == False:
                                                print("월드맵 아니닷4, clean_screen")
                                                full_path = "c:\\coobcco\\imgs\\worldmap_5.png"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                                                if imgs_ is None or imgs_ == False:
                                                    print("월드맵 아니닷5, clean_screen")
                                                else:
                                                    print("월드맵이닷5, clean_screen", imgs_)
                                                    thisWorld = True
                                            else:
                                                print("월드맵이닷4, clean_screen", imgs_)
                                                thisWorld = True
                                        else:
                                            print("월드맵이닷3, clean_screen", imgs_)
                                            thisWorld = True
                                    else:
                                        print("월드맵이닷2, clean_screen", imgs_)
                                        thisWorld = True
                                else:
                                    print("월드맵이닷, clean_screen", imgs_)
                                    thisWorld = True

                                if thisWorld == True:
                                    isSoongan = True
                                    click_pos_2(920, 55, cla)
                                time.sleep(random_int())
                            else:
                                isSoongan = True
                                click_pos_2(900, 890, cla)
                                result = now_hunting_is(data, cla)
                                time.sleep(random_int())
                                # if result == False:
                                #     click_pos_2(585, 985, cla)
                                #     time.sleep(random_int())
                                #     now_hunting_is(data, cla)


                                result__ = mydungeon_check(cla, 'ing_check')
                                if result__ == False:
                                    # 던전 아닐 가능성 높음.
                                    click_pos_2(125, 215, cla)
                                    time.sleep(random_int())

                                result___ = go_potion_off(cla)
                                if result___ == False:
                                    click_pos_2(800, 840, cla)
                                    time.sleep(random_int())
                                    click_pos_2(700, 840, cla)
                                    time.sleep(random_int())
                                    # click_pos_2(570, 50, cla)
                                    pyautogui.moveTo(490, 550, 0.2)


            game_event_popup(cla)
            result = mydungeon_check(cla, 'ing_check')
            print("던전 진행중인지 mydungeon_check로 확인중", result)
            if result == True:
                isdunjeonCheck = True
                dungeon_decision = True
                myPotion_check(data, cla)
                print("mydungeoncheck로 확인하니 현재 던전 진행 중.")
                if cla == 'one':
                    v_.one_cla_ing = data
                if cla == 'two':
                    v_.two_cla_ing = data
                print("good", str(cla) + " 클라_ing :" + str(data))
            else:
                isdunjeonCheck = True
                print("mydungeoncheck로 확인하니 던전 진행중이지 않음")

        print("def dunjeonCheck(cla, data, same): end", same)
        return dungeon_decision
    except Exception as e:
        print(e)
        return 0

def mydungeon_check(cla, data):
    try:
        from function import drag_pos, click_pos_2, imgs_set
        import numpy as np
        import cv2

        go_ = False

        if data == 'ing_check':
            full_path = "c:\\coobcco\\imgs\\dunjeon\\namum_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(100, 280, 200, 330, cla, img)
            if imgs_ is not None:
                go_ = True
            full_path = "c:\\coobcco\\imgs\\dunjeon\\namum_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(100, 280, 200, 330, cla, img)
            if imgs_ is not None:
                go_ = True

            isMap = False
            while isMap is False:
                full_path = "c:\\coobcco\\imgs\\dun_x.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(630, 320, 700, 365, cla, img)
                if imgs_ is None:
                    print("던전 X 안보여")
                    click_pos_2(125, 215, cla)
                    time.sleep(1)
                    full_path = "c:\\coobcco\\imgs\\namum.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(100, 280, 200, 330, cla, img)
                    if imgs_ is None:
                        print("던전 남음 안보여")
                        full_path = "c:\\coobcco\\imgs\\dangye.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(360, 320, 600, 365, cla, img)
                        if imgs_ is None:
                            print("던전 단계 안보여")
                            isMap = True
                            go_ = False
                            click_pos_2(920, 55, cla)
                        else:
                            print("던전 단계 보여", imgs_)
                            isMap = True
                            go_ = True
                    else:
                        print("던전 남음 보여", imgs_)
                        isMap = True
                        go_ = True
                else:
                    print("던전 X 보여", imgs_)
                    isMap = True
                    go_ = True

            if go_ == False:
                drag_pos(545, 725, 600, 725, cla)
                time.sleep(1)
                click_pos_2(125, 215, cla)
                time.sleep(1)

                full_path = "c:\\coobcco\\imgs\\dunjeon\\namum_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(100, 280, 200, 330, cla, img)
                if imgs_ is not None:
                    go_ = True
                full_path = "c:\\coobcco\\imgs\\dunjeon\\namum_3.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(100, 280, 200, 330, cla, img)
                if imgs_ is not None:
                    go_ = True

                isMap = False
                while isMap is False:
                    full_path = "c:\\coobcco\\imgs\\dun_x.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(630, 320, 700, 365, cla, img)
                    if imgs_ is None:
                        print("던전 X 안보여")
                        click_pos_2(125, 215, cla)
                        time.sleep(1)
                        full_path = "c:\\coobcco\\imgs\\namum.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(100, 280, 200, 330, cla, img)
                        if imgs_ is None:
                            print("던전 남음 안보여")
                            full_path = "c:\\coobcco\\imgs\\dangye.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(360, 320, 600, 365, cla, img)
                            if imgs_ is None:
                                print("던전 단계 안보여")
                                isMap = True
                                go_ = False
                                click_pos_2(920, 55, cla)
                            else:
                                print("던전 단계 보여", imgs_)
                                isMap = True
                                go_ = True
                        else:
                            print("던전 남음 보여", imgs_)
                            isMap = True
                            go_ = True
                    else:
                        print("던전 X 보여", imgs_)
                        isMap = True
                        go_ = True

        # 던전 사진들 비교하기기 x 545 y 725 x 600
        if data =='in_check':
            full_path = "c:\\coobcco\\imgs\\dunjeon\\namum_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(100, 280, 200, 330, cla, img)
            if imgs_ is not None:
                go_ = True
            full_path = "c:\\coobcco\\imgs\\dunjeon\\namum_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(100, 280, 200, 330, cla, img)
            if imgs_ is not None:
                go_ = True
            full_path = "c:\\coobcco\\imgs\\namum.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(100, 280, 200, 330, cla, img)
            if imgs_ is None or imgs_ == False:
                print("던전 남음 안보여(in_check)")
                full_path = "c:\\coobcco\\imgs\\dangye.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(360, 320, 600, 365, cla, img)
                if imgs_ is not None:
                    print("던전 단계 보여(in_check)", imgs_)
                    go_ = True
                else:
                    print("던전 단계 안보여(in_check)")
                    click_pos_2(120, 210, cla)
                    time.sleep(1)
                    drag_pos(545, 725, 600, 725, cla)
                    time.sleep(1)
                    full_path = "c:\\coobcco\\imgs\\dangye.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(360, 320, 600, 365, cla, img)
                    full_path2 = "c:\\coobcco\\imgs\\jiha.png"
                    img_array2 = np.fromfile(full_path2, np.uint8)
                    img2 = cv2.imdecode(img_array2, cv2.IMREAD_COLOR)
                    imgs_2 = imgs_set(360, 320, 600, 365, cla, img2)
                    if imgs_ is not None:
                        print("던전 단계 보여2(in_check)", imgs_)
                        go_ = True
                    else:
                        print("던전 단계 안보여2(in_check)")
                    if imgs_2 is not None:
                        print("던전 지하 보여2(in_check)", imgs_2)
                        go_ = True
                    else:
                        print("던전 지하 안보여2(in_check)")

            else:
                print("던전 남음 보여(in_check)", imgs_)
                go_ = True



        if data == 'soongan_ready':
            full_path = "c:\\coobcco\\imgs\\dangye.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(360, 320, 600, 365, cla, img)
            if imgs_ is None:
                print("던전 단계 안보여")
            else:
                print("던전 단계 보여", imgs_)
                go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0




