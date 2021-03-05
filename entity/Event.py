class Event:
    """
    # DateAndTime     时间
    StageID         阶段ID（一共6个回合，24个阶段）
    # TimeID          一个阶段倒计时所在的秒（前15秒间瞄，后15秒最终射击）
    ObjID           棋子ID
    ObjRot          记录棋子当前的角度
    ObjPass         回放棋子是否处于行军状态 0：未行军，1：行军
    D3              如果是行军状态，当前行军了多少格
    ObjHide         回放棋子是否处于掩蔽状态 0：未掩蔽，1：掩蔽
    ObjKeep         回放棋子是否处于被压制状态 0：正常，1：被压制
    ObjTire         回放棋子是否处于疲劳状态 0：正常，1：1级疲劳，2：2级疲劳
    ObjRound        棋子该阶段是否机动过 0：未机动，1：已机动
    ObjAttack       棋子该阶段是否射击过 0：未射击，1：已射击
    ObjSon          车辆是否载人 0：未载人，>0：载哪个棋子（ID）
    ObjBlood        当前几个车（班） 1～3
    ObjStep         当前机动力值
    C2              当前弹药数
    A3              当前导弹数
    UserID          原控制员ID
    # UserNewID       新控制员ID 0：未交换控制
    ObjPos          棋子原来在哪格
    ObjNewPos       棋子移动到了哪格，未移动则记录当前格
    AttackID        此ID关联原数据库中的Caijue表，用于查询裁决过程，因此原数据库的Caijue表需要保存 0：未射击
    TarID           被射击的棋子ID 0：未射击
    TarLost         被射击的棋子损失车（班）数 0：无效，1～3：损失车（班）数
    TarKeep         被射击的棋子是否被压制 0：未压制，1：压制
    TarBlood        被射击后棋子剩余车（班）数  0～3
    # FireID          开火图片，仅用于回放中显示效果，何种武器通过AttackID查Caijue表 0：未射击
    ObjInto         上车则记录该车ID 0：无动作，>0：上哪辆车（ID）
    ObjOut          下车则记录该车ID 0：无动作，>0：从哪辆车下来（ID）
    ObjKeepCancel   此列只记录是否进行了移除压制动作，不用于回放，回放通过判断状态数据即可 0：无动作，1：移除压制
    CityTake        0：无动作，1：执行占领
    CityID          如果有数据，则该格ID显示被占领 0：无占领
    # KeepRemoveArr   被移除压制的棋子ID
    # TireRemoveArr   被移除疲劳的棋子ID
    # JmArr           间瞄计划格
    # JmColor         移除某一方间瞄计划时需要用
    # JmResult        间瞄裁决结果
    # JmObjResult     间瞄所造成的单位损失
    # Scenario
    # Area            地区 河北
    # Level           比赛级别 预赛
    # Scale           比赛规模 个人
    """
    def __init__(self):


        pass
