class Caijue:
    '''
    AttackID        裁决ID 和RoomRecord表里的AttackID关联
    # RoomID          推演室ID
    Huihe           阶段ID
    RoundColor      阶段所属方
    StageShoot      最终射击阶段 直瞄射击 0：不是，1：是 间瞄射击 间瞄计划ID
    Yanhu           掩护射击 0：不是，1：是
    ObjID           射击单位
    ObjName         射击单位名称
    ObjColor        射击单位所属方
    ObjA1           行进间射击能力 0：无，1：有
    ObjType         单位类型 1：人员，2：车辆
    ObjKeep         射击单位被压制状态 0：未被压制，>0：被压制的阶段
    ObjNum          射击单位车/班数 间瞄射击表示炮数
    ObjPass         射击单位状态 1：一级疲劳，2：二级疲劳
    TarID           目标单位
    TarUserID       目标所属用户ID
    TarName         目标单位名称
    TarColor        目标单位所属方
    TarB0           目标单位装甲防护 0：无，1：轻型，2：中型，3：重型，4：复合
    TarType         目标单位类型 1：人员，2：车辆
    TarHide         目标单位是否掩蔽 0：否，1：是
    TarKeep         目标单位被压制状态 0：未被压制，>0：被压制的阶段
    TarPass         目标单位状态 1：机动中，2：行军中
    TarStack        目标单位是否堆叠 0：否，1：是
    WeaponID        使用的武器ID
    WeaponF1        使用的武器火力线
    WeaponName      使用的武器名称
    Dist            射击距离
    EleDiff         高差 直瞄射击用这列表示高差1-8 间瞄射击用这列表示表示战斗结果修正随机数
    AttackLevel     攻击等级 1到10 间瞄射击用这列表示火力散布裁决结果 null：命中，0-N：散布N格
    TarPos          目标单位所在坐标
    TarHex          目标单位所在格地形 51：居民地，52：丛林地
    RandomNum1      战斗结果表随机数 直瞄射击用这列表示战斗结果表随机数 间瞄射击用这列表示火力散布裁决随机数
    Result1         战斗结果 null：无效，0：压制，1-3：消灭车/班数
    RandomNum2      战果修正随机数 直瞄射击用这列表示战果修正随机数 间瞄射击用这列表示战斗结果裁决随机数
    Diff            战果修正值
    Result          最终战果
    Keep            是否压制
    Kills           是否消灭
    TarLost         目标损失的车/班数
    TarNum          目标还剩几个单位
    Flag            裁决类型 0：直瞄射击，1：间瞄射击
    UserRead        观摩者是否看到
    Scenario
    Area
    Level
    Scale
    '''
    def __init__(self):
        pass