import pandas as pd
import os
import util
import numpy as np


# # 显示所有列
# pd.set_option('display.max_columns', None)
# 显示所有行
# pd.set_option('display.max_rows', None)
# # 设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth', 100)


def getDataSet_Object():
    """
    读取数据集中双方的棋子
    :return:
    """
    path = './'
    filename = 'Object.csv'
    filepath = os.path.join(path, filename)
    with open(filepath, encoding='utf-8') as csvfile:
        data = pd.read_csv(csvfile)
        # print(len(data.columns))
        data.drop(['Room', 'GameName', 'Army', 'ObjSonName', 'ObjRes', 'ObjRes2', 'ObjSee', 'ObjDataID', 'ObjDate', 'ObjAim', 'ObjSup', 'ObjValue2', 'ObjMoney', 'ObjStep', 'ObjFlag', 'ObjIco', 'ObjIcon', 'A0', 'A2', 'A4', 'A5', 'B1', 'B2',
                   'B3', 'B4', 'B5', 'C0', 'C1', 'C3', 'D2', 'D3', 'E1', 'E2', 'F0', 'F1', 'F2', 'F3', 'R5', 'S3', 'S4', 'S5', 'Scenario',
                   'Area', 'Level', 'Scale'], axis=1, inplace=True)
        return data
        # print(len(data.columns))
        # # 按照文件名称进行分组，得到一局游戏中的双方棋子
        # for index, group in data.groupby(by=['filename']):
        #     print(index)
        #     print(group)
        #     break


def getDataSet_City():
    """
    读取数据集中主要和次要夺控点
    :return:
    """
    path = './'
    filename = 'City1.csv'
    filepath = os.path.join(path, filename)
    with open(filepath, encoding='utf-8') as csvfile:
        data = pd.read_csv(csvfile)
        data.drop(['UserID', 'UserFlag', 'CityIco', 'Flag', 'CityRot', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'C0',
                   'C2', 'C3', 'Mark', 'Army', 'Scenario', 'Area', 'Level', 'Scale'], axis=1, inplace=True)
        # print(data.columns)
        return data
        # # 按照文件名称进行分组，得到一局游戏中的双方棋子
        # for index, group in data.groupby(by=['filename']):
        #     print(index)
        #     print(group)
        #     break


def getDataSet_Caijue():
    """
    读取数据集中的裁决表
    :return:
    """
    path = './'
    filename = 'Caijue.csv'
    filepath = os.path.join(path, filename)
    with open(filepath, encoding='utf-8') as csvfile:
        data = pd.read_csv(csvfile)
        # print(data.columns)
        # print(len(data.columns))
        data.drop(['RoomID', 'Scenario', 'Area', 'Level', 'Scale'], axis=1, inplace=True)
        # print(data.columns)
        # print(len(data.columns))
        # print(data.head())
        return data


def getDataSet_RoomRecord():
    """
    读取数据集中推演过程
    :return: 返回推演序列，一个游戏为一个事件
    """
    path = './'
    filename = 'RoomRecord.csv'
    filepath = os.path.join(path, filename)
    obj_data = getDataSet_Object()
    city_data = getDataSet_City()
    # caijue_data = getDataSet_Caijue()
    total_seq = []
    with open(filepath, encoding='utf-8') as csvfile:
        data = pd.read_csv(csvfile)
        data.drop(['TimeID', 'ObjRot', 'UserNewID', 'FireID', 'KeepRemoveArr', 'TireRemoveArr', 'JmArr', 'ObjKeepCancel',
                   'JmColor', 'JmResult', 'JmObjResult', 'Scenario', 'Area', 'Level', 'Scale'], axis=1, inplace=True)
        i = 0
        for index, group in data.groupby(by=['filename']):
            i += 1
            # 输出当前处理的文件名
            # print(index)
            # print(i)
            # 当前这场游戏的总序列
            cur_seq = []
            # 输出当前处理的文件
            # group.to_excel('group.xls')
            objs = obj_data[obj_data['filename'] == index]
            vs = get_vs(objs)
            citys = city_data[city_data['filename'] == index]
            # caijues = caijue_data[caijue_data['filename'] == index]
            objs_cols_to_use = objs.columns.difference(group.columns)
            citys_cols_to_use = citys.columns.difference(group.columns)
            group_merge = group.merge(objs[objs_cols_to_use], left_on='ObjID', right_on='ID', how='left', sort=False)
            group_merge = group_merge.merge(citys[citys_cols_to_use],
                                            left_on="CityID", right_on="ID", how='left', sort=False)
            group_merge.sort_values(by='DateAndTime', axis=0, ascending=True, inplace=True)

            # 生成合并的表格
            # head = {}
            # head.update(util.city)
            # head.update(util.object)
            # head.update(util.caijue)
            # head.update(util.event)
            # group_merge.rename(columns=head, inplace=True)
            # group_merge.to_excel('merge.xls')

            for _, row in group_merge.iterrows():
                # print(row.index)
                actions, vs = action(row, vs)
                cur_item = (row['StageID'], row['GameColor'], row['ObjID'], row['ObjName'], actions, vs)
                cur_seq.append(cur_item)
                print(cur_item)
            total_seq.append(cur_seq)
            # print(len(cur_seq))
            win = "RED" if vs[4] > vs[9] else "BLUE"
            print(win + " Win")
            # print(cur_seq)
            if i == 1:
                break
    # print(totol_seq)
    # m = np.array(totol_seq)
    # np.save('demo.npy', m)
    # return totol_seq


def getDataSet_Map():
    """
    读取兵棋地图
        MapID 六角格坐标
        Elevation 海拔数据
        Note 地名标注
        Cond 地质 6松软地，7道路穿过的居民地
        ObjStep 机动力消耗值
        GridID 六角格类型
        GridType 六角格类型 0开阔地，1河流，2道路，3遮蔽
        GroundID 高程
        HexEdge 六角格作用边 河流专用，|分隔，数字表示度方向
        Flag 道路类型 0一般道路，1一般公路，2等级公路
    :return:地图的dataframe
    """
    path = './map/'
    filename = 'map_processed.csv'
    filepath = os.path.join(path, filename)
    with open(filepath, encoding='utf-8') as csvfile:
        data = pd.read_csv(csvfile)
        print(data.columns)
        print(data)


def action(row, vs):
    """
    :param: RoomRecord 战斗记录中的一行数据 row
    :param: vs 当前比分
    :return: 此回合的动作类型
    """
    # print(row)
    actions = []
    if row['ObjPass'] == 1:
        actions.append('行军')
    if row['ObjHide'] == 1:
        actions.append('掩蔽')
    if row['ObjKeep'] == 1:
        actions.append('被压制')
    if row['ObjSon'] != 0:
        actions.append('载人')
    if (row['ObjNewPos'] != row['ObjPos']) or row['ObjRound'] != 0:
        actions.append('机动')
    if row['AttackID'] != 0:
        actions.append('攻击')
        if row['TarLost'] != 0:
            score = row['ObjValue'] * row['TarLost']
            if row['GameColor'] == 'RED':
                vs[2] += score
                vs[6] -= score
            else:
                vs[7] += score
                vs[1] -= score
    if row['ObjInto'] != 0:
        actions.append('上车')
    if row['ObjOut'] != 0:
        actions.append('下车')
    if row['CityTake'] == 1:
        actions.append('占领地区')
        actions.append(row['CityName'])
        score = row['C1']
        if row['GameColor'] == 'RED':
            vs[0] += score
        else:
            vs[5] += score
    vs[3] = vs[0] + vs[1] + vs[2]
    vs[8] = vs[5] + vs[6] + vs[7]
    t = vs[3] - vs[8]
    vs[4] = t
    vs[9] = -t
    return actions, vs[:]


def get_vs(objs):
    """
    获得当前这场游戏的初始兵力比分
    :param objs: 对象数据
    :return: 剩余兵力比分
    """
    red_data = objs[objs['GameColor'] == "RED"]
    red_score = 0
    for _, row in red_data.iterrows():
        red_score += row["ObjBlood"] * row["ObjValue"]
    blue_data = objs[objs['GameColor'] == "BLUE"]
    blue_score = 0
    for _, row in blue_data.iterrows():
        blue_score += row["ObjBlood"] * row["ObjValue"]
    # 红， 夺控得分 剩余兵力得分 歼灭对手得分 胜分 净胜分
    return [0, red_score, 0, 0, 0, 0, blue_score, 0, 0, 0]
    # return [red_score, blue_score]


if __name__ == '__main__':
    getDataSet_RoomRecord()
    # getDataSet_Caijue()
    # getDataSet_City()
    # getDataSet_Map()
