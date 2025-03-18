class node:
    nodeId : int = 0
    nodeNo : int = 0
    x_pt : float = 0
    y_pt : float = 0
    z_pt : float = 0

    def __init__(self,nodeId,nodeNo) -> None:
        self.nodeId = nodeId
        self.nodeNo = nodeNo
        pass

class beam:
    beamId : int = 0
    beamNo : int = 0
    length : float = 0
    nodeA : int = 0
    nodeB : int = 0

    def __init__(self,beamId,beamNo) -> None:
        self.beamId = beamId
        self.beamNo = beamNo
        pass