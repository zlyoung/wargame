import pandas as pd
import os
import numpy as np
# # 显示所有列
# pd.set_option('display.max_columns', None)
# # 显示所有行
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
        data.drop(['Room', 'GameName', 'Army', 'ObjSonName', 'ObjIco', 'ObjIcon', 'C1', 'Scenario', 'Area', 'Level', 'Scale'], axis=1, inplace=True)
        return data
        # print(len(data.columns))
        # # 按照文件名称进行分组，得到一局游戏中的双方棋子
        # for index, group in data.groupby(by=['filename']):
        #     print(index)
        #     print(group)
        #     break


def getDataSet_City():
    """
    读取数据集中双方的棋子
    :return:
    """
    path = './'
    filename = 'City1.csv'
    filepath = os.path.join(path, filename)
    with open(filepath, encoding='utf-8') as csvfile:
        data = pd.read_csv(csvfile)
        # print(len(data.columns))
        data.drop(['Room', 'GameName', 'Army', 'ObjSonName', 'ObjIco', 'ObjIcon', 'C1', 'Scenario', 'Area', 'Level', 'Scale'], axis=1, inplace=True)
        return data
        # print(len(data.columns))
        # # 按照文件名称进行分组，得到一局游戏中的双方棋子
        # for index, group in data.groupby(by=['filename']):
        #     print(index)
        #     print(group)
        #     break


def getDataSet_Caijue():
    '''
    读取数据集中的裁决表
    :return:
    '''
    path = './'
    filename = 'Caijue.csv'
    filepath = os.path.join(path, filename)
    with open(filepath, encoding='utf-8') as csvfile:
        data = pd.read_csv(csvfile)
        print(data.columns)
        data.drop(['RoomID', 'Scenario', 'Area', 'Level', 'Scale'], axis=1, inplace=True)
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
    # caijue_data = getDataSet_Caijue()
    totol_seq = []
    with open(filepath, encoding='utf-8') as csvfile:
        data = pd.read_csv(csvfile)
        data.drop(['TimeID', 'UserNewID', 'FireID', 'KeepRemoveArr', 'TireRemoveArr', 'JmArr',
                   'JmColor', 'JmResult', 'JmObjResult', 'Scenario', 'Area', 'Level', 'Scale'], axis=1, inplace=True)
        i = 0
        for index, group in data.groupby(by=['filename']):
            print(index)
            i += 1
            # print(i)
            cur_seq = []
            objs = obj_data[obj_data['filename'] == index]
            # caijues = caijue_data[caijue_data['filename'] == index]
            cols_to_use = objs.columns.difference(group.columns)
            group_merge = group.merge(objs[cols_to_use], left_on='ObjID', right_on='ID')
            group_merge.sort_values(by='DateAndTime',axis=0,ascending=True,inplace=True)
            # print(group_merge.columns)
            # print(group_merge.head())
            vs = [0, 0]
            for _, row in group_merge.iterrows():
                # print(row.index)
                actions, vs = action(row, vs)
                cur_item = (row['StageID'], row['GameColor'], row['ObjID'], row['ObjName'], actions, vs)
                cur_seq.append(cur_item)
                print(cur_item)
            totol_seq.append(cur_seq)
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
                vs[0] += score
            else:
                vs[1] += score
    if row['ObjInto'] != 0:
        actions.append('上车')
    if row['ObjOut'] != 0:
        actions.append('下车')
    if row['CityTake'] == 1:
        actions.append('占领地区')

    return actions, vs[:]


if __name__ == '__main__':

    getDataSet_RoomRecord()
#     getDataSet_Map()
