class Object:
    """
    :param
    ID          棋子ID 每一场比赛不同
    # Room        推演室ID
    UserID      用户ID
    # GameName    用户昵称
    GameColor   推演方
    # Army        编号
    ObjName     棋子名称
    # ObjDataID   棋子模型ID
    ObjSup      车上步兵ID
    ObjSon      能搭载哪些模型
    ObjSonNum   车上步兵棋子数量
    # ObjSonName  车上步兵名称
    ObjSpace    最多搭载几个步兵
    ObjFlag     棋子颜色
    ObjPos      当前所在格
    # ObjIco      三维图标
    # ObjIcon     二级图标
    ObjType     棋子类型：1 人员 2 车辆
    ObjRot      当前角度
    ObjStep     机动力上限
    ObjStepMax  当前机动力
    ObjPass     人员 1 1级疲劳 人员 2 2级疲劳 车辆 1 行军中
    ObjBlood    当前车/班数
    ObjBlood2   初始的车/班数
    ObjKeep     第X阶段被压制过
    ObjSee
    ObjHide     1 掩蔽中
    ObjAim
    ObjValue    车/班分值
    ObjValue2   是否指挥车 0否，1是
    ObjMoney    是否上过车 上过车的步兵原始ID在这
    ObjRound    第X阶段机动过
    ObjAttack   第X阶段射击过
    ObjDate
    ObjRadar    是否夺控过 1 夺控过
    ObjRes
    ObjRes2
    Slope
    A0
    B0          装甲级别 0 无装甲 1 轻型 2 中型 3 重型 4 复合
    A1          行进间射击能力 0无 1 有
    A2
    A3          当前导弹数
    A4', 'A5',
    'B1', 'B2', 'B3','B4', 'B5',
    'C0
    # C1          图标显示大小 0小，1大
    C2          当前炮弹数
    C3
    D0          当前道路行军上限（走到不同的道路上会变）
    D1          车辆道路行军消耗机动力值 每几格消耗1个机动力
    D2', 'D3',
    E0          炮弹上限 0 表示棋子是炮兵
    E1', 'E2',
    F0          常规弹药消耗量 每次射击
       F1', 'F2', 'F3',
    R1          步兵攻击力（当前格）
    R2          步兵攻击力（相临格）
    R3          步兵攻击力（隔1格）
    R4          步兵攻击力（隔2格）
    R5
    S1          观察距离 对人
    S2          观察距离 对车
    S3', 'S4', 'S5',
    Wz          关联的武器ID
    Scenario
    Area        地区 河北
    Level       比赛级别 预赛
    Scale       比赛规模 个人
    :return
    """


    def __init__(self, ID, UserID, GameColor):
        self.ID = ID
        self.UserId = UserID
        self.GameColor = GameColor



