import pandas as pd
import os

def map_process():
    '''
    处理兵棋地图
    :return: 兵棋地图csv 10 columns
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
    '''

    path = './'
    map_filename = 'map.csv'
    maptype_filename = 'maptype.csv'
    map_filepath = os.path.join(path, map_filename)
    maptype_filepath = os.path.join(path, maptype_filename)
    with open(map_filepath, encoding='utf-8') as mapfile, open(maptype_filepath, encoding='utf-8') as maptypefile:
        mapdata = pd.read_csv(mapfile)
        maptypedata = pd.read_csv(maptypefile)
        mapdata = mapdata.drop(['列值', 'RoomID', 'MapID2'], axis=1, inplace=True)
        maptypedata = maptypedata.drop(['HexType', 'HexCons'], axis=1, inplace=True)
        map_merge = mapdata.merge(maptypedata, left_on='GridType', right_on='ID')
        map_merge = map_merge.drop(['ID'], axis=1)
        map_merge.sort_values(by='MapID',axis=0,ascending=True,inplace=True)
        map_merge.to_csv(path+'map_processed.csv', index=False)

if __name__ == '__main__':
    map_process()