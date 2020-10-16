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
    '''
    读取数据集中双方的棋子
    :return:
    '''
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


def getDataSet_RoomRecord():
    '''
    读取数据集中推演过程
    :return: 返回推演序列，一个游戏为一个事件
    '''
    path = './'
    filename = 'RoomRecord.csv'
    filepath = os.path.join(path, filename)
    objdata = getDataSet_Object()
    totol_seq = []
    with open(filepath, encoding='utf-8') as csvfile:
        data = pd.read_csv(csvfile)
        data.drop(['TimeID', 'UserNewID', 'FireID', 'KeepRemoveArr', 'TireRemoveArr', 'JmArr',
                   'JmColor', 'JmResult', 'JmObjResult', 'Scenario', 'Area', 'Level', 'Scale'], axis=1, inplace=True)
        i = 0
        for index, group in data.groupby(by=['filename']):
            i += 1
            print(i)
            cur_seq = []
            objs = objdata[objdata['filename'] == index]
            cols_to_use = objs.columns.difference(group.columns)
            group_merge = group.merge(objs[cols_to_use], left_on='ObjID', right_on='ID')
            group_merge.sort_values(by='DateAndTime',axis=0,ascending=True,inplace=True)
            # print(group_merge.columns)
            # print(group_merge.head())
            for _, row in group_merge.iterrows():
                # print(row.index)
                cur_item = (row['StageID'], row['GameColor'], row['ObjName'], action(row))
                cur_seq.append(cur_item)
            totol_seq.append(cur_seq)
            # if i == 5:
            #     break
    # print(totol_seq)
    m = np.array(totol_seq)
    print(m)
    np.save('demo.npy', m)
    return totol_seq

def getDataSet_Map():
    '''
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
    '''
    path = './map/'
    filename = 'map_processed.csv'
    filepath = os.path.join(path, filename)
    with open(filepath, encoding='utf-8') as csvfile:
        data = pd.read_csv(csvfile)
        print(data.columns)
        print(data.head())


def action(row):
    '''
    :param: RoomRecord 战斗记录中的一行数据 row
    :return: 此回合的动作类型
    '''
    if row['ObjPass'] == 1:
        return '行军'
    elif row['ObjHide'] == 1:
        return '掩蔽'
    elif row['ObjKeep'] == 1:
        return '被压制'
    elif row['ObjNewPos'] != row['ObjPos']:
        return '机动'
    elif row['AttackID'] != 0:
        return '攻击'
    elif row['ObjInto'] != 0:
        return '上车'
    elif row['ObjOut'] != 0:
        return '下车'
    elif row['CityTake'] == 1:
        return '占领地区'
    return None

if __name__ == '__main__':
#     objs = getDataSet_Object('201851912743 01-06-03-03-02 推演室1')
#     print(objs[objs['ID'] == 14181])
    getDataSet_RoomRecord()
#     # getDataSet_Map()